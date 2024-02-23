import React, {ReactNode} from 'react'

interface RouterWrapperProps {
    children : ReactNode
}

function RouterWrapper(props : RouterWrapperProps) {

    return (
        <div className="container">
            { props.children }
        </div>

    )

}

export default RouterWrapper