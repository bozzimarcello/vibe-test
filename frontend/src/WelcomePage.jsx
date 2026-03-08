import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function WelcomePage() {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          navigate('/login');
          return;
        }

        const response = await fetch('http://localhost:8000/welcome/', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });

        if (!response.ok) {
          throw new Error('Failed to fetch user data');
        }

        const data = await response.json();
        setUserData(data);
      } catch (err) {
        setError(err.message);
        console.error('Error fetching user data:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchUserData();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    navigate('/login');
  };

  if (loading) {
    return (
      <div className="d-flex justify-content-center align-items-center min-vh-100">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="d-flex justify-content-center align-items-center min-vh-100">
        <div className="alert alert-danger" role="alert">
          {error}. Please <button className="btn btn-link p-0" onClick={() => navigate('/login')}>login again</button>.
        </div>
      </div>
    );
  }

  return (
    <div className="d-flex justify-content-center align-items-center min-vh-100">
      <div className="login-card text-center">
        <h1 className="login-title h3 mb-4">Welcome!</h1>
        <div className="mb-4">
          <p className="fs-5 mb-2"><strong>Name:</strong> {userData?.message.replace('Welcome back, ', '')}</p>
          <p className="fs-5 mb-2"><strong>Username:</strong> {userData?.username}</p>
          <p className="fs-5"><strong>Email:</strong> {userData?.email}</p>
        </div>
        <button
          className="btn btn-outline-primary w-100"
          onClick={handleLogout}
        >
          Logout
        </button>
      </div>
    </div>
  );
}
