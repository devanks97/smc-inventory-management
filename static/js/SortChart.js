function renderCanvas(){
	document.getElementById("activateChart").style.display = "none";
	tbodyTaggedElements = document.getElementsByTagName("tbody")[0];
	trTaggedElements = tbodyTaggedElements.children;
	length = trTaggedElements.length; 
	var i;
	var j;
	var labelList = [];


	for(i=0;i<length;i++)
	{
		
		tempRow = trTaggedElements[i];
		tempDepartment = tempRow.children[0].innerText;
		tempDevice = tempRow.children[1].innerText;
		tempTotal = tempRow.children[2].innerText;
		if(!labelList[tempDepartment])
		{
			labelList[tempDepartment] = {lt:0,pc:0,aio:0};
		}
		
		if(tempDevice[0] == "L")
		{
			labelList[tempDepartment].lt = tempTotal;
		}
		else if(tempDevice[0] == "P")
		{
			labelList[tempDepartment].pc = tempTotal;
		}
		else
		{
			labelList[tempDepartment].aio = tempTotal;
		}

	}

	var departmentList = [];
	var departmentListPC = [];
	var departmentListLaptop = [];
	var departmentListAIO = [];
	for(var key in labelList) {
	  if(labelList.hasOwnProperty(key)) 
	  { //to be safe
		departmentListPC.push(labelList[key].pc);
		departmentListLaptop.push(labelList[key].lt);
		departmentListAIO.push(labelList[key].aio);
		departmentList.push(key);
	  }
	}


	var summaryBarChartElement = document.getElementById("summaryBarChart");
	summaryBarChartElement.style.display = "block";
	document.getElementById("closeChart").style.display = "block";
	var ctx = summaryBarChartElement.getContext('2d');
	var myChart = new Chart(ctx, {
		type: 'bar',
		data: {
			labels: departmentList,
			datasets: [{
				label: 'PC',
				data: departmentListPC,
				backgroundColor:'rgba(255, 99, 132, 0.5)',
				borderColor:'rgba(255,99,132,1)',
				borderWidth: 1
			},
			{
				label: 'Laptop',
				data: departmentListLaptop,
				backgroundColor:'rgba(54, 162, 235, 0.5)',
				borderColor:'rgba(54, 162, 235, 1)',
				borderWidth: 1
			},
			{
				label: 'All In One',
				data: departmentListAIO,
				backgroundColor:'rgba(255, 206, 86, 0.5)',
				borderColor:'rgba(255, 206, 86, 1)',
				borderWidth: 1
			}
			
			]
		},
		options: {
			scales: {
				yAxes: [{
					ticks: {
						beginAtZero:true
					}
				}]
			}
		}
	});
}
function hideCanvas(){
	var summaryBarChartElement = document.getElementById("summaryBarChart");
	summaryBarChartElement.style.display = "none";
	document.getElementById("closeChart").style.display = "none";
	document.getElementById("activateChart").style.display = "block";
}
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