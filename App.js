import React from 'react'
import logo  from './logo.svg'
import './App.css'
function App(){
  const handleAttachFile = e =>{
    console.log('files uploaded', e.terget.files)}
}
return(
  <dev className='App'>
    <header className="App-header">
      <img src={logo} className='App-logo' alt='logo'/>
      <input type="file" multiple onChange={handleAttachFile} />
    </header>
  </dev>  
 )
}
export default App

//By doing so, we've added an input button that when we upload a file, it will console.log the file that being uploaded.

//Now let's set up our redux in the mail page.




