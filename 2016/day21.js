// Day 21: Scrambled Letters and Hash

const fs = require('fs');

const INPUT_FILE_NAME = "./inputs/day21input.txt";
const INPUT_PASSWORD = 'abcdefgh';
const INPUT_SCRAMBLED_PASSWORD = 'fbgdceah';
const TEST_FILE_NAME = "./inputs/day21testinput.txt";
const TEST_PASSWORD = 'abcde';

const INSTRUCTIONS = {
  SWAP_POSITION: 0,
  SWAP_LETTERS: 1,
  MOVE: 2,
  REVERSE: 3,
  ROTATE_LEFT: 4,
  ROTATE_RIGHT: 5,
  ROTATE_BY_LETTER: 6
};

/**
 * Pass in a file name and return an array of instructions parsed from the file.
 * @param   {string} fileName the file name
 * @returns {Array}           the list of instructions to scramble a password
 */
const readFile = (fileName) => {
  const instructions = fs.readFileSync(fileName, 'utf-8').split('\n');
  return instructions.map(instr => {
    const instruction = instr.split(' ');
    switch(instruction[0]) {
      case "swap": 
        return instruction[1] === 'position' ?
          [INSTRUCTIONS.SWAP_POSITION,  parseInt(instruction[2]), parseInt(instruction[instruction.length - 1])] :
          [INSTRUCTIONS.SWAP_LETTERS,  instruction[2], instruction[instruction.length - 1]];
      case "move":
        return [INSTRUCTIONS.MOVE, parseInt(instruction[2]), parseInt(instruction[instruction.length - 1])];
      case "reverse":
        return [INSTRUCTIONS.REVERSE, parseInt(instruction[2]), parseInt(instruction[instruction.length - 1])];
      case "rotate":
        const instructionVal = instruction[1] === 'left' ? INSTRUCTIONS.ROTATE_LEFT : 
            instruction[1] === 'right' ? INSTRUCTIONS.ROTATE_RIGHT : INSTRUCTIONS.ROTATE_BY_LETTER;
        const shiftOn = instructionVal === INSTRUCTIONS.ROTATE_RIGHT || instructionVal === INSTRUCTIONS.ROTATE_LEFT ? 
            parseInt(instruction[2]) : instruction[instruction.length - 1];
        return [instructionVal, shiftOn];
      default:
        return;
    }
  })
}

/**
 * Pass in an array of characters and two positions and swap the letters
 * at the two positions.
 * @param {Array}  characters  the array of characters
 * @param {number} positionOne the first position
 * @param {number} positionTwo the second position
 */
const swap = (characters, positionOne, positionTwo) => {
  const positionOneLetter = characters[positionOne];
  characters[positionOne] = characters[positionTwo];
  characters[positionTwo] = positionOneLetter;
}

/**
 * Pass in an array of characters and two positions and move the letter
 * at the source position to the destination posiiton.
 * @param {Array}  characters          the array of characters
 * @param {number} sourcePosition      the source position (index)
 * @param {number} destinationPosition the destination position (index)
 */
const move = (characters, sourcePosition, destinationPosition) => {
  const letter = characters[sourcePosition];
  characters.splice(sourcePosition, 1);
  characters.splice(destinationPosition, 0, letter);
}

/**
 * Pass in an array of characters and two positions and reverse the order of 
 * the letters within the two positions.
 * @param {Array}  characters    the array of characters
 * @param {number} startPosition the start position to reverse from
 * @param {number} endPosition   the end position to reverse from
 */
const reverse = (characters, startPosition, endPosition) => {
  let leftMarker = startPosition;
  let rightMarker = endPosition;
  while (leftMarker < rightMarker) {
    const leftLetter = characters[leftMarker];
    characters[leftMarker] = characters[rightMarker];
    characters[rightMarker] = leftLetter;

    leftMarker++;
    rightMarker--;
  }
}

/**
 * Pass in an array of characters and a shift amount and return the 
 * a new array where the characters are rotated to the left.
 * @param   {Array}  characters  the array of characters
 * @param   {number} shiftAmount the amount to shift left by
 * @returns {Array}              the rotated version of the array
 */
const rotateLeft = (characters, shiftAmount) => {
  const firstPart = characters.slice(0, shiftAmount);
  const secondPart = characters.slice(shiftAmount);
  return secondPart.concat(firstPart);
}

/**
 * Pass in an array of characters and a shift amount and return the 
 * a new array where the characters are rotated to the right.
 * @param   {Array}  characters  the array of characters
 * @param   {number} shiftAmount the amount to shift right by
 * @returns {Array}              the rotated version of the array
 */
const rotateRight = (characters, shiftAmount) => {
  const firstPart = characters.slice(characters.length - shiftAmount);
  const secondPart = characters.slice(0, characters.length - shiftAmount);
  return firstPart.concat(secondPart);
}

