import React, { useEffect, useState } from 'react';
import './App.css';
import { setDirection, nullBoardState, setBoardSpace, toggleHorizontalRoad, toggleVerticalRoad } from './boardUtils';
import BoardSpaceRow from './components/BoardSpaceRow';
import HorizontalRoadRow from './components/HorizontalRoadRow';
import Options from './components/Options';
import car from './images/car.png';
import ResultRoute from './components/ResultRoute';


function App() {
  const [board, setBoard] = useState(nullBoardState);
  const [results, setResults] = useState([
    {
        "description": "Successful Route",
        "route": [
            "Coffee House",
            "Right",
            "Ballroom",
            "Up",
            "Up",
            "Up",
            "Left",
            "Fair",
            "Up",
            "Taco Stand",
            "Up",
            "Up",
            "Gas Station",
            "Left",
            "Juice Bar",
            "Up",
            "Right",
            "Down",
            "Flower Garden",
            "Down",
            "Down",
            "Gas Station",
            "Down",
            "Taco Stand",
            "Fair"
        ],
        "state": {
            "drink": 41,
            "entertainment": 92,
            "food": 100,
            "fuel": 90,
            "time": 0
        }
    },
    {
      "description": "Route with Shopping Mall and Jewelry Store then Airport",
      "route": [
          "Coffee House",
          "Right",
          "Ballroom",
          "Up",
          "Up",
          "Up",
          "Left",
          "Fair",
          "Up",
          "Taco Stand",
          "Up",
          "Up",
          "Gas Station",
          "Left",
          "Juice Bar",
          "Up",
          "Right",
          "Down",
          "Flower Garden",
          "Down",
          "Down",
          "Gas Station",
          "Down",
          "Taco Stand",
          "Fair"
      ],
      "state": {
          "drink": 41,
          "entertainment": 92,
          "food": 100,
          "fuel": 90,
          "time": 0
      }
  }
]);

  function clearBoard() {
    setBoard(nullBoardState);
  }

  useEffect(() => {
    localStorage.setItem('board', JSON.stringify(board));
  }, [board])

  useEffect(() => {
    const retrievedBoard = JSON.parse(localStorage.getItem('board'));
    console.log(retrievedBoard);
    if (retrievedBoard.board_spaces !== undefined) {
      setBoard(retrievedBoard);
    }
  }, [])

  function mapBoardRows() {
    const mappedRows = [];

    for (let row = 0; row < board.board_spaces.length; row++) {
      mappedRows.push(
        <React.Fragment>
          <HorizontalRoadRow row={row}
            boardHorizontalRoads={board.horizontal_roads[row]}
            toggleHorizontalRoad={(column) => 
              toggleHorizontalRoad(board, setBoard, row, column)} />
          <BoardSpaceRow row={row}
            boardVerticalRoads={board.vertical_roads[row]}
            toggleVerticalRoad={(column) => 
              toggleVerticalRoad(board, setBoard, row, column)}
            boardSpaceRow={board.board_spaces[row]}
            setBoardSpace={(column, boardSpaceType) => 
              setBoardSpace(board, setBoard, row, column, boardSpaceType)} />
        </React.Fragment>
      )
    }

    mappedRows.push(
      <HorizontalRoadRow row={7}
        boardHorizontalRoads={board.horizontal_roads[7]}
        toggleHorizontalRoad={(column) => 
          toggleHorizontalRoad(board, setBoard, 7, column)} />
    )

    return mappedRows;
  }

  return (
    <div className="App">
      <div className="board">
        {mapBoardRows()}
        <img 
          className={`car${board.direction === "Left" ? " flipped" : ""}`}
          alt="Car" src={car} />
      </div>
      <Options board={board} 
        setDirection={(direction) => setDirection(board, setBoard, direction)}
        clearBoard={clearBoard}
        setResults={setResults} />
      <div className="result-list">
        {results.map(result => <ResultRoute result={result} />)}
      </div>
    </div>
  );
}

export default App;
