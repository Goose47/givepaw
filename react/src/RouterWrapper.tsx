import React, { ReactNode } from 'react';
import Header from './components/global/Header';
import Footer from './components/global/Footer';

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
