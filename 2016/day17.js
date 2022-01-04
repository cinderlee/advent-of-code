// Day 17: Two Steps Forward

const crypto = require('crypto');

const INPUT_PASSCODE = 'qzthpkfp';
const TEST_PASSCODE = 'ihgpwlah';
const TEST_PASSCODE_2 = 'kglvqrro';
const TEST_PASSCODE_3 = 'ulqzkmiv';

const GRID_SIZE = 4;
const OPEN_DOOR_VALUES = 'bcdef';
const DIRECTIONS = {
  'U': [0, -1, 0],
  'D': [1, 1, 0],
  'L': [2, 0, -1],
  'R': [3, 0, 1]
};

/**
 * Pass in a room location and return whether the location is valid. The
 * grid of rooms has a size of GRID_SIZE
 * @param   {number} row the row number 
 * @param   {number} col the column number
 * @returns {boolean}    whether the row and column are valid
 */
const isValidRoom = (row, col) => {
  return row >= 0 && row < GRID_SIZE && col >= 0 && col < GRID_SIZE;
}

/**
 * Pass in an array of doors and information about the current room (row, col, directions)
 * and return a list of accessible adjacent rooms such that the doors to them are open.
 * @param {string} doors              the first four characters of the hash 
 *                                    representing the doors of the current room
 * @param {number} currentRow         the current room's row number
 * @param {number} currentCol         the current room's column number
 * @param {string} passcodeDirections the concatenation of the passcode and directions 
 *                                    to reach the current room
 * @returns {Array}                   the list of adjacent rooms, each represents as an 
 *                                    array containing its row, column, and directions 
 *                                    attached to the end of the passcode
 */
const getAdjacentRooms = (doors, currentRow, currentCol, passcodeDirections) => {
  const adjacentRooms = [];
  Object.keys(DIRECTIONS).forEach(direction => {
    const [index, rowDisp, colDisp] = [...DIRECTIONS[direction]];
    if (OPEN_DOOR_VALUES.includes(doors[index])) {
      adjacentRooms.push([currentRow + rowDisp, currentCol + colDisp, passcodeDirections + direction]);
    }
  });

  return adjacentRooms;
}

/**
 * Pass in a passcode and a boolean and return the shortest or longest
 * path from the start to the end of the grid of rooms. Starting
 * point is (0, 0) and ending point is the bottom right corner of the grid.
 * 
 * The doors to every room are open depending on the first four characters 
 * of the MD5 hash of the concatenation of the passcode and the directions 
 * leading up to that room. 
 * 
 * The characters respectively represent the up, down, left and right doors. 
 * The door is open if the hash character is b, c, d, e, or f. 
 * @param {string}  passcode       the passcode
 * @param {boolean} isLongestPath  whether to return the longest or shortest path
 * @returns {string}               the path
 */
const findPath = (passcode, isLongestPath=false) => {
  const queue = [[0, 0, passcode]];
  let longestPath = "";

  while (queue.length) {
    const [row, col, passcodeDirections] = [...queue.shift()];
    
    if (row === GRID_SIZE - 1 && col === GRID_SIZE - 1) {
      const directions = passcodeDirections.substring(passcode.length);
      if (!isLongestPath) {
        return directions;
      } else {
        longestPath = directions;
      }
      continue;
    }

    if (!isValidRoom(row, col)) {
      continue;
    }
    
    const doors = crypto.createHash('md5').update(passcodeDirections).digest('hex').toString().substring(0, 4);
    queue.push(...getAdjacentRooms(doors, row, col, passcodeDirections));
  }

  return longestPath;
}

/**
 * Pass in a passcode and return the shortest path to the vault in the 
 * bottom right corner of the grid.
 * @param   {string} passcode the passcode
 * @returns {string}          the shortest path to the vault
 */
const solvePartOne = (passcode) => {
  return findPath(passcode);
}

/**
 * Pass in a passcode and return the length of the longest path to 
 * the vault in the bottom right corner of the grid.
 * @param   {string} passcode the passcode
 * @returns {number}          the length of the longest path to the vault
 */
const solvePartTwo = (passcode) => {
  return findPath(passcode, true).length;
}

const main = () => {
  console.assert(solvePartOne(TEST_PASSCODE) === "DDRRRD");
  console.assert(solvePartTwo(TEST_PASSCODE) === 370);

  console.assert(solvePartOne(TEST_PASSCODE_2) === "DDUDRLRRUDRD");
  console.assert(solvePartTwo(TEST_PASSCODE_2) === 492);

  console.assert(solvePartOne(TEST_PASSCODE_3) === "DRURDRUDDLLDLUURRDULRLDUUDDDRR");
  console.assert(solvePartTwo(TEST_PASSCODE_3) === 830);

  console.log('Part One:', solvePartOne(INPUT_PASSCODE));
  console.log('Part Two:', solvePartTwo(INPUT_PASSCODE));
}

main()
