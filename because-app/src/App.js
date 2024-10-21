import React, { useState } from "react";
import "./App.css";
import axios from "axios";

function App() {
  // State variables for the inputs
  const [prompt, setPrompt] = useState("");
  const [context, setContext] = useState("");
  const [character, setCharacter] = useState("");
  const [goal, setGoal] = useState("");


  // Function to handle the button click
  const handleGeneratePlot = () => {
    console.log("Prompt:", prompt);
    console.log("Context:", context);
    console.log("Context:", character);
    console.log("Context:", goal);


    // getChars(prompt);
    getChars(character, goal);
    // Clear the inputs after generating
    setPrompt("");
    setContext("");
    setCharacter("");
    setGoal("");

  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>NuScript</h1>
        <div className="input-container">
          <div>
            <label>
              Prompt:
              <input
                type="text"
                value={character}
                onChange={(e) => setCharacter(e.target.value)}
                placeholder="Enter character name(s)"
              />
            </label>
          </div>

          <div>
              <input
                type="text"
                value={goal}
                onChange={(e) => setGoal(e.target.value)}
                placeholder="Enter the end goal"
              />
          </div>
        </div>
        {/* <div>
          <label>
            Context:
            <input
              type="text"
              value={context}
              onChange={(e) => setContext(e.target.value)}
              placeholder="Enter your context here"
            />
          </label>
        </div> */}
        <button onClick={handleGeneratePlot}>Generate Plot</button>
      </header>
    </div>
  );
}

// will be needed later to allow for multi-generation history
function appendToStorage(name, data){
    var old = localStorage.getItem(name);
    if(old === null) old = "";
    localStorage.setItem(name, old + data);
}

async function getChars(charInfo, promptInfo) {
  try {
    const response = await axios.post("http://localhost:5000/characters", {
      charInfo,
      promptInfo,
    });
    const dat = response.data;
    console.log(response.data);
    // Save the token to local storage
    localStorage.setItem("chars", dat[0]);
    localStorage.setItem("sentences", dat[1]);
    alert(localStorage.getItem("sentences")[-1]);

  } catch (error) {
    console.error(error);
  }
}

export default App;
