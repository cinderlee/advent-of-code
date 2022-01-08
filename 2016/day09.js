// Day 9: Explosives in Cyberspace

const fs = require('fs');

const INPUT_FILE_NAME = './inputs/day09input.txt';
const TEST_INPUT_1 = "ADVENT";
const TEST_INPUT_2 = "A(1x5)BC";
const TEST_INPUT_3 = "(3x3)XYZ";
const TEST_INPUT_4 = "A(2x2)BCD(2x2)EFG";
const TEST_INPUT_5 = "(6x1)(1x3)A";
const TEST_INPUT_6 = "X(8x2)(3x3)ABCY";
const TEST_INPUT_7 = "(27x12)(20x12)(13x14)(7x10)(1x12)A";
const TEST_INPUT_8 = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN";

/**
 * Pass in a file name and return a string representing contents of a 
 * file that is compressed using an experimental format
 * @param   {string} fileName the file name
 * @returns {string}          the compressed file content
 */
const readFile = (fileName) => {
  return fs.readFileSync(fileName, 'utf-8');
}

/**
 * Pass in a compressed sequence and return the length of the decompressed data.
 * Each marker is in the form of (AxB) where A represents the number of subsequent 
 * characters and B represents the number of times to repreat those characters.
 * 
 * In version one, if a marker is included in the subsequent characters during
 * decompression, the marker is NOT decompressed. In version two, the marker
 * included IS decompressed as well. 
 * @param   {string}  compressedSequence the sequence to decompress
 * @param   {boolean} isVersionTwo       whether to use version one or version two
 * @returns {number}                     the length of the decompressed data
 */
const getDecompressedLength = (compressedSequence, isVersionTwo=false) => {
  let i = 0;
  let decompressedLength = 0;
  while (i < compressedSequence.length) {
    if (compressedSequence[i] === '(') {
      const markerEnd = compressedSequence.indexOf(')', i);
      const marker = compressedSequence.substring(i + 1, markerEnd).split('x')
      const numCharacters = parseInt(marker[0]);
      const multiplier = parseInt(marker[1]);
      i = markerEnd + 1;

      if (isVersionTwo) {
        const subSequence = compressedSequence.substr(i, numCharacters);
        decompressedLength += multiplier * getDecompressedLength(subSequence, isVersionTwo);
      }
      else {
        decompressedLength += numCharacters * multiplier;
      }
      i += numCharacters;
    }
    else {
      decompressedLength++;
      i++;
    }
  }
  return decompressedLength;
}

/**
 * Pass in a string of compressed data and return the length of the decompressed data
 * that was compressed using version one.
 * @param   {string} compressedData the compressed data
 * @returns {number}                the length of the decompressed data
 */
const solvePartOne = (compressedData) => {
  return getDecompressedLength(compressedData);
}

/**
 * Pass in a string of compressed data and return the length of the decompressed data
 * that was compressed using version two.
 * @param   {string} compressedData the compressed data
 * @returns {number}                the length of the decompressed data
 */
const solvePartTwo = (compressedData) => {
  return getDecompressedLength(compressedData, isVersionTwo = true);
}

const main = () => {
  console.assert(solvePartOne(TEST_INPUT_1) == 6);
  console.assert(solvePartOne(TEST_INPUT_2) == 7);
  console.assert(solvePartOne(TEST_INPUT_3) == 9);
  console.assert(solvePartOne(TEST_INPUT_4) == 11);
  console.assert(solvePartOne(TEST_INPUT_5) == 6);
  console.assert(solvePartOne(TEST_INPUT_6) == 18);

  console.assert(solvePartTwo(TEST_INPUT_3) == 9);
  console.assert(solvePartTwo(TEST_INPUT_6) == 20);
  console.assert(solvePartTwo(TEST_INPUT_7) == 241920);
  console.assert(solvePartTwo(TEST_INPUT_8) == 445);

  const compressedData = readFile(INPUT_FILE_NAME);
  console.log('Part One:', solvePartOne(compressedData));
  console.log('Part Two:', solvePartTwo(compressedData));
}

main();