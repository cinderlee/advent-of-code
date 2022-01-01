// Day 1: No Time for a Taxicab

const fs = require('fs');

const INPUT_FILE_NAME = './inputs/day01input.txt';

const readFile = (fileName) => {
  /*
    Returns a list of directions from a file, where each direction 
    is also a list containing a rotation and the number of steps to move
    forward by.
  */
  const fileData = fs.readFileSync(fileName, 'utf-8');
  const directions = fileData.split(', ').map(dir => {
    const rotation = dir[0];
    const steps = parseInt(dir.substring(1));
    return [rotation, steps];
  });

  return directions;
}

const getNextDirection = (currentDirection, rotation) => {
  /*
    Returns the next direction you should face given your current direction and rotation.
  */
  const directions = ['N', 'E', 'S', 'W'];
  const directionIndex = directions.indexOf(currentDirection);
  let nextDirectionIndex = rotation === 'R' ? (directionIndex + 1) % directions.length : (directionIndex - 1) % directions.length;
  if (nextDirectionIndex === -1) {
    nextDirectionIndex = directions.length - 1;
  }
  return directions[nextDirectionIndex];
}

const trackLocations = (direction, steps, currentLocation) => {
  /*
    Returns a list of locations you will visit starting from your current location,
    the direction you will travel in, and the number of steps you will take.
  */
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

const solvePartOne = (directions) => {
  /*
    Returns the number of blocks away the Easter Bunny HQ. You start by facing north 
    and determine what is the shortest path to the HQ given a current list of directions.
  */
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

const findFirstRevisitedLocation = (locations) => {
  /*
    Returns the first location that is revisited given a list of locations.
  */
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

const solvePartTwo = (directions) => {
  /*
    Returns the number of blocks away the first location you visit twice. You start again 
    by facing north and following along the set of directions.
  */
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