/*
Function to fill data witin html element of modal
*/

/*function modelOpen(source, score, author, date) {

	//document.getElementById("myModal").setAttribute("id", model_id);
	document.getElementById("modalHeader").innerHTML = "Data Availability: "+score+"%";

	if (source != "null"){
		document.getElementById("newsSource").innerHTML = `News Source: 
			<a href="https://www.google.com/search?q=`+source+`" style="color: blue;" 
			target="-blank">`+source+`</a>`
	}
	else{
		document.getElementById("newsSource").innerHTML = "";
	}

	if (author != "null" && author != "" && author != source && isNaN(author)){
		document.getElementById("author").innerHTML = `Author: 
			<a href="https://www.google.com/search?q=`+author+` `+source+`
			"style="color: blue;" target="-blank">`+author+`</a>`
	}
	else{
		document.getElementById("author").innerHTML = "";
	}

	if (date != "null"){
		document.getElementById("pubDate").innerHTML = "Published Date: "+date;
	}
	else{
		document.getElementById("pubDate").innerHTML = "";	
	}
}*/

/*
	Function to set attribure of image url in the image within a modal
*/
function ImgModel(imgurl){
	//console.log(imgurl);
	document.getElementById("imgid").setAttribute("src", imgurl);	
}

/* 
	Enable search btn only when text is entered in search bar.
*/
function searchElement(txt) {
        var bt = document.getElementById('srcBtn');
        if (txt.value != '') {
            bt.disabled = false;
        }
        else {
            bt.disabled = true;
        }
    }  

/*
	Remove image div if image failed loading
*/
function imgError(title_id, img_id){
	//console.log(title_id, img_id);
	//document.getElementById(img_id).setAttribute("class", "");
	document.getElementById(img_id).style.display = 'none';
	document.getElementById(title_id).setAttribute("class", "col-12");

}


/*
	Function to set attribure of youtube url in the iframe within model
*/
//https://www.youtube.com/embed/{{d.url|videoid}}?

function ytModel(vid_id){
	url = "https://www.youtube.com/embed/"+vid_id+"?rel=0&autoplay=1"
	document.getElementById("ytplayer").setAttribute("src", url);
}

function closeModal(){
	document.getElementById("ytplayer").setAttribute("src", "");
}

/* refresh current page content */

function refPage(){
	location.reload(true);
}