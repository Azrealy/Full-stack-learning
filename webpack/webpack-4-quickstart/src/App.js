import React from "react";
import ReactDOM from "react-dom";
import ReactMarkdown from "react-markdown";
import tutorial from "./tutorial.md"

const App = () => {
  return (
    <div>
			<ReactMarkdown source={tutorial}/>
			<h1>Here is the title</h1>
      <p>React here! good learning of webpack 4 e</p>
    </div>
  );
};
export default App;
ReactDOM.render(<App />, document.getElementById("app"));