// Day 7: Internet Protocol Version 7

const fs = require('fs');

const INPUT_FILE_NAME = './inputs/day07input.txt';
const TEST_FILE_NAME = './inputs/day07testinput.txt';

/**
 * Pass in an IP address and parse the address into two arrays of hypernet
 * and supernet sequences. Hypernet sequences are sequences wrapped inside of 
 * square brackets, while supernet sequences are outide of the square brackets.
 * @param   {string} ipAddress the IP address
 * @returns {Array}            the array of hypernet and supernet sequences
 */
const parseIpAddress = (ipAddress) => {
  const hypernetSeqeuences = [];
  const supernetSequences = [];
  let currIpAddressPart = ipAddress;
  while (currIpAddressPart.indexOf('[') !== -1) {
    const hypernetSequenceStart = currIpAddressPart.indexOf('[');
    const hypernetSequenceEnd = currIpAddressPart.indexOf(']');
    supernetSequences.push(currIpAddressPart.substring(0, hypernetSequenceStart));
    hypernetSeqeuences.push(currIpAddressPart.substring(hypernetSequenceStart + 1, hypernetSequenceEnd));
    currIpAddressPart = currIpAddressPart.substring(hypernetSequenceEnd + 1);
  }
  supernetSequences.push(currIpAddressPart)
  return [hypernetSeqeuences, supernetSequences];
}

/**
 * Pass in a file name and return an array of IP addresses, each represented
 * as an array of hypernet and supernet sequences.
 * @param   {string} fileName the file name
 * @returns {Array}           the array of IP addresses
 */
const readFile = (fileName) => {
  const ipAddresses =  fs.readFileSync(fileName, 'utf-8').split('\n');
  return ipAddresses.map(ipAddress => parseIpAddress(ipAddress));
}

/**
 * Pass in a part (hypernet or supernet) of an IP address and return whether
 * the part contains an Autonomous Bridge Bypass Annotation (ABBA).
 * @param   {string} ipAddressPart the IP address part
 * @returns {boolean}              whether the part contains an ABBA
 */
const hasABBA = (ipAddressPart) => {
  for (let i = 0; i < ipAddressPart.length - 3; i++) {
    if (ipAddressPart[i] !== ipAddressPart[i + 1] && 
      ipAddressPart[i] === ipAddressPart[i + 3] && 
      ipAddressPart[i + 1] === ipAddressPart[i + 2]) {
      return true;
    } 
  }
  return false;
}

/**
 * Pass in the IP address, which is an array containing the hypernet and supernet
 * sequences, and return whether the address supports TLS.
 * 
 * An address supports TLS when it has an Autonomous Bridge Bypass Annotation (in 
 * the form of ABBA) in any of the supernet sequences but not in any of the hypernet
 * sequences.
 * @param   {Array}   ipAddress the IP address
 * @returns {boolean}           whether the address supports TLS
 */
const supportsTLS = (ipAddress) => {
  const [hypernetSeqeuences, supernetSequences] = [...ipAddress];

  if (hypernetSeqeuences.every(sequence => !hasABBA(sequence))) {
    return supernetSequences.some(sequence => hasABBA(sequence));
  }
  return false;
}

/**
 * Pass in a supernet sequence and return an array of possible Byte Allocation 
 * Blocks (BAB). To find a possible BAB, an Area-Broadcast Accessor (ABA) must 
 * be found in a supernet sequence.
 * @param   {Array} supernetSequence the supernet sequence
 * @returns {Array}                  the array of possible BABs
 */
const getPossibleBABs = (supernetSequence) => {
  const babs = [];
  for (let i = 0; i < supernetSequence.length - 2; i++) {
    if (supernetSequence[i] !== supernetSequence[i + 1] && supernetSequence[i] === supernetSequence[i + 2]) {
      babs.push(`${supernetSequence[i + 1]}${supernetSequence[i]}${supernetSequence[i + 1]}`);
    }
  }
  return babs;
}

/**
 * Pass in the IP address, which is an array containing the hypernet and supernet
 * sequences, and return whether the address supports SSL.
 * 
 * An address supports SSL when it has an Area-Broadcast Accessor (in the form of ABA) 
 * in any of the supernet sequences and a matching Byte Allocation Block (in the form
 * of BAB) in any of the hypernet sequences.
 * @param   {Array}   ipAddress the IP address
 * @returns {boolean}           whether the address supports SSL
 */
const supportsSSL = (ipAddress) => {
  const [hypernetSeqeuences, supernetSequences] = [...ipAddress];
  const babs = [];

  supernetSequences.forEach(sequence => {
    babs.push(...getPossibleBABs(sequence));
  })

  return hypernetSeqeuences.some(sequence => (
    babs.some(bab => sequence.indexOf(bab) !== -1))
  );
}

/**
 * Pass in an array of IP addresses and return the number of addresses
 * that support TLS.
 * @param   {Array} ipAddresses the array of IP addresses
 * @returns {number}            the number of addresses that support TLS
 */
const solvePartOne = (ipAddresses) => {
  let count = 0;
  ipAddresses.forEach(ipAddress => {
    if (supportsTLS(ipAddress)) {
      count++;
    }
  });

  return count;
}

/**
 * Pass in an array of IP addresses and return the number of addresses
 * that support SSL.
 * @param   {Array} ipAddresses the array of IP addresses
 * @returns {number}            the number of addresses that support SSL
 */
const solvePartTwo = (ipAddresses) => {
  let count = 0;
  ipAddresses.forEach(ipAddress => {
    if (supportsSSL(ipAddress)) {
      count++;
    }
  });

  return count;
}

const main = () => {
  const testIPAddresses = readFile(TEST_FILE_NAME);
  console.assert(solvePartOne(testIPAddresses) == 2);
  console.assert(solvePartTwo(testIPAddresses) == 3);
  
  const ipAddresses = readFile(INPUT_FILE_NAME);
  console.log("Part One:", solvePartOne(ipAddresses));
  console.log("Part Two:", solvePartTwo(ipAddresses));
};

main();
