convert_temperature = () => {
  // Take celcius and convert to farenheit
  // Display the farenheit value in the field
  let c = document.getElementById("c").value;
  let f = (c * 9) / 5 + 32;
  document.getElementById("f").value = f;
};

convert_weight = () => {
  // Take kilo and convert to pound
  // Display the pound value in the field
  let kilo = document.getElementById("kilo").value;
  let pound = kilo * 2.2;
  document.getElementById("pound").value = pound;
};

convert_distance = () => {
  // Take km and convert to mile
  // Display the mile value in the field
  let km = document.getElementById("km").value;
  let mile = km * 0.62137;
  document.getElementById("mile").value = mile;
};
