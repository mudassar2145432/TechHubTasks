// static/js/script.js

const video = document.getElementById("webcam");

// Start webcam stream
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(err => {
    document.getElementById("message").innerText = "Camera error: " + err.message;
    console.error("Camera error:", err);
  });

function captureImage() {
  // This is optional – your image capture logic goes here
  alert("Capture button clicked (you can add image capture code here).");
}
