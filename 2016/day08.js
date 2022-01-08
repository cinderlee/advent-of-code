// Day 8: Two-Factor Authentication

const fs = require('fs');

const INPUT_FILE_NAME = './inputs/day08input.txt';

const RECT = 0;
const ROTATE_ROW = 1;
const ROTATE_COL = 2;

const SCREEN_WIDTH = 50;
const SCREEN_LENGTH = 6;

const ON = '#';
const OFF = '.'

/**
 * Pass in an array of instruction parts and returns an array containing information
 * about an instruction.
 * 
 * The first value of the instruction will represent the instruction type.
 * For RECT instructions, the next two values represent the dimensions of the rectangle.
 * For ROTATE_ROW instruction, the next two values represent the row number and shift value.
 * For ROTATE_COL instruction, the next two values represent the column number and shift value.
 * @param   {Array} instructionParts the list of instruction parts
 * @returns {Array}                  the array representing the parsed instruction
 */
const parseInstruction = (instructionParts) => {
  if (instructionParts[0] === 'rect') {
    const dimensions = instructionParts[1].split('x').map(dim => parseInt(dim));
    return [RECT, ...dimensions];
  }

  const num = parseInt(instructionParts[2].split('=')[1]);
  const shift = parseInt(instructionParts[instructionParts.length - 1]);
  const instructionType = instructionParts[1] === 'row' ? ROTATE_ROW : ROTATE_COL;
  return [instructionType, num, shift]
}

/**
 * Pass in a file name and return a list of instructions read from the file.
 * @param   {string} fileName the file name
 * @returns {Array}           the list of instructions
 */
const readFile = (fileName) => {
  const instructions = fs.readFileSync(fileName, 'utf-8').split('\n');
  const instructionsList = [];
  instructions.forEach(instr => {
    const instructionParts = instr.split(' ');
    instructionsList.push(parseInstruction(instructionParts));
  });
  return instructionsList;
}

/**
 * Pass in an array and a shift value and rotates the values in the array
 * by the shift amount
 * @param {Array} list   the list
 * @param {number} shift the shift amount
 */
const rotateList = (list, shift) => {
  const loopOver = list.slice(list.length - shift)
  for (let i = list.length - shift - 1; i >= 0; i--) {
    list[i + shift] = list[i];
  }

  for (let i = 0; i < loopOver.length; i++) {
    list[i] = loopOver[i];
  }
}

/**
 * Pass in the grid, row number, and shift value and rotate the grid row.
 * @param {Array}  grid   the grid
 * @param {number} rowNum the row number
 * @param {number} shift  the shift value
 */
const rotateRow = (grid, rowNum, shift) => {
  rotateList(grid[rowNum], shift);
}

/**
 * Pass in the grid, row number, and shift value and rotate the grid column.
 * @param {Array}  grid   the grid
 * @param {number} colNum the column number
 * @param {number} shift  the shift value
 */
const rotateColumn = (grid, colNum, shift) => {
  const columnValues = Array.from(Array(SCREEN_LENGTH).keys()).map(rowNum => grid[rowNum][colNum]);
  rotateList(columnValues, shift);
  for (let i = 0; i < SCREEN_LENGTH; i++) {
    grid[i][colNum] = columnValues[i];
  }
}

/**
 * Pass in a set of instructions and the grid of pixels and run the instructions.
 * 
 * The RECT AxB instruction turns on all the pixels in the rectangle that is 
 * A pixels wide and B pixels tall, starting from the top left corner of the grid.
 * 
 * The ROTATE_ROW instruction circularly rotates the pixels in a row.
 * 
 * The ROTATE_COL instruction circularly rotates the pixels in the column. 
 * @param {Array} instructions the set of instructions
 * @param {Array} grid         the grid of lights.
 */
const runInstructions = (instructions, grid) => {
  instructions.forEach(instr => {
    switch(instr[0]) {
      case RECT:
        const numRows = instr[2];
        const numCols = instr[1];
        for (let i = 0; i < numRows; i++) {
          for (let j = 0; j < numCols; j++) {
            grid[i][j] = ON;
          }
        }
        break;
      case ROTATE_ROW:
        rotateRow(grid, instr[1], instr[2]);
        break;
      case ROTATE_COL:
        rotateColumn(grid, instr[1], instr[2]);
        break;
      default:
        break;
    }
  });
}

/**
 * Pass in a set of instructions and a starting grid of pixels and return
 * the number of pixels on after running the instructions.
 * @param   {Array} instructions the set of instructions
 * @param   {Array} grid         the initial grid of pixels
 * @returns {number}             the number of pixels on
 */
const solvePartOne = (instructions, grid) => {
  runInstructions(instructions, grid);
  let pixelsCount = 0;
  grid.forEach(row => {
    row.forEach(pixel => {
      if (pixel === '#') {
        pixelsCount++;
      }
    })
  });
  return pixelsCount;
}

/**
 * Pass in the grid after running the set of instructions and log out
 * the pixels to retrieve the code displayed on the screen.
 * @param {Array} grid the grid after runnning instructions from part one
 */
const solvePartTwo = (grid) => {
  grid.forEach(row => {
    console.log(row.join(''));
  })
}

const main = () => {
  const instructions = readFile(INPUT_FILE_NAME);
  const grid = Array(SCREEN_LENGTH).fill([]).map(() => Array(SCREEN_WIDTH).fill(OFF));
  console.log("Part One:", solvePartOne(instructions, grid));
  console.log("Part Two:")
  solvePartTwo(grid);
}

main()