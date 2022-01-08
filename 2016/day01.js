// Day 1: No Time for a Taxicab

const fs = require('fs');

const INPUT_FILE_NAME = './inputs/day01input.txt';

/**
 * Pass in a file name and return an array of directions where each direction
 * is also an array containing a rotation and the number of steps to move
 * forward by.
 * @param   {string} fileName the file name
 * @returns {Array}           the directions
 */
const readFile = (fileName) => {
  const fileData = fs.readFileSync(fileName, 'utf-8');
  const directions = fileData.split(', ').map(dir => {
    const rotation = dir[0];
    const steps = parseInt(dir.substring(1));
    return [rotation, steps];
  });

  return directions;
}

/**
 * Pass in the current direction and rotation and return the next direction. A 
 * rotation can be left 90 degress or right 90 degrees.
 * @param   {string} currentDirection the current direction
 * @param   {string} rotation         the rotation
 * @returns {string}                  the next direction
 */
const getNextDirection = (currentDirection, rotation) => {
  const directions = ['N', 'E', 'S', 'W'];
  const directionIndex = directions.indexOf(currentDirection);
  let nextDirectionIndex = rotation === 'R' ? (directionIndex + 1) % directions.length : (directionIndex - 1) % directions.length;
  if (nextDirectionIndex === -1) {
    nextDirectionIndex = directions.length - 1;
  }
  return directions[nextDirectionIndex];
}

/**
 * Pass in the direction you will travel in, number of steps, and current location 
 * and return an array of locations you will visit.
 * @param   {string} direction      the direction
 * @param   {Number} steps          the number of steps
 * @param   {Array} currentLocation the current location
 * @returns {Array}                 the locations you will visit
 */
const trackLocations = (direction, steps, currentLocation) => {
  const [x, y] = [...currentLocation];
  const locations = Array.from(Array(steps).keys()).map(i => {
    const step = i + 1;
    switch(direction) {
      case 'N':
        return [x, y + step];
      case 'S':
        return [x, y - step];
      case 'W':
        return [x - step, y];
      case 'E':
        return [x + step, y];
      default:
        return [];
    }
  });
  return locations;
}

/**
 * Pass in an array of locations and return the first location to be visited twice
 * @param   {Array} locations the locations
 * @returns {Array}           the first location to be visited twice
 */
 const findFirstRevisitedLocation = (locations) => {
  let revisitedLocation = null;
  const locationRecords = new Set();

  locations.some((loc) => {
    const locRecord = `${loc[0]},${loc[1]}`;
    if (locationRecords.has(locRecord)) {
      revisitedLocation = loc;
      return true;
    }
    locationRecords.add(locRecord);
  });

  return revisitedLocation;
}

/**
 * Pass in an array of directions and start by facing north. Returns the number of
 * blocks away from the Easter Bunny HQ after determining what is the shortest 
 * path to the HQ.
 * @param   {Array} directions the direction
 * @returns {number}           the number of blocks away the HQ is
 */
const solvePartOne = (directions) => {
  const displacements = {
    N: 0,
    S: 0,
    W: 0,
    E: 0
  };
  
  let currentDirection = 'N';

  directions.forEach((dir) => {
    const [rotation, steps] = [...dir];
    currentDirection = getNextDirection(currentDirection, rotation);
    displacements[currentDirection] += steps;
  });

  return Math.abs(displacements.N - displacements.S) + Math.abs(displacements.E - displacements.W);
}

/**
 * Pass in an array of directions and start by facing north. Follow along the set of
 * directions and return the number of blocks away the first location to be visited twice is.
 * @param   {Array} directions the direction
 * @returns {number}           the number of blocks away the first location revisited is
 */
const solvePartTwo = (directions) => {
  let currentLoc = [0, 0];
  let currentDirection = 'N';
  const locations = [];

  directions.forEach((dir) => {
    const [rotation, steps] = [...dir];
    currentDirection = getNextDirection(currentDirection, rotation);
    const visitedLocations = trackLocations(currentDirection, steps, currentLoc);
    locations.push(...visitedLocations);
    currentLoc = visitedLocations[visitedLocations.length - 1];
  });

  const revisitedLocation = findFirstRevisitedLocation(locations);

  return Math.abs(revisitedLocation[0]) + Math.abs(revisitedLocation[1]);
}

const main = () => {
  // R2, L3
  console.assert(solvePartOne([['R', 2], ['L', 3]]) === 5);
  // R2, R2, R2
  console.assert(solvePartOne([['R', 2], ['R', 2], ['R', 2]]) === 2);
  // R5, L5, R5, R3
  console.assert(solvePartOne([['R', 5], ['L', 5], ['R', 5], ['R', 3]]) === 12);
  // R8, R4, R4, R8
  console.assert(solvePartTwo([['R', 8], ['R', 4], ['R', 4], ['R', 8]]) === 4);

  const directions = readFile(INPUT_FILE_NAME);
  console.log('Part One:', solvePartOne(directions));
  console.log('Part Two:',solvePartTwo(directions));
}

main();
