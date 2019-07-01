$(document).foundation();

var autoRefreshIsOn = false;

//TODO(bumbo): mark it in HTML
document.getElementById("serverStart").addEventListener('click', serverStart);
document.getElementById("serverStop").addEventListener('click', serverStop);
document.getElementById("statsRefresh").addEventListener('click', statsRefresh);

var cpuLabel = document.getElementById("cpuLabel");
var ramLabel = document.getElementById("ramLabel");
var diskLabel = document.getElementById("discLabel");
var cpuProgress = document.getElementById("cpuProgress");
var ramProgress = document.getElementById("ramProgress");
var diskProgress = document.getElementById("diskProgress");

var cpuUsed = 75;
var ramUsed = 5;
var spaceUsed = 95;

var baseAddress = "https://IP:port/method/";
//TODO(bumbo): having secret key right here in js is not a good idea!
var key_secret = "123";
var xhttp = new XMLHttpRequest();

function httpGet(theUrl) {
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", theUrl, false); 
	xmlHttp.send(null);
	return xmlHttp.responseText;
}

function serverStart() {
	//TODO(bumbo): use API to start the server
}

function serverStop() {
	//TODO(bumbo): use API to stop the server
}

function statsRefresh() {
	//TODO(bumbo): use API to get the values
	//NOTE(bumbo): TEST CODE!!!
	cpuUsed += 20;
	ramUsed += 20;
	spaceUsed -= 20;
	if (spaceUsed < 0) spaceUsed += 100;
	if (cpuUsed > 100) cpuUsed = 0;
	if (ramUsed > 100) ramUsed = 0;
	
	//var ramUsageResponce = httpGet(baseAddress + "stats.get_ram_usage?secret=" + key_secret + "&format=percent");

	cpuLabel.innerHTML = 'CPU (' + cpuUsed + '%)';
	ramLabel.innerHTML = 'RAM (' + ramUsed + '%)';
	diskLabel.innerHTML = 'Disk space used (' + spaceUsed + '%)';
	cpuProgress.setAttribute("style", "width:" + cpuUsed + "%");
	ramProgress.setAttribute("style", "width:" + ramUsed + "%");
	diskProgress.setAttribute("style", "width:" + spaceUsed + "%");
}