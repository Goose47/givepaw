import React from 'react'
import {Link} from "react-router-dom";

interface SmallButtonProps {
    children: React.ReactNode,
    to: string
    icon ?: React.ReactNode
}

function SmallButton(props: SmallButtonProps) {
    return <>
        <div>
            <Link to={props.to}
               className="uitk-button uitk-button-small uitk-button-has-text uitk-button-as-link uitk-button-secondary uitk-layout-flex-item">
                { props.icon }
                <div className="uitk-text uitk-type-300 uitk-text-white-space-nowrap uitk-text-default-theme">
                    { props.children }
                </div>
            </Link>
        </div>
    </>
}

export default SmallButton