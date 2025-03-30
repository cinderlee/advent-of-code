// Day 8: Matchsticks

#include <iostream>
#include <string>
#include <fstream>
#include <cassert>
using namespace std;

const string TEST_INPUT_1 = "\"\"";
const string TEST_INPUT_2 = "\"abc\"";
const string TEST_INPUT_3 = "\"aaa\\\"aaa\"";
const string TEST_INPUT_4 = "\"\\x27\"";
const string INPUT_FILE_NM = "./inputs/day8input.txt";

int getNumberOfCharacters(const string& str);
int getEncodedNumberOfCharacters(const string& str);
void solvePartOne(ifstream& inputFile);
void solvePartTwo(ifstream& inputFile);

int main() {
    ifstream inputFile(INPUT_FILE_NM);
    solvePartOne(inputFile);
    inputFile.clear();
    inputFile.seekg(0);
    solvePartTwo(inputFile);
    inputFile.close();
}

void solvePartOne(ifstream& inputFile) {
    assert(getNumberOfCharacters(TEST_INPUT_1) == 0);
    assert(getNumberOfCharacters(TEST_INPUT_2) == 3);
    assert(getNumberOfCharacters(TEST_INPUT_3) == 7);
    assert(getNumberOfCharacters(TEST_INPUT_4) == 1);

    int codeCharAndMemoryCharDifference = 0;
    string str;
    while (getline(inputFile, str)) {
        int memoryChar = getNumberOfCharacters(str);
        codeCharAndMemoryCharDifference += str.length() - memoryChar;
    }
    cout << "Part One: " << codeCharAndMemoryCharDifference << endl;
}

void solvePartTwo(ifstream& inputFile) {
    assert(getEncodedNumberOfCharacters(TEST_INPUT_1) == 6);
    assert(getEncodedNumberOfCharacters(TEST_INPUT_2) == 9);
    assert(getEncodedNumberOfCharacters(TEST_INPUT_3) == 16);
    assert(getEncodedNumberOfCharacters(TEST_INPUT_4) == 11);

    int encodedCharAndCurrentCodeCharDifference = 0;
    string str;
    while (getline(inputFile, str)) {
        int numEncodedChar = getEncodedNumberOfCharacters(str);
        encodedCharAndCurrentCodeCharDifference += numEncodedChar - str.length();
    }
    cout << "Part Two: " << encodedCharAndCurrentCodeCharDifference << endl;
}

// Returns the number of characters in memory for a given string
// Double quotes are used at the ends of the string but do not count
// Escape sequences are used to represent a single character -- could be used 
// for a lone character or for hexidecimal characters
int getNumberOfCharacters(const string& str) {
    int numCharacters = 0;
    int i = 1;
    while (i < str.length() - 1) {
        numCharacters++;
        if (str[i] == '\\') {
            i += str[i + 1] == 'x' ? 4 : 2;
        } else {
            i++;
        }
    }
    return numCharacters;
}

// Returns the number of code characters after encoding each code representation as an ew string
// This number should include encoding the surrounding double quotes
int getEncodedNumberOfCharacters(const string& str) {
    // Start of with 6 
    // An empty string "" will be encoded into "\"\"" ("" still used to wrap the text, each " becomes an escape character)
    int numEncodedCharacters = 6;
    for (int i = 1; i < str.length() - 1; i++) {
        if (str[i] == '\\' || str[i] == '"') {
            numEncodedCharacters += 2;
        } else {
            numEncodedCharacters++;
        }
    }
  
    return numEncodedCharacters;
}
