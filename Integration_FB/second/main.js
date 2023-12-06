const fetch = require('electron-fetch').default
const { app , BrowserWindow } = require('electron')
const axios = require('axios').default;

function createWindow () {
let win = new BrowserWindow({
width: 800,
height: 600,
webPrefernces: {
nodeIntegration: true
}
})

win.loadFile('index.html')
win.webContents.openDevTools()
}
app.whenReady().then(createWindow)

// fetch('http://127.0.0.1:8000/first/')
// .then(res => res.json())
// .then(json => console.log(json))

// const body = {}
// fetch('http://127.0.0.1:8000/first/',{
// method: 'POST',
// body: JSON.stringify(body),
// headers:{'Content-Type':'application/json'},
// })
// .then(res => res.json())
// .then(json => console.log(json))

axios.post('http://127.0.0.1:8000/first/', {
name: "Fred",
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});

// axios.post('http://127.0.0.1:8000/scoring_values/', {
// TBT_Allowed:"tbt_allowed",
// TBT_Completed:"tbt_completed",
// Wo_Attend: "wo_attend",
// Lab_InAug:"lab_inaug"
// })
// .then(function (response) {
// console.log(response);
// })
// .catch(function (error) {
// console.log(error);
// });

app.on('window-all-closed',() => {

if(process.platform !== 'darwin'){
app.quit()
}
})

app.on('activate',() =>{
if (BrowserWindow.getAllWindows().length === 0){
createWindow()
}
})