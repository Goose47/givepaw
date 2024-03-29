import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { store } from './redux/store';
import { Provider } from 'react-redux';
import ScrollToTop from './util/ScrollToTop';

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <Provider store={store}>
    <App />
  </Provider>
);
