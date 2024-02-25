import React from 'react';
import "./App.css";
import * as Boxicons from 'react-icons/bi';

import SwiperCore, { Navigation, Pagination, Autoplay } from 'swiper';
import { Swiper, SwiperSlide } from 'swiper/react';

import "./components/main.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Doctor from './components/Doctor';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCoffee, faHeart } from '@fortawesome/free-solid-svg-icons';


import "bootstrap/dist/css/bootstrap.min.css";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import TopBar from './components/TopBar';
//import About from "./components/About";
//import Services from "./components/Services";
import Departments from "./components/Departments";
import Footer from "./components/Footer";
import Contact from './components/Contact';
import Gallery from './components/Gallery';
import FAQ from './components/Faq';
import Testimonials from './components/Testimonials';
import Services from './components/Services';
import Counts from './components/Counts';
import About from './components/About';
import WhyUs from './components/WhyUs';



function App() {
  return (
    <div>
    <TopBar/>
      <Navbar />
      
      <Hero/>
      <WhyUs/>
      <About/>
      <Counts/>
      <Services/>
      
      <Departments/>
      <Doctor/>
      <FAQ/>
      <Testimonials/>
      <Gallery/>




      
      

      
      <Contact/>
      <Footer />
      
    </div>
  );
}

export default App;
