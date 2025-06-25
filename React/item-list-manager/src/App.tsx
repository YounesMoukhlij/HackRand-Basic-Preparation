import { useState } from "react";
import "./App.css";

function App() {
    const [items, setItems] = useState([]);
    const [input, setInput] = useState("");

    const handleAddItem = () => {

        if (input === "")
            return;
        setItems([...items, input]);
        setInput("");


    };

    return (
        <>
            <div className="app">
                <h3  className="title">Item List</h3>

                <div className="item-list">

                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Enter item"
                    data-testid="input-field"
                />
                <button onClick={handleAddItem} data-testid="add-button">
                    Add Item
                </button>
                </div>
                <ul data-testid="item-list">
                    {items.map((item, index) => (
                        <li key={index} data-testid="list-item">
                            {item}
                        </li>
                    ))}
                </ul>
            </div>
        </>
    );
}

export default App;
