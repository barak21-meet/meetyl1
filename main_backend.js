//To add this in the first HTML use: <script type="text/javascript" src="main_backend.js"></script>
//**In the first page (Celine's) this should be in the head but on the second page (Meera's) it should be inside the body

//Add to Celine's HTML form-tag action and method: <form action="./second_page.html" method="POST">

//!Make sure that when combining all codes that all IDs are the same!

function first()
{
	//saving data from first page using localStorage
	localStorage.setItem("time1",document.getElementById("time1").value);
	localStorage.setItem("time2",document.getElementById("time2").value);
	localStorage.setItem("time3",document.getElementById("time3").value);
	localStorage.setItem("time4",document.getElementById("time4").value);
	localStorage.setItem("time5",document.getElementById("time5").value);
	localStorage.setItem("time6",document.getElementById("time6").value);
	localStorage.setItem("time7",document.getElementById("time7").value);
	localStorage.setItem("want",document.getElementById("want").value);
}

//In order for the elements in the second page to change according to this code you need to append the lines down below in the page below to HTML code
/*
	//these lines will apply to the second page. make sure to use the right ID names.

	<script>
		document.getElementById("second_time1").innerHTML=localStorage.getItem("time1");
		document.getElementById("second_time2").innerHTML=localStorage.getItem("time2");
		document.getElementById("second_time3").innerHTML=localStorage.getItem("time3");
		document.getElementById("second_time4").innerHTML=localStorage.getItem("time4");
		document.getElementById("second_time5").innerHTML=localStorage.getItem("time5");
		document.getElementById("second_time6").innerHTML=localStorage.getItem("time6");
		document.getElementById("second_time7").innerHTML=localStorage.getItem("time7");
		document.getElementById("second_want").innerHTML=localStorage.getItem("want");
	</script>
*/

/* EXAMPLE:

<html>
<head>
<title>my_title</title>
</head>

<body>
...
...
<p id=second_time1>Example that will get the value in "time1"</p>
...
...

<script>
	localStorage.setItem("time1",document.getElementById("time1").value);
	localStorage.setItem("time2",document.getElementById("time2").value);
	localStorage.setItem("time3",document.getElementById("time3").value);
	localStorage.setItem("time4",document.getElementById("time4").value);
	localStorage.setItem("time5",document.getElementById("time5").value);
	localStorage.setItem("time6",document.getElementById("time6").value);
	localStorage.setItem("time7",document.getElementById("time7").value);
	localStorage.setItem("want",document.getElementById("want").value);
</script>
</body>
</html>
*/