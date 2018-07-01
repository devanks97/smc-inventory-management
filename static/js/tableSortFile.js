function sortTable(n) {
  var table, rows, switching, i, x, y, dir;
  // document.getElementsByTagName("thead")[0].getElementsByTagName("th")[0].classList.contains("sorted")
  table = document.getElementById("graphResultsTable");
  switching = true;
/*Make a loop that will continue until
no switching has been done:*/
  rows = table.getElementsByTagName("TR");
  if(rows[0].children[n].classList.contains("ascending"))
  {
	dir = "desc";
	rows[0].children[n].classList.toggle("ascending");
	rows[0].children[n].children[0].children[1].classList.toggle("ascending")
	rows[0].children[n].classList.toggle("descending");
	rows[0].children[n].children[0].children[1].classList.toggle("descending")
  }
  else if(rows[0].children[n].classList.contains("descending"))
  {
	dir = "asc";
	rows[0].children[n].classList.toggle("ascending");
	rows[0].children[n].children[0].children[1].classList.toggle("ascending")
	rows[0].children[n].classList.toggle("descending");
	rows[0].children[n].children[0].children[1].classList.toggle("descending")
  }
  else
  {
	dir = "asc";
	sortedElements = document.getElementsByClassName("sorted");
	if(sortedElements.length != 0)
	{
		for (i = 0; i < (sortedElements.length); i++)
		{
			sortedElements[i].classList.remove("sorted");
			sortedElements[i].classList.remove("ascending");
			sortedElements[i].classList.remove("descending");
		}
	}
	rows[0].children[n].classList.toggle("ascending");
	rows[0].children[n].children[0].children[1].classList.toggle("ascending")
	rows[0].children[n].classList.toggle("sorted");
  }
  while (switching)
  {
	//start by saying: no switching is done:
	switching = false;
	/*Loop through all table rows (except the
	first, which contains table headers):*/
	for (i = 1; i < (rows.length - 1); i++)
	{
	  /*Get the two elements you want to compare,
	  one from current row and one from the next:*/
	  if(n!=2)
	  {
		  x = rows[i].getElementsByTagName("TD")[n].childNodes[1].innerHTML;
		  y = rows[i + 1].getElementsByTagName("TD")[n].childNodes[1].innerHTML;
		  /*check if the two rows should switch place,
		  based on the direction, asc or desc:*/
		  if (dir == "asc")
		  {
			if (x.toLowerCase() > y.toLowerCase())
			{
			  //if so, mark as a switch and break the loop:
			  rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
			  switching = true;
			  break;
			}
		  } else if (dir == "desc")
		  {
			if (x.toLowerCase() < y.toLowerCase())
			{
			  //if so, mark as a switch and break the loop:
			  rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
			  switching = true;
			  break;
			}
		  }
	  }
	  else
	  {
	  x = Number(rows[i].getElementsByTagName("TD")[n].innerHTML);
	  y = Number(rows[i+1].getElementsByTagName("TD")[n].innerHTML);
	  /*check if the two rows should switch place,
	  based on the direction, asc or desc:*/
	  if (dir == "asc")
	  {
		if (x > y)
		{
		  //if so, mark as a switch and break the loop:
		  rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
		  switching = true;
		  break;
		}
	  }
	  else if (dir == "desc")
	  {
		if (x < y)
		{
		  //if so, mark as a switch and break the loop:
		  rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
		  switching = true;
		  break;
		}
	  }
	  }
	}
  }
}