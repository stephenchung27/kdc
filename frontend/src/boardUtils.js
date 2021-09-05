export const nullBoardState = {
  horizontalRoads: [
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
  ],
  verticalRoads: [
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
  ],
  boardSpaces: [
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
  ],
  startingDirection: null,
}

Object.freeze(nullBoardState);

export function copyBoard(board) {
  return JSON.parse(JSON.stringify(board));
}

export function toggleHorizontalRoad(board, setBoard, row, column) {
  // Block first and last horizontal road rows
  if (row === 0 || row === 7) {
    return
  }

  const newBoard = copyBoard(board);
  newBoard.horizontalRoads[row][column] = !board.horizontalRoads[row][column];

  // Unblock intersecting vertical roads
  newBoard.verticalRoads[row-1][column] = true;
  newBoard.verticalRoads[row-1][column+1] = true;
  newBoard.verticalRoads[row][column] = true;
  newBoard.verticalRoads[row][column+1] = true;

  setBoard(newBoard);
}

export function toggleVerticalRoad(board, setBoard, row, column) {
  // Block first and last vertical road columns
  if (column === 0 || column === 5) {
    return
  }

  const newBoard = copyBoard(board);
  newBoard.verticalRoads[row][column] = !board.verticalRoads[row][column];

  // Unblock intersecting vertical roads
  newBoard.horizontalRoads[row][column] = true;
  newBoard.horizontalRoads[row][column-1] = true;
  newBoard.horizontalRoads[row+1][column] = true;
  newBoard.horizontalRoads[row+1][column-1] = true;

  setBoard(newBoard);
}

export function setBoardSpace(board, setBoard, row, column, boardSpaceType) {
  const newBoard = copyBoard(board);
  console.log(boardSpaceType)
  newBoard.boardSpaces[row][column] = boardSpaceType;
  setBoard(newBoard);
}

export function flipCar(board, setBoard) {
  const newBoard = copyBoard(board);
  newBoard.startingDirection = board.startingDirection === "Right" ? "Left" : "Right";
  setBoard(newBoard);
}
