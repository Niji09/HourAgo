var nav_opened = false;
var nav_closed = true;
/*
console.log("openNav", nav_opened)
console.log('closeNav', nav_closed)
*/

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  nav_opened = true;
  nav_closed = false;
  //console.log("openNav", nav_opened)
  //console.log('closeNav', nav_closed)
  if(nav_opened){
	document.getElementById("nav-menu").setAttribute("onclick", "closeNav()");
	//console.log('Attibute changed to closeNav()')
}
}

function closeNav() {
  	document.getElementById("mySidenav").style.width = "0px";
  	nav_opened = false;
  	nav_closed = true;
  	//console.log("openNav", nav_opened)
	//console.log('closeNav', nav_closed)
  	if(nav_closed){
	document.getElementById("nav-menu").setAttribute("onclick", "openNav()");
	//console.log('Attibute changed to openNav()')
}
}
