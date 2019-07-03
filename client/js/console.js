$(document).foundation();

var commandText = document.getElementById("commandText");
var textField = document.getElementById("commandTextField");
//TODO(bumbo): redraw canvas on widow resize!
commandText.width = textField.offsetWidth;
commandText.style.width = textField.offsetWidth + "px";
commandText.height = 500;
commandText.style.height = "500px";

function sendCommand(command) {
	//TODO(bumbo): send the command to the server
}

function commandEnter(event) {	
	if (event.key === "Enter") {
		//TODO(bumbo): add command to the stack
		sendCommand(textField.value);
		textField.value = "";
	}
}

function update() {
	//TODO(bumbo): get commands from the sevrer
	var consoleValue = "" 
	commandText.innerHTML = consoleValue;
}

setInterval(update, 2000);