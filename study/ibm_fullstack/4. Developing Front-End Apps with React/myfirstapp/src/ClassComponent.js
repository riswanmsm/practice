import React from 'react';

class ClassComponent extends React.Component {
    state = {counter: "0"}

    incrementCounter = () => {
        this.setState({counter: parseInt(this.state.counter) + 1});
        this.props.showPopup();
    }
    render() {
        return <div>
            <p>The count is: {this.state.counter}</p>
            <button onClick={this.incrementCounter}>Show Class Popup</button>
        </div>;
    }
}

export default ClassComponent;