import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import AddApplication from './pages/AddApplication';
import ResumeUpload from './pages/ResumeUpload';
import Login from './pages/Login';
import Signup from './pages/Signup';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={Dashboard} />
                <Route path="/add-application" component={AddApplication} />
                <Route path="/upload-resume" component={ResumeUpload} />
                <Route path="/login" component={Login} />
                <Route path="/signup" component={Signup} />
            </Switch>
        </Router>
    );
};

export default App;