function toggleDropdown(selEle) {
	elementToToggle = selEle.nextElementSibling;
	allDropdowns = document.getElementsByClassName("dropdown-content");
	for(i = 0; i < allDropdowns.length; i++)
	{
		if(elementToToggle != allDropdowns[i] && allDropdowns[i].classList.contains("show"))
			allDropdowns[i].classList.toggle("show");
    }
    elementToToggle.classList.toggle("show");
}

function filterFunction(selEle) {
    var input, filter, ul, li, a, i;
    input = selEle;
    filter = input.value.toUpperCase();
    div = selEle.nextElementSibling;
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++)
	{
        if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}
