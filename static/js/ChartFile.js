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