/**
 * Pass in a password and the instructions to scramble a password and return
 * the scrambled version. 
 * 
 * Instructions;
 * - SWAP_POSITION: swaps the letters at two specified positions
 * - SWAP_LETTERS: swap the letters
 * - MOVE: moves a letter from a specified position to another position
 * - REVERSE: the letters between two specified positions are reversed in order
 * - ROTATE_LEFT/ROTATE_RIGHT: the whole array of characters is rotated by a 
 *                             specified amount
 * - ROTATE_BY_LETTER: the array is rotated to the array depending on the index of
 *                     a specified letter. If the index is at least 4, the array
 *                     is rotated by the index + 2. Otherwise, the array is rotated 
 *                     by index + 1.
 * @param   {string} password     the password
 * @param   {Array}  instructions the scrambling instructions
 * @returns {string}              the scrambled version of the passowrd
 */
const scramblePassword = (password, instructions) => {
  let characters = password.split("");
  
  instructions.forEach(instruction => {
    switch(instruction[0]) {
      case INSTRUCTIONS.SWAP_POSITION:
        swap(characters, instruction[1], instruction[2]);
        return;
      case INSTRUCTIONS.SWAP_LETTERS:
        const posOne = characters.indexOf(instruction[1]);
        const posTwo = characters.indexOf(instruction[2]);
        swap(characters, posOne, posTwo);
        return;
      case INSTRUCTIONS.MOVE:
        move(characters, instruction[1], instruction[2]);
        return
      case INSTRUCTIONS.REVERSE:
        reverse(characters, instruction[1], instruction[2]);
        return;
      case INSTRUCTIONS.ROTATE_LEFT:
        characters = rotateLeft(characters, instruction[1] % characters.length);
        return;
      case INSTRUCTIONS.ROTATE_RIGHT:
        characters = rotateRight(characters, instruction[1] % characters.length);
        return;
      case INSTRUCTIONS.ROTATE_BY_LETTER:
        let shiftAmount = characters.indexOf(instruction[1]);
        shiftAmount += shiftAmount >= 4 ? 2 : 1;
        characters = rotateRight(characters, shiftAmount % characters.length);
        return;
      default:
        return;
    }
  });

  return characters.join('')
}

/**
 * Pass in a scrambled password and the instructions to scramble a password 
 * and return the unscrambled version. 
 * 
 * Instructions;
 * - SWAP_POSITION: swaps the letters at two specified positions
 * - SWAP_LETTERS: swap the letters
 * - MOVE: moves a letter from a specified position to another position
 * - REVERSE: the letters between two specified positions are reversed in order
 * - ROTATE_LEFT/ROTATE_RIGHT: the whole array of characters is rotated by a 
 *                             specified amount
 * - ROTATE_BY_LETTER: the array is rotated to the array depending on the index of
 *                     a specified letter. If the index is at least 4, the array
 *                     is rotated by the index + 2. Otherwise, the array is rotated 
 *                     by index + 1.
 * @param   {string} scrambledPassword the scrambled password
 * @param   {Array}  instructions      the scrambling instructions
 * @returns {string}                   the unscrambled password
 */
const unscramblePassword = (scrambledPassword, instructions) => {
  let characters = scrambledPassword.split("");
  
  instructions.reverse().forEach(instruction => {
    switch(instruction[0]) {
      case INSTRUCTIONS.SWAP_POSITION:
        swap(characters, instruction[1], instruction[2]);
        return;
      case INSTRUCTIONS.SWAP_LETTERS:
        const posOne = characters.indexOf(instruction[1]);
        const posTwo = characters.indexOf(instruction[2]);
        swap(characters, posOne, posTwo);
        return;
      case INSTRUCTIONS.MOVE:
        move(characters, instruction[2], instruction[1]);
        return
      case INSTRUCTIONS.REVERSE:
        reverse(characters, instruction[1], instruction[2]);
        return;
      case INSTRUCTIONS.ROTATE_LEFT:
        characters = rotateRight(characters, instruction[1] % characters.length);
        return;
      case INSTRUCTIONS.ROTATE_RIGHT:
        characters = rotateLeft(characters, instruction[1] % characters.length);
        return;
      case INSTRUCTIONS.ROTATE_BY_LETTER:
        const letterIndex = characters.indexOf(instruction[1]);
        let shiftAmount = 0;
        for (let originalIndex = 0; originalIndex < characters.length; originalIndex++) {
          shiftAmount = originalIndex >= 4 ? originalIndex + 2 : originalIndex + 1;
          if ((originalIndex + shiftAmount) % characters.length === letterIndex) {
            break;
          }
        }
        characters = rotateLeft(characters, shiftAmount % characters.length);
        return;
      default:
        return;
    }
  });

  return characters.join('')
}

const solvePartOne = (password, instructions) => {
  return scramblePassword(password, instructions);
}

const solvePartTwo = (scrambledPassword, instructions) => {
  return unscramblePassword(scrambledPassword, instructions);
}

const main = () => {
  const testInstructions = readFile(TEST_FILE_NAME);
  console.assert(solvePartOne(TEST_PASSWORD, testInstructions) === 'decab');

  const instructions = readFile(INPUT_FILE_NAME);
  console.log("Part One:", solvePartOne(INPUT_PASSWORD, instructions));
  console.log("Part Two:", solvePartTwo(INPUT_SCRAMBLED_PASSWORD, instructions));
}

main()
