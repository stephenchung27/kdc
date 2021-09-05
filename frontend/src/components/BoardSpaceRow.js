import React from 'react';
import BoardSpace from './BoardSpace';
import VerticalRoad from './VerticalRoad';
import '../css/board-space-row.css';

function BoardSpaceRow({
  row, boardVerticalRoads, toggleVerticalRoad, boardSpaceRow, setBoardSpace
}) {

  function mapBoardSpaceRow() {
    const mappedBoardSpaceRow = [];

    for (let column = 0; column < boardSpaceRow.length; column++) {
      mappedBoardSpaceRow.push(
        <React.Fragment>
          <VerticalRoad key={`vertical-road-${row}-${column}`}
            blocked={!boardVerticalRoads[column]}
            toggleVerticalRoad={() => toggleVerticalRoad(column)} />
          <BoardSpace key={`board-space-${row}-${column}`}
            boardSpaceType={boardSpaceRow[column]}
            setBoardSpace={(boardSpaceType) => setBoardSpace(column, boardSpaceType)} />
        </React.Fragment>
      )
    }

    mappedBoardSpaceRow.push(
      <VerticalRoad key={5}
        boardVerticalRoad={boardVerticalRoads[5]}
        toggleVerticalRoad={() => toggleVerticalRoad(5)} />
    )

    return mappedBoardSpaceRow;
  }

  return (
    <div key={row} className='board-space-row'>
      {mapBoardSpaceRow()}
    </div>
  )
}

export default BoardSpaceRow;
