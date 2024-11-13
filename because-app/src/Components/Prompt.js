import React, { useState } from "react";
import "../App.css";
import axios from "axios";

export const PromptForm = () => {
  const [startState, setStartState] = useState("");
  const [endState, setEndState] = useState("");
  const [storyBeat, setStoryBeat] = useState(null);
  const [buttonText] = useState("Generate Plot");

  const handleGeneratePlot = async () => {
    if (startState && endState) {
      try {
        const response = await axios.post("http://localhost:5000/characters", {
          starting_state: startState,
          ending_state: endState,
        });

        setStoryBeat(response.data.structure);
      } catch (error) {
        console.error("Error generating plot structure: ", error);
      }

      setStartState("");
      setEndState("");
    }
  };

  const handleChoice = async (choice) => {
    try {
      const response = await axios.post("http://localhost:5000/characters", {
        choice,
      });

      //AS I HAVE IT NOW THIS HAS TO BE GIVE AS A JSON FILE.

      setStoryBeat(response.data);
    } catch (error) {
      console.error("Error continuing story: ", error);
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
              value={startState}
              placeholder="Starting Point"
              onChange={(e) => setStartState(e.target.value)}
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
              value={endState}
              placeholder="Ending point"
              onChange={(e) => setEndState(e.target.value)}
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

        {/* THIS SHOULD BE WHERE EVERYTHING IS DISPLAYED */}
        {storyBeat && (
          <div>
            <h3>{storyBeat.header}</h3>
            <p>{storyBeat.conext}</p>
            <p>{storyBeat.option_a}</p>
            <p>{storyBeat.option_b}</p>
            <div>
              <button onClick={() => handleChoice("A")}>A</button>
              <button onClick={() => handleChoice("B")}>B</button>
            </div>
          </div>
        )}
      </div>
    </section>
  );
};

export default PromptForm;
