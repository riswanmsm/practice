import React from "react";
import ReactDOM from "react-dom/client";

class SampleComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: 1,
      name: "Riswan",
      age: 36,
    };
    console.log("this is from constructor");
  }

  componentDidMount = () => console.log("this is from component did mount");

  render() {
    console.log("this is from render method");
    return (
      <div>
        <p>{this.state.name}</p>
        <p>{this.state.age}</p>
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<SampleComponent />);
