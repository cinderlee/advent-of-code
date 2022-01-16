// Day 10: Balance Bots

const fs = require('fs');

const INPUT_FILE_NAME = "./inputs/day10input.txt";

/**
 * Pass in a file name and parse the bot instructions into two arrays: one
 * for initializing the bots, the other for giving microchips to other bots.
 * @param   {string} fileName the file name
 * @returns {Array}           an array of two arrays of initializing and giving instructions
 */
const readFile = (fileName) => {
  const instructions = fs.readFileSync(fileName, 'utf-8').split('\n');
  const initializeInstructions = [];
  const giveInstructions = [];
  instructions.forEach(instruction => {
    const instructionParts = instruction.split(' ');
    if (instructionParts.indexOf('value') !== -1) {
      initializeInstructions.push(
        [instructionParts[1], `${instructionParts[4]} ${instructionParts[5]}`]
      );
    } else {
      const botName = `${instructionParts[0]} ${instructionParts[1]}`;
      const lowBotName = `${instructionParts[5]} ${instructionParts[6]}`;
      const highBotName = `${instructionParts[10]} ${instructionParts[11]}`;
      giveInstructions.push([botName, lowBotName, highBotName]);
    }
  });

  return [initializeInstructions, giveInstructions];
}

/**
 * Pass in a bot name, the microchip vlaue to give to the bot, and the map that stores the 
 * microchips for each bot and append the value.
 * @param {string} botName         the bot name
 * @param {number} val             the microchip value to give to the bot
 * @param {Object} botMicrochipMap the map of microchips to bots
 */
const addMicrochip = (botName, val, botMicrochipMap) => {
  if (botMicrochipMap.hasOwnProperty(botName)) {
    botMicrochipMap[botName].push(val);
  } else {
    botMicrochipMap[botName] = [val];
  }
}

/**
 * Pass in an array of instructions and return an object representing the bots
 * mapped to their initial array of microchip values.
 * @param   {Array} instructions the array of instructions that initialize the bots
 * @returns {Object}             the map of microchips to bots
 */
const initializeBots = (instructions) => {
  const botMicrochipMap = {};
  instructions.forEach(instruction => {
    const [val, botName] = instruction;
    addMicrochip(botName, parseInt(val), botMicrochipMap);
  });
  return botMicrochipMap;
}

/**
 * Pass in bot instructions, the initial map of microchips to bots, and the stop requirement
 * and run the bot instructions. If the stop requirement is not null, the process stops when
 * a bot is comparing values that are in the stop requirement array. A bot can only hand off 
 * its microchips to other bots when it has 2 microchips.
 * 
 * Return the index of the last instruction that was not performed. If all instructions 
 * were performed, return the length of the instructions array.
 * @param   {Array}  instructions the array of bot instructions
 * @param   {Object} botMicrochipMap the map of microchips to bots
 * @param   {Array}  stopRequirement the stop requirement
 * @returns {number}                 the index of the last instruction that was not performed
 */
const runInstructions = (instructions, botMicrochipMap, stopRequirement=null) => {
  const completedInstructions = new Set();
  while (completedInstructions.size !== instructions.length) {

    for (let i = 0; i < instructions.length; i++) {
      const [botName, lowBotName, highBotName] = instructions[i];

      if (completedInstructions.has(i) || 
          !botMicrochipMap.hasOwnProperty(botName) || 
          botMicrochipMap[botName].length !== 2
      ) {
        continue;
      }

      const lowMicrochip = Math.min(...botMicrochipMap[botName]);
      const highMicrochip = Math.max(...botMicrochipMap[botName]);

      if (stopRequirement) {
        if (stopRequirement.includes(lowMicrochip) && stopRequirement.includes(highMicrochip)) {
          return i;
        }
      }

      addMicrochip(lowBotName, lowMicrochip, botMicrochipMap);
      addMicrochip(highBotName, highMicrochip, botMicrochipMap);
      botMicrochipMap[botName] = [];
      completedInstructions.add(i);
    };
  }

  return instructions.length;
}

/**
 * Pass in the instructions to initialize the bots and to give microchips to bots. 
 * Return the bot that is comparing value-61 and value-17 microchips;
 * @param   {Array} initializeInstructions the instructions to initialize the bots
 * @param   {Array} giveInstructions       the instructions to hand off microchips to other bots
 * @returns {string}                       the bot name that compares value 61 and value 17 microchips
 */
const solvePartOne = (initializeInstructions, giveInstructions) => {
  const botMicrochipMap = initializeBots(initializeInstructions);
  const instructionIndex = runInstructions(giveInstructions, botMicrochipMap, [61, 17]);
  return giveInstructions[instructionIndex][0];
}

/**
 * Pass in the instructions to initialize the bots and to give microchips to bots. 
 * Return the product of the microchip values stored in outputs 0-2 after running the bot
 * instructions.
 * @param   {Array} initializeInstructions the instructions to initialize the bots
 * @param   {Array} giveInstructions       the instructions to hand off microchips to other bots
 * @returns {number}                       the product of the microchip values in outputs 0-2
 */
const solvePartTwo = (initializeInstructions, giveInstructions) => {
  const botMicrochipMap = initializeBots(initializeInstructions);
  runInstructions(giveInstructions, botMicrochipMap);
  const outputOne = botMicrochipMap['output 0'][0];
  const outputTwo = botMicrochipMap['output 1'][0];
  const outputThree = botMicrochipMap['output 2'][0];
  return outputOne * outputTwo * outputThree;
}

const main = () => {
  const [initializeInstructions, giveInstructions] = readFile(INPUT_FILE_NAME);
  console.log("Part One:", solvePartOne(initializeInstructions, giveInstructions));
  console.log("Part Two:", solvePartTwo(initializeInstructions, giveInstructions));
}

main();
