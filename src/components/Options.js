import { useState } from 'react';
import ResultRoute from './ResultRoute';
import '../css/options.css';

const boardSpaceCount = {
    'Gas Station': 3,
    'Italian Restaurant': 1,
    'Taco Stand': 1,
    'Sandwich Shop': 1,
    'Fair': 1,
    'Juice Bar': 1,
    'Coffee House': 1,
    'Nightclub': 1,
    'Flower Garden': 1,
    'Ballroom': 1,
    'Theatre': 1,
    'Airport': 1,
    'Home': 1,
    // 'Jewelry Store': -1,
    // 'Shopping Mall': -1,
}

function Options({
  board,
  flipCar,
}) {
  const [results, setResults] = useState([]);
  const [calculating, setCalculating] = useState(false);

  async function calculate() {
    setCalculating(true);
    const response = await fetch("./calculate", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(board)
    });
    response.json().then((data) => {
      setResults(data);
      setCalculating(false);
    })
  }

  function getMissingBoardSpaces() {
    const runningBoardSpaceCounts = Object.assign({}, boardSpaceCount);
  
    for (const row of board.board_spaces) {
      for (const boardSpace of row) {
        runningBoardSpaceCounts[boardSpace] -= 1;
      }
    }

    const missingBoardSpaces = []

    for (const boardSpaceType in runningBoardSpaceCounts) {
      if (runningBoardSpaceCounts[boardSpaceType] > 0) {
        missingBoardSpaces.push([boardSpaceType, runningBoardSpaceCounts[boardSpaceType]])
      }
    }
  
    if (missingBoardSpaces.length > 0) {
      return (
        <div className="missing-board-spaces-list">
          <p>Missing the following board spaces:</p>
          <ul>
            {missingBoardSpaces.map(boardSpace => {
              const [name, count] = boardSpace;
              return (
                <li>
                  {count > 1 ? `${count} ` : ""}{name}{count > 1 ? "s" : ""}
                </li>
              );
            })}
          </ul>
        </div>
      )
    } else {
      return (
        <span className="no-missing-spaces">
          "All board spaces covered."
        </span>
      );
    }
  }

  return (
    <div className="options">
      <div className="buttons">
        <div className="car-direction-options">
          <button onClick={flipCar}>FLIP</button>
          <span>Car is facing <span className="direction">{board.direction}</span></span>
        </div>
        <div className="missing-board-spaces">
          {getMissingBoardSpaces()}
        </div>
        <button onClick={calculate} disabled={calculating}>CALCULATE</button>
      </div>
      <div>
        {results.map(result => <ResultRoute result={result} />)}
      </div>
    </div>
  );
}

export default Options;
