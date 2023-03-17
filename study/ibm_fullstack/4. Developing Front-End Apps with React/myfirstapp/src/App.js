function App(props) {
  const currentTime = new Date();
  return (
    <div className="App">
      <h1>Hello, Riswan</h1>
      <h2>
        The time is {currentTime.toLocaleDateString()},{" "}
        {currentTime.toLocaleTimeString()}
      </h2>
      <button onClick={props.showPopup}>Show Popup</button>
    </div>
  );
}

export default App;
