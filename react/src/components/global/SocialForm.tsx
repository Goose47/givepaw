import React, { useState } from 'react';

const SocialForm = () => {
  const [telegram, setTelegram] = useState('');
  const [vk, setVk] = useState('');

  const handleChange = (event: any, setter: any) => {
    setter(event.target.value);
  };

  const handleSave = (setter: any) => {
    // Perform save action, for example, send data to server
  };

  return (
    <div>
      <div>
        <label htmlFor="facebook">Facebook:</label>
        <input type="text" id="facebook" value={telegram} onChange={(e) => handleChange(e, setTelegram)} />
      </div>
      <div>
        <label htmlFor="twitter">Twitter:</label>
        <input type="text" id="twitter" value={vk} onChange={(e) => handleChange(e, setVk)} />
      </div>
      {/* <div>
        <button onClick={() => handleSave(setTelegram)}>Save Facebook</button>
        <button onClick={() => handleSave(setVk)}>Save Twitter</button>
      </div> */}
    </div>
  );
};

export default SocialForm;
