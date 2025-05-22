async function sendEmail() {
  const subject = document.getElementById('subject').value;
  const message = document.getElementById('message').value;
  const loader = document.getElementById('loader');
  const statusText = document.getElementById('status');
  const sendBtn = document.getElementById('sendBtn');

  loader.style.display = 'block';
  statusText.innerText = '';
  sendBtn.disabled = true;

  try {
    const response = await fetch('https://g3k5vw1gx6.execute-api.us-east-1.amazonaws.com/prod/MassEmailSender', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ subject, message })
    });

    const data = await response.json();
    statusText.innerText = data.body || "Emails sent!";
    statusText.style.color = 'green';
  } catch (error) { 
    console.error(error);
    statusText.innerText = "Error sending emails.";
    statusText.style.color = 'red';
  } finally {
    loader.style.display = 'none';
    sendBtn.disabled = false;
    setTimeout(() => {
      statusText.innerText = '';
      statusText.style.color = 'green';
    }, 5000);
  }
}
