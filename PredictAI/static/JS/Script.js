
/**
 * Preloader
 */

$(function () {
  "use strict";

	setTimeout(function () {
		$('.loader_bg').fadeToggle();
	}, 500);
});



/**
 * login/register Transtion
 */

// These functions are used to create a sliding transition effect between a login form and 
// a registration form. The Login() function slides both forms to the right and moves an indicator 
// element to the left, while the Register() function slides both forms to the left and moves the 
// indicator element to the right. The translate() CSS function is used to move the elements horizontally.

// Select the login form, registration form, and indicator elements
var Log_form = document.getElementById("Log_form");
var Reg_form = document.getElementById("Reg_form");
var indicator = document.getElementById("indicator");
// Function to slide the login and registration forms to the right and move the indicator to the left
function Login() {
  Reg_form.style.transform = "translate(300px)";
  Log_form.style.transform = "translate(300px)";
  indicator.style.transform = "translate(0px)";
}
// Function to slide the login and registration forms to the left and move the indicator to the right
function Register() {
  Reg_form.style.transform = "translate(0px)";
  Log_form.style.transform = "translate(0px)";
  indicator.style.transform = "translate(100px)";
}





/**
 * Light/Dark Mode
 */

// This code selects elements from the HTML document and updates them based on 
// whether the user has set dark mode or not. The toggle button changes the mode 
// between light and dark, and updates the logo and body accordingly. The comments 
// explain what each section of the code does, making it easy to understand and modify.

// Select the toggle button and body element
const toggle = document.getElementById("toggleDark");
const body = document.querySelector("body");
// Select the logo images (white and black versions)
const logo1 = document.getElementById("logo1");
const logo2 = document.getElementById("logo2");

// Check if user has set dark mode previously
let mode = localStorage.getItem("mode");
// If dark mode is set, update the logo and body with dark theme class
if (mode == "true") {
  logo1.src = "static/Images/Predict.ai logo Black.png";
  logo2.src = "static/Images/Predict.ai logo Black.png";
  body.classList.add("Light-theme");
} else {
    // Otherwise, use light mode
  logo1.src = "static/Images/Predict.ai logo White.png";
  logo2.src = "static/Images/Predict.ai logo White.png";
  body.classList.remove("Light-theme");
}


