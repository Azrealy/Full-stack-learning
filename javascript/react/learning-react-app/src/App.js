import React, { Component, useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

const INITIAL_LIST = [
  {
    id: '0',
    title: 'React',
    description: 'This is react description'
  },
  {
    id: '1',
    title: 'Java',
    description: 'This is java description'
  }
]

const Example = () => {
  // Declare a new state variable, which we'll call "count"
  const [list, setList] = useState(INITIAL_LIST);

  const onRemoveItem = (id) => {
    const nextList = list.filter(item => item.id !== id);
    setList(nextList)
  }

  return (
    <div>
      {list.map(item => {
        return (
          <li key={item.id}>
            <strong>{item.title}</strong>
            <h2>{item.description}</h2>
            <button type="button" onClick={() => onRemoveItem(item.id)}>
            Remove
            </button>
          </li>
        )
      })}

    </div>
  );
}

const EffectedButton = () => {
  const [isOn, setIsOn] = useState(true)
  const [timer, setTimer] = useState(0)

  useEffect(()=> {
    // this side-effect setup when mounting the component 
    // and the clean up when unmounting the component
    console.log('effect run')
    
    const interval = setInterval(
      () => isOn && setTimer(timer + 1), 
      1000
    );
    document.title = `You clicked ${timer} times`;
    return () => clearInterval(interval)
  }, [timer]);

  const resetTimer = () => {
    setIsOn(false);
    setTimer(0);
  }

  return (
    <div>
      {timer}
      {!isOn && (
        <button type="button" onClick={() => setIsOn(true)}>
          Start
        </button>
      )}

      {isOn && (
        <button type="button" onClick={() => setIsOn(false)}>
          Stop
        </button>
      )}
      <button type="button" disabled={timer===0}onClick={resetTimer}>
        Reset
      </button>
    </div>
  )
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
          <Example/>
          <EffectedButton/>
        </header>
      </div>
    );
  }
}

function ExampleOfficial() {
  const [isOn, setIsOn] = useState(false)
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log("effect has run")
    const interval = setInterval(
      () => isOn && setCount(count + 1), 
      1000
    );
    document.title = `You clicked ${count} times`;
    return () => clearInterval(interval)
  },[count, isOn]);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
      {!isOn && (
        <button type="button" onClick={() => setIsOn(true)}>
          Start
        </button>
      )}

      {isOn && (
        <button type="button" onClick={() => setIsOn(false)}>
          Stop
        </button>
      )}
    </div>
  );
}

function todoReducer(state, action) {
  switch (action.type) {
    case 'add':
      return [...state, {
        id: state.length + 1,
        text: action.text,
        completed: false
      }];
    case 'delete':
      return state.filter(item => 
        item.id !== action.id
      )
    default:
      return state;
  }
}

function useReducer(reduce, initialState) {
  const [state, setState] = useState(initialState)

  function dispatch(action) {
    const nextState = reduce(state, action)
    setState(nextState)
  }

  return [state, dispatch]
}

const initialTodos = [
  {id: 1, text: "hello world", completed: false}
]

function Todos() {
  const [todos, dispatch] = useReducer(todoReducer, initialTodos);
  const [text, setText] = useState("")

  function handleAddClick(text) {
    dispatch({type: 'add', text })
    setText("")
  }

  function onChange(event) {
    setText(event.target.value)
  }

  function handleDeleteClick(id) {
    dispatch({type: 'delete', id})
  }

  return (
    <div>
      <input onChange={(e) => onChange(e)} value={text}/>
      <button onClick={() => handleAddClick(text)}>
        add
      </button>
      <ul>
      {todos.map( todo => 
        <div key={todo.id}>
          <li>{todo.text} &nbsp;
          <button onClick={() => handleDeleteClick(todo.id)}>
            Delete
          </button>
          </li>
        </div>
      )}
      </ul>
    </div>
  )
}


export default Todos;
