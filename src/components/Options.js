import { useState } from 'react';
import '../css/options.css';
import CarDirectionOption from './CarDirectionOption';
import MissingBoardSpaces from './MissingBoardSpaces';

function Options({
  board,
  setDirection,
  clearBoard,
  setResults,
}) {
  const [calculating, setCalculating] = useState(false);
  const [validBoard, setValidBoard] = useState(false);

  async function calculate() {
    setCalculating(true);
    const response = await fetch("./calculate", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(board)
    });
    response.json().then((data) => {
      console.log(data);
      setResults(data);
      setCalculating(false);
    })
  }

  return (
    <div className="options">
      <MissingBoardSpaces boardSpaces={board.board_spaces} 
        setValidBoard={setValidBoard} />
      <CarDirectionOption setDirection={setDirection} direction={board.direction} />
      <div className="buttons">
        <button onClick={calculate} disabled={!validBoard || calculating}>
          {calculating ? "RUNNING" : "CALCULATE"}
        </button>
        <button onClick={clearBoard}>CLEAR</button>
      </div>
    </div>
  );
}

export default Options;
