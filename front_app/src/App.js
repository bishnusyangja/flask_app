import React from 'react';
import {useState} from 'react';

import './App.css';
import 'antd/dist/antd.css'
import { Row, Col } from 'antd';

import RegisterForm from './components/register'
import LoginForm from './components/login'
import HomePage from './components/home'


function App() {
    let auth_token = localStorage.getItem('auth_token', '')
    const [isLoggedin, setIsLoggedin]=useState({status: false});

    if (isLoggedin.status)
        return (
            <Row>
                <HomePage />
            </Row>
    );
    else
        return (
          <Row>
              <Col span={10} > <LoginForm setIsLoggedin={setIsLoggedin} /> </Col>
              <Col span={10} > <RegisterForm /> </Col>
          </Row>
    );

}

export default App;