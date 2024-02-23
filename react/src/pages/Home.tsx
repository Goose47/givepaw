import React from 'react';
import '../scss/main.scss';
import HomeHeader from '../components/Home/HomeHeader';
import HomeRecipients from '../components/Home/HomeRecipients';

const Home = () => {
  return (
    <div className="Home">
      <HomeHeader />
      <HomeRecipients />
    </div>
  );
};

export default Home;
