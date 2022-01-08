// Day 18: Like a Rogue

const fs = require("fs");

const INPUT_FILE_NAME = './inputs/day18input.txt';
const TEST_INPUT = '.^^.^.^^^^';

const SAFE_TILE = '.';
const TRAP = '^';

/**
 * Pass in a file name and return an array representing the tiles
 * in the first row of the room.
 * @param   {string} fileName the file name
 * @returns {Array}           the first row of the room.
 */
const readFile = (fileName) => {
  return fs.readFileSync(fileName, 'utf-8').split("");
}

/**
 * Pass in the current row and the current column and return a character 
 * representing the type of tile below the current location.
 * 
 * As stated in the problem, tile G depends on the types of A, B and C - 
 * named left, center, and right respectively.
 *   ABCDE
 *   FGHIJ
 * 
 * The next tile below the current tile is a trap if a condition is met:
 *   - left and center tiles are traps but right tile is safe
 *   - right and center tiles are traps but left tile is safe
 *   - only the left tile is a trap
 *   - only the right tile is a trap
 * @param   {Array}  row the current row of the room 
 * @param   {number} i   index in the row representing the column location
 * @returns {string}     the tile type of the tile below current location  
 */
const getTileBelow = (row, i) => {
  const left = i - 1 < 0 ? SAFE_TILE : row[i - 1];
  const right = i + 1 === row.length ? SAFE_TILE : row[i + 1];
  const middle = row[i];

  if ((left === TRAP && middle === TRAP && right === SAFE_TILE) ||
    (left === SAFE_TILE && middle === TRAP && right === TRAP) ||
    (left === TRAP && middle === SAFE_TILE && right === SAFE_TILE) ||
    (left === SAFE_TILE && middle === SAFE_TILE && right === TRAP)) {
      return TRAP;
  }
  return SAFE_TILE;
}

/**
 * Pass in the initial row of the room and the number of rows in the room and
 * return the number of safe tiles.
 * @param   {Array} row      the first row in the room
 * @param   {number} numRows the number of rows in the room
 * @returns {number}         number of safe tiles in the room
 */
const countSafeTiles = (row, numRows) => {
  let count = row.filter(tile => tile === SAFE_TILE).length;
  let nextRow = [];

  for (let num = 0; num < numRows - 1; num++) {
    for (let i = 0; i < row.length; i++) {
      const tileBelow = getTileBelow(row, i);
      nextRow.push(tileBelow);
      count += tileBelow === SAFE_TILE ? 1 : 0;
    }
    row = nextRow;
    nextRow = [];
  }
  return count;
}

const solvePartOne = (firstRow) => {
  return countSafeTiles(firstRow, 40);
}

const solvePartTwo = (firstRow) => {
  return countSafeTiles(firstRow, 400000);
}

const main = () => {
  console.assert(countSafeTiles(TEST_INPUT.split(""), 10) === 38);

  const firstRow = readFile(INPUT_FILE_NAME);
  console.log("Part One:", solvePartOne(firstRow));
  console.log("Part Two:", solvePartTwo(firstRow));
}

main();