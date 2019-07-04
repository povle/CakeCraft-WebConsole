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

function getValue(id) {
	return document.getElementById(id);
}

function getRadioValue(id) {
	var btns = document.getElementsById(id).value;
	for (var i = 0; i < btns.length; i++) {
		if (btns[i].checked) return btns[i].value;
	}
	return "";
}

function onSave() {
	document.getElementById("savedWindow").style.display = "block";
}

function playerSubmit() {
	var maxPlayers = getValue("max-players");
	var playerIdleTimeout = getValue("player-idle-timeout");
}

function serverSubmit() {
	var serverPort = getValue("server-port");
	var enableCommandBlock = getRadioValue("enable-command-block");
	var maxTickTime = getValue("max-tick-time");
	var allowFlight = getRadioValue("allow-flight");
	var opPermissionLevel = getValue("op-permission-level");
	var enableWhitelist = getRadioValue("enable-whitelist");
	var enforceWhitelist = getRadioValue("enforce-whitelist");
	var broadcastConsoleToOps = getRadioValue("broadcast-console-to-ops");
	var snooperEnable = getRadioValue("snooper-enabled");
	var useNativeTransport = getRadioValue("native-transport");
	var preventProxyConnections = getRadioValue("prevent-proxy-connections");
	var onlineMode = getValue("online-mode");
	var motd = getValue = getValue("motd");

	//...//

	onSave();
}

function RCONSubmit() {
	var enableRCON = getRadioValue("enable-rcon");
	var broadcastRCONToOps = getRadioValue("broadcast-rcon-to-ops");
	var RCONPort = getValue("rcon-port");
	var RCONPassword = getValue("rcon-password");

	//...//

	onSave();

}

function gameplaySubmit() {
	var difficulty = getRadioValue("difficulty");
	var pvp = getRadioValue("pvp");
	var forceGamemode = getRadioValue("force-gamemode");
	var gamemode = getRadioValue("gamemode");
	var hardcore = getRadioValue("hardcore");
	var allowNether = getRadioValue("allow-nether");

	//...//

	onSave();

}

function spawnSubmit() {
	var spawnProtection = getValue("spawn-protection");
	var spawnAnimals = getValue("spawn-animals");
	var spawnNPCs = getRadioValue("spawn-npcs");
	var spawnMonsters = getRadioValue("spawn-monsters");

	//...//

	onSave();

}

function worldSubmit() {
	var viewDistance = getValue("view-distance");
	var maxWorldSize = getValue("max-world-size");
	var maxBuildHeight = getValue("max-build-height");

	//...//

	onSave();

}