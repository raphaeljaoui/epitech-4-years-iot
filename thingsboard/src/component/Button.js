import React,{useState} from 'react';
import Light from '../light-sensor.png'

const ButtonLightSensor = ({title}) => {
    const [name, setname] = useState("")
    const [boolLight, setboolLight] = useState(false)
    const [status, setStatus] = useState(undefined)
    const [lightIntensity, setlightIntensity] = useState(undefined)
    const [time, setTime] = useState(0)

    const send = () => {
        var obj = {
            name,
            is_open: boolLight,
            light_sensor: status,
            time:lightIntensity
        }


        setInterval(() => {
            fetch("http://127.0.0.1:5000/light_sensor", {
                method:"POST",
                headers:{
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify(obj)
            }).then(res=> {return res.json()})
            .then(res=> console.log(res))
        }, time* 1000)
    }

    return (
        <>
            <img src={Light} style={{width:50, height:50}}/>
            <label for="pet-select">{title}</label> <br/>
            <button onClick={() => setboolLight(!boolLight)}>{title}</button> <br/>
            <label>select Ligth</label> <br/>
            <select name="status" id="pet-select" onChange={e => setname(e.target.value)}>
                <option value="">--Please choose a ligth sensor--</option>
                <option value="1">1 - Outside light</option>
                <option value="2">2 - Kitchen room</option>
                <option value="3">3 - Light parent room</option>
            </select><br/>
            <label>Status</label> <br/>
            <select name="status" id="pet-select" onChange={e => setStatus(e.target.value)}>
                <option value="">--Please choose a status--</option>
                <option value="Day">Day</option>
                <option value="night">night</option>
            </select><br/>
            <label>Light intensity</label> <br/>
            <input type="number" onChange={e => setlightIntensity(e.target.value)}/> <br/>
            <label>time</label> <br/>
            <input type="number" onChange={e => setTime(e.target.value)}/> <br/>
            <button onClick={send}>send</button>
        </>
    );
};

export default ButtonLightSensor;