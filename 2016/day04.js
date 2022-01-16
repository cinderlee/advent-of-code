// Day 4: Security Through Obscurity

const fs = require('fs');

const INPUT_FILE_NAME = "./inputs/day04input.txt";
const TEST_ROOM_1 = "aaaaa-bbb-z-y-x-123[abxyz]";
const TEST_ROOM_2 = "a-b-c-d-e-f-g-h-987[abcde]";
const TEST_ROOM_3 = "not-a-real-room-404[oarel]";
const TEST_ROOM_4 = "totally-real-room-200[decoy]";
const TEST_ROOM_5 = "qzmt-zixmtkozy-ivhz-343[something]";

const Z_CODE = 'z'.charCodeAt(0);

/**
 * Pass in the room data and return an array of the parsed room information. 
 * Each room has an encrypted name whose parts are separated by dashes, 
 * sector id, and a checksum.
 * @param   {string} roomData the room data
 * @returns {Array}           the array: [checksum, sector id, and encrypted name as an array]
 */
const parseRoomData = (roomData) => {
  const [encryptedName, checksum] = [...roomData.substring(0, roomData.length - 1).split('[')];
  const encryptedNameParts = encryptedName.split('-');
  const sectorId = parseInt(encryptedNameParts.pop());

  return [checksum, sectorId, encryptedNameParts];
};

/**
 * Pass in a file name and return an array of rooms, each represented as an 
 * array of information: the checksum, sector id, and encrypted name.
 * @param   {string} fileName the file name
 * @returns {Array}           the rooms
 */
const readFile = (fileName) => {
  const rooms = fs.readFileSync(fileName, 'utf-8').split('\n');
  return rooms.map(room => parseRoomData(room));
}

/**
 * Pass in the encrypted room name and cecksum and return whether the room
 * is real or not. A room is real if the checksum is the five most common
 * letters in the name. If there are ties, the letters are in alphabetical
 * order.
 * @param   {Array}  encryptedName the encrypted name
 * @param   {string} checksum      the checksum
 * @returns {boolean}              whether the room is real
 */
const isRealRoom = (encryptedNameParts, checksum) => {
  const letterCounts = {};

  encryptedNameParts.forEach(part => {
    for (const letter of part) {
      if (letterCounts.hasOwnProperty(letter)) {
        letterCounts[letter] += 1;
      } else {
        letterCounts[letter] = 1;
      }
    }
  });

  const letterCountsArray = Object.keys(letterCounts).sort((letterOne, letterTwo) => {
    if (letterCounts[letterOne] < letterCounts[letterTwo]) {
      return 1;
    } else if (letterCounts[letterOne] > letterCounts[letterTwo]) { 
      return -1;
    }

    return letterOne > letterTwo ? 1 : -1;
  });


  return letterCountsArray.join('').indexOf(checksum) === 0;
}

/**
 * Pass in part of the room name and a shift amount and return the decrypted version
 * of the name that was encrypted using a shift cypher.
 * @param   {string} encryptedPart a part of the encrypted room name
 * @param   {number} shift         the amount to shift by
 * @returns {string}               the decrypted name part
 */
const decryptRoomPart = (encryptedPart, shift) => {
  const decryptedLetters = encryptedPart.split("").map(letter => {
    let decryptedCharacter = letter.charCodeAt(0) + shift;
    decryptedCharacter = decryptedCharacter > Z_CODE ? decryptedCharacter - 26 : decryptedCharacter;
    return String.fromCharCode(decryptedCharacter);
  })

  return decryptedLetters.join("");
}

/**
 * Pass in an array of rooms read in from the information kiosk list and
 * return the sum of sector ids that belong to real rooms. 
 * @param   {Array} rooms the array of rooms
 * @returns {number}      the total of real room sector ids
 */
const solvePartOne = (rooms) => {
  let realRoomSectorIdTotal = 0;
  rooms.forEach(room => {
    const [checksum, sectorId, encryptedNameParts] = room;
   
    if (isRealRoom(encryptedNameParts, checksum)) {
      realRoomSectorIdTotal += sectorId;
    }
  });
  return realRoomSectorIdTotal;
}

/**
 * Pass in an array of rooms read in from the information kiosk list and
 * return the sector id of the room where the North Pole objects are stored.
 * @param   {Array} rooms the array of rooms
 * @returns {number}      the sector id of the North Pole objects room
 */
const solvePartTwo = (rooms) => {
  const realRooms = rooms.filter(room => isRealRoom(room[2], room[0]));

  const northPoleObjectRoom = realRooms.find(room => {
    const [checksum, sectorId, encryptedNameParts] = room;
    const shift = sectorId % 26;
    return encryptedNameParts.some(part => decryptRoomPart(part, shift).indexOf("northpole") !== -1);
  });

  return northPoleObjectRoom[1];
}

const runTestCases = () => {
  testRoomOne = parseRoomData(TEST_ROOM_1);
  console.assert(isRealRoom(testRoomOne[2], testRoomOne[0]));

  testRoomTwo = parseRoomData(TEST_ROOM_2);
  console.assert(isRealRoom(testRoomTwo[2], testRoomTwo[0]));

  testRoomThree = parseRoomData(TEST_ROOM_3);
  console.assert(isRealRoom(testRoomThree[2], testRoomThree[0]));

  testRoomFour = parseRoomData(TEST_ROOM_4);
  console.assert(!isRealRoom(testRoomFour[2], testRoomFour[0]));

  testRoomFive = parseRoomData(TEST_ROOM_5);
  const [testChecksum, testSectorId, testEncryptedNameParts] = testRoomFive;
  const testShift = testSectorId % 26;
  const testDecrypted = testEncryptedNameParts.map(part => decryptRoomPart(part, testShift));
  console.assert(testDecrypted.join(' ') === "very encrypted name");
}

const main = () => {
  runTestCases(); 

  const rooms = readFile(INPUT_FILE_NAME);
  console.log("Part One:", solvePartOne(rooms));
  console.log("Part Two:", solvePartTwo(rooms));
}

main();