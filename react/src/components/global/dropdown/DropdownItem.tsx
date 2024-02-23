import React from "react";

interface DropdownItemProps {
  children: React.ReactNode;
  to: string;
}

function DropdownItem(props: DropdownItemProps) {
  return (
    <>
      <div className="DropdownItem">
        <a href={props.to} rel="" className="DropdownItem__Link">
          <div className="DropdownItem__Title">{props.children}</div>
        </a>
      </div>
    </>
  );
}

export default DropdownItem;
