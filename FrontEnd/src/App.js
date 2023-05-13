import WeatherData from './components/weatherData';
import WeatherStats from './components/weatherStats';
import {useState} from 'react';

import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom';


export default function WebApp(){

  const [stateCode, setStateCode] = useState("");
  const [inputStateCode, setInputStateCode] = useState("")
  const [date, setDate] = useState("")
  const [inputDate, setInputDate] = useState("")

  const handleSubmit = (event) => {
    event.preventDefault();
    setDate(inputDate);
    setStateCode(inputStateCode);
    
  }

	return(
    <>
    <h1>Weather data</h1>
    <br></br>
      <form onSubmit={handleSubmit}>
          <input name="stateCode" value={inputStateCode} placeholder="State Code" onChange={(e) => setInputStateCode(e.target.value)} />
          <input name="date" value={inputDate} placeholder="Date or Year" onChange={(e) => setInputDate(e.target.value)} />
          <input type="submit" />
          </form>
            <br></br>
            <Router>
            <div >
            <ul >
              <li>
                <Link to="/weather">Raw data</Link>
              </li>
              <li>
                <Link to="/statistics">Weather Statistics</Link>
              </li>
            </ul>
           <Routes>
                 <Route exact path='/weather' element={< WeatherData stateCode={stateCode} date={date}/>}></Route>
                 <Route exact path='/statistics' element={<WeatherStats stateCode={stateCode} date={date}/>}></Route>
          </Routes>
          </div>
        
       </Router>
        
    </>
		
	);
}
