import React from 'react';

function Navbar() {
  return (
    <header id="header" className="fixed-top">
      <div className="container d-flex align-items-center">
        <h1 className="logo me-auto"><a href="index.html">Consultiva</a></h1>
        {/* Uncomment below if you prefer to use an image logo */}
        {/* <a href="index.html" className="logo me-auto"><img src="assets/img/logo.png" alt="" className="img-fluid" /></a> */}

        <nav id="navbar" className="navbar order-last order-lg-0">
          <ul>
            <li><a className="nav-link scrollto active" href="#hero">Home</a></li>
            <li><a className="nav-link scrollto" href="#about">About</a></li>
            <li><a className="nav-link scrollto" href="#services">Services</a></li>
            <li><a className="nav-link scrollto" href="#departments">Departments</a></li>
            <li><a className="nav-link scrollto" href="#doctors">Doctors</a></li>
            <li className="dropdown">
              <a href="#">
                <span>Health Tool</span>
                <i className="bi bi-chevron-down"></i>
              </a>
              <ul>
                <li><a href="https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm">BMI Calculator</a></li>
                
                <li><a href="https://www.calculator.net/calorie-calculator.html">Calorie Calculator</a></li>
                <li><a href="https://www.nhs.uk/pregnancy/finding-out/due-date-calculator/">Due Date Calculator</a></li>
                <li><a href="https://www.adityabirlacapital.com/healthinsurance/active-together/health-tools/cost-of-smoking/">Cost of Smoking Calculator</a></li>
              </ul>
            </li>
            <li><a className="nav-link scrollto" href="#contact">Contact</a></li>
          </ul>
          <i className="bi bi-list mobile-nav-toggle"></i>
        </nav>

        <a href="http://localhost:8501/" target="_blank" className="appointment-btn scrollto">
          <span className="d-none d-md-inline">Predict your </span> Disease
        </a>
      </div>
    </header>
  );
}

export default Navbar;
