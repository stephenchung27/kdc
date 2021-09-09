import { useState } from 'react';
import '../css/options.css';
import CarDirectionOption from './CarDirectionOption';
import MissingBoardSpaces from './MissingBoardSpaces';

function Options({
  board,
  setDirection,
  clearBoard,
  setResults,
  setBoard,
}) {
  const [calculating, setCalculating] = useState(false);
  const [validBoard, setValidBoard] = useState(false);
  const [inputtedBoard, setInputtedBoard] = useState("");
  const [showMessage, setShowMessage] = useState(false);

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

  function handleSubmit(event) {
    if (inputtedBoard.length === 0) {
      return
    }
    setBoard(JSON.parse(inputtedBoard));
    setInputtedBoard("");
    event.preventDefault();
  }

  function handleCopy() {
    navigator.clipboard.writeText(JSON.stringify(board));
    setShowMessage(true);
  }

  function handleTransitionEnd() {
    setShowMessage(false);
  }

  return (
    <div className="options">
      <MissingBoardSpaces boardSpaces={board.board_spaces} 
        directionNotSet={board.direction === null}
        setValidBoard={setValidBoard} />
      <CarDirectionOption setDirection={setDirection} direction={board.direction} />
      <div className="buttons">
        <button onClick={calculate} disabled={!validBoard || calculating}>
          {calculating ? "RUNNING..." : "CALCULATE"}
        </button>
        <button onClick={clearBoard}>CLEAR</button>
      </div>
      <div className={`load-bar-wrapper`}>
        <div className={`load-bar${calculating ? " loading" : ""}`}></div>
      </div>
      <div className="credits">
        Created by stephen#1111
      </div>
      <div className={`copy-message${showMessage ? "" : " hidden"}`}
        onTransitionEnd={handleTransitionEnd}>
        BOARD WAS COPIED
      </div>
      <div className="copy-options">
        <form onSubmit={handleSubmit} >
        <input type="text" value={inputtedBoard} 
          onChange={(e) => setInputtedBoard(e.target.value)} />
        </form>
        <button onClick={handleCopy}>
          COPY
        </button>
      </div>
    </div>
  );
}

export default Options;
