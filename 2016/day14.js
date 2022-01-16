// Day 14: One-Time Pad

const crypto = require('crypto');

const INPUT_SALT = "yjdafjpo";
const TEST_SALT = "abc";

/**
 * Pass in a salt and an index and return the MD5 hash of the concatenation 
 * of the salt and index.
 * @param   {string} salt   the salt
 * @param   {number} index  the index
 * @returns {string}        the MD5 hash
 */
const getHashPartOne = (salt, index) => {
  return crypto.createHash('md5').update(`${salt}${index}`).digest('hex').toString();
}

/**
 * Pass in a salt and an index and return the hash of the concatenation 
 * of the salt and index. The hash is generated using key stretching by 
 * starting with the MD5 hash, like part one, and then another 2016 
 * additional hashings are performed.
 * @param   {string} salt   the salt
 * @param   {number} index  the index
 * @returns {string}        the 2017th MD5 hash
 */
const getHashPartTwo = (salt, number) => {
  let hash = crypto.createHash('md5').update(`${salt}${number}`).digest('hex').toString();
  for (let i = 0; i < 2016; i++) {
    hash = crypto.createHash('md5').update(hash).digest('hex').toString();
  }
  return hash;
}

/**
 * Pass in the salt, a number n, and the hash function and return the index
 * of the nth one-time pad key.
 * @param   {string}   salt     the door idea
 * @param   {number}   n        n
 * @param   {Function} hashFunc the hash function
 * @returns {number}            the index of the nth key
 */
const getIndexOfNthKey = (salt, n, hashFunc) => {
  i = 0;
  const indices = [];
  const hashes = {};
  
  while (indices.length !== n) {
    const hashString = hashes.hasOwnProperty(i) ? hashes[i] : hashFunc(salt, i);

    for (let j = 0; j <= hashString.length - 3; j++) {
      if (hashString[j] === hashString[j + 1] && hashString[j + 1] === hashString[j + 2]) {
        for (let k = i + 1; k < 1000 + i + 1; k++) {
          const nextKHash = hashes.hasOwnProperty(k) ? hashes[k] : hashFunc(salt, k);
          hashes[k] = nextKHash;
          if (nextKHash.indexOf(hashString[j].repeat(5)) !== -1) {
            indices.push(i);
            break;
          }
        }
        break;
      }
    }
    i++;
  }

  return indices[n - 1];
}

const solvePartOne = (salt) => {
  return getIndexOfNthKey(salt, 64, getHashPartOne);
}

const solvePartTwo = (salt) => {
  return getIndexOfNthKey(salt, 64, getHashPartTwo);
}

const main = () => {
  console.assert(solvePartOne(TEST_SALT) === 22728);
  console.assert(solvePartTwo(TEST_SALT) === 22551);

  console.log("Part One:", solvePartOne(INPUT_SALT));
  console.log("Part Two:", solvePartTwo(INPUT_SALT));
}

main()
