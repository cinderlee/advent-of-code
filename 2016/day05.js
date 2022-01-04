// Day 5: How About a Nice Game of Chess?

const crypto = require('crypto');

const INPUT_DOOR_ID = "ojvtpuvg";
const TEST_DOOR_ID = "abc";

const PASSWORD_LENGTH = 8;

/**
 * Pass in an index value and return whether it is a valid index. A valid index 
 * is a number that is less than the password length. The value passed in can be
 * NaN when trying to parse a letter as an integer.
 * @param   {number}  index 
 * @returns {boolean} whether the index is valid
 */
const isValidIndex = (index) => {
  return index !== NaN && index >= 0 && index < PASSWORD_LENGTH;
}

/**
 * Pass in a door id and return the eight-character security password to the 
 * first door designed by the Easter Bunny engineers. 
 * 
 * The password is created by taking the MD5 hash of the concatenation of the 
 * door id and an integer (starting from 0). If the hash starts with 5 leading 
 * zeroes (00000), then the sixth character of the hash is the next character 
 * of the password.
 * 
 * @param   {string} doorId the door id
 * @returns {string}        the security password
 */
const getPasswordForFirstDoor = (doorId) => {
  i = 0;
  const password = [];
  
  while (password.length !== PASSWORD_LENGTH) {
    const hashString = crypto.createHash('md5').update(`${doorId}${i}`).digest('hex').toString();
    if (hashString.indexOf('00000') === 0) {
      password.push(hashString[5]);
    }
    i++;
  }

  return password.join('');
}

/**
 * Pass in a door id and return the eight-character security password to the 
 * second door designed by the Easter Bunny engineers. 
 * 
 * The password is created by taking the MD5 hash of the concatenation of the 
 * door id and an integer (starting from 0). If the hash starts with 5 leading 
 * zeroes (00000), then the sixth character of the hash represents the index
 * of where the seventh character should go in the password. Only the first 
 * character found for each position is used (no replacements).
 * 
 * @param   {string} doorId the door id
 * @returns {string}        the security password
 */
const getPasswordForSecondDoor = (doorId) => {
  i = 0;
  const password = [null, null, null, null, null, null, null, null];
  
  let filled = 0;
  while (filled !== PASSWORD_LENGTH) {
    const hashString = crypto.createHash('md5').update(`${doorId}${i}`).digest('hex').toString();
    if (hashString.indexOf('00000') === 0) {
      const index = parseInt(hashString[5]);
      if (isValidIndex(index) && password[index] === null) {
        password[index] = hashString[6];
        filled++;
      }
    }
    i++;
  }

  return password.join('');
}

const solvePartOne = (doorId) => {
  return getPasswordForFirstDoor(doorId);
};

const solvePartTwo = (doorId) => {
  return getPasswordForSecondDoor(doorId);
};

const main = () => {
  console.assert(solvePartOne(TEST_DOOR_ID) === '18f47a30');
  console.assert(solvePartTwo(TEST_DOOR_ID) === '05ace8e3');

  console.log('Part One:', solvePartOne(INPUT_DOOR_ID));
  console.log('Part Two:', solvePartTwo(INPUT_DOOR_ID));
}

main();
