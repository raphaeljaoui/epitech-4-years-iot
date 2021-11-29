import React,{useState} from 'react';
import Fluid from'../fluid-sensor.jpeg'

const FluidSensor = ({title}) => {
    const [name, setname] = useState("")
    const [value, setvalue] = useState(0)
    const [time, settime] = useState(0)
    const [color, setColor] = useState(undefined)
    const [quantity, setQuantity] = useState(0)


    const send = () => {
        var obj = {
            name,
            value,
            color,
            quantity,
            time
        }

        return setInterval(() => {
            // console.log(obj);
            fetch("http://127.0.0.1:5000/fluid_sensor", {
                method:"POST",
                headers:{
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify(obj)
            }).then(res=> {return res.json()})
            .then(res=> console.log(res))
        }, time*1000)
        // setTimeout(() => {
        //     console.log(obj);
        // }, time* 1000)
    }

    const stop = () => {
        var x  = send()
        clearInterval(x)
    }
    return (
        <div>
            <img src={Fluid} style={{width:50, height:50}}/>
            <label>{title}</label> <br/>
            <label>value</label> <br/>
            <input type="text" onChange={e => setvalue(e.target.value)}/> <br/>
            <label>select Fluid</label> <br/>
            <select name="status" id="pet-select" onChange={e => setname(e.target.value)}>
                <option value="">--Please choose a fluid sensor--</option>
                <option value="1">1 - Pipeline 1</option>
                <option value="2">2 - Pipeline 2</option>
                <option value="3">3 - Fluide sensor printer</option>
            </select><br/>
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
            {/* <button onClick={stop}>stop</button> */}
        </div>
    );
};

export default FluidSensor;