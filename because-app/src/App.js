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

// will be needed later to allow for multi-generation history
function appendToStorage(name, data) {
  var old = localStorage.getItem(name);
  if (old === null) old = "";
  localStorage.setItem(name, old + data);
}

export default App;
