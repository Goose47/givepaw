import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <>
      <div className="Footer">
        <div className="Footer__Boxes">
          <div className="Footer__Box">
            <h3>О донорстве</h3>
            <ul>
              <li>
                <Link to="#">Донорство крови</Link>
              </li>
              <li>
                <Link to="#">Как стать донором?</Link>
              </li>
              <li>
                <Link to="#">Где сдать кровь?</Link>
              </li>
              <li>
                <Link to="#">Требования к донору</Link>
              </li>
              <li>
                <Link to="#">Костный мозг</Link>
              </li>
            </ul>
          </div>
          <div className="Footer__Box">
            <h3>О Donor.Search</h3>
            <ul>
              <li>
                <Link to="#">Наш магазин</Link>
              </li>
              <li>
                <Link to="#">Журнал</Link>
              </li>
              <li>
                <Link to="#">Мероприятия</Link>
              </li>
            </ul>
          </div>
          <div className="Footer__Box">
            <h3>НКО</h3>
            <ul>
              <li>
                <Link to="#">Об организации</Link>
              </li>
              <li>
                <Link to="#">Помочь проекту</Link>
              </li>
              <li>
                <Link to="#">Найти донора</Link>
              </li>
              <li>
                <Link to="#">Спецпроекты</Link>
              </li>
              <li>
                <Link to="#">Награды</Link>
              </li>
            </ul>
          </div>
          <div className="Footer__Box">
            <h3>Наши партнеры</h3>
            <ul>
              <li>
                <Link to="#">Благодарности</Link>
              </li>
              <li>
                <Link to="#">Партнеры</Link>
              </li>
            </ul>
          </div>
          <div className="Footer__Box">
            <h3>Организациям</h3>
            <ul>
              <li>
                <Link to="#">Партнерство с бизнесом</Link>
              </li>
              <li>
                <Link to="#">HR и донорство</Link>
              </li>
              <li>
                <Link to="#">Бизнес и донорство</Link>
              </li>
              <li>
                <Link to="#">Бонусная программа</Link>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div className="Footer__Message">
        <div>
          DonorSearch © 2010-2024.Все права защищены. <br />
          Если не указано иное, все материалы сайта доступны по лицензии Creative Commons CC-BY-SA 4.0. <br />
          Прочтите нашу политику конфиденциальности и пользовательское соглашение. <br />
        </div>
      </div>
    </>
  );
};

export default Footer;
