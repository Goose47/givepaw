import React from "react";
import { Link } from "react-router-dom";
import Dropdown from "./dropdown/Dropdown";
import DropdownItem from "./dropdown/DropdownItem";
import SmallButton from "./buttons/SmallButton";
import { BsGeoAltFill, BsChevronDown } from "react-icons/bs";

const Header = () => {
  return (
    <header className="Header">
      <div className="Header__Left">
        <div className="Header__Logo">
          <Link to="/haha">Как стать донором?</Link>
          <Link to="/haha">Как сдать кровь?</Link>
        </div>
      </div>
      <div className="Header__Right">
        <Dropdown
          title={
            <>
              <span className="Icon__Small Icon__Small--Before">
                <BsGeoAltFill />
              </span>
              <span>Ваш регион</span>
            </>
          }
        >
          <DropdownItem to="hello">Hello</DropdownItem>
          <DropdownItem to="hello">Hello1</DropdownItem>
          <DropdownItem to="hello">Hell2o</DropdownItem>
          <DropdownItem to="hello">Hell3o</DropdownItem>
        </Dropdown>
        <SmallButton to="/sign-in">Войти</SmallButton>
      </div>
    </header>
  );
};

export default Header;
