import React from 'react';
import Vapi from "@vapi-ai/web";

const vapi = new Vapi("05a15f00-9fd2-4923-a02b-39cd5723c558");

const FetchButton = ({ selectedRestaurant }) => {
  const handleButtonClick = () => {
    if (selectedRestaurant) {
      fetch(`http://127.0.0.1:8000/restaurant/get_information?name=${selectedRestaurant}`)
        .then(response => response.json())
        .then(data => {
          if (data.error) {
            console.error('Error fetching restaurant information:', data.error);
          } else {
            console.log('Restaurant information:', data.restaurant);
            
            // vapi.start("47c7afde-9078-4060-957a-2b542e478733") //Test Vapi call

            vapi.start(
                {
                  name: "Appetite AI",
                  voice: {
                      voiceId: "asteria",
                      provider: "deepgram"
                  },
                  model: {
                      model: "gpt-3.5-turbo",
                      messages: [
                          {
                              role: "system",
                              content: `You are a voice assistant. You are a waiter for a restaurant. All of the restaurant information is inside of the following JSON file: ${JSON.stringify(data.restaurant)}`,
                            }
                      ],
                      provider: "openai",
                      maxTokens: 250,
                      temperature: 0.7,
                      emotionRecognitionEnabled: false
                  },
                  recordingEnabled: true,
                  firstMessage: "Welcome! I'm TablePal, your assistant for today! Please feel free to ask me anything about the restaurant!",
                  endCallFunctionEnabled: false,
                  transcriber: {
                      model: "nova-2-drivethru",
                      language: "en",
                      provider: "deepgram"
                  },
                  clientMessages: [
                      "transcript",
                      "hang",
                      "function-call",
                      "speech-update",
                      "metadata",
                      "conversation-update"
                  ],
                  serverMessages: [
                      "end-of-call-report",
                      "status-update",
                      "hang",
                      "function-call"
                  ],
                  dialKeypadFunctionEnabled: false,
                  endCallPhrases: [
                      "Goodbye"
                  ],
                  hipaaEnabled: false,
                  voicemailDetectionEnabled: false,
              }
            ); //Vapi json ends here
          }
        })
        .catch(error => console.error('Error fetching restaurant information:', error));
    } else {
      console.error('No restaurant selected');
    }
  };

  return (
    <button className="circular-button" onClick={handleButtonClick}>
      Press Me
    </button>
  );
};

export default FetchButton;
