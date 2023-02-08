const express = require("express");
const jsontoken = require("jsonwebtoken");
const JWT_SECRET = "MoonIsNotBlue@2023";
const app = express();

app.use(express.json());

app.post("/signin", (req, res) => {
  const { username, pwd } = req.body;
  if (username === "riswan" && pwd === "Moon") {
    return res.json({
      token: jsontoken.sign(
        {
          user: "riswan",
        },
        JWT_SECRET
      ),
    });
  }
  return res.status(401).json({ message: "Invalid username and/or password" });
});

app.get("/employee", (req, res) => {
  let tkn = req.header("Authorization");
  if (!tkn) return res.status(401).send("No Token");
  if (tkn.startsWith("Bearer"))
    tokenValue = tkn.slice(7, tkn.length).trimLeft();

  const verificationStatus = jsontoken.verify(tokenValue, "MoonIsNotBlue@2023");

  if (verificationStatus.user === "riswan") {
    return res
      .status(200)
      .json({ message: "Access Successful to Employee Endpoint" });
  }

  return res.status(401).json({
    message: "Please login to access this resource",
  });
});

app.listen(5001, () => {
  console.log("API Server is hosted in port:5001");
});

// curl commands to check this
// curl -X POST -H "Content-Type: application/json" -d '{"username": "riswan", "pwd": "Moon"}' localhost:5001/signin
// curl -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoicmlzd2FuIiwiaWF0IjoxNjc1ODIwNTc4fQ.2eV2IIk4Pqm5RZrlDlfvifQOTqWoCZa7Azwn4pEk3P0" localhost:5001/employee
