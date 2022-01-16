// Day 13: A Maze of Twisty Little Cubicles

const START_LOCATION = [1, 1];

const INPUT_FAVORITE_NUMBER = 1350;
const INPUT_DESTINATION = [39, 31];

const TEST_FAVORITE_NUMBER = 10;
const TEST_DESTINATION = [4, 7];

const DISP = [[1,0], [0, 1], [-1, 0], [0, -1]];

// stop requirements type
const DESTINATION_TYPE = 0;
const STEP_TYPE = 1;

/**
 * Pass in a location (row, column) in the cube maze and a favorite number and 
 * return when the space is an open space. 
 * 
 * Steps to determine if a location is an open space:
 *  - Calculate x * x + 3 * x + 2 * x * y + y + y * y, where row = y and col = x
 *  - Add the favorite number 
 *  - Count the number of one bits in the binary representation of the sum. If 
 *    there is an even number of one bits, the location is an open space, otherwise
 *    it is a wall.
 * @param   {number} row          the row number 
 * @param   {number} col          the column number
 * @param   {number} favoriteNum  the favorite number
 * @returns {boolean}             whether the location is an open space
 */
const isOpenSpace = (row, col, favoriteNum) => {
  let sum = col * col + 3 * col + 2 * col * row + row + row * row + favoriteNum;
  const binary = sum.toString(2);

  let countOnes = 0;
  for (let i = 0; i < binary.length; i++) {
    countOnes += binary[i] === '1' ? 1 : 0;
  }

  return countOnes % 2 === 0;
}

/**
 * Pass in the current location (row, column), the favorite number, and an 
 * array of known walls and return an array of next open space locations you
 * can move to. If any new walls are found, add their locations to the array.
 * @param   {number} row         the current row
 * @param   {number} col         the current column
 * @param   {number} favoriteNum the favorite number
 * @param   {Array}  walls       the array of known walls
 * @returns {Array}              the array of next open space locations
 */
const getNextOpenSpaceLocations = (row, col, favoriteNum, walls) => {
  const nextLocations = [];

  DISP.forEach((disp) => {
    const [dispRow, dispCol] = [...disp];
    const nextRow = row + dispRow;
    const nextCol = col + dispCol;

    if (walls.has(`${nextRow},${nextCol}`) || nextRow < 0 || nextCol < 0) {
      return;
    }

    if (isOpenSpace(nextRow, nextCol, favoriteNum)) {
      nextLocations.push([nextRow, nextCol]);
    }
    else {
      walls.add(`${nextRow},${nextCol}`);
    }
  });

  return nextLocations;
}

/**
 * Pass in the favorite number and location of destination and return the
 * minimum number of steps needed to reach the destination.
 * @param   {number} favoriteNum the favorite number
 * @param   {Array}  destination the destination
 * @returns {number}             the minimum number of steps to the destination
 */
const getMinimumStepsToDestination = (favoriteNum, destination) => {
  const walls = new Set();
  const seen = new Set();

  const queue = [[...START_LOCATION, 0]];

  while (queue.length !== 0) {
    const [posRow, posCol, step] = queue.shift();

    if (posRow === destination[0] && posCol === destination[1]) {
      return step;
    }

    if (seen.has(`${posRow},${posCol}`)) {
      continue;
    }

    seen.add(`${posRow},${posCol}`);
    getNextOpenSpaceLocations(posRow, posCol, favoriteNum, walls).forEach(loc => {
      queue.push([...loc, step + 1]);
    });
  }
}

/**
 * Pass in the favorite number and maximum number of steps and return the number
 * of locations you can travel to within the max number.
 * @param   {number} favoriteNum the favorite number
 * @param   {number} maxSteps    the maximum number of steps
 * @returns {number}             the number of locations within the max steps
 */
const getNumberOfLocationsWithinSteps = (favoriteNum, maxSteps) => {
  const walls = new Set();
  const seen = new Set();

  const queue = [[...START_LOCATION, 0]];

  while (queue.length !== 0) {
    const [posRow, posCol, step] = queue.shift();

    if (seen.has(`${posRow},${posCol}`)) {
      continue;
    }
    
    if (step > maxSteps) {
      continue;
    }

    seen.add(`${posRow},${posCol}`);
    getNextOpenSpaceLocations(posRow, posCol, favoriteNum, walls).forEach(loc => {
      queue.push([...loc, step + 1]);
    });
  }

  return seen.size;
}

const solvePartOne = (favoriteNum, destination) => {
  return getMinimumStepsToDestination(favoriteNum, destination);
}

/**
 * Pass in the favorite number and return the number of locations you can visit
 * within 50 steps.
 * @param   {number} favoriteNum the favorite number
 * @returns {number}             the number of locations you can visit within 50 steps
 */
const solvePartTwo = (favoriteNum) => {
  return getNumberOfLocationsWithinSteps(favoriteNum, 50);
}

const main = () => {
  console.assert(solvePartOne(TEST_FAVORITE_NUMBER, TEST_DESTINATION) === 11);
  console.log(solvePartOne(INPUT_FAVORITE_NUMBER, INPUT_DESTINATION));
  console.log(solvePartTwo(INPUT_FAVORITE_NUMBER));
}

main();
