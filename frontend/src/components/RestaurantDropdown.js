import React, { useEffect, useState } from 'react';

const BACKENDURL = process.env.NEXT_PUBLIC_BACKEND_URL;

const RestaurantDropdown = ({ selectedRestaurant, onSelectRestaurant }) => {
    const [restaurantNames, setRestaurantNames] = useState([]);

    useEffect(() => {
        // fetch(`${BACKENDURL}/restaurant/list_restaurants`)
        fetch(`http://127.0.0.1:8000/restaurant/list_restaurants`)
            .then(response => response.json())
            .then(data => setRestaurantNames(data.restaurant_names))
            .catch(error => console.error('Error fetching restaurant names:', error));
    }, []);

    const handleSelectChange = (event) => {
        onSelectRestaurant(event.target.value);
        console.log(BACKENDURL);
        console.log('Environment Variables:', process.env);
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
