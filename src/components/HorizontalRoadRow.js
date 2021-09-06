import React from 'react';
import HorizontalRoad from './HorizontalRoad';
import '../css/horizontal-road-row.css';

function HorizontalRoadRow({
  row,
  boardHorizontalRoads,
  toggleHorizontalRoad,
}) {

  function mapHorizontalRow() {
    const mappedHorizontalRow = [];

    for (let column = 0; column < boardHorizontalRoads.length; column++) {
      mappedHorizontalRow.push(
        <React.Fragment>
          <div key={`intersection-${row}-${column}`} className="intersection" />
          <HorizontalRoad key={`horizontal-road-${row}-${column}`}
            blocked={!boardHorizontalRoads[column]}
            toggleHorizontalRoad={() => toggleHorizontalRoad(column)}/>
        </React.Fragment>
      )
    }

    mappedHorizontalRow.push(<div className="intersection" />);

    return mappedHorizontalRow;
  }

  return (
    <div key={row} className="horizontal-road-row">
      {mapHorizontalRow()}
    </div>
  )
}

export default HorizontalRoadRow;
