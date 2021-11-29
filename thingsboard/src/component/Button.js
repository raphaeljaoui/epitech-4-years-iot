import React,{useState} from 'react';

const ButtonLightSensor = ({title}) => {
    const [boolLight, setboolLight] = useState(false)
    const [status, setStatus] = useState(undefined)
    const [time, setTime] = useState(0)

    const send = () => {
        var obj = {
            is_open: "boolLight",
            light_sensor: "status",
            time,
        }

        return fetch("http://127.0.0.1:5000/light_sensor", {
            method:"POST",
            headers:{
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body:JSON.stringify(obj)
        }).then(res=> {return res.json()})
        .then(res=> console.log(res))

        // setInterval(() => {
        //     console.log(obj);
        // }, time* 1000)
    }

    return (
        <>
            <label for="pet-select">{title}</label> <br/>
            <button onClick={() => setboolLight(!boolLight)}>{title}</button> <br/>

            <select name="status" id="pet-select" onChange={e => setStatus(e.target.value)}>
                <option value="">--Please choose a status--</option>
                <option value="Day">Day</option>
                <option value="night">night</option>
            </select><br/>
            <label>time</label> <br/>
            <input type="number" onChange={e => setTime(e.target.value)}/> <br/>
            <button onClick={send}>send</button>
        </>
    );
};

export default ButtonLightSensor;