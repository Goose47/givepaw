import React, { useState } from 'react';
import '@egjs/react-flicking/dist/flicking.css';
import Flicking from '@egjs/react-flicking';

const HomeRecipientsLibrary = () => {
  const [panels, setPanels] = useState([0, 1, 2, 3, 4]);

  return (
    <div className="HomeRecipients">
      <Flicking
        align="prev"
        circular={true}
        onMoveEnd={(e) => {
          console.log(e);
        }}
      >
        <div className="flicking-panel has-background-primary has-text-white is-size-1 ">1</div>
        <div className="flicking-panel has-background-primary has-text-white is-size-1 ">2</div>
        <div className="flicking-panel has-background-primary has-text-white is-size-1 ">3</div>
      </Flicking>
    </div>
  );
};

export default HomeRecipientsLibrary;
