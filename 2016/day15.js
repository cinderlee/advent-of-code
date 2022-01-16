// Day 15: Timing is Everything

const fs = require('fs');

const INPUT_FILE_NAME = './inputs/day15input.txt';
const TEST_FILE_NAME = './inputs/day15testinput.txt';

/**
 * Pass in a file name and return a map of disc numbers to an array
 * containing the number of positions it has and its starting position.
 * @param   {string} fileName the file name
 * @returns {Object}          the map of discs to their number of positions and starting position
 */
const readFile = (fileName) => {
  const discInfo = {};
  const lines = fs.readFileSync(fileName, 'utf-8').split('\n');
  lines.forEach(discLine => {
    const discData = discLine.split(' ');
    const discNum = parseInt(discData[1].substring(1));
    const numPositions = parseInt(discData[3]);
    const startPos = parseInt(discData[discData.length - 1].substring(0, discData[discData.length - 1].length - 1))
    discInfo[discNum] = [numPositions, startPos]
  });
  return discInfo;
}

/**
 * Pass in the map of disc information and return the first time you can press the button
 * so that you can obtain a capsule from kinetic sculpture.
 * 
 * The capsule falls each second and the slots for the capsule to fall through is at 
 * position 0. Each spinning disc moves forward a position each second and moves back
 * to 0 after its last position. 
 * @param   {Object} discInfo the disc information
 * @returns {number}          the first time you can press the button
 */
const getCapsule = (discInfo) => {
  let t = 0;
  while (true) {
    let canGetCapsule = true;
    for (const disc in discInfo) {
      const [numPositions, startPos] = discInfo[disc];
      let loc = (((startPos + t) % numPositions) + parseInt(disc)) % numPositions;
      if (loc !== 0) {
        canGetCapsule = false;
        break;
      }
    }
    if (canGetCapsule) {
      return t;
    }
    t++;
  }
}

/**
 * Pass in the disc information and return the first time that you 
 * can press the button to obtain a capsule.
 * @param   {Object} discInfo the disc information
 * @returns {number}          the first time you can press the button
 */
const solvePartOne = (discInfo) => {
  return getCapsule(discInfo);
}

/**
 * Pass in the disc information and return the first time that you 
 * can press the button to obtain a capsule.
 * 
 * This time, there is a new disc one second below the the lowest disc
 * with 11 positions and starts at position 0. 
 * @param   {Object} discInfo the disc information
 * @returns {number}          the first time you can press the button
 */
const solvePartTwo = (discInfo) => {
  discInfo[Object.keys(discInfo).length + 1] = [11, 0];
  return getCapsule(discInfo);
}

const main = () => {
  const testDiscInfo = readFile(TEST_FILE_NAME);
  console.assert(solvePartOne(testDiscInfo) === 5);

  const discInfo = readFile(INPUT_FILE_NAME);
  console.log("Part One:", solvePartOne(discInfo));
  console.log("Part Two:", solvePartTwo(discInfo));
}

main();
