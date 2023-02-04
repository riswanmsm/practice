const fs = require("fs");

const data = fs.readFile("./read_sample.txt", "utf-8", (err, data) => {
  if (err) throw err;
  console.log(data);
});

// read file using readFileSync
const data_rfs = fs.readFileSync("./read_sample.txt"); // blocks here until file is read
console.log(data_rfs); //writes data in the content.md file to the console

// os information using os module
var os = require("os");
console.log("Computer OS Platform Info : " + os.platform());
console.log("Computer OS Architecture Info: " + os.arch());

// path module
const path = require("path");
let result = path.basename("/content/index/home.html");
console.log(result); //outputs home.html to the console

// util module
var util = require("util");
var str = "The loop has executed %d time(s).";
for (let i = 1; i <= 10; i++) {
  console.log(util.format(str, i)); //outputs "The loop has executed <i> time(s)
}

// url module
const url = require("url");
let webAddress =
  "http://localhost:2000/index.html?lastName=Kent&firstName=Clark";
const qry = url.parse(webAddress, true);
const qrydata = qry.query; //returns an object: {lastName: 'Kent', firstName: 'Clark'} console.log(qrydata.firstName); //returns Clark
console.log(qrydata);

// querystring module
let qryStr = require("querystring");
let qryParams = qryStr.parse("lastName=Kent&firstName=Clark");
console.log(qryParams.firstName); //returns Clark
