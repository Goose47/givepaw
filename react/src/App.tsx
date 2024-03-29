import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import RouterWrapper from './RouterWrapper';
import Home from './pages/Home';
import Login from './pages/Login';
import { ConfigProvider } from 'antd';
import axios from 'axios';
import Register from './pages/Register';
import RecipientForm from './pages/RecipientForm';
import DonorForm from './pages/DonorForm';
import Mockup from './pages/Mockup';
import Profile from './pages/Profile';
import RecipientsLibrary from './components/Recipient/RecipientsLibrary';
import RespondForm from './pages/RespondForm';
import AnimalForm from "./pages/AnimalForm";
import ProfileEdit from './pages/ProfileEdit';
import ChangePasswordForm from './pages/ChangePasswordForm';

axios.defaults.baseURL = 'https://dev.api.uvuv643.ru';
axios.defaults.withCredentials = true;

function App() {
  const router = createBrowserRouter([
    {
      path: '/',
      element: (
        <RouterWrapper>
          <Home />
        </RouterWrapper>
      ),
    },
    {
      path: '/login',
      element: (
        <RouterWrapper>
          <Login />
        </RouterWrapper>
      ),
    },
    {
      path: '/profile-edit',
      element: (
        <RouterWrapper>
          <ProfileEdit/>
        </RouterWrapper>
      ),
    },
    {
      path: '/password-edit',
      element: (
        <RouterWrapper>
          <ChangePasswordForm/>
        </RouterWrapper>
      ),
    },
    {
      path: '/register',
      element: (
        <RouterWrapper>
          <Register />
        </RouterWrapper>
      ),
    },
    {
      path: '/recipient-form',
      element: (
        <RouterWrapper>
          <AnimalForm mode="recipient" />
        </RouterWrapper>
      ),
    },
    {
      path: '/donor-form',
      element: (
        <RouterWrapper>
          <AnimalForm mode="donor" />
        </RouterWrapper>
      ),
    },
    {
      path: '/respond-form/:id',
      element: (
        <RouterWrapper>
          <AnimalForm mode="respond" />
        </RouterWrapper>
      ),
    },
    {
      path: '/donor/:id',
      element: (
        <RouterWrapper>
          <DonorForm />
        </RouterWrapper>
      ),
    },
    {
      path: '/recipient/:id',
      element: (
        <RouterWrapper>
          <RecipientForm />
        </RouterWrapper>
      ),
    },
    {
      path: '/respond/:pet/:id',
      element: (
        <RouterWrapper>
          <RespondForm />
        </RouterWrapper>
      ),
    },
    {
      path: '/profile',
      element: (
        <RouterWrapper>
          <Profile />
        </RouterWrapper>
      ),
    },
    {
      path: '/recipients',
      element: (
        <RouterWrapper>
          <RecipientsLibrary />
        </RouterWrapper>
      ),
    },
    {
      path: '*',
      element: (
        <RouterWrapper>
          <Mockup />
        </RouterWrapper>
      ),
    },
  ]);

  return (
    <>
      <ConfigProvider
        theme={{
          token: {
            fontFamily: 'Inter',
            fontSize: 14,
            colorPrimary: '#f63e3e',
          },
        }}
      >
        <React.StrictMode>
          <RouterProvider router={router} />
        </React.StrictMode>
      </ConfigProvider>
    </>
  );
}

export default App;
