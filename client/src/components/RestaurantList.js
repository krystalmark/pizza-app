import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);
  const [searchId, setSearchId] = useState('');

  useEffect(() => {
    fetchRestaurants();
  }, []);

  const fetchRestaurants = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/restaurants');
      if (response.ok) {
        const data = await response.json();
        setRestaurants(data);
      } else {
        console.error('Error fetching restaurant list:', response.statusText);
      }
    } catch (error) {
      console.error('Error fetching restaurant list:', error);
    }
  };

  const handleSearch = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/restaurants/${searchId}`);
      if (response.ok) {
        const data = await response.json();
        setRestaurants([data]); 
      } else if (response.status === 404) {
        console.error('Restaurant not found');
        setRestaurants([]); 
      } else {
        console.error('Error fetching restaurant by ID:', response.statusText);
      }
    } catch (error) {
      console.error('Error fetching restaurant by ID:', error);
    }
  };

  const handleDeleteRestaurant = async (id) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/restaurants/${id}`, {
        method: 'DELETE',
      });

      if (response.ok) {
        fetchRestaurants();
      } else if (response.status === 404) {
        console.error('Restaurant not found');
      } else {
        console.error('Error deleting restaurant:', response.statusText);
      }
    } catch (error) {
      console.error('Error deleting restaurant:', error);
    }
  };

  return (
    <div>
      <h1>Restaurant List</h1>
      <div>
        {/* <label>Search by ID: </label>
        <input
          type="number"
          value={searchId}
          onChange={(e) => setSearchId(e.target.value)}
        /> */}
        {/* <button onClick={handleSearch}>Search</button> */}
      </div>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Address</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {restaurants.map((restaurant) => (
            <tr key={restaurant.id}>
              <td>
                <Link to={`/restaurants/${restaurant.id}`}>{restaurant.name}</Link>
              </td>
              <td>{restaurant.address}</td>
              <td>
                <button
                  onClick={() => handleDeleteRestaurant(restaurant.id)}
                  style={{ backgroundColor: 'red', color: 'white' }}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default RestaurantList;