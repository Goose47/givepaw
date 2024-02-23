import React from 'react'
import Dropdown from "../utils/dropdown/Dropdown";
import Communicate from "../../icons/Communicate";
import Languages from "../../icons/Languages";
import DropdownItem from "../utils/dropdown/DropdownItem";
import Flights from "../../icons/Flights";
import Cars from "../../icons/Cars";
import Packages from "../../icons/Packages";
import Activities from "../../icons/Activities";
import Cruises from "../../icons/Cruises";
import SmallButton from "../utils/buttons/SmallButton";

function Menu() {
    return (
        <header className="global-navigation-site-header">
            <div className="global-navigation-site-header-container">
                <section className="global-navigation-row primary">
                    <div className="global-navigation-row-container">
                        <div
                            className="uitk-layout-flex uitk-layout-flex-align-items-center uitk-layout-flex-flex-wrap-nowrap uitk-spacing uitk-spacing-margin-unset uitk-spacing-padding-inlinestart-six uitk-spacing-padding-small-inlineend-three uitk-spacing-padding-medium-inlineend-three uitk-spacing-padding-large-inlineend-two uitk-spacing-padding-extra_large-inlineend-two uitk-layout-flex-item uitk-layout-flex-item-flex-grow-1">
                            <a className="uitk-header-brand-logo" href="https://www.expedia.com/">
                                <img src="images/Logo.png" alt="expedia logo"/>
                            </a>
                            <div
                                className="uitk-layout-flex uitk-layout-flex-align-items-center uitk-layout-flex-justify-content-flex-start uitk-layout-flex-flex-wrap-nowrap uitk-spacing uitk-spacing-padding-inlinestart-one uitk-layout-flex-item uitk-layout-flex-item-flex-basis-half_width uitk-layout-flex-item-flex-grow-1"
                                id="primary-navigation">
                                <Dropdown title="Категории">
                                    <DropdownItem to=""><Flights/>Flights</DropdownItem>
                                    <DropdownItem to=""><Cars/>Cars</DropdownItem>
                                    <DropdownItem to=""><Packages/>Packages</DropdownItem>
                                    <DropdownItem to=""><Activities/>Things to do</DropdownItem>
                                    <DropdownItem to=""><Cruises/>Cruises</DropdownItem>
                                    <DropdownItem to="">Groups &amp; meetings</DropdownItem>
                                    <DropdownItem to="">Deals</DropdownItem>
                                    <DropdownItem to="">Magazine</DropdownItem>
                                </Dropdown>
                            </div>
                            <div
                                className="uitk-layout-flex uitk-layout-flex-align-items-center uitk-layout-flex-justify-content-flex-end uitk-layout-flex-flex-wrap-nowrap uitk-layout-flex-item uitk-layout-flex-item-flex-basis-half_width uitk-layout-flex-item-flex-grow-1">
                                <button type="button" className="uitk-button uitk-button-medium uitk-button-tertiary global-navigation-nav-button">
                                    <Languages/>
                                    English
                                </button>
                                <a href="/" className="uitk-button uitk-button-medium uitk-button-has-text uitk-button-as-link uitk-button-tertiary uitk-layout-flex-item global-navigation-nav-button uitk-layout-flex-item-flex-basis-zero uitk-layout-flex-item-flex-grow-0">
                                    List your property
                                </a>
                                <a href="/service/" className="uitk-button uitk-button-medium uitk-button-has-text uitk-button-as-link uitk-button-tertiary uitk-layout-flex-item global-navigation-nav-button uitk-layout-flex-item-flex-basis-zero uitk-layout-flex-item-flex-grow-0">
                                    Support
                                </a>
                                <a href="/trips" className="uitk-button uitk-button-medium uitk-button-has-text uitk-button-as-link uitk-button-tertiary uitk-layout-flex-item global-navigation-nav-button uitk-layout-flex-item-flex-basis-zero uitk-layout-flex-item-flex-grow-0">
                                    Trips
                                </a>
                                <a href="/inbox/notifications">
                                    <button type="button" className="uitk-button uitk-button-large uitk-button-tertiary uitk-button-only-icon global-navigation-nav-button">
                                        <div className="uitk-layout-position uitk-layout-position-display-inline-block uitk-layout-position-relative">
                                            <Communicate/>
                                        </div>
                                    </button>
                                </a>
                                <SmallButton to="sign-in">Sign in</SmallButton>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        </header>
    )
}

export default Menu