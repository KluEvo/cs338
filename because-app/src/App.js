
import React, { useEffect, useState } from 'react';
import './App.css';

import axios from 'axios';

function App() {
  // State variables for the inputs
  const [prompt, setPrompt] = useState("");
  const [context, setContext] = useState("");

  // Function to handle the button click
  const handleGeneratePlot = () => { 
    // Here you can implement the logic to generate the plot
    console.log('Prompt:', prompt);
    console.log('Context:', context);
    getChars(prompt)
    // You can also clear the inputs after generating
    setPrompt("");
    setContext("");
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>NuScript</h1>
        <div>
          <label>
            Prompt:
            <input
              type="text"
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Enter your prompt here"
            />
          </label>
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


async function getChars(charInfo) {
    try {
        const response = await axios.post('http://localhost:5000/characters', {
            charInfo,
        });
        let dat = response.data
        console.log(response.data);
        // Save the token to local storage
        localStorage.setItem('chars', dat);
    } catch (error) {
        console.error(error);
    }
}


export default App;
