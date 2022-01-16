// Day 16: Dragon Checksum

const INPUT_INITIAL_STATE = '11011110011011101';
const INPUT_DISK_LENGTH = 272;
const INPUT_DISK_LENGTH_2 = 35651584;

const TEST_INPUT_INITIAL_STATE = '10000';
const TEST_INPUT_DISK_LENGTH = 20;

/**
 * Pass in the current data and the disk length and use a modified dragon
 * curve to return the data to fill the disk.
 * 
 * Steps:
 *   - a is your current data. Make a copy of your current data and 
 *     reverse te order of bits. Call this b.
 *   - Replace the 0s in b with 1s and 1s with 0s. 
 *   - Your updated data is a concatenaton of a, 0, and b.
 * @param   {string} data       the current data
 * @param   {number} diskLength the disk length to fill
 * @returns {string}            the final data to fill the disk;
 */
const getDataToFillDisk = (data, diskLength) => {
  while (data.length < diskLength) {
    let dataSecondHalf = data.split("").reverse();

    for (let i = 0; i < dataSecondHalf.length; i++) {
      dataSecondHalf[i] = dataSecondHalf[i] === '1' ? '0' : '1';
    }

    data += '0' + dataSecondHalf.join('');
  }

  return data.substring(0, diskLength);
}

/**
 * Pass in the initial disk data and disk length and return the dragon checksum. 
 * 
 * To find the checksum: 
 *   - For every pair of bits in the current checksum (beginning with the disk data),
 *     if the pair has matching bits, the next checksum character is a 1. Otherwise
 *     the character is a 0.
 *   - Repeat until the checksum length is odd.
 * @param   {string} initialData the initial disk data
 * @param   {number} diskLength  the disk length
 * @returns {string}             the checksum
 */
const getDragonChecksum = (initialData, diskLength) => {
  let checksum = getDataToFillDisk(initialData, diskLength);;
  
  while (checksum.length % 2 === 0) {
    const newChecksum = [];
    for (let i = 0; i < checksum.length; i += 2) {
      newChecksum.push(checksum[i] === checksum[i + 1] ? '1' : '0');
    }

    checksum = newChecksum.join('');
  }
  return checksum;
}

/**
 * Pass in the initial state and return the checksum for a disk of length 272.
 * @param   {string} initialState the initial state
 * @returns {string}              the checksum for disk of length 272
 */
const solvePartOne = (initialState) => {
  return getDragonChecksum(initialState, INPUT_DISK_LENGTH);
}

/**
 * Pass in the initial state and return the checksum for a disk of length 35651584.
 * @param   {string} initialState the initial state
 * @returns {string}              the checksum for disk of length 35651584
 */
const solvePartTwo = (initialState) => {
  return getDragonChecksum(initialState, INPUT_DISK_LENGTH_2);
}

const main = () => {
  console.assert(getDragonChecksum(TEST_INPUT_INITIAL_STATE, TEST_INPUT_DISK_LENGTH) === '01100');
  console.log("Part One:", solvePartOne(INPUT_INITIAL_STATE));
  console.log("Part Two:", solvePartTwo(INPUT_INITIAL_STATE));
}

main();
