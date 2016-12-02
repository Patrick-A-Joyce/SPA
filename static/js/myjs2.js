var Btn = document.getElementById("btn");
var myDiv = document.getElementById("info");


Btn.addEventListener("click", function() {

	var dbRequest = new XMLHttpRequest();
		dbRequest.open('GET', 'http://127.0.0.1:5984/_emails/9f8423e4-22fc-4b41-8677-56ef9ad5591c');
		dbRequest.onload = function() {

			var myData = JSON.parse(dbRequest.responseText);
			renderHTML(myData);
			};

		dbRequest.send();

});


function renderHTML(myData){
		var jData = "<pre>" + myData.message + "<pre>";
		myDiv.insertAdjacentHTML('beforeend', jData);

}
