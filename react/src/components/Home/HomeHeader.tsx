import React from 'react';
import { BiDonateBlood } from 'react-icons/bi';
import { MdHealing } from 'react-icons/md';

const HomeHeader = () => {
  return (
    <div className="HomeHeader">
      <div className="HomeHeader__Wrapper">
        <div className="HomeHeader__Background">
          <img src="images/header.jpg" alt="#" />
        </div>
        <div className="HomeHeader__Content">
          <h1>Банк крови Donor.Search</h1>
          <p>
            Вы готовы помогать другим животным и хотите узнать больше подробностей про донорство? <br />
            Вам нужна кровь или другие препараты для питомца и хотите узнать, как ее получить?
          </p>
        </div>
      </div>
      <div className="HomeHeader__Buttons">
        <div className="HomeHeader__Button">
          <div>
            <div className="HomeHeader__Button__Icon">
              <BiDonateBlood />
            </div>
            <div>Стать донором</div>
          </div>
        </div>
        <div className="HomeHeader__Button">
          <div>
            <div className="HomeHeader__Button__Icon">
              <MdHealing />
            </div>
            <div>Нужна кровь</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomeHeader;
