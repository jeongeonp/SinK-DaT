import React, { Component } from 'react'
import './App.css';
import { Form, Button, Card, TextArea } from 'semantic-ui-react'
import { MainPage } from './components/MainPage';

class App extends Component {



  render() {
    const description = "Hello"

    return (
      <div className="App">
        <main className="center">
          <MainPage ></MainPage>

        </main>

        
        
      </div>
    );
  }
  
}

export default App;
