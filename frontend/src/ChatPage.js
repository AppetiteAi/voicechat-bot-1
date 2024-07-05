import React from "react";
import smile from './smile.jpg'; 
import './index.css'

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
                <button className="pressme"> Press to Talk!</button>

            </div>
        </div>
    </div>
)
}

export default ChatPage; 