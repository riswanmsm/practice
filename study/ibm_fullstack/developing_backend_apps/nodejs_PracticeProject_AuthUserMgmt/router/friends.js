const express = require("express");

const router = express.Router();

var friends = {
  "johnsmith@gamil.com": {
    firstName: "John",
    lastName: "Doe",
    DOB: "22-12-1990",
  },
  "annasmith@gamil.com": {
    firstName: "Anna",
    lastName: "smith",
    DOB: "02-07-1983",
  },
  "peterjones@gamil.com": {
    firstName: "Peter",
    lastName: "Jones",
    DOB: "21-03-1989",
  },
};

// GET request: Retrieve all friends
router.get("/", (req, res) => {
  res.send(JSON.stringify(friends, null, 4));
});

// GET by specific ID request: Retrieve a single friend with email ID
router.get("/:email", (req, res) => {
  const email = req.params.email;
  res.send(friends[email]);
});

// POST request: Add a new friend
router.post("/", (req, res) => {
  const email = req.body.email;
  if (email) {
    friends[email] = {
      firstName: req.body.firstName,
      lastName: req.body.lastName,
      DOB: req.body.DOB,
    };
  }
  res.send(`The user ${req.body.firstName} has been added`);
});

// PUT request: Update the details of a friend with email id
router.put("/:email", (req, res) => {
  const email = req.params.email;
  // choose the friend for editing and assign it to change it. The changes will effect the original object
  let friend = friends[email];

  if (friend) {
    const firstName = req.body.firstName;
    const lastName = req.body.lastName;
    const DOB = req.body.DOB;
    // if the firstName lastName or DOB value has been given in body then change those values
    firstName && (friend.firstName = firstName);
    lastName && (friend.lastName = lastName);
    DOB && (friend.DOB = DOB);

    res.send(`Friend with the email  ${email} updated.`);
  } else {
    res.send("Invalid Email has been given please correct the email");
  }
});

// DELETE request: Delete a friend by email id
router.delete("/:email", (req, res) => {
  const email = req.params.email;
  if (email && friends[email]) {
    delete friends[email];
    res.send("Friend with the email " + email + " has been deleted.");
  } else {
    res.send("The email entered is not available");
  }
});

module.exports = router;
