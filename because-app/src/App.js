import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [options, setOptions] = useState([]);
    const [beats, setBeats] = useState([]);
    const [startingState, setStartingState] = useState("");
    const [endingState, setEndingState] = useState("");
    const [showChoices, setShowChoices] = useState(false);
    const [storyStruct, setStoryStruct] = useState([]);
    const [lineNum, setLineNum] = useState(0);
    var story = [];
    // localStorage.setItem("storybeat", JSON.stringify(storyBeat));

    const handleStart = async () => {
        const response = await axios.post("http://localhost:5001/entry", {
            starting_state: startingState,
            ending_state: endingState,
        });
        story = (response.data.story_structure);
        localStorage.setItem("storyStruct", response.data.story_structure);
        setStoryStruct(story)

        
        console.log(story);
        if (story.length > 1){
            handleGenerateChoices(1);
        } 

    };

    const handleGenerateChoices = async (num) => {
        
        console.log("curent line: ", num)
        console.log(story)

        const romanNumeralRegex = /^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$/;

        var lineslist = [story[num]];
        num ++;
        while (!romanNumeralRegex.test(story[num])){
            lineslist.push(story[num]);
            num++;
        }
        console.log(lineslist);
        setLineNum(num);
        const response = await axios.post(
            "http://localhost:5001/text",
            {
                txt: lineslist,
            }
        );
        var msg = response.data.outputTxt;
        var choicesText = response.data.choices;

        var msgArr = [...messages];
        console.log(msg)
        console.log(choicesText)

        msg.forEach(element => {
            msgArr.push({ text: element, sender: "bot" });
        });
        msgArr.push({ text: "Pick an outcome:", sender: "bot" });
        msgArr.push({ text: choicesText[0], sender: "bot" });
        msgArr.push({ text: choicesText[1], sender: "bot" });

        console.log("recieve")
        setMessages(msgArr);

        console.log(response.data)

        setShowChoices(true);



    };

    const handleGenerateBeats = async (choice) => {
        const response = await axios.post(
            "http://localhost:5001/choices",
            {
                choice: choice,
            }
        );
        setBeats([...beats, response.data.beat]);
        setMessages([...messages, { text: response.data.beat, sender: "bot" }]);
    };

    const handleSendMessage = () => {
        if (input.trim()) {
            setMessages([...messages, { text: input, sender: "user" }]);
            setInput("");

            // Handle different types of user input
            if (startingState === "" && endingState === "") {
                setStartingState(input);
            } else if (startingState !== "" && endingState === "") {
                setEndingState(input);
                handleStart();
            } else if (options.length > 0) {
                const choice = input.toLowerCase();
                if (choice === "a" || choice === "1") {
                    handleGenerateBeats(options[0]);
                } else if (choice === "b" || choice === "2") {
                    handleGenerateBeats(options[1]);
                } else {
                    setMessages([
                        ...messages,
                        {
                            text: "Invalid choice, defaulting to the first option.",
                            sender: "bot",
                        },
                    ]);
                    handleGenerateBeats(options[0]);
                }
                setOptions([]);
            } else {
                handleGenerateChoices();
            }
        }
    };

    const handleChoice = async (input) => {
        story = storyStruct
        const response = await axios.post("http://localhost:5001/choices", {
            choice: input,
        });

        setMessages([
            ...messages,
            { text: response.data.result, sender: "bot" },
        ]);

        console.log(lineNum, story.length);
        
        console.log(story);
        if (story.length > lineNum){
            handleGenerateChoices(lineNum);
        } 
    };

    return (
        <div className="chat-container">
            <div className="chat-messages">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        {msg.text}
                    </div>
                ))}
                {showChoices && (
                    <div className="choices">
                        <button onClick={() => handleChoice("A")}>A</button>
                        <button onClick={() => handleChoice("B")}>B</button>
                    </div>
                )}
                
            </div>
            <div className="chat-input">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type a message..."
                    onKeyPress={(e) => e.key === "Enter" && handleSendMessage()}
                />
                <button onClick={handleSendMessage}>Send</button>
            </div>
        </div>
    );
}

export default App;

// import React from "react";
// import "./App.css";
// import { PromptForm } from "./Components/Prompt";
// // import "bootstrap/dist/css/bootstrap.min.css";

// function App() {
//   return (
//     <div className="bg-sky-900 h-screen content-center">
//       <PromptForm />
//     </div>
//   );
// }

// export default App;
