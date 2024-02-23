import React from 'react';
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import RouterWrapper from "./RouterWrapper";
import Menu from "./components/Header/Header";
import Home from './components/Home/Home'
import Login from "./components/Login/Login";

export const APP_URL = 'http://localhost:3000/'

function App() {

    const router = createBrowserRouter([
        {
            path: "/",
            element: <RouterWrapper><Home /></RouterWrapper>,
        },
        {
            path: "/sign-in",
            element: <RouterWrapper><Login /></RouterWrapper>,
        },
    ]);

    return (
        <>
            <React.StrictMode>
                <RouterProvider router={router} />
            </React.StrictMode>
        </>

    )
}

export default App