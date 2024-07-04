import React from 'react';
import Vapi from "@vapi-ai/web";
import './App.css'; // Make sure this path is correct based on your file structure

const vapi = new Vapi("05a15f00-9fd2-4923-a02b-39cd5723c558");

function App() {
  return (
    <div className="center-button-container">
      <input type="text" className="text-box" placeholder="Type here..." />
      <button className="circular-button" onClick={handleButtonClick}>Press Me</button>
    </div>
  );
}

function handleButtonClick() {
  vapi.start("47c7afde-9078-4060-957a-2b542e478733");
}

// function handleButtonClick() {
//   vapi.start({
//     transcriber: {
//       provider: "deepgram",
//       model: "nova-2",
//       language: "en-US",
//     },
//     model: {
//       provider: "openai",
//       model: "gpt-3.5-turbo",
//       messages: [
//         {
//           role: "system",
//           content: "You are a helpful assistant.",
//         },
//       ],
//     },
//     voice: {
//       provider: "playht",
//       voiceId: "jennifer",
//     },
//     name: "My Inline Assistant",
//   });
// }

export default App;
