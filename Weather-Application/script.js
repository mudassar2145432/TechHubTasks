const apiUrl = "https://e5i971xno6.execute-api.us-east-1.amazonaws.com/prod/GetWeatherData"; // Your API Gateway URL

function getWeatherIcon(description) {
  const desc = description.toLowerCase();
  if (desc.includes("clear")) return "☀️";
  if (desc.includes("cloud")) return "☁️";
  if (desc.includes("rain")) return "🌧️";
  if (desc.includes("storm") || desc.includes("thunder")) return "⛈️";
  if (desc.includes("snow")) return "❄️";
  if (desc.includes("fog") || desc.includes("mist")) return "🌫️";
  if (desc.includes("few clouds")) return "🌤️";
  return "⛅";
}

function getFeelsLikeIcon(temp) {
  if (temp >= 35) return "🥵";    // very hot
  if (temp >= 25) return "😓";    // warm
  if (temp >= 15) return "🙂";    // mild
  if (temp >= 5)  return "🧥";    // cool
  return "🥶";                   // cold
}

async function fetchWeatherData() {
  const response = await fetch(apiUrl);
  if (!response.ok) throw new Error("Network response was not ok");
  return await response.json();
}

function populateDropdown(data) {
  const select = document.getElementById("citySelect");
  select.innerHTML = ""; // Clear options first
  const cities = [...new Set(data.map(item => item.location))];
  cities.forEach(city => {
    const option = document.createElement("option");
    option.value = city;
    option.textContent = city;
    select.appendChild(option);
  });

  select.onchange = () => {
    const cityData = data.find(item => item.location === select.value);
    showWeather(cityData);
  };

  if (cities.length > 0) {
    select.value = cities[0];
    showWeather(data.find(item => item.location === cities[0]));
  }
}

function showWeather(item) {
  if (!item) return;
  const weatherIcon = getWeatherIcon(item.description);
  const feelsLikeIcon = getFeelsLikeIcon(parseFloat(item.feels_like));
  const container = document.getElementById("weatherCard");

  container.innerHTML = `
    <div class="location-title">${item.location}</div>

    <div class="info-block">
      <div class="icon">🌡️</div>
      <strong>${item.temperature} °C</strong>
      <span>Temperature</span>
    </div>

    <div class="info-block">
      <div class="icon">${feelsLikeIcon}</div>
      <strong>${item.feels_like} °C</strong>
      <span>Feels Like</span>
    </div>

    <div class="info-block">
      <div class="icon">${weatherIcon}</div>
      <strong>${item.description}</strong>
      <span>Condition</span>
    </div>

    <div class="info-block">
      <div class="icon">⚖️</div>
      <strong>${item.pressure} hPa</strong>
      <span>Pressure</span>
    </div>

    <div class="info-block">
      <div class="icon">🌬️</div>
      <strong>${item.wind_speed} m/s</strong>
      <span>Wind Speed</span>
    </div>

    <div class="info-block">
      <div class="icon">☁️</div>
      <strong>${item.clouds} %</strong>
      <span>Cloud Coverage</span>
    </div>

    <div class="info-block">
      <div class="icon">👁️</div>
      <strong>${item.visibility} m</strong>
      <span>Visibility</span>
    </div>

    <div class="info-block">
      <div class="icon">📍</div>
      <strong>${item.latitude}, ${item.longitude}</strong>
      <span>Coordinates</span>
    </div>
    
    <div class="info-block">
      <div class="icon">💧</div>
      <strong>${item.humidity} %</strong>
      <span>Humidity</span>
    </div>
    

    <div class="timestamp">Updated: ${new Date(item.timestamp).toLocaleString()}</div>
  `;
  container.style.display = "flex";
}

async function fetchAndUpdate() {
  try {
    const data = await fetchWeatherData();
    const select = document.getElementById("citySelect");

    if (select.options.length === 0) {
      populateDropdown(data);
    } else {
      const cityData = data.find(item => item.location === select.value);
      showWeather(cityData);
    }
  } catch (err) {
    console.error("Failed to fetch weather data:", err);
  }
}

fetchAndUpdate();
setInterval(fetchAndUpdate, 30000); // Update every 30 seconds
