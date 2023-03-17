const e = require("express");
const express = require("express");
const router = express.Router();

let users = [
  {
    firstName: "John",
    lastName: "wick",
    email: "johnwick@gamil.com",
    DOB: "22-01-1990",
  },
  {
    firstName: "John",
    lastName: "smith",
    email: "johnsmith@gamil.com",
    DOB: "21-07-1983",
  },
  {
    firstName: "Joyal",
    lastName: "white",
    email: "joyalwhite@gamil.com",
    DOB: "21-03-1989",
  },
];

// GET request: Retrieve all users
router.get("/", (req, res) => {
  // Copy the code here
  res.send(JSON.stringify({ users }, null, 4)); //This line is to be replaced with actual return value
});

// GET by specific ID request: Retrieve a single user with email ID
router.get("/:email", (req, res) => {
  // Copy the code here
  const email = req.params.email;
  const filteredUser = users.filter((user) => user.email === email);
  res.send(filteredUser); //This line is to be replaced with actual return value
});

// GET by lastname: Retrieve all users with same last name
router.get("/lastname/:lastname", (req, res) => {
  const lastName = req.params.lastname;
  const usersFiltered = users.filter((user) => user.lastName === lastName);
  res.send(usersFiltered);
});

// GET sorted list of users: Retrieve all users and sort and send
function getDateFromString(strDate) {
  let [dd, mm, yyyy] = strDate.split("-");
  return new Date(yyyy + "/" + mm + "/" + dd);
}

router.get("/sort", (req, res) => {
  let sorted_users = users.sort(function (a, b) {
    let d1 = getDateFromString(a.DOB);
    let d2 = getDateFromString(b.DOB);
    return d1 - d2;
  });
  console.log(sorted_users);
  res.send(sorted_users);
});

// POST request: Create a new user
router.post("/", (req, res) => {
  // Copy the code here
  queryParams = req.query;
  const firstName = queryParams.firstName;
  const lastName = queryParams.lastName;
  const email = queryParams.email;
  const DOB = queryParams.DOB;

  const newUser = {
    firstName: firstName,
    lastName: lastName,
    email: email,
    DOB: DOB,
  };

  users.push(newUser);

  res.send("The user " + firstName + " has been added"); //This line is to be replaced with actual return value
});

// PUT request: Update the details of a user by email ID
router.put("/:email", (req, res) => {
  // Copy the code here
  const email = req.params.email;
  let updatingUser = users.filter((user) => user.email === email);
  if (updatingUser) {
    updatingUser = updatingUser[0];
    const firstName = req.query.firstName;
    const lastName = req.query.lastName;
    const DOB = req.query.DOB;
    if (firstName) {
      updatingUser.firstName = firstName;
    }
    if (lastName) {
      updatingUser.lastName = lastName;
    }
    if (DOB) {
      updatingUser.DOB = DOB;
    }
    // remove the user from the array and add the updated user
    users = users.filter((user) => user.email != email);
    users.push(updatingUser);
    res.send("User with the email " + email + " has been updated");
  } else {
    res.send("Unable to find the user with email: " + email);
  }
  // res.send("Yet to be implemented"); //This line is to be replaced with actual return value
});

// DELETE request: Delete a user by email ID
router.delete("/:email", (req, res) => {
  // Copy the code here
  const email = req.params.email;
  users = users.filter((user) => user.email != email);
  res.send("User with the email " + email + " has been deleted"); //This line is to be replaced with actual return value
});

module.exports = router;
