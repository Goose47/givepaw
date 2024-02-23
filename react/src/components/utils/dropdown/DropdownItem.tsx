import React from 'react'

interface DropdownItemProps {
    children: React.ReactNode,
    to: string
}

function DropdownItem(props : DropdownItemProps) {
    return <>
        <div
            className="uitk-layout-flex-item uitk-list uitk-layout-flex-item-flex-basis-zero uitk-layout-flex-item-flex-grow-0">
            <a href={ props.to } rel=""
               className="uitk-link uitk-list-item uitk-link-align-left uitk-link-layout-default uitk-link-medium">
                <div className="uitk-text uitk-type-300 uitk-text-default-theme">
                    { props.children }
                </div>
            </a>
        </div>
    </>
}

export default DropdownItem