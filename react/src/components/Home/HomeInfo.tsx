import React from 'react';
import { BiDonateBlood } from 'react-icons/bi';
import { MdHealing } from 'react-icons/md';
import { Link } from 'react-router-dom';

const HomeInfo = () => {
  return (
    <div className="HomeHeader">
      <div className="HomeHeader__Wrapper">
        <div className="HomeHeader__Info">
          <div className='HomeHeader__Content'>
          <h1>Подайте лапу помощи нуждающимся животным</h1>
          <h2>Банк крови GivePaw</h2>
          
          </div>
          <img src="images/givepaw.png" alt="#" height={"500px"} />
        </div>
      </div>
      <div>
         
      </div>
      
      <div className="HomeHeader__Buttons">
        <Link to={'donor-form'}>
          <div className="HomeHeader__Button">
            <div>
              <div className="HomeHeader__Button__Icon">
                <BiDonateBlood />
              </div>
              <div>Стать донором</div>
            </div>
          </div>
        </Link>
        <Link to={'recipient-form'}>
          <div className="HomeHeader__Button">
            <div>
              <div className="HomeHeader__Button__Icon">
                <MdHealing />
              </div>

              <div>Нужна кровь</div>
            </div>
          </div>
        </Link>
      </div>
    </div>
  );
};

export default HomeInfo;
