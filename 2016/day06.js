// Day 6: Signals and Noise

const fs = require('fs');

const INPUT_FILE_NAME = './inputs/day06input.txt';
const TEST_FILE_NAME = './inputs/day06testinput.txt';

/**
 * Pass in a file name and return an object of character counts for
 * each position of all messages that were sent.
 * @param   {string} fileName the file name
 * @returns {Object}          object of character counts for each index
 */
const readFileAndParseMessages = (fileName) => {
  const fileData = fs.readFileSync(fileName, 'utf-8');
  const messages = fileData.split('\n');
  return getCharacterCounts(messages)
}

/**
 * Pass in an array of messages and return an object of character 
 * counts for each position.
 * For example:
 *     messages = ['hi', 'bye']
 *     the object for index 0 would be {'h': 1, 'b': 1}
 * @param   {Array} messages array of messages
 * @returns {Object}         object mapping index to an object of 
 *                           letter counts
 */
const getCharacterCounts = (messages) => {
  const letterCounts = Array.from(Array(messages[0].length).keys()).map(() => ({}));
  messages.forEach(message => {
    for (let i = 0; i < message.length; i++) {
      if (letterCounts[i].hasOwnProperty(message[i])) {
        letterCounts[i][message[i]]++;
      } else {
        letterCounts[i][message[i]] = 1;
      }
    }
  });

  return letterCounts;
}

/**
 * Pass in an object of character counts and return the error-corrected
 * version of the message, which is formed from combining the most frequent
 * characters for each position.
 * @param   {Object} characterCounts object of character counts for each position
 * @returns {string}                 the error-corrected version of the message
 */
const solvePartOne = (characterCounts) => {
  const finalMessage = characterCounts.map(characterCountsObj => (
    Object.keys(characterCountsObj).reduce(
      (characterOne, characterTwo) => characterCountsObj[characterOne] > characterCountsObj[characterTwo] ? characterOne : characterTwo)
  ));

  return finalMessage.join('');
}

/**
 * Pass in an object of character counts and return the error-corrected
 * version of the message, which is formed from combining the least frequent
 * characters for each position.
 * @param   {Object} characterCounts object of character counts for each position
 * @returns {string}                 the error-corrected version of the message
 */
const solvePartTwo = (characterCounts) => {
  const finalMessage = characterCounts.map(characterCountsObj => (
    Object.keys(characterCountsObj).reduce(
      (characterOne, characterTwo) => characterCountsObj[characterOne] < characterCountsObj[characterTwo] ? characterOne : characterTwo)
  ));

  return finalMessage.join('');
}

const main = () => {
  const testCharacterCounts = readFileAndParseMessages(TEST_FILE_NAME);
  console.assert(solvePartOne(testCharacterCounts) === 'easter');

  const characterCounts = readFileAndParseMessages(INPUT_FILE_NAME);
  console.log('Part One:', solvePartOne(characterCounts));
  console.log('Part Two:', solvePartTwo(characterCounts));
};

main();
