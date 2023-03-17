"use strict";

/**
 * login/register Transtion
 */

var Log_form = document.getElementById("Log_form");
var Reg_form = document.getElementById("Reg_form");
var indicator = document.getElementById("indicator");

function Login() {
  Reg_form.style.transform = "translate(300px)";
  Log_form.style.transform = "translate(300px)";
  indicator.style.transform = "translate(0px)";
}

function Register() {
  Reg_form.style.transform = "translate(0px)";
  Log_form.style.transform = "translate(0px)";
  indicator.style.transform = "translate(100px)";
}

/**
 * Light/Dark Mode
 */

const toggle = document.getElementById("toggleDark");
const body = document.querySelector("body");
const logo1 = document.getElementById("logo1");
const logo2 = document.getElementById("logo2");

let mode = localStorage.getItem("mode");

if (mode == "true") {
  logo1.src = "static/Images/Predict.ai logo Black.png";
  logo2.src = "static/Images/Predict.ai logo Black.png";
  body.classList.add("Light-theme");
} else {
  logo1.src = "static/Images/Predict.ai logo White.png";
  logo2.src = "static/Images/Predict.ai logo White.png";
  body.classList.remove("Light-theme");
}

toggle.addEventListener("click", function () {
  this.classList.toggle("bi-brightness-high-fill");
  if (this.classList.toggle("bi-moon")) {
    localStorage.setItem("mode", "true");
    logo1.src = "static/Images/Predict.ai logo Black.png";
    logo2.src = "static/Images/Predict.ai logo Black.png";
    body.classList.add("Light-theme");
    body.style.transition = "1.5s";
  } else {
    localStorage.setItem("mode", "false");
    logo1.src = "static/Images/Predict.ai logo White.png";
    logo2.src = "static/Images/Predict.ai logo White.png";
    body.classList.remove("Light-theme");
    body.style.transition = "1.5s";
  }
});

/**
 * add event on element
 */

const addEventOnElem = function (elem, type, callback) {
  if (elem.length > 1) {
    for (let i = 0; i < elem.length; i++) {
      elem[i].addEventListener(type, callback);
    }
  } else {
    elem.addEventListener(type, callback);
  }
};

/**
 * navbar toggle
 */

const navbar = document.querySelector("[data-navbar]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");
const navToggler = document.querySelector("[data-nav-toggler]");

const toggleNavbar = function () {
  navbar.classList.toggle("active");
  navToggler.classList.toggle("active");
  document.body.classList.toggle("active");
};

addEventOnElem(navToggler, "click", toggleNavbar);

const closeNavbar = function () {
  navbar.classList.remove("active");
  navToggler.classList.remove("active");
  document.body.classList.remove("active");
};

addEventOnElem(navbarLinks, "click", closeNavbar);

/**
 * header active
 */

const header = document.querySelector("[data-header]");

const activeHeader = function () {
  if (window.scrollY > 300) {
    header.classList.add("active");
  } else {
    header.classList.remove("active");
  }
};

addEventOnElem(window, "scroll", activeHeader);

/**
 * toggle active on add to fav
 */

const addToFavBtns = document.querySelectorAll("[data-add-to-fav]");

const toggleActive = function () {
  this.classList.toggle("active");
};

addEventOnElem(addToFavBtns, "click", toggleActive);

/**
 * scroll revreal effect
 */

const sections = document.querySelectorAll("[data-section]");

const scrollReveal = function () {
  for (let i = 0; i < sections.length; i++) {
    if (sections[i].getBoundingClientRect().top < window.innerHeight / 1.5) {
      sections[i].classList.add("active");
    } else {
      sections[i].classList.remove("active");
    }
  }
};

scrollReveal();



addEventOnElem(window, "scroll", scrollReveal);
$(function () {
  if ($("body").is("body404")) {
    document.addEventListener("DOMContentLoaded", function () {
      var body = document.body;
      setInterval(createStar, 100);
      function createStar() {
        var right = Math.random() * 500;
        var top = Math.random() * screen.height;
        var star = document.createElement("div");
        star.classList.add("star");
        body.appendChild(star);
        setInterval(runStar, 10);
        star.style.top = top + "px";
        function runStar() {
          if (right >= screen.width) {
            star.remove();
          }
          right += 3;
          star.style.right = right + "px";
        }
      }
    });
  }
});


