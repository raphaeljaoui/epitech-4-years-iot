import React,{useState} from 'react';

const FluidSensor = ({title}) => {
    const [value, setvalue] = useState(0)
    const [time, settime] = useState(0)
    const [color, setColor] = useState(undefined)
    const [qunatity, setQuantity] = useState(0)


    const send = () => {
        var obj = {
            value,
            color,
            qunatity
        }

        setTimeout(() => {
            console.log(obj);
        }, time* 1000)
    }
    return (
        <div>
            <label>{title}</label> <br/>
            <label>value</label> <br/>
            <input type="text" onChange={e => setvalue(e.target.value)}/> <br/>
            <label>color</label> <br/>
            <select name="status" id="pet-select" onChange={e => setColor(e.target.value)}>
                <option value="">--Please choose a color--</option>
                <option value="red">red</option>
                <option value="green">green</option>
                <option value="blue">blue</option>
            </select><br/>
            <label>quantity</label> <br/>
            <input type="number" onChange={e => setQuantity(e.target.value)}/> <br/>
            <label>time</label> <br/>
            <input type="number" onChange={e => settime(e.target.value)}/> <br/>
            <button onClick={send}>send</button>
        </div>
    );
};

export default FluidSensor;