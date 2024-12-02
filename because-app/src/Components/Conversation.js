import React, { useState, useEffect } from "react";
import axios from "axios";
import "./Conversation.css";

var msgArr = [];
var lineNum = 0;
var showChoices = false;
var summary = "";

export const Conversation = (startingState, endingState) => {
  const [messages, setMessages] = useState([
    { text: "Processing", sender: "bot" },
  ]);
  const [storyStruct, setStoryStruct] = useState([]);
  // const [lineNum, setLineNum] = useState(0);
  var story = [];
  console.log(startingState, endingState);
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
    while (num < story.length && !romanNumeralRegex.test(story[num])) {
      lineslist.push(story[num]);
      num++;
    }
    if (num >= story.length) {
      showChoices = false;
      console.log(showChoices);
    }

    // lineslist.push(story[num]);
    console.log("This is line list in handleGenerateChoices: ", lineslist);
    lineNum = num;
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

    showChoices = true;
  };

  const handleChoice = async (input) => {
    story = storyStruct;
    const response = await axios.post("http://localhost:5001/choices", {
      choice: input,
    });
    summary += response.data.result;

    msgArr.push({ text: response.data.result, sender: "bot" });
    // msgArr.push({ text: "", sender: "bot" });
    setMessages(msgArr);
    console.log("this is messages: ", messages);
    console.log("this is story: ", story);

    if (story.length > lineNum) {
      handleGenerateChoices(lineNum);
    } else {
      console.log("EOL");
      getSummary(summary);
    }
  };

  const getSummary = async (input) => {
    showChoices = false;
    console.log("done");

    // Create a copy of msgArr and add new messages to it
    const updatedMsgArr = [...msgArr];
    updatedMsgArr.push({ text: "Summary:", sender: "bot" });
    updatedMsgArr.push({ text: input, sender: "bot" });

    // Update the state with the new messages array
    setMessages(updatedMsgArr);

    // Log the updated messages array
    console.log("Updated messages: ", updatedMsgArr);
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
            <button
              onClick={() => {
                console.log("A pressed");
                handleChoice("A");
              }}
            >
              A
            </button>
            <button onClick={() => handleChoice("B")}>B</button>
          </div>
        )}
      </div>
      <div className="chat-input"></div>
    </div>
  );
};

export default Conversation;
