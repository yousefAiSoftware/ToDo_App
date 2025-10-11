import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './repository/authentication_interface';
import LoginPage from './login_page';
import TasksPage from './task_page';
import './App.css';

const ProtectedRoute = ({ children }) => {
  const { isAuthenticated, loading } = useAuth();
  
  if (loading) {
    return <div>Loading...</div>;
  }
  
  return isAuthenticated ? children : <Navigate to="/login" />;
};

function App() {
  return (
    <AuthProvider>
      <div className="min-h-screen bg-background text-foreground">
        <Router>
          <Routes>
            <Route path="/login" element={<LoginPage />} />
            <Route path="/tasks" element={
              <ProtectedRoute>
                <TasksPage />
              </ProtectedRoute>
            } />
            <Route path="/" element={<Navigate to="/tasks" />} />
          </Routes>
        </Router>
      </div>
    </AuthProvider>
  );
}

export default App;