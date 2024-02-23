import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import RouterWrapper from './RouterWrapper';
import Menu from './components/global/Header';
import Home from './pages/Home';
import Login from './pages/Login';
import { ConfigProvider } from 'antd';
import axios from "axios";

axios.defaults.baseURL = "https://dev.api.uvuv643.ru"

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
      path: '/sign-in',
      element: (
        <RouterWrapper>
          <Login />
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
