import React, { useEffect, useState } from 'react';

const RestaurantDropdown = ({ selectedRestaurant, onSelectRestaurant }) => {
    const [restaurantNames, setRestaurantNames] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/restaurant/list_restaurants')
            .then(response => response.json())
            .then(data => setRestaurantNames(data.restaurant_names))
            .catch(error => console.error('Error fetching restaurant names:', error));
    }, []);

    const handleSelectChange = (event) => {
        onSelectRestaurant(event.target.value);
    };

    return (
        <div>
            <select value={selectedRestaurant} onChange={handleSelectChange}>
                <option value="" disabled>Select a restaurant</option>
                {restaurantNames.map(name => (
                    <option key={name} value={name}>{name}</option>
                ))}
            </select>
        </div>
    );
};

export default RestaurantDropdown;
