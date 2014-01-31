function indexChange(element_id){
	Things = document.getElementsByClassName('lab-index')[0].getElementsByTagName('li')
	for (var i = Things.length - 1; i >= 0; i--) {
		Things[i].classList.remove("active");
	};
	element_id.classList.add("active");
}