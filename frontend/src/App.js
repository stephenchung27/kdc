import React, { useState } from 'react';
import './App.css';
import { flipCar, nullBoardState, setBoardSpace, toggleHorizontalRoad, toggleVerticalRoad } from './boardUtils';
import BoardSpaceRow from './components/BoardSpaceRow';
import HorizontalRoadRow from './components/HorizontalRoadRow';
import car from './images/car.png';

function App() {
  const [board, setBoard] = useState(nullBoardState);

  function mapBoardRows() {
    const mappedRows = [];

    for (let row = 0; row < board.boardSpaces.length; row++) {
      mappedRows.push(
        <React.Fragment>
          <HorizontalRoadRow row={row}
            boardHorizontalRoads={board.horizontalRoads[row]}
            toggleHorizontalRoad={(column) => 
              toggleHorizontalRoad(board, setBoard, row, column)} />
          <BoardSpaceRow row={row}
            boardVerticalRoads={board.verticalRoads[row]}
            toggleVerticalRoad={(column) => 
              toggleVerticalRoad(board, setBoard, row, column)}
            boardSpaceRow={board.boardSpaces[row]}
            setBoardSpace={(column, boardSpaceType) => 
              setBoardSpace(board, setBoard, row, column, boardSpaceType)} />
        </React.Fragment>
      )
    }

    mappedRows.push(
      <HorizontalRoadRow row={7}
        boardHorizontalRoads={board.horizontalRoads[7]}
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
          className={`car${board.startingDirection === "Left" ? " flipped" : ""}`}
          alt="Car" src={car} />
      </div>
      <div>
        <button onClick={() => flipCar(board, setBoard)}>FLIP</button>
      </div>
    </div>
  );
}

export default App;
