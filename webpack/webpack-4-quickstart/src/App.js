import React from "react";
import ReactDOM from "react-dom";
const App = () => {
  return (
    <div>
			<h1>Here is the title</h1>
      <p>React here! good learning of webpack 4</p>
    </div>
  );
};
export default App;
ReactDOM.render(<App />, document.getElementById("app"));