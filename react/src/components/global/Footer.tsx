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
                <Link to="haha">Донорство крови</Link>
              </li>
              <li>
                <Link  to="haha">Как стать донором?</Link>
              </li>
              <li>
                <Link  to="haha">Где сдать кровь?</Link>
              </li>
              <li>
                <Link  to="haha">Требования к донору</Link>
              </li>
            </ul>
          </div>
          <div className="Footer__Box">
            <h3>О GivePaw</h3>
            <ul>
              <li>
                <Link  to="haha">Наш магазин</Link>
              </li>
              <li>
                <Link  to="haha">Журнал</Link>
              </li>
              <li>
                <Link  to="haha">Мероприятия</Link>
              </li>
            </ul>
          </div>
          <div className="Footer__Box">
            <h3>НКО</h3>
            <ul>
              <li>
                <Link  to="haha">Об организации</Link>
              </li>
              <li>
                <Link  to="haha">Помочь проекту</Link>
              </li>
              <li>
                <Link  to="haha">Найти донора</Link>
              </li>
              <li>
                <Link  to="haha">Спецпроекты</Link>
              </li>
              <li>
                <Link  to="haha">Награды</Link>
              </li>
            </ul>
          </div>
          <div className="Footer__Box">
            <h3>Наши партнеры</h3>
            <ul>
              <li>
                <Link  to="haha">Благодарности</Link>
              </li>
              <li>
                <Link  to="haha">Партнеры</Link>
              </li>
            </ul>
          </div>
          <div className="Footer__Box">
            <h3>Организациям</h3>
            <ul>
              <li>
                <Link  to="haha">Партнерство с бизнесом</Link>
              </li>
              <li>
                <Link  to="haha">HR и донорство</Link>
              </li>
              <li>
                <Link  to="haha">Бизнес и донорство</Link>
              </li>
              <li>
                <Link  to="haha">Бонусная программа</Link>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div className="Footer__Message">
        <div>
          GivePaw © 2010-2024.Все права защищены. <br />
          Если не указано иное, все материалы сайта доступны по лицензии Creative Commons CC-BY-SA 4.0. <br />
          Прочтите нашу политику конфиденциальности и пользовательское соглашение. <br />
        </div>
      </div>
    </>
  );
};

export default Footer;
