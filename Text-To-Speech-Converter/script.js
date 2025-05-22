async function convertText() {
  const text = document.getElementById("textInput").value.trim();
  if (!text) {
    alert("Please enter some text.");
    return;
  }

  try {
    const response = await fetch("https://lo0ge8u33h.execute-api.us-east-1.amazonaws.com/prod/tts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: text })
    });

    if (!response.ok) {
      alert("Error from server: " + response.statusText);
      return;
    }

    const result = await response.json();

    if (result.audioUrl) {
      const audio = document.getElementById("audioPlayer");
      const section = document.getElementById("audioSection");
      audio.src = result.audioUrl;
      section.style.display = "block";
      audio.play();
    } else {
      alert("No audio URL returned. Response: " + JSON.stringify(result));
    }
  } catch (error) {
    alert("Fetch error: " + error.message);
  }
}
