import React, { useState, useEffect } from "react";
import axios from "axios";
import "./Conversation.css";

var msgArr = [];

export const Conversation = (startingState, endingState) => {
    const [messages, setMessages] = useState([
        { text: "Please enter a starting point:", sender: "bot" },
    ]);
    const [input, setInput] = useState("");
    const [showChoices, setShowChoices] = useState(false);
    const [storyStruct, setStoryStruct] = useState([]);
    const [lineNum, setLineNum] = useState(0);
    var story = [];
    const handleStart = async (startingState, endingState) => {
        const response = await axios.post("http://localhost:5001/entry", {
            starting_state: startingState,
            ending_state: endingState,
        });
        story = response.data.story_structure;

        setStoryStruct(story);

        // console.log("This is in handleStart story : ", story);
        if (story.length > 1) {
            handleGenerateChoices(1);
        }
    };

    const handleGenerateChoices = async (num) => {
        console.log("curent line: ", num);
        // console.log(story)

        const romanNumeralRegex =
            /^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$/;

        var lineslist = [story[num]];
        num++;
        while (!romanNumeralRegex.test(story[num])) {
            lineslist.push(story[num]);
            num++;
        }
        // lineslist.push(story[num]);
        console.log("This is line list in handleGenerateChoices: ", lineslist);
        setLineNum(num);
        const response = await axios.post("http://localhost:5001/text", {
            txt: lineslist,
        });

        // console.log("full response data: ", response.data);
        // console.log("response.data.outputTxt in msg: ", response.data.outputTxt);
        // console.log(
        //   " response.data.choices in choicesText: ",
        //   response.data.choices
        // );

        var msg = response.data.outputTxt;
        var choicesText = response.data.choices;

        msgArr = [...msgArr];
        console.log("msgArr: ", msgArr);
        console.log("this is msg", msg);
        console.log("this is choicesText: ", choicesText);

        // msg.forEach((element) => {
        //   msgArr.push({ text: element, sender: "bot" });
        // });

        // Find and push the element with a Roman numeral

        const romannumeralRegex = /^[IVXLCDM]+\.\s/;
        let contextMessage = "";
        msg.forEach((element) => {
            if (romannumeralRegex.test(element)) {
                msgArr.push({ text: element, sender: "bot" }); // Push the Roman numeral element
            } else {
                // Remove '-' or '*' and add the cleaned element to combinedMessage
                contextMessage += element.replace(/[-*]/g, "").trim() + " ";
            }
        });

        // Trim the final combinedMessage and push it to msgArr if it's not empty
        if (contextMessage.trim()) {
            msgArr.push({ text: contextMessage.trim(), sender: "bot" });
        }

        msgArr.push({ text: "Pick an outcome:", sender: "bot" });
        msgArr.push({ text: choicesText[0], sender: "bot" });
        msgArr.push({ text: choicesText[1], sender: "bot" });

        // console.log("recieve")
        setMessages(msgArr);

        // console.log(response.data)

        setShowChoices(true);
    };


    const handleChoice = async (input) => {
        story = storyStruct;
        const response = await axios.post("http://localhost:5001/choices", {
            choice: input,
        });

        msgArr.push({ text: response.data.result, sender: "bot" });
        // msgArr.push({ text: "", sender: "bot" });
        setMessages(msgArr);
        console.log("this is messages: ", messages);

        if (story.length > lineNum) {
            handleGenerateChoices(lineNum);
        }
    };
    useEffect(() => {
        handleStart(startingState, endingState);
      }, []);
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
                    
            </div>
        </div>
    );
}

export default Conversation;