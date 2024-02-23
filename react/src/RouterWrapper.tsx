import React, { ReactNode } from "react";
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";

interface RouterWrapperProps {
  children: ReactNode;
}

function RouterWrapper(props: RouterWrapperProps) {
  return (
    <>
      <Header />
      <div className="container">{props.children}</div>
      <Footer />
    </>
  );
}

export default RouterWrapper;
