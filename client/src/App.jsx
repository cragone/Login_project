import React from 'react';
import { Route, Routes, BrowserRouter as Router } from 'react-router-dom';
import LoginPage from './containers/LoginPage';

function App() {
  return (
    <div>
      <div>
        <Navbar />
      </div>
      <Router>
        <Routes>
          <Route path="/login" element={<LoginPage />} />

        </Routes>
      </Router>
    </div>
  );
}

export default App;