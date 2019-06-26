$(document).foundation()

var autoRefreshIsOn = false;

document.getElementsByName("serverStart")[0].addEventListener('click', serverStart);
document.getElementsByName("serverStop")[0].addEventListener('click', serverStop);
document.getElementsByName("statsRefresh")[0].addEventListener('click', statsRefresh);
document.getElementsByName("autoRefreshEnabled")[0].addEventListener('input', autoRefreshEnabled);
var autoRefreshRate = document.getElementsByName("autoRefreshRate")[0];
var autoRefreshRateSlider = document.getElementsByName("autoRefreshRateSlider")[0];
autoRefreshRate.addEventListener('input', autoRefreshRate);
var lastAutoRefreshTimer;

var cpuLabel = document.getElementsByName("cpuLabel")[0];
var ramLabel = document.getElementsByName("ramLabel")[0];
var diskLabel = document.getElementsByName("discLabel")[0];
var cpuProgress = document.getElementsByName("cpuProgress")[0];
var ramProgress = document.getElementsByName("ramProgress")[0];
var diskProgress = document.getElementsByName("diskProgress")[0];

var cpuUsed = 75;
var ramUsed = 5;
var spaceUsed = 95;

function serverStart() {
	//TODO(bumbo): use API to start the server
}

function serverStop() {
	//TODO(bumbo): use API to stop the server
}

function statsRefresh() {
	//TODO(bumbo): use API to get the values
	cpuUsed += 20;
	ramUsed += 20;
	spaceUsed -= 20;
	if (spaceUsed < 0) spaceUsed += 100;
	if (cpuUsed > 100) cpuUsed = 0;
	if (ramUsed > 100) ramUsed = 0;

	cpuLabel.innerHTML = 'CPU (' + cpuUsed + '%)';
	ramLabel.innerHTML = 'RAM (' + ramUsed + '%)';
	diskLabel.innerHTML = 'Disk space used (' + spaceUsed + '%)';
	cpuProgress.setAttribute("style", "width:" + cpuUsed + "%");
	ramProgress.setAttribute("style", "width:" + ramUsed + "%");
	diskProgress.setAttribute("style", "width:" + spaceUsed + "%");
}

function autoRefreshEnabled() {
	if (autoRefreshIsOn) {
		clearInterval(lastAutoRefreshTimer);
		autoRefreshRate.setAttribute("disabled", "");
		autoRefreshRateSlider.classList.add("disabled");
	} else {
		lastAutoRefreshTimer = setInterval(statsRefresh, autoRefreshRate.value);
		autoRefreshRate.removeAttribute("disabled");
		autoRefreshRateSlider.classList.remove("disabled");
	}
	autoRefreshIsOn = !autoRefreshIsOn;
}

function autoRefreshRate() {
	clearInterval(lastAutoRefreshTimer);
	lastAutoRefreshTimer = setInterval(statsRefresh, autoRefreshRate.value);
}

function httpGet(theUrl) {
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", theUrl, false); // false for synchronous request
	xmlHttp.send(null);
	return xmlHttp.responseText;
}