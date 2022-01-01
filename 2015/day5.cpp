#include <iostream>
#include <string>
#include <set>
#include <fstream>
#include <sstream>
#include <map>
using namespace std;

const string TEST_INPUT_1 = "ugknbfddgicrmopn";
const string TEST_INPUT_2 = "aaa";
const string TEST_INPUT_3 = "jchzalrnumimnmhp";
const string TEST_INPUT_4 = "haegwjzuvuyypxyu";
const string TEST_INPUT_5 = "dvszwmarrgswjxmb";
const string TEST_INPUT_6 = "qjhvhtzxzqqjkmpb";
const string TEST_INPUT_7 = "xxyxx";
const string TEST_INPUT_8 = "uurcxstgmygtbstg";
const string TEST_INPUT_9 = "ieodomkazucvgmuy";
const string INPUT_FILE_NM = "day5input.txt";
const set<string> INVALID_STRINGS = { "ab", "cd", "pq", "xy" };

bool isNiceStringPartOne(const string& str);
bool isNiceStringPartTwo(const string& str);
bool isInvalidString(char firstChar, char secondChar);
bool isVowel(char c);
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
    assert(isNiceStringPartOne(TEST_INPUT_1) == true);
    assert(isNiceStringPartOne(TEST_INPUT_2) == true);
    assert(isNiceStringPartOne(TEST_INPUT_3) == false);
    assert(isNiceStringPartOne(TEST_INPUT_4) == false);
    assert(isNiceStringPartOne(TEST_INPUT_5) == false);

    int countNiceStrings = 0;
    string str;
    while (getline(inputFile, str)) {
        if (isNiceStringPartOne(str)) {
            countNiceStrings++;
        }
    }
    cout << countNiceStrings << endl;
}

void solvePartTwo(ifstream& inputFile) {
    assert(isNiceStringPartTwo(TEST_INPUT_6) == true);
    assert(isNiceStringPartTwo(TEST_INPUT_7) == true);
    assert(isNiceStringPartTwo(TEST_INPUT_8) == false);
    assert(isNiceStringPartTwo(TEST_INPUT_9) == false);

    int countNiceStrings = 0;
    string str;
    while (getline(inputFile, str)) {
        if (isNiceStringPartTwo(str)) {
            countNiceStrings++;
        }
    }
    cout << countNiceStrings << endl;
}

bool isNiceStringPartOne(const string& str) {
    int vowelCount = 0;
    bool hasDoubleLeters = false;


    for (int i = 0; i < str.length(); i++) {
        char letter = str[i];
        char secondLetter = '\0';

        if (isVowel(letter)) {
            vowelCount++;
        }

        if (i != str.length() - 1) {
            secondLetter = str[i + 1];
        }

        if (isInvalidString(letter, secondLetter)) {
            return false;
        }

        if (letter == secondLetter) {
            hasDoubleLeters = true;
        }
    }
    return vowelCount >= 3 && hasDoubleLeters;
}

bool isNiceStringPartTwo(const string& str) {
    map<string, int> locations;
    bool repeatsTwoLetterSubstring = false;
    bool repeatsLetterAfterAnother = false;


    for (int i = 0; i < str.length(); i++) {
        char letter = str[i];
        char secondLetter = '\0';
        if (i != str.length() - 1) {
            secondLetter = str[i + 1];
        }

        string substring = {letter, secondLetter};
        if (locations.count(substring)) {
            if (i != locations.at(substring) + 1) {
                repeatsTwoLetterSubstring = true;
            } 
        } else {
            locations.insert({substring, i});
        }

        if (i >= 2) {
            char c = str[i - 2];
            if (c == letter) {
                repeatsLetterAfterAnother = true;
            }
        }
    }
    return repeatsTwoLetterSubstring && repeatsLetterAfterAnother;
}


bool isInvalidString(char firstChar, char secondChar) {
    for (const string& str : INVALID_STRINGS) {
        if (firstChar == str[0] && secondChar == str[1]) {
            return true;
        }
    }
    return false;
}

bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}
