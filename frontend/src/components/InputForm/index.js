import React, { useState } from "react";
import "./index.css";

const FORM_STATES = {
    WAITING_INPUT: 1,
    INPUT_LOADED: 2,
    SHOW_RESULTS: 3,
};

export default function InputForm() {
    const [currentState, setCurrentState] = useState(FORM_STATES.WAITING_INPUT);
    const [plate, setPlate] = useState();
    const [result, setResult] = useState([]);

    const handlePlateChange = (e) => {
        setPlate(e.target.value);

        if (e.target.value.length) setCurrentState(FORM_STATES.INPUT_LOADED);
        else setCurrentState(FORM_STATES.WAITING_INPUT);
    };

    const handleSubmit = async () => {
        fetch(`http://localhost:80/?plate=${plate}`).then( r => {
            r.json().then( d => {
                setResult(d);
                setCurrentState(FORM_STATES.SHOW_RESULTS);
            });
        }, r => {
            console.log(r);
        });
    }

    return (
        <>
            <div className="result-title-container">
                <p>Search a Car's Model:</p>
            </div>
    
            <div className="input-container">
                <input
                    id="plate"
                    value={plate}
                    placeholder="The car's plate:"
                    onChange={handlePlateChange}
                />
            </div>

            {currentState === FORM_STATES.INPUT_LOADED && (
            <div style={{ display: "flex", justifyContent: "center", marginTop: "20px"}}>
                <button onClick={() => {handleSubmit();}} className="submit-button">
                    Search
                </button>
            </div>
            )}

            <div className={`result-container ${currentState === FORM_STATES.SHOW_RESULTS ? "div-show" : "div-hide"}`}>
                <label>{result}</label>
            </div>
        </>
    );
}