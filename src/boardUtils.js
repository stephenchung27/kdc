export const nullBoardState = {
  horizontal_roads: [
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
    [true, true, true, true, true],
  ],
  vertical_roads: [
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
    [true, true, true, true, true, true],
  ],
  board_spaces: [
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
  ],
  direction: "Right",
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
  newBoard.horizontal_roads[row][column] = !board.horizontal_roads[row][column];

  // Unblock intersecting vertical roads
  newBoard.vertical_roads[row-1][column] = true;
  newBoard.vertical_roads[row-1][column+1] = true;
  newBoard.vertical_roads[row][column] = true;
  newBoard.vertical_roads[row][column+1] = true;

  setBoard(newBoard);
}

export function toggleVerticalRoad(board, setBoard, row, column) {
  // Block first and last vertical road columns
  if (column === 0 || column === 5) {
    return
  }

  const newBoard = copyBoard(board);
  newBoard.vertical_roads[row][column] = !board.vertical_roads[row][column];

  // Unblock intersecting vertical roads
  newBoard.horizontal_roads[row][column] = true;
  newBoard.horizontal_roads[row][column-1] = true;
  newBoard.horizontal_roads[row+1][column] = true;
  newBoard.horizontal_roads[row+1][column-1] = true;

  setBoard(newBoard);
}

export function setBoardSpace(board, setBoard, row, column, boardSpaceType) {
  const newBoard = copyBoard(board);
  newBoard.board_spaces[row][column] = boardSpaceType;
  setBoard(newBoard);
}

export function flipCar(board, setBoard) {
  const newBoard = copyBoard(board);
  newBoard.direction = board.direction === "Right" ? "Left" : "Right";
  setBoard(newBoard);
}
