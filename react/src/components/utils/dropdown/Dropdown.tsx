import React, {useEffect, useRef, useState} from 'react'
import DropdownIcon from '../../../icons/DropdownIcon';
import Stays from '../../../icons/Stays';
import Flights from "../../../icons/Flights";
import Cars from '../../../icons/Cars';
import Packages from "../../../icons/Packages";
import Activities from '../../../icons/Activities';
import Cruises from '../../../icons/Cruises';
import DropdownItem from "./DropdownItem";


interface DropdownProps {
    children: React.ReactNode,
    title: string
}

function Dropdown(props: DropdownProps) {


    const [expanded, setExpanded] = useState(false);
    const [clickedOutside, setClickedOutside] = useState(true);

    const handleOpenDropdown = () => {
        setExpanded(!expanded)
    }

    useEffect(() => {
        setExpanded(!clickedOutside)
    }, [clickedOutside]);


    const componentRef = useRef<HTMLDivElement>(null);

    const handleClickOutside = (e: any) => {
        console.log("happened", e)
        if (componentRef.current && !componentRef.current.contains(e.target)) {
            setClickedOutside(true);
        }
    };
    const handleClickInside = () => setClickedOutside(false);

    useEffect(() => {
        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, []);

    return (
        <>
            <div
                onClick={handleClickInside}
                ref={componentRef}
                className="uitk-layout-flex-item uitk-layout-flex-item-flex-basis-zero uitk-layout-flex-item-flex-grow-0 uitk-menu uitk-menu-mounted"
                id="">
                <button onClick={handleOpenDropdown} title="More travel" data-testid="header-menu-button"
                        aria-expanded="false" data-context="global_navigation" type="button"
                        className="uitk-button uitk-button-medium uitk-button-has-text uitk-button-tertiary uitk-menu-trigger global-navigation-nav-button">
                    { props.title }
                    <DropdownIcon />
                </button>
                <div
                    className={`uitk-menu-container uitk-menu-pos-left uitk-menu-container-autoposition uitk-menu-container-has-intersection-root-el ` + (expanded ? 'uitk-menu-open' : '') }
                    aria-hidden="true" style={{"width": "375px"}}>
                    <div>
                        <div>
                            { props.children }
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Dropdown