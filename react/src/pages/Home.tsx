import React from 'react';
import '../scss/main.scss';
import HomeInfo from '../components/Home/HomeInfo';
import HomeRecipientsLibrary from '../components/Home/HomeRecipientsLibrary';

const Home = () => {
  return (
    <div className="Home">
      <HomeInfo />
      <HomeRecipientsLibrary />
    </div>
  );
};

export default Home;
