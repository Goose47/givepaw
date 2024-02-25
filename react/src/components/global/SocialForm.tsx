import React, { useState } from 'react';
import { Input } from 'antd';


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
       <label htmlFor="telegram">Telegram</label>
        <Input
          size="large"
          id="telegram"
          placeholder={'@telegramTag'}
          value={telegram}
          type="text"
          onChange={(e) => handleChange(e, setTelegram)}
        />

        <label htmlFor="vk">VK</label>
        <Input
          size="large"
          id="vk"
          placeholder={'https://vk.com/yourname'}
          value={vk}
          type="text"
          onChange={(e) => handleChange(e, setVk)}
        />

    </div>
  );
};

export default SocialForm;
