import React, { useState } from 'react';
import './App.css'; // Make sure this path is correct based on your file structure
import RestaurantDropdown from './components/RestaurantDropdown';
import FetchButton from './components/FetchButton';
import ChatPage from './components/TestButton';

function App() {
  const [selectedRestaurant, setSelectedRestaurant] = useState('');

  return (
    <div className="center-button-container">
      <RestaurantDropdown 
        selectedRestaurant={selectedRestaurant}
        onSelectRestaurant={setSelectedRestaurant}
      />
      <FetchButton selectedRestaurant={selectedRestaurant} />
      
    </div>
  );
}

export default App;
