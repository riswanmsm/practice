const express = require("express");
const app = new express();
const port = 3333;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(port, () => {
  console.log(`app is listning on port ${port}`);
});
