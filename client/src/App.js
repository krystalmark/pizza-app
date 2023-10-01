import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

import CreateRestaurantPizza from './components/CreateRestaurantPizza';
import PizzaList from './components/PizzaList';
import RestaurantList from './components/RestaurantList';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/pizzas">Pizza List</Link>
            </li>
            
            <li>
              <Link to="/create-restaurant-pizza">Create Restaurant Pizza</Link>
            </li>
            <li>
              <Link to="/">Restaurant List</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/pizzas" element={<PizzaList />} />
          <Route path="/create-restaurant-pizza" element={<CreateRestaurantPizza />} />
          <Route path="/" element={<RestaurantList />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
