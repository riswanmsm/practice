import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import ClassComponent from "./ClassComponent";

const root = ReactDOM.createRoot(document.getElementById("root"));
const ref = () => root.render(
    <div>
        <App showPopup={() => alert("Hi, You clicked 'Show Popup' button")} />
        <ClassComponent showPopup={() => alert("Look at the count above, it will increase!")} />
    </div>
);

setInterval(ref, 1000);