// Add event listener to toggle button
toggle.addEventListener("click", function () {
    // Toggle the class for the icon
  this.classList.toggle("bi-brightness-high-fill");
  // Toggle the class for the icon and update the mode in local storage
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
 * Home Trend Navigation
 */



// Select the element with id "Trend_content"
var Trend_content = document.getElementById("Trend_content");
// When the window loads
window.onload = function() {
  // Select the elements with ids "Nav_EGX30", "Nav_EGP", and "Nav_Gold"
  var Nav_EGX30 = document.getElementById("Nav_EGX30");
  var Nav_EGP = document.getElementById("Nav_EGP");
  var Nav_Gold = document.getElementById("Nav_Gold");
  // If all three elements exist
  if (Nav_EGX30 && Nav_EGP && Nav_Gold) {
    // Hide the elements by setting their display property to "none"
    Nav_EGX30.style.display = "none";
    Nav_EGP.style.display = "none";
    Nav_Gold.style.display = "none";
  }
};

// Select the elements with ids "Tbtn", "Ebtn", "Ubtn", and "Gbtn"
var Tbtn = document.getElementById("Tbtn");
var Ebtn = document.getElementById("Ebtn");
var Ubtn = document.getElementById("Ubtn");
var Gbtn = document.getElementById("Gbtn");

// Function to show Trending content
function NavTrend() {
  // Add the "active" class to the Trending button and remove it from the other buttons
  Tbtn.classList.add('active');
  Ebtn.classList.remove('active');
  Ubtn.classList.remove('active');
  Gbtn.classList.remove('active');
  // Show the Trending content and hide the other content
  Trend_content.style.display = "grid";
  Nav_EGX30.style.display = "none";
  Nav_EGP.style.display = "none";
  Nav_Gold.style.display = "none";
}

// Function to show EGX30 content
function NavEGX30() {
  // Add the "active" class to the EGX30 button and remove it from the other buttons
  Tbtn.classList.remove('active');
  Ebtn.classList.add('active');
  Ubtn.classList.remove('active');
  Gbtn.classList.remove('active');
  // Show the EGX30 content and hide the other content
  Trend_content.style.display = "none";
  Nav_EGX30.style.display = "block";
  Nav_EGP.style.display = "none";
  Nav_Gold.style.display = "none";
}

// Function to show EGP content
function NavEGP() {
  // Add the "active" class to the EGP button and remove it from the other buttons
  Tbtn.classList.remove('active');
  Ebtn.classList.remove('active');
  Ubtn.classList.add('active');
  Gbtn.classList.remove('active');
  // Show the EGP content and hide the other content
  Trend_content.style.display = "none";
  Nav_EGX30.style.display = "none";
  Nav_EGP.style.display = "block";
  Nav_Gold.style.display = "none";
}

// Function to show Gold content
function NavGold() {
  // Add the "active" class to the Gold button and remove it from the other buttons
  Tbtn.classList.remove('active');
  Ebtn.classList.remove('active');
  Ubtn.classList.remove('active');
  Gbtn.classList.add('active');
  // Show the Gold content and hide the other content
  Trend_content.style.display = "none";
  Nav_EGX30.style.display = "none";
  Nav_EGP.style.display = "none";
  Nav_Gold.style.display = "block";
}



/**
 * add event on element
 */

// This is a function that takes 3 arguments: an element, an event type, and a callback function
const addEventOnElem = function (elem, type, callback) {
  // If elem is an array of elements
  if (elem.length > 1) {
    // Loop through each element and add the event listener to each one
    for (let i = 0; i < elem.length; i++) {
      elem[i].addEventListener(type, callback);
    }
    // If elem is a single element
  } else {
    // Add the event listener to the element
    elem.addEventListener(type, callback);
  }
};



/**
 * navbar toggle
 */

// selects the element with the "data-navbar" attribute and assigns it to the variable "navbar".
const navbar = document.querySelector("[data-navbar]");
// selects all elements with the "data-nav-link" attribute and assigns them to the variable "navbarLinks".
const navbarLinks = document.querySelectorAll("[data-nav-link]");
// selects the element with the "data-nav-toggler" attribute and assigns it to the variable "navToggler".
const navToggler = document.querySelector("[data-nav-toggler]");
// is defined to toggle the "active" class on the navbar, navToggler, 
// and document.body elements when the navToggler is clicked. 
const toggleNavbar = function () {
  navbar.classList.toggle("active");
  navToggler.classList.toggle("active");
  document.body.classList.toggle("active");
};
// is called to add a "click" event listener to the navToggler 
// element that triggers the toggleNavbar function when clicked.
addEventOnElem(navToggler, "click", toggleNavbar);

// is defined to remove the "active" class from the navbar, 
// navToggler, and document.body elements when any navbar link is clicked. 
const closeNavbar = function () {
  navbar.classList.remove("active");
  navToggler.classList.remove("active");
  document.body.classList.remove("active");
};
// The "addEventOnElem" function is called again to add a "click" event 
// listener to all navbarLinks elements that triggers the closeNavbar function when clicked.
addEventOnElem(navbarLinks, "click", closeNavbar);



/**
 * header active
 */

// Select the element with a data attribute of "data-header"
const header = document.querySelector("[data-header]");
// Define a function that adds or removes the "active" class based on the user's scroll position
const activeHeader = function () {
  if (window.scrollY > 300) {
    header.classList.add("active");
  } else {
    header.classList.remove("active");
  }
};

// Call a function to add a "scroll" event listener to the window element that triggers the activeHeader function when the user scrolls
addEventOnElem(window, "scroll", activeHeader);



/**
 * toggle active on add to fav
 */

// Select all elements with the "data-add-to-fav" attribute and assign them to the constant "addToFavBtns"
const addToFavBtns = document.querySelectorAll("[data-add-to-fav]");
// Define a function "toggleActive" that toggles the "active" class on the clicked element
const toggleActive = function () {
  this.classList.toggle("active");
};

// Attach a "click" event listener to all elements in the "addToFavBtns" collection, and call the "toggleActive" function when clicked
addEventOnElem(addToFavBtns, "click", toggleActive);



/**
 * scroll revreal effect
 */
// Select all elements with the "data-section" attribute
const sections = document.querySelectorAll("[data-section]");

// Create a function that checks if an element is within view and adds/removes "active" class accordingly
const scrollReveal = function () {
  for (let i = 0; i < sections.length; i++) {
    if (sections[i].getBoundingClientRect().top < window.innerHeight / 1.5) {
      sections[i].classList.add("active");
    } else {
      sections[i].classList.remove("active");
    }
  }
};

// Call the function once to apply the "active" class to elements in view
scrollReveal();


// Add a "scroll" event listener to the window that triggers the scrollReveal function
addEventOnElem(window, "scroll", scrollReveal);
// Wait for the DOM to load and check if the body has the class "body404"
$(function () {
  if ($("body").is("body404")) {
    document.addEventListener("DOMContentLoaded", function () {
      var body = document.body;
      // Create a star every 100ms and animate it to the right
      setInterval(createStar, 100);
      function createStar() {
        var right = Math.random() * 500;
        var top = Math.random() * screen.height;
        var star = document.createElement("div");
        star.classList.add("star");
        body.appendChild(star);
        // Animate the star to the right until it reaches the screen edge or is removed from the DOM
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

