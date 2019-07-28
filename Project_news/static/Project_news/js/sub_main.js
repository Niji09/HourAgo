/* get the url of browser and make selected nav link active */
	
var baseUrl = "http://127.0.0.1:8000/" // http://www.hourago.in/
var currentURL = window.location.href;
//console.log(currentURL);
var ele = document.getElementsByClassName("active");
//console.log(ele);
ele[0].setAttribute("class", "nav-link");

if(currentURL==baseUrl){
	document.getElementById("topheadline").setAttribute("class", "nav-link active");
}
else if(currentURL.includes("business")){
	document.getElementById("business").setAttribute("class", "nav-link active");
}
else if(currentURL.includes("entertainment")){
	document.getElementById("entertainment").setAttribute("class", "nav-link active");
}
else if(currentURL.includes("health")){
	document.getElementById("health").setAttribute("class", "nav-link active");
}
else if(currentURL.includes("science")){
	document.getElementById("science").setAttribute("class", "nav-link active");
}
else if(currentURL.includes("sports")){
	document.getElementById("sports").setAttribute("class", "nav-link active");
}
else if(currentURL.includes("technology")){
	document.getElementById("technology").setAttribute("class", "nav-link active");
}
else if(currentURL.includes("news_source")){
	document.getElementById("news_source").setAttribute("class", "nav-link active");
}
else if(currentURL.includes("yt_news")){
	document.getElementById("yt_news").setAttribute("class", "nav-link active");
}

 /*<script>*/
	var badges = document.getElementsByClassName("badge");
	for(var i=0; i<badges.length; i++){
		var score =parseFloat(badges[i].innerText.substring(19));
		if (score>=85.0){
			badges[i].setAttribute("class", "badge badge-success");
			badges[i].setAttribute("style", "color: #111;");
		}
		else if (score>=70.0){
			badges[i].setAttribute("class", "badge badge-warning");
		}
		else{
			badges[i].setAttribute("class", "badge badge-danger");
		}
	}
/*</script>*/

/*<script>*/
	function searchIcon(){

		document.getElementById("brand-icon").style.display = "none";
		document.getElementById("search-icon").style.display = "none";
		document.getElementById("menu-icon").style.display = "none";

		document.getElementById("search-bar").style.display = "block";
		document.getElementById("remove-icon").style.display = "block";
	}

	function removeIcon(){

		document.getElementById("search-bar").style.display = "none";
		document.getElementById("remove-icon").style.display = "none";

		document.getElementById("brand-icon").style.display = "block";
		document.getElementById("search-icon").style.display = "block";
		document.getElementById("menu-icon").style.display = "block";
	}
/*</script>*/