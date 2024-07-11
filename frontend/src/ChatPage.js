import React from "react";
import smile from './smile.jpg'; 
import Vapi from "@vapi-ai/web";
import './index.css'

const vapi = new Vapi("05a15f00-9fd2-4923-a02b-39cd5723c558");

const ChatPage = () => {
return(
    <div className="background-image">
        <h1>TablePal</h1>
        <div className="card">
            <div className="profile">
                <img src={smile} alt="Description of Image" />
                <div className="profile-name">
                    <h3>Sunny :)</h3>
                </div>
            </div>            
            <h5> Think of me as you personal waiter!</h5>
            <div className="search-bar-container">
                <input type="text" placeholder="Type your message..." className="search-input"/>
                <button className="pressme" onClick={handleButtonClick}> Press to Talk!</button>

            </div>
        </div>
    </div>
)
}

function handleButtonClick() {
    vapi.start("47c7afde-9078-4060-957a-2b542e478733");
}

export default ChatPage; 



