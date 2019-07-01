$(document).foundation();

var backups = [];

var htmlBackups = document.getElementById("backupList");

function loadBackup(id) {
	//TODO(bumbo): load backup and use it as current
}

function deleteBackup(id) {
	backups.pop(id);
	htmlBackups.deleteRow(id);
}

function pushRow(targetId, backup) {
	var backupRow = htmlBackups.insertRow(targetId);
	var indexCell = backupRow.insertCell(0);
	var nameCell = backupRow.insertCell(1);
	var dateCell = backupRow.insertCell(2);
	var loadButton = backupRow.insertCell(3);
	var deleteButton = backupRow.insertCell(4);

	indexCell.innerHTML = targetId + "";
	nameCell.innerHTML = backup.name;
	var date = new Date(backup.timestamp);
	var h = "0" + date.getHours();
	var m = "0" + date.getMinutes();
	var s = "0" + date.getSeconds();
	var d = "0" + date.getDay();
	var mm = new Intl.DateTimeFormat('en-US', {month:"long"}).format(date);
	var y = date.getFullYear();
	var formattedTime = h.substr(-2) + ":" + m.substr(-2) + ":" + s.substr(-2) + " " + d.substr(-2) + " " + mm.substr(0, 3) + " " + y;
	dateCell.innerHTML = formattedTime;
	loadButton.innerHTML = "<button class=\"hollow button\" onclick=\"loadBackup(" + targetId + ")\">Load</button>";
	deleteButton.innerHTML = "<button class=\"hollow button alert\" onclick=\"deleteBackup(" + targetId + ")\">Delete</button>";
}

function addRow(backup) {
	var targetId = 0;
	for (var i = 0; i < backups.length; i++) {
		if (backup.timestamp > backups[i].timestamp) {
			targetId = i - 1;
			break;
		}
	}

	backups.splice(targetId, 0, backup);
	pushRow(targetId, backup);
}

function updateBackupList() {
	//TODO(bumbo): load backups using API

	htmlBackups.innerHTML = "";
	for(var i = 0; i < backups.length; i ++) {
		pushRow(i, backups[i]);
	}	
}