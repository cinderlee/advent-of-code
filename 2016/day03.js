// Day 3: Squares With Three Sides

const fs = require('fs');

const INPUT_FILE_NAME = './inputs/day03input.txt';

/**
 * Pass in a file name and return an array of side lengths, each represented as an
 * array of 3 numbers.
 * @param  {string} fileName the file name
 * @return {Array}           array of arrays of side lengths   
 */
const readFile = (fileName) => {
  const fileData = fs.readFileSync(fileName, 'utf-8');
  trianglesData = fileData.split('\n');
  return trianglesData.map(data => {
    const lst = data.trim().split(' ');
    const sideLengths = lst.filter(elem => elem !== '').map(num => parseInt(num));
    return sideLengths;
  });
}

/**
 * Pass in three sides and returns whether the sides make up a triangle.
 * @param  {number} sideOne   the first side
 * @param  {number} sideTwo   the second side
 * @param  {number} sideThree the third side
 * @return {boolean}          whether the three sides form a triangle    
 */
const isTriangle = (sideOne, sideTwo, sideThree) => {
  const longestSide = Math.max(sideOne, sideTwo, sideThree);
  let sumOfTwoShortest = 0;
  if (longestSide === sideOne) {
    sumOfTwoShortest = sideTwo + sideThree;
  }
  else if (longestSide === sideTwo) {
    sumOfTwoShortest = sideOne + sideThree;
  }
  else {
    sumOfTwoShortest = sideOne + sideTwo;
  }

  return sumOfTwoShortest > longestSide;
}

/**
 * Pass in an array of arrays of side lengths and returns the number of
 * valid triangles.
 * @param  {Array} trianglesData the array of arrays of side lengths
 * @return {number}              the number of valid triangles
 */
const solvePartOne = (trianglesData) => {
  let triangleCount = 0;
  trianglesData.forEach(sideLengths => {
    if (isTriangle(...sideLengths)) {
      triangleCount++;
    }
  });
  return triangleCount;
}

/**
 * Pass in an array of arrays of side lengths and returns the number of
 * valid triangles. The triangles are specified in groups of three sides
 * vertically instead of horizontally.
 * @param  {Array} trianglesData the array of arrays of side lengths
 * @return {number}              the number of valid triangles
 */
const solvePartTwo = (trianglesData) => {
  let triangleCount = 0;

  for (let i = 0; i < 3; i++) {
    for (let row = 0; row < trianglesData.length; row += 3) {
      if (isTriangle(trianglesData[row][i], trianglesData[row + 1][i], trianglesData[row + 2][i])) {
        triangleCount++;
      }
    }
  }
  return triangleCount;
}

const main = () => {
  trianglesData = readFile(INPUT_FILE_NAME);
  console.log('Part One:', solvePartOne(trianglesData));
  console.log('Part Two:',solvePartTwo(trianglesData));
}

main();
