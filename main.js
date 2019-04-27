const electron = require('electron')
const { app, BrowserWindow } = require('electron')

let win;

function createWindow () {
  win = new BrowserWindow({resizable: false, width: 850, height: 550})
  win.loadFile('/home/himesh/Desktop/FinalProject/main.html')
}

app.on('ready', createWindow)
