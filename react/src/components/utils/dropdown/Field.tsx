import React from 'react'

interface FieldProps {
    label: string,
    id: string,
    type ?: string,
    value: string,
    setValue: (e: string) => void
}

function Field(props: FieldProps) {
    return <>
        <div className="uitk-field has-floatedLabel-label has-no-placeholder">
            <label htmlFor={props.id} className="uitk-field-label is-visually-hidden">{ props.label }</label>
            <input value={props.value} onChange={(e: any) => props.setValue(e.target.value)} type={props.type ? props.type : 'text'} id={props.id} name={props.id} className={"uitk-field-input replay-reveal " + (!props.value ? 'empty-placeholder' : '')} aria-required="false" aria-invalid="false"/>
            <div className="uitk-field-label" aria-hidden="true">{ props.label }</div>
        </div>
    </>
}

export default Field