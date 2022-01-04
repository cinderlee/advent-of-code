// Day 12: Leonardo's Monorail

const fs = require('fs');

const INPUT_FILE_NAME = "./inputs/day12input.txt";
const TEST_FILE_NAME = "./inputs/day12testinput.txt";

/**
 * Pass in a file name and return an array of assembunny instructions
 * @param   {string} fileName the file name
 * @returns {Array}           the array of assembunny instructions
 */
const readFile = (fileName) => {
  const fileData = fs.readFileSync(fileName, 'utf-8');
  return fileData.split('\n').map(instruction => instruction.split(' '));
}

/**
 * Pass in an object of registers and array of instructions.
 * Run the assembunny instructions.
 * 
 * Instructions:
 *   - cpy x y: copies the value of x into y where y is a register and x 
 *              can be a value or a register
 *   - inc x: increments the value of register x by 1
 *   - dec x: decrements the value of register x by 1
 *   - jnz x y: jumps y steps away from current instruction if x is not 0
 * @param {Object} registers    the object of registers with their initial values
 * @param {Array}  instructions the array of assembunny instructions   
 */
const runInstructions = (registers, instructions) => {
  let i = 0;
  while (i < instructions.length) {
    const instruction = instructions[i];
    if (instruction[0] === 'cpy') {
      const val = registers.hasOwnProperty(instruction[1]) ? registers[instruction[1]] : parseInt(instruction[1]);
      registers[instruction[2]] = val;
    }
    else if (instruction[0] === 'inc') {
      registers[instruction[1]]++;
    }
    else if (instruction[0] === 'dec') {
      registers[instruction[1]]--;
    }
    else if (instruction[0] === 'jnz') {
      const val = registers.hasOwnProperty(instruction[1]) ? registers[instruction[1]] : parseInt(instruction[1]);
      if (val !== 0) {
        i += parseInt(instruction[2]);
        continue;
      }
    }
    i++;
  }
}

/**
 * Pass in an array of assembunny instructions and execute them. Return
 * the value stored in register a. All registers have an initial value of 0.
 * @param   {Array} instructions the array of assembunny instructions
 * @returns {number}             the value of register a
 */
const solvePartOne = (instructions) => {
  const registers = {
    a: 0,
    b: 0,
    c: 0,
    d: 0
  };

  runInstructions(registers, instructions);
  return registers.a;
}

/**
 * Pass in an array of assembunny instructions and execute them. Return
 * the value stored in register a. Register c has an initial value of 1, 
 * the other registers have an initial value of 0.
 * @param   {Array} instructions the array of assembunny instructions
 * @returns {number}             the value of register a
 */
const solvePartTwo = (instructions) => {
  const registers = {
    a: 0,
    b: 0,
    c: 1,
    d: 0
  };

  runInstructions(registers, instructions);
  return registers.a;
}

const main = () => {
  testAssembunnyInstructions = readFile(TEST_FILE_NAME);
  console.assert(solvePartOne(testAssembunnyInstructions) === 42);
  
  assembunnyInstructions = readFile(INPUT_FILE_NAME);
  console.log('Part One:', solvePartOne(assembunnyInstructions));
  console.log('Part Two:', solvePartTwo(assembunnyInstructions));
}

main();
