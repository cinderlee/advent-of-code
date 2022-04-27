// Day 23: Safe Cracking

const fs = require('fs');

const INPUT_FILE_NAME = "./inputs/day23input.txt";
const INPUT_SIMPLIFIED_FILE_NAME = "./inputs/day23inputsimplified.txt";
const TEST_FILE_NAME = "./inputs/day23testinput.txt";

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
 * Pass in an instruction and list of arguments and return the toggled 
 * version of the instruction.
 * @param   {string} instruction the instruction
 * @param   {Array}  args        the arguments
 * @returns {Array}              the toggled instruction with arguments
 */
const getToggledInstruction = (instruction, ...args) => {
  let toggledInstruction;
  if (instruction === 'inc') {
    toggledInstruction = 'dec';
  }
  else if (instruction === 'jnz') {
    toggledInstruction = 'cpy';
  }
  else {
    toggledInstruction = args.length === 1 ? 'inc' : 'jnz';
  }
  return [toggledInstruction, ...args];
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
 *   - tgl x: toggles the instruction x steps away where 
 *            one op instructions: inc becomes dec, else instruction becomes inc
 *            two op instructions: jnz becomes cpy, else instruction becomes jnz
 *   - add x y: adds the value of x to y
 *   - mult x y: multiplies the value of x to y
 * @param {Object} registers    the object of registers with their initial values
 * @param {Array}  instructions the array of assembunny instructions   
 */

const runInstructions = (registers, instructions) => {
  let i = 0;
  while (i < instructions.length) {
    const instruction = instructions[i];

    if (instruction[0] === 'cpy') {
      const val = registers.hasOwnProperty(instruction[1]) ? registers[instruction[1]] : parseInt(instruction[1]);
      if (registers.hasOwnProperty(instruction[2])) {
        registers[instruction[2]] = val;
      }
    }
    else if (instruction[0] === 'inc') {
      if (registers.hasOwnProperty(instruction[1])) {
        registers[instruction[1]]++;
      }
    }
    else if (instruction[0] === 'dec') {
      if (registers.hasOwnProperty(instruction[1])) {
        registers[instruction[1]]--;
      }
    }
    else if (instruction[0] === 'jnz') {
      const val = registers.hasOwnProperty(instruction[1]) ? registers[instruction[1]] : parseInt(instruction[1]);
      if (val !== 0) {
        const addend = registers.hasOwnProperty(instruction[2]) ? registers[instruction[2]] : parseInt(instruction[2]);
        i += addend;
        continue;
      }
    }
    else if (instruction[0] === 'mult') {
      const val = registers.hasOwnProperty(instruction[1]) ? registers[instruction[1]] : parseInt(instruction[1]);
      if (registers.hasOwnProperty(instruction[2])) {
        registers[instruction[2]] *= val;
      }
    }
    else if (instruction[0] === 'add') {
      const val = registers.hasOwnProperty(instruction[1]) ? registers[instruction[1]] : parseInt(instruction[1]);
      if (registers.hasOwnProperty(instruction[2])) {
        registers[instruction[2]] += val;
      }
    }
    else {
      const val = registers.hasOwnProperty(instruction[1]) ? registers[instruction[1]] : parseInt(instruction[1]);
      const toggleInstructionIndex = i + val;
      if (toggleInstructionIndex >= 0 && toggleInstructionIndex < instructions.length) {
        instructions[toggleInstructionIndex] = getToggledInstruction(...instructions[toggleInstructionIndex]);
      }
    }

    i++;
  }
}

const solvePartOne = (instructions) => {
  const registers = {
    a: 7,
    b: 0,
    c: 0,
    d: 0
  };
  runInstructions(registers, instructions);
  return registers.a;
}

const solvePartTwo = (instructions) => {
  const registers = {
    a: 12,
    b: 0,
    c: 0,
    d: 0
  };
  runInstructions(registers, instructions);
  return registers.a;
}

const main = () => {
  const testAssembunnyInstructions = readFile(TEST_FILE_NAME);
  console.assert(solvePartOne(testAssembunnyInstructions) === 3);
  
  const assembunnyInstructions = readFile(INPUT_FILE_NAME);
  console.log('Part One:', solvePartOne(assembunnyInstructions));

  // With the new input for part two, the prototype computer running the instructions 
  // begin to overheat. The instructions are simplified to use multiplication
  // and addition, reducing the number of instructions. 
  const assembunnySimplifiedInstructions = readFile(INPUT_SIMPLIFIED_FILE_NAME);
  console.log('Part Two:', solvePartTwo(assembunnySimplifiedInstructions));
}

main();