import React, { useState } from 'react';

// Function to check if a date is a holiday (you may need to replace this with your own implementation)
const isHoliday = (date : Date) => {
  const day = date.getDay();
  return day === 0 || day === 6; // 0 represents Sunday, 6 represents Saturday
};

const DateSelector = (props : any) => {
  const [selectedDate, setSelectedDate] = useState(null);

  // Function to handle date selection
  const handleDateSelect = (event : any) => {
    props.onChange(event.target.value)
    setSelectedDate(event.target.value);
  };

  // Function to generate an array of dates for the next two weeks
  const generateDates = () => {
    const dates = [];
    const today = new Date();
    const twoWeeksLater = new Date(today.getTime() + 14 * 24 * 60 * 60 * 1000);

    while (today < twoWeeksLater) {
      // Exclude weekends and holidays
      if (today.getDay() !== 0 && today.getDay() !== 6 && !isHoliday(today)) {
        dates.push(new Date(today));
      }
      today.setDate(today.getDate() + 1);
    }

    return dates;
  };

  return (
    <div className="date-selector-container">
      <div className="date-options">
        {generateDates().map((date, index) => (
          <div key={index} className="date-option">
            <input
              type="radio"
              id={`date${index}`}
              name="selectedDate"
              value={date.toISOString().split('T')[0]}
              onChange={handleDateSelect}
              checked={selectedDate === date.toISOString().split('T')[0]}
            />
            <label htmlFor={`date${index}`}>
              { date.toLocaleDateString('ru-RU') }
            </label>
          </div>
        ))}
      </div>
    </div>
  );
};

export default DateSelector;
