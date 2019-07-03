$(document).foundation();

var autoRefreshIsOn = false;

var cpuLabel = document.getElementById("cpuLabel");
var ramLabel = document.getElementById("ramLabel");
var diskLabel = document.getElementById("discLabel");
var cpuProgress = document.getElementById("cpuProgress");
var ramProgress = document.getElementById("ramProgress");
var diskProgress = document.getElementById("diskProgress");

var baseAddress = "https://IP:port/method/";
//TODO: having secret key right here, in js might be not a good idea!
var key_secret = "123";
var xhttp = new XMLHttpRequest();

function httpGet(theUrl) {
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", theUrl, false); 
	xmlHttp.send(null);
	return xmlHttp.responseText;
}

function serverStart() {
	//TODO: use API to start the server
}

function serverStop() {
	//TODO: use API to stop the server
}

function statsRefresh() {
	//TODO: use API to get the values

	//var ramUsageResponce = httpGet(baseAddress + "stats.get_ram_usage?secret=" + key_secret + "&format=percent");

	var ramUsed;
	var cpuUsed
	var spaceUsed;

	//TODO(bumbo): change progress bar attributes depending on ramUsed, cpuUsed, spaceUsed values.
	cpuLabel.innerHTML = 'CPU (' + cpuUsed + '%)';
	ramLabel.innerHTML = 'RAM (' + ramUsed + '%)';
	diskLabel.innerHTML = 'Disk space used (' + spaceUsed + '%)';
	cpuProgress.setAttribute("style", "width:" + cpuUsed + "%");
	ramProgress.setAttribute("style", "width:" + ramUsed + "%");
	diskProgress.setAttribute("style", "width:" + spaceUsed + "%");
}