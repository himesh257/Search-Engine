const electron = require('electron')
const { app, BrowserWindow } = require('electron')
const gs = electron.globalShortcut

let win;

function createWindow () {
  //win = new BrowserWindow({resizable: false, width: 850, height: 550})
  win = new BrowserWindow()
  win.loadFile('/home/himesh/Desktop/FinalProject/main.html')
 
  gs.register('Control+R', function(){
     win.reload();
  })
}

app.on('ready', createWindow)
