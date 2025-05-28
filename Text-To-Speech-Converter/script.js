// Create floating particles
function createParticles() {
  const particlesContainer = document.getElementById('particles');
  const particleCount = window.innerWidth < 768 ? 30 : 50;
  
  for (let i = 0; i < particleCount; i++) {
    const particle = document.createElement('div');
    particle.classList.add('particle');
    
    // Random properties
    const size = Math.random() * 5 + 2;
    const posX = Math.random() * window.innerWidth;
    const duration = Math.random() * 20 + 10;
    const delay = Math.random() * 5;
    const opacity = Math.random() * 0.5 + 0.1;
    
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;
    particle.style.left = `${posX}px`;
    particle.style.bottom = `-10px`;
    particle.style.animationDuration = `${duration}s`;
    particle.style.animationDelay = `${delay}s`;
    particle.style.opacity = opacity;
    
    particlesContainer.appendChild(particle);
  }
}

// Update character count
function updateCharCount() {
  const text = document.getElementById('textInput').value;
  document.getElementById('charCount').textContent = `${text.length} characters`;
}

// Clear text input
function clearText() {
  document.getElementById('textInput').value = '';
  updateCharCount();
}

// Download audio
function downloadAudio() {
  const audioSrc = document.getElementById('audioPlayer').src;
  if (!audioSrc) return;
  
  const a = document.createElement('a');
  a.href = audioSrc;
  a.download = 'voicecraft-audio.mp3';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

// Convert text to speech
async function convertText() {
  const text = document.getElementById('textInput').value.trim();
  if (!text) {
    alert('Please enter some text to convert.');
    return;
  }

  const convertBtn = document.getElementById('convertBtn');
  convertBtn.innerHTML = "<i class='fas fa-spinner fa-spin'></i> Processing";
  convertBtn.classList.add('loading');
  convertBtn.disabled = true;

  try {
    const response = await fetch('https://lo0ge8u33h.execute-api.us-east-1.amazonaws.com/prod/tts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: text })
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.statusText}`);
    }

    const result = await response.json();

    if (result.audioUrl) {
      const audio = document.getElementById('audioPlayer');
      const section = document.getElementById('audioSection');
      audio.src = result.audioUrl;
      section.style.display = 'block';
      
      // Stop the waveform animation when audio ends
      audio.onended = () => {
        document.querySelectorAll('.wave').forEach(wave => {
          wave.style.animationPlayState = 'paused';
        });
      };
      
      // Start playing
      audio.play().then(() => {
        document.querySelectorAll('.wave').forEach(wave => {
          wave.style.animationPlayState = 'running';
        });
      }).catch(e => {
        console.error('Playback failed:', e);
      });
    } else {
      throw new Error('No audio URL returned');
    }
  } catch (error) {
    console.error('Error:', error);
    alert(`Error: ${error.message}`);
  } finally {
    convertBtn.innerHTML = "<i class='fas fa-microphone-alt'></i> Convert to Speech";
    convertBtn.classList.remove('loading');
    convertBtn.disabled = false;
  }
}

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
  createParticles();
  
  // Event listeners
  document.getElementById('textInput').addEventListener('input', updateCharCount);
  document.getElementById('clearBtn').addEventListener('click', clearText);
  document.getElementById('convertBtn').addEventListener('click', convertText);
  document.getElementById('downloadBtn').addEventListener('click', downloadAudio);
  
  // Handle window resize
  window.addEventListener('resize', () => {
    document.getElementById('particles').innerHTML = '';
    createParticles();
  });
});
