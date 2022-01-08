// Day 2: Bathroom Security

const fs = require('fs');

const INPUT_FILE_NAME = './inputs/day02input.txt';
const TEST_FILE_NAME = './inputs/day02testinput.txt';

/**
 * Pass in a file name and return an array of directions where each direction
 * is also an array containing up, down, left, right steps.
 * @param   {string} fileName the file name
 * @returns {Array}           the code directions
 */
const readFile = (fileName) => {
  const fileData = fs.readFileSync(fileName, 'utf-8');
  return fileData.split('\n').map(direction => direction.split(''));
}

/**
 * Pass in a instruction, keyPad, current row and column. Return the next
 * row and column after following the instruction.
 * is also an array containing up, down, left, right steps.
 * @param   {string} instruction the instruction (U, D, L, R)
 * @param   {Array} keyPad     the keypad
 * @param   {number} row       the current row
 * @param   {number} col       the current column
 * @returns {Array}            the next location [row, column]
 */
const followInstruction = (instruction, keyPad, row, col) => {
  switch(instruction) {
    case 'U':
      if (row - 1 >= 0 && keyPad[row - 1][col] !== null) {
        row--;
      }
      break;
    case 'D':
      if (row + 1 < keyPad.length && keyPad[row + 1][col] !== null) {
        row++;
      }
      break;
    case 'L':
      if (col - 1 >= 0 && keyPad[row][col - 1] !== null) {
        col--;
      }
      break;
    case 'R':
      if (col + 1 < keyPad.length && keyPad[row][col + 1] !== null) {
        col++;
      }
      break;
    default:
      break
  }
  return [row, col];
}

/**
 * Pass in a keyPad and button and return the location of the button.
 * @param   {Array} keyPad  the keypad
 * @param   {string} button the button
 * @returns {Array}         the location [row, column] of the button in the keypad
 */
const findKeyButton = (keyPad, button) => {
  for(let i = 0; i < keyPad.length; i++) {
    for (let j = 0; j < keyPad.length; j++) {
      if (keyPad[i][j] === button) {
        return [i, j];
      }
    }
  }
}

/**
 * Pass in a list of code directions and a keypad and return the bathroom code. 
 * Each set of directions start from the location of the previous button. The
 * first button is 5.
 * @param   {Array} codeDirections the code directions
 * @param   {Array} keyPad         the keypad
 * @returns {string}               the bathroom code
 */
const getBathroomCode = (codeDirections, keyPad) => {
  const codeNumbers = [];
  let [posRow, posCol] = [...findKeyButton(keyPad, '5')];
  codeDirections.forEach((directions) => {
    directions.forEach((move) => {
      [posRow, posCol] = [...followInstruction(move, keyPad, posRow, posCol)];
    });

    codeNumbers.push(keyPad[posRow][posCol]);
  });
  return codeNumbers.join('');
}

const solvePartOne = (codeDirections) => {
  const keyPad = [
    ['1', '2', '3'], 
    ['4', '5', '6'], 
    ['7', '8', '9']
  ];
  
  return getBathroomCode(codeDirections, keyPad);
}

const solvePartTwo = (codeDirections) => {
  const keyPad = [
    [null, null, '1', null, null], 
    [null, '2', '3', '4', null], 
    ['5', '6', '7', '8', '9'], 
    [null, 'A', 'B', 'C', null], 
    [null, null, 'D', null, null]
  ];
  return getBathroomCode(codeDirections, keyPad);
}

const main = () => {
  const testCodeDirections = readFile(TEST_FILE_NAME);
  console.assert(solvePartOne(testCodeDirections) === '1985');
  console.assert(solvePartTwo(testCodeDirections) === '5DB3');
  
  const codeDirections = readFile(INPUT_FILE_NAME);
  console.log('Part One:', solvePartOne(codeDirections));
  console.log('Part Two:', solvePartTwo(codeDirections));
}

main();
