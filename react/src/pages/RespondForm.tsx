import React from 'react';
import { useLocation } from 'react-router-dom';

const RespondForm = () => {
  const location = useLocation();
  const { deadline, id, place, bloodGroup } = location.state;

  return (
    <div>
      <div>Дата: {deadline}</div>
      <div>Место: {place}</div>
      <div> Группа крови: {bloodGroup}</div>
    </div>
  );
};

export default RespondForm;
