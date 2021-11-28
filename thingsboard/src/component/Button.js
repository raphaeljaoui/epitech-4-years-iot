import React,{useState} from 'react';

const ButtonLightSensor = ({title}) => {
    const [boolLight, setboolLight] = useState(false)
    const [status, setStatus] = useState(undefined)
    const [time, setTime] = useState(0)

    const send = () => {
        var obj = {
            value: boolLight,
            status,
        }

        setTimeout(() => {
            console.log(obj);
        }, time* 1000)
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