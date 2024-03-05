import React from "react"
import ChatPage from "./component/ChatPage";
import RegistrationForm from "./component/RegistrationForms"
import Header from "./component/Header"
function App() {
  // request
 
  return(
    <div className="App">
      <Header/>
      <RegistrationForm/>
      <ChatPage/>
    </div>
    
  )
}

export default App