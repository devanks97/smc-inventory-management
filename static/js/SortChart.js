function rainbow(numOfSteps, step)
{
	var r, g, b;
    var h = step / numOfSteps;
    var i = ~~(h * 6);
    var f = h * 6 - i;
    var q = 1 - f;
    switch(i % 6)
	{
		case 0: r = 1; g = f; b = 0; break;
		case 1: r = q; g = 1; b = 0; break;
		case 2: r = 0; g = 1; b = f; break;
		case 3: r = 0; g = q; b = 1; break;
		case 4: r = f; g = 0; b = 1; break;
		case 5: r = 1; g = 0; b = q; break;
    }
    var c = "rgba(" + parseInt(("00" + (~ ~(r * 255)).toString(16)).slice(-2), 16)+ "," + parseInt(("00" + (~ ~(g * 255)).toString(16)).slice(-2), 16)+ "," + parseInt(("00" + (~ ~(b * 255)).toString(16)).slice(-2), 16)+ ",0.6)";
    return (c);
}
function renderCanvas(){
	document.getElementById("activateChart").style.display = "none";
	tbodyTaggedElements = document.getElementsByTagName("tbody")[0];
	trTaggedElements = tbodyTaggedElements.children;
	length = trTaggedElements.length; 
	var i;
	var j;
	var labelList = {};
	var list_devices = [];
	var dropdownUL_device_element =  document.getElementById("dropdownUL_device");
	var list_devices_elements_a = dropdownUL_device_element.getElementsByTagName("a");
	var selected_device = dropdownUL_device_element.getElementsByClassName("selected")[0].children[0].innerText;
	if(selected_device == "All")
	{
		for(i=1;i<list_devices_elements_a.length;i++)
		{
			list_devices.push(list_devices_elements_a[i].innerText);
		}
	}
	else
	{
		list_devices.push(selected_device);
	}
	var list_departments = [];
	var dropdownUL_department_element = document.getElementById("dropdownUL_department");
	var list_departments_elements_a = dropdownUL_department_element.getElementsByTagName("a");
	var selected_department = dropdownUL_department_element.getElementsByClassName("selected")[0].children[0].innerText;
	if(selected_department == "All")
	{
		for(i=1;i<list_departments_elements_a.length;i++)
		{
			list_departments.push(list_departments_elements_a[i].innerText);
		}
	}
	else
	{
		list_departments.push(selected_department);
	}
	for(j=0;j<list_departments.length;j++)
	{
		temp_department = list_departments[j];
		labelList[temp_department] = {};
		for(i=0;i<list_devices.length;i++)
		{
			tempDevice = list_devices[i];
			labelList[temp_department][tempDevice] = 0;
		}
	}
	
	for(i=0;i<length;i++)
	{
		tempRow = trTaggedElements[i];
		tempDepartment = tempRow.children[0].getElementsByTagName("a")[0].innerHTML;
		tempDevice = tempRow.children[1].getElementsByTagName("a")[0].innerHTML;
		tempTotal = tempRow.children[2].innerText;
		labelList[tempDepartment][tempDevice] = Number(tempTotal);

	}

	var departmentList = {};
	for(var x in list_devices)
	{
		tempDevice=list_devices[x];
		departmentList[tempDevice] = [];
	}
	departmentList["Departments"] = [];
	for(var key in labelList) {
		for(var x in list_devices)
		{
			tempDevice=list_devices[x];
			departmentList[tempDevice].push(labelList[key][tempDevice]);
		}
		departmentList["Departments"].push(key);
	}


	var summaryBarChartElement = document.getElementById("summaryBarChart");
	summaryBarChartElement.style.display = "block";
	document.getElementById("closeChart").style.display = "block";
	var ctx = summaryBarChartElement.getContext('2d');
	var myChart = new Chart(ctx, {
		type: 'bar',
		data: {
			labels: departmentList["Departments"],
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
	var colorStep = 0;
	for(var x in list_devices)
	{
		tempDevice=list_devices[x];
		myChart.data.datasets.push({label:tempDevice,data:departmentList[tempDevice],backgroundColor:rainbow(10,colorStep)});
		colorStep++;
	}
	myChart.update();
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