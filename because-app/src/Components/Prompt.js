import React, { useState } from "react";
import "../App.css";
import { Conversation } from "./Conversation";
import axios from "axios";

export const PromptForm = () => {
  const [startState, setStartState] = useState("");
  const [endState, setEndState] = useState("");
  const [storyBeat, setStoryBeat] = useState(null);
  const [buttonText] = useState("Generate Plot");

  const handleGeneratePlot = async () => {
    if (!(startState && endState)) {
      setStartState("John and Amy are rivals");
      setEndState("John and Amy start dating");
    }
    setStoryBeat("data");

    // try {
    //   const response = await axios.post("http://localhost:5001/entry", {
    //     starting_state: startState,
    //     ending_state: endState,
    //   });
    //   localStorage.setItem("storybeat", JSON.stringify(storyBeat));
    // } catch (error) {
    //   console.error("Error generating plot structure: ", error);
    // }
  };

  return (
    <section className="">
      <header className="App-header text-center mb-4">
        <h2 className="text-3xl font-bold text-gray-800">NuScript</h2>
      </header>
      <div className=" max-w-xl mx-auto bg-white p-6 rounded-lg shadow-md">
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
              placeholder="EX: John and Amy are rivals"
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
              placeholder="EX: John and Amy start dating"
              onChange={(e) => setEndState(e.target.value)}
              className="w-full mt-2 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <button
            type="button"
            onClick={handleGeneratePlot}
            className="w-full mt-4 ml-0 p-3 bg-sky-900 text-gray-100 font-semibold rounded-md hover:bg-sky-900	 transition"
          >
            <span>{buttonText}</span>
          </button>
        </form>

        {/* THIS SHOULD BE WHERE EVERYTHING IS DISPLAYED */}
        {storyBeat && (
          <div>
            <Conversation startingState={startState} endingState={endState} />
            {/* <button onClick={() => handleChoice("A")}>A</button>
              <button onClick={() => handleChoice("B")}>B</button> */}
          </div>
        )}
      </div>
    </section>
  );
};

export default PromptForm;
