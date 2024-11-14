// // src/App.js
// import React, { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//     const [messages, setMessages] = useState([]);
//     const [input, setInput] = useState("");
//     const [options, setOptions] = useState([]);
//     const [beats, setBeats] = useState([]);
//     const [startingState, setStartingState] = useState("");
//     const [endingState, setEndingState] = useState("");
//     const [showChoices, setShowChoices] = useState("");
//     const [storyStruct, setStoryStruct] = useState(null);
//     const [lineNum, setLine] = useState(0);

//     // localStorage.setItem("storybeat", JSON.stringify(storyBeat));

//     const handleStart = async () => {
//         const response = await axios.post("http://localhost:5001/entry", {
//             starting_state: startingState,
//             ending_state: endingState,
//         });
//         var story = (response.data.story_structure);
//         // localStorage.setItem("storyStruct", response.data.story_structure);

//         setMessages([
//             ...messages,
//             { text: story[0], sender: "bot" },
//         ]);
//         setLine(1);
//         console.log(story);
//         console.log(story[1]);
//         if (story.length > lineNum){
//             handleGenerateChoices(story, 1);
//         } 

//     };

//     const handleGenerateChoices = async (story, num) => {
        
//         console.log("send")

//         const response = await axios.post(
//             "http://localhost:5001/text",
//             {
//                 txt: story[num],
//             }
//         );
//         var msg = response.data.outputTxt;
//         console.log("recieve")
//         setMessages([
//             ...messages,
//             { text: msg, sender: "bot" },
//         ]);

//         console.log(messages)

//         // setMessages([
//         //     ...messages,
//         //     { text: "Choose an option:", sender: "bot" },
//         //     ...response.data.options.map((option) => ({
//         //         text: option,
//         //         sender: "bot",
//         //     })),
//         // ]);

//         if (response.data.giveChoice){
//             setShowChoices(true);
//         } 
//         else {
//             setShowChoices(false);
//             if (story.length > num+1){
//                 handleGenerateChoices(story, num+1);
//             } 
//         } 


//     };

//     const handleGenerateBeats = async (choice) => {
//         const response = await axios.post(
//             "http://localhost:5001/choices",
//             {
//                 choice: choice,
//             }
//         );
//         setBeats([...beats, response.data.beat]);
//         setMessages([...messages, { text: response.data.beat, sender: "bot" }]);
//     };

//     const handleSendMessage = () => {
//         if (input.trim()) {
//             setMessages([...messages, { text: input, sender: "user" }]);
//             setInput("");

//             // Handle different types of user input
//             if (startingState === "" && endingState === "") {
//                 setStartingState(input);
//             } else if (startingState !== "" && endingState === "") {
//                 setEndingState(input);
//                 handleStart();
//             } else if (options.length > 0) {
//                 const choice = input.toLowerCase();
//                 if (choice === "a" || choice === "1") {
//                     handleGenerateBeats(options[0]);
//                 } else if (choice === "b" || choice === "2") {
//                     handleGenerateBeats(options[1]);
//                 } else {
//                     setMessages([
//                         ...messages,
//                         {
//                             text: "Invalid choice, defaulting to the first option.",
//                             sender: "bot",
//                         },
//                     ]);
//                     handleGenerateBeats(options[0]);
//                 }
//                 setOptions([]);
//             } else {
//                 handleGenerateChoices();
//             }
//         }
//     };

//     const handleChoice = async (input) => {
//         const response = await axios.post("http://localhost:5001/choices", {
//             starting_state: startingState,
//             ending_state: endingState,
//         });

//         setMessages([
//             ...messages,
//             { text: response.data.story_structure, sender: "bot" },
//         ]);

        
//         setLine(lineNum+1);
//         if (storyStruct.length > lineNum){
//             handleGenerateChoices([], lineNum);
//         } 
//     };

//     return (
//         <div className="chat-container">
//             <div className="chat-messages">
//                 {messages.map((msg, index) => (
//                     <div key={index} className={`message ${msg.sender}`}>
//                         {msg.text}
//                     </div>
//                 ))}
//                 {showChoices && (
//                     <div className="choices">
//                         <button onClick={() => handleChoice("A")}>A</button>
//                         <button onClick={() => handleChoice("B")}>B</button>
//                     </div>
//                 )}
//             </div>
//             <div className="chat-input">
//                 <input
//                     type="text"
//                     value={input}
//                     onChange={(e) => setInput(e.target.value)}
//                     placeholder="Type a message..."
//                     onKeyPress={(e) => e.key === "Enter" && handleSendMessage()}
//                 />
//                 <button onClick={handleSendMessage}>Send</button>
//             </div>
//         </div>
//     );
// }

// export default App;

import React from "react";
import "./App.css";
import { PromptForm } from "./Components/Prompt";
// import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <div className="bg-sky-900 h-screen content-center">
      <PromptForm />
    </div>
  );
}

export default App;
