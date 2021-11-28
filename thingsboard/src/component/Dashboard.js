import React, {useState} from 'react';
import ButtonLightSensor from './Button';
import ButtonHumidity from './ButtonHumidity';
import '../App.css'
import FluidSensor from './FluidSensor';

const Dashboard = () => {


    return (
        <div>
            <div className="divcard">
                <div>
                    <ButtonLightSensor title="Light sensor"/> <br/>
                </div>
                <div>
                    <ButtonHumidity title="Temperature and Humidity" />
                </div>
                <div>
                    <FluidSensor title="Fluid sensor" />
                </div>
            </div>
        </div>
    );
};

export default Dashboard;