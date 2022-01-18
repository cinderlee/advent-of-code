// Day 20: Firewall Rules

const fs = require('fs');

const INPUT_FILE_NAME = './inputs/day20input.txt';
const TEST_FILE_NAME = './inputs/day20testinput.txt';

/**
 * Pass in a file name and return the blacklist of IP ranges that are blocked
 * the corporate firewall. The ranges are sorted according to the starting number
 * of each range.
 * @param   {string} fileName the file name
 * @returns {Array}           the ranges of IPs blocked by the firewall
 */
const readFile = (fileName) => {
  const blockedIpRanges = fs.readFileSync(fileName, 'utf-8').split('\n').map(range => 
    range.split('-').map(num => parseInt(num))
  );
  blockedIpRanges.sort((rangeOne, rangeTwo) => rangeOne[0] < rangeTwo[0] ? -1 : 1);
  return blockedIpRanges;
}

/**
 * Pass in a list of blocked IP ranges and and return the lowest-valued IP address
 * that the firewall allows.
 * @param   {Array} blockedIpRanges the ranges of IPs blocked by the firewall
 * @returns {number}                the lowesst-valued IP allowed
 */
const getLowestIpAllowed = (blockedIpRanges) => {
  let ip = 0;
  for (const range of blockedIpRanges) {
    const [rangeStart, rangeEnd] = range;
    if (ip < rangeStart) {
      return ip;
    }

    if (ip < rangeEnd) {
      ip = rangeEnd + 1;
    }
  }

  return ip;
}

/**
 * Pass in a list of blocked IP ranges and and count the number of IP addresses
 * allowed by the blacklist. The IP addresses are written as 32-bit integers, which
 * can range from 0 to 4294967295 inclusive.
 * @param   {Array} blockedIpRanges the ranges of IPs blocked by the firewall
 * @returns {number}                the number of IP addresses allowed
 */
const countAllowedIps = (blockedIpRanges) => {
  let count = 0;
  let ipMarker = 0;
  for (const range of blockedIpRanges) {
    const [rangeStart, rangeEnd] = range;
    if (ipMarker < rangeStart) {
      count += rangeStart - ipMarker;
    }

    if (ipMarker < rangeEnd) {
      ipMarker = rangeEnd + 1;
    }
  }

  if (ipMarker < 4294967295) {
    count += 4294967295 - ipMarker;
  }

  return count;
}

const solvePartOne = (blockedIpRanges) => {
  return getLowestIpAllowed(blockedIpRanges);
}

const solvePartTwo = (blockedIpRanges) => {
  return countAllowedIps(blockedIpRanges);
}

const main = () => {
  const testBlockedIpRanges = readFile(TEST_FILE_NAME);
  console.assert(solvePartOne(testBlockedIpRanges) === 3);
  
  const blockedIpRanges = readFile(INPUT_FILE_NAME);
  console.log("Part One:", solvePartOne(blockedIpRanges));
  console.log("Part Two:", solvePartTwo(blockedIpRanges));
}

main()