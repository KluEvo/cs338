import React, { useState } from "react";
import "../App.css";
import axios from "axios";

export const PromptForm = () => {
  const [prompt, setPrompt] = useState("");
  const [context, setContext] = useState("");
  const [character, setCharacter] = useState("");
  const [goal, setGoal] = useState("");
  const [buttonText] = useState("Send");

  const handleGeneratePlot = () => {
    if (prompt && character && goal) {
      // Guard against empty inputs
      console.log("Prompt:", prompt);
      console.log("Context:", context);
      console.log("Character:", character);
      console.log("Goal:", goal);

      async function getChars(charInfo) {
        try {
          const response = await axios.post(
            "http://localhost:5000/characters",
            {
              charInfo,
            }
          );
          const dat = response.data;
          console.log(response.data);
          localStorage.setItem("chars", dat);
        } catch (error) {
          console.error(error);
        }
      }

      getChars(prompt);
      getChars(character);
      getChars(goal);

      setPrompt("");
      setContext("");
      setCharacter("");
      setGoal("");
    } else {
      console.warn("One or more fields are empty.");
    }
  };

  return (
    <section className="prompt">
      <header className="App-header">
        <h2>NuScript</h2>
      </header>
      <div className="prompt-container">
        <form>
          <div>
            <label>
              <h3>Prompt: </h3>
            </label>
            <input
              type="text"
              value={character || ""}
              placeholder="Character Names"
              onChange={(e) => setCharacter(e.target.value)}
            />
          </div>
          <div>
            <input
              type="text"
              value={prompt || ""}
              placeholder="End Goal"
              onChange={(e) => setPrompt(e.target.value)}
            />
          </div>
          <button type="button" onClick={handleGeneratePlot}>
            <span>{buttonText}</span>
          </button>
        </form>
      </div>
    </section>
  );
};

export default PromptForm;
