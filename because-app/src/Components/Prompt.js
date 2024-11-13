import React, { useState } from "react";
import "../App.css";
import axios from "axios";

export const PromptForm = () => {
  const [prompt, setPrompt] = useState("");
  const [context, setContext] = useState("");
  const [character, setCharacter] = useState("");
  const [goal, setGoal] = useState("");
  const [buttonText] = useState("Generate Plot");

  const handleGeneratePlot = () => {
    if (prompt) {
      // Guard against empty inputs
      console.log("Prompt:", prompt);
      console.log("Context:", context);
      console.log("Character:", character);
      console.log("Goal:", goal);

      async function getChars(
        charInfo = "Jane",
        promptInfo = "was late to school"
      ) {
        try {
          const response = await axios.post(
            "http://localhost:5000/characters",
            {
              charInfo,
              promptInfo,
            }
          );
          const dat = response.data;
          console.log(response.data);
          // Save the token to local storage
          localStorage.setItem("chars", dat[0]);
          localStorage.setItem("sentences", dat[1]);
          alert(localStorage.getItem("sentences"));
        } catch (error) {
          console.error(error);
        }
      }

      // getChars(prompt);
      getChars(character, goal);

      // Clear the inputs after generating
      setPrompt("");
      setContext("");
      setCharacter("");
      setGoal("");
    }
  };

  return (
    <section className="">
      <header className="App-header text-center mb-4">
        <h2 className="text-3xl font-bold text-gray-800">NuScript</h2>
      </header>
      <div className=" max-w-md mx-auto bg-white p-6 rounded-lg shadow-md">
        <form className="space-y-4">
          <div>
            <label>
              <h3 className="text-lg font-semibold text-gray-700">
                Current Character Situation:
              </h3>
            </label>
            <input
              type="text"
              value={character}
              placeholder="Starting Point"
              onChange={(e) => setCharacter(e.target.value)}
              className="w-full mt-2 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div>
            <label>
              <h3 className="text-lg font-semibold text-gray-700">
                Outcome of Story Arc:
              </h3>
            </label>
            <input
              type="text"
              value={goal}
              placeholder="Ending point"
              onChange={(e) => setGoal(e.target.value)}
              className="w-full mt-2 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <button
            type="button"
            onClick={handleGeneratePlot}
            className="w-full mt-4 p-3 bg-sky-900	 text-white font-semibold rounded-md hover:bg-sky-900	 transition"
          >
            <span>{buttonText}</span>
          </button>
        </form>
      </div>
    </section>
  );
};

export default PromptForm;
