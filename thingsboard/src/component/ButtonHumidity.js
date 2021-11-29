import React, {useState} from 'react';

const ButtonHumidity = ({title}) => {
    const [value, setvalue] = useState(0)
    const [time, settime] = useState(0)

    const send = () => {
        var obj = {
            value,
            time
        }

        return fetch("http://127.0.0.1:5000/temp_humidity", {
            method:"POST",
            headers:{
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body:JSON.stringify(obj)
        }).then(res=> {return res.json()})
        .then(res=> console.log(res))
        // setTimeout(() => {
        //     console.log(obj);
        // }, time* 1000)
    }

    return (
        <div>
            <label>{title}</label> <br/>
            <label>value</label> <br/>
            <input type="number"  onChange={e => setvalue(e.target.value)}/> <br/>
            <label>time</label> <br/>
            <input type="number" onChange={e => settime(e.target.value)}/> <br/>
            <button onClick={send}>send</button>

        </div>
    );
};

export default ButtonHumidity;