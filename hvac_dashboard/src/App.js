import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  // State for login and energy data submission
  const [token, setToken] = useState('');
  const [message, setMessage] = useState('');
  const [temperature, setTemperature] = useState('');
  const [humidity, setHumidity] = useState('');
  const [occupancy, setOccupancy] = useState('');
  const [timestamp, setTimestamp] = useState('');

  // Handle login request
  const handleLogin = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/login/', {
        token: 'test-token', // You can replace this with a dynamic token later
      });
      setMessage(response.data.message);
    } catch (error) {
      console.error(error);
      setMessage('Login failed!');
    }
  };

  // Handle energy data submission
  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent default form submission
    try {
      const response = await axios.post('http://127.0.0.1:8000/submit/', {
        temperature: parseFloat(temperature),
        humidity: parseFloat(humidity),
        occupancy: parseInt(occupancy),
        timestamp: timestamp,
      });
      setMessage(response.data.message);
    } catch (error) {
      console.error(error);
      setMessage('Data submission failed!');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Hello, Welcome to the HVAC Data Dashboard!</h1>
        <p>{message}</p>
        
        {/* Login Button */}
        <button onClick={handleLogin}>Login</button>
        
        {/* Form for submitting energy data */}
        <form onSubmit={handleSubmit} style={{ marginTop: '20px' }}>
          <input
            type="number"
            placeholder="Temperature"
            value={temperature}
            onChange={(e) => setTemperature(e.target.value)}
          />
          <input
            type="number"
            placeholder="Humidity"
            value={humidity}
            onChange={(e) => setHumidity(e.target.value)}
          />
          <input
            type="number"
            placeholder="Occupancy"
            value={occupancy}
            onChange={(e) => setOccupancy(e.target.value)}
          />
          <input
            type="text"
            placeholder="Timestamp (YYYY-MM-DD HH:MM:SS)"
            value={timestamp}
            onChange={(e) => setTimestamp(e.target.value)}
          />
          <button type="submit">Submit Data</button>
        </form>
      </header>
    </div>
  );
}

export default App;