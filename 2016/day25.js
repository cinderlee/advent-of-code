// Day 25: Clock Signal

const fs = require('fs');

const INPUT_FILE_NAME = "./inputs/day25input.txt";

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
 * Pass in an object of registers and array of instructions. Run the assembunny 
 * instructions except for the last instruction, which would cause an infinite 
 * loop, and return whether an output of alternating 0s and 1s occur.
 * 
 * Instructions:
 *   - cpy x y: copies the value of x into y where y is a register and x 
 *              can be a value or a register
 *   - inc x: increments the value of register x by 1
 *   - dec x: decrements the value of register x by 1
 *   - jnz x y: jumps y steps away from current instruction if x is not 0
 *   - out x: outputs the value of x as the next clock signal
 * @param   {Object} registers    the object of registers with their initial values
 * @param   {Array}  instructions the array of assembunny instructions   
 * @returns {boolean}             whether the clock signal output is alternating 0s and 1s
 */
const runInstructions = (registers, instructions) => {
  const output = []
  let i = 0;
  while (i < instructions.length - 1) {
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
    else if (instruction[0] === 'out') {
      const val = registers.hasOwnProperty(instruction[1]) ? registers[instruction[1]] : parseInt(instruction[1]);
      if (val === output[output.length - 1]) {
        return false;
      }
      output.push(val);
    }
    i++;
  }
  return true;
}

/**
 * Pass in an array of assembunny instructions and return the lowest starting 
 * a value that will output a clock signal of repeating 0s and 1s forever.
 * @param   {Array} instructions the array of assembunny instructions
 * @returns {number}             the lowest initial value of register a
 */
const solvePartOne = (instructions) => {
  const registers = {
    a: 0,
    b: 0,
    c: 0,
    d: 0
  };
  let i = 0;

  while (true) {
    registers.a = i;
    const canCauseAlternatingSignal = runInstructions(registers, instructions);
    if (canCauseAlternatingSignal) {
      return i;
    }
    i++;
  }
}

const main = () => {
  assembunnyInstructions = readFile(INPUT_FILE_NAME);
  console.log('Part One:', solvePartOne(assembunnyInstructions));
}

main();
