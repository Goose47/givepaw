import '../scss/main.scss';
import HomeHeader from '../components/Home/HomeHeader';

const Home = () => {
  return (
    <div className="Home">
      <HomeHeader />
      <HomeRecipients />
    </div>
  );
};

export default Home;
