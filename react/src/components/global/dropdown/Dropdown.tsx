import React, { useEffect, useRef, useState } from "react";
import DropdownIcon from "../../../icons/DropdownIcon";
import { BsChevronDown, BsDropbox } from "react-icons/bs";

interface DropdownProps {
  children: React.ReactNode;
  title: React.ReactNode;
}

function Dropdown(props: DropdownProps) {
  const [expanded, setExpanded] = useState(false);
  const [clickedOutside, setClickedOutside] = useState(true);

  const handleOpenDropdown = () => {
    setExpanded(!expanded);
  };

  useEffect(() => {
    setExpanded(!clickedOutside);
  }, [clickedOutside]);

  const componentRef = useRef<HTMLDivElement>(null);

  const handleClickOutside = (e: any) => {
    console.log("happened", e);
    if (componentRef.current && !componentRef.current.contains(e.target)) {
      setClickedOutside(true);
    }
  };
  const handleClickInside = () => setClickedOutside(false);

  useEffect(() => {
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <>
      <div
        onClick={handleClickInside}
        ref={componentRef}
        className="Dropdown"
        id=""
      >
        <button
          onClick={handleOpenDropdown}
          type="button"
          className="Dropdown__Button"
        >
          {props.title}
          <span className="Icon__Small">
            <BsChevronDown />
          </span>
        </button>
        <div
          className={
            `Dropdown__Content` +
            (expanded ? "_active" : "")
          }
          aria-hidden="true"
          style={{ width: "375px" }}
        >
          <div>
            <div>{props.children}</div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Dropdown;
