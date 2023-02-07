//Creating a promise method. The promise will get resolved when timer times out after 6 seconds.
let promiseOne = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Promise 1 resolved");
  }, 6000);
});

//Creating a promise method. The promise will get resolved when timer times out after 3 seconds.
let promiseTwo = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Promise 2 resolved");
  }, 3000);
});

//Console log before calling the promise
console.log("Before calling promise");

//Call the promise and wait for it to be resolved and then print a message.
promiseOne.then((successMessage) => {
  console.log("From Callback 1 " + successMessage);
});

promiseTwo.then((successMessage) => {
  console.log("From Callback 2 " + successMessage);
});

//Console log after calling the promise
console.log("After calling promise");
