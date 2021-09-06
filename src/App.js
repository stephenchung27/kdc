import React, { useState } from 'react';
import './App.css';
import { flipCar, nullBoardState, setBoardSpace, toggleHorizontalRoad, toggleVerticalRoad } from './boardUtils';
import BoardSpaceRow from './components/BoardSpaceRow';
import HorizontalRoadRow from './components/HorizontalRoadRow';
import Options from './components/Options';
import car from './images/car.png';

function App() {
  const [board, setBoard] = useState(nullBoardState);

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
      <Options board={board} flipCar={() => flipCar(board, setBoard)} />
    </div>
  );
}

export default App;
