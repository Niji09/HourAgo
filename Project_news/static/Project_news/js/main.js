/*
Function to fill data witin html element of modal
*/

function modelOpen(source, score, author, date) {

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
}

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
	Add default image if image failed to load
*/
function imgError(img, altimg){
	img.onerror = "";
    img.src = altimg;
    return true;
}

