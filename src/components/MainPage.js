import React, { Component } from 'react';
import {Form, TextArea, Button, Card, Popup } from 'semantic-ui-react';
import './MainPage.css'

export class MainPage extends Component {
    constructor(props) {
        super(props)
        this.state = {
            result: false,
        }
        this.showResult = this.showResult.bind(this)
    }

    showResult = () => {
        this.setState({
            result: !this.state.result,
        })
        console.log("true?")
    }


    render() {
        const { result } = this.state
        const { showResult } = this
        const defaultButton = (word, explanation) => <Popup content={explanation} trigger={<Button size='tiny' compact style={{backgroundColor: '#b5c7d3', borderRadius: 0}} content={word}/>} />

        return (
            <div>
                <Form>
                    <Form.Field>
                        <h2 style={{margin: "10px 0"}}>Hanja-to-Korean Converter</h2>
                        <TextArea placeholder='Put in your text' style={{minHeight: "150px"}} />
                        <Button color='blue' style={{margin: "20px"}} onClick={showResult}>Click to ~~?</Button>
                    </Form.Field>
                    { result 
                        ?
                        <Form.Field>
                            <Card style={{width: "100%", minHeight: "200px"}}>
                            <Card.Content>
                                <Card.Header content='Result' />
                                <Card.Meta content='2020-06-15 21:34' />
                                <br/>
                                <div style={{fontSize: '17px', lineHeight: '1.5'}}> 
                                    This is a  <Popup content='Hanja: Korean name for Chinese characters' trigger={<Button size='tiny' compact style={{backgroundColor: '#f5b895', borderRadius: 0}} content='hanja'/>} /> word. <br/>
                                    People use hanja to understand basic Korean words, 한글. <br/>
                                    한글은 자음과 {defaultButton('모음', '모음: 자음이 아닌 것')}으로 이루어져 있다.
                                </div>
                            </Card.Content>
                            </Card>
                        </Form.Field>
                        : null
                    }
                </Form>
            </div>
        )
    }
}