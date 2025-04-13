// Day 11: Corporate Policy

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cassert>
using namespace std;

const string INPUT = "vzbxkghb";
const string TEST_INPUT_1 = "abcdefgh";
const string TEST_INPUT_2 = "ghijklmn";

bool isValidPassword(const vector<char>& characters);
bool hasInvalidCharacters(const vector<char>& characters);
bool hasConsecutiveCharacters(const vector<char>& characters);
bool hasTwoPairsNonOverlappingCharacters(const vector<char>& characters);
void incrementPassword(vector<char>& characters);
string findValidPassword(vector<char>& characters);
string solvePartOne(const string& input);
string solvePartTwo(const string& input);

int main() {
    assert(solvePartOne(TEST_INPUT_1) == "abcdffaa");
    assert(solvePartOne(TEST_INPUT_2) == "ghjaabcc");
    string firstValidPassword = solvePartOne(INPUT);
    cout << "Part One: " << firstValidPassword << endl;
    string nextValidPassword = solvePartTwo(firstValidPassword);
    cout << "Part Two: " << nextValidPassword << endl;
}

string solvePartOne(const string& input){
    vector<char> characters;
    for (const char& c: input) {
        characters.push_back(c);
    }
    return findValidPassword(characters);
}

string solvePartTwo(const string& input){
    vector<char> characters;
    for (const char& c: input) {
        characters.push_back(c);
    }

    // The input used for part 2 is the first valid password. Need to increment so that 
    // the next valid password can be found.
    incrementPassword(characters);
    return findValidPassword(characters);
}

// Returns the next valid password given a vector of characters
string findValidPassword(vector<char>& characters) {    
    while(true) {
        if(isValidPassword(characters)) {
            return string(characters.begin(), characters.end());
        }

        // if there are invalid characters reset substring to next character + 'aa...'
        if (hasInvalidCharacters(characters)) {
            for (size_t index = characters.size() - 1; index >= 0; index--) {
                if (characters[index] == 'i' || characters[index] == 'o' || characters[index] == 'l') {
                    characters[index] += 1;
                    for (size_t resetIndex = index + 1; resetIndex < characters.size(); resetIndex++) {
                        characters[resetIndex] = 'a';
                    }
                    break;
                }
            }
            continue;
        }

        incrementPassword(characters);
    }
}

// Increments a vector of characters by 1, similar to increment numbers
// If the letter is z, the letter will wrap around to a and repeat with the next letter to the 
// left until there's no more wrapping around
void incrementPassword(vector<char>& characters) {
    for (size_t index = characters.size() - 1; index >= 0; index--) {
        if(characters[index] == 'z') {
            characters[index] = 'a';
        } else {
            characters[index] += 1;
            break;
        }
    }
}

// Determines whether a vector of characters is a valid password
// A valid password must not include invalid characters, needs to have a straight of at least
// 3 consecutive characters and needs to have at least 2 pairs of non-overlapping characters
bool isValidPassword(const vector<char>& characters) {
    if (hasInvalidCharacters(characters)) {
        return false;
    }

    return hasConsecutiveCharacters(characters) && hasTwoPairsNonOverlappingCharacters(characters);
}

// Returns whether vector of characters contains any invalid letters (i, o, or l)
bool hasInvalidCharacters(const vector<char>& characters) {
    for (const char& c: characters) {
        if (c == 'i' || c == 'o' || c == 'l') {
            return true;
        }
    }

    return false;
}

// Returns whether vector of characters has an increasing straight of at least three letters
bool hasConsecutiveCharacters(const vector<char>& characters) {
    for (size_t index = 0; index < characters.size() - 3; index++) {
        char firstChar = characters[index];
        char secondChar = characters[index + 1];
        char thirdChar = characters[index + 2];
        if (firstChar + 1 == secondChar && secondChar + 1 == thirdChar) {
            return true;
        }
    }
    return false;
}

// Returns whether vector characters contains two pairs of nonoverlapping characters
// ex: aa, bb, cc etc.
bool hasTwoPairsNonOverlappingCharacters(const vector<char>& characters) {
    set<char> characterPair;
    size_t index = 0;
    while (index <= characters.size() - 1) {
        char firstCharacter = characters[index];
        char secondCharacter = characters[index + 1];
        if (firstCharacter == secondCharacter) {
            characterPair.insert(firstCharacter);
            index += 2;
        } else {
            index++;
        }
    }

    return characterPair.size() >= 2;
}