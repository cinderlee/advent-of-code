// Day 12: JSAbacusFramework.io

#include <iostream>
#include <string>
#include <fstream>
#include <cassert>
#include <cctype>
using namespace std;

const string INPUT_FILE_NM = "./inputs/day12input.txt";
const string COLLECTION_START_CHARACTERS = "{[";
const string COLLECTION_END_CHARACTERS = "}]";

const string TEST_INPUT_1 = "[1,2,3]";
const string TEST_INPUT_2 = "{\"a\":2,\"b\":4}";
const string TEST_INPUT_3 = "[[[3]]]";
const string TEST_INPUT_4 = "{\"a\":{\"b\":4},\"c\":-1}";
const string TEST_INPUT_5 = "{\"a\":[-1,1]}";
const string TEST_INPUT_6 = "[-1,{\"a\":1}]";
const string TEST_INPUT_7 = "{}";
const string TEST_INPUT_8 = "[]";
const string TEST_INPUT_9 = "[1, {\"c\":\"red\",\"b\":2},3]";
const string TEST_INPUT_10 = "{\"d\":\"red\",\"e\":[1,2,3,4],\"f\":5}";
const string TEST_INPUT_11 = "[1,\"red\",5]";

void solvePartOne(const string& jsonText);
void solvePartTwo(const string& jsonText);
int getSumOfJsonText(const string& jsonText, bool shouldNotCalculateIfRed);
string getIntegerStringFromStartPosition(const string& jsonText, size_t startPos);
int getSumOfStringStack(const vector<string>& stack, bool isObject, bool shouldNotCalculateIfRed);

int main() {
    ifstream inputFile(INPUT_FILE_NM);
    string jsonText;
    inputFile >> jsonText;
    inputFile.close();

    solvePartOne(jsonText);
    solvePartTwo(jsonText);
}

void solvePartOne(const string& jsonText) {
    assert(getSumOfJsonText(TEST_INPUT_1, false) == 6);
    assert(getSumOfJsonText(TEST_INPUT_2, false) == 6);
    assert(getSumOfJsonText(TEST_INPUT_3, false) == 3);
    assert(getSumOfJsonText(TEST_INPUT_4, false) == 3);
    assert(getSumOfJsonText(TEST_INPUT_5, false) == 0);
    assert(getSumOfJsonText(TEST_INPUT_6, false) == 0);
    assert(getSumOfJsonText(TEST_INPUT_7, false) == 0);
    assert(getSumOfJsonText(TEST_INPUT_8, false) == 0);

    int total = getSumOfJsonText(jsonText, false);
    cout << "Part One: " << total << endl;
}

void solvePartTwo(const string& jsonText) {
    assert(getSumOfJsonText(TEST_INPUT_1, true) == 6);
    assert(getSumOfJsonText(TEST_INPUT_9, true) == 4);
    assert(getSumOfJsonText(TEST_INPUT_10, true) == 0);
    assert(getSumOfJsonText(TEST_INPUT_11, true) == 6);

    int total = getSumOfJsonText(jsonText, true);
    cout << "Part Two: " << total << endl;
}

// Returns the sum of integers in the json text
// Uses a stack to calculate sums for nested arrays / objects 
// If shouldNotCalculateIfRed is true, then objects with property value of "red" will evaluate to 0
int getSumOfJsonText(const string& jsonText, bool shouldNotCalculateIfRed) {
    vector<string> stack;
    size_t pos = 0;
    while (pos < jsonText.size()) {
        if (isdigit(jsonText[pos])) {
            string integerString = getIntegerStringFromStartPosition(jsonText, pos);
            // Calculate next position depending on whether the number is negative
            pos += integerString[0] == '-' ? integerString.size() - 1 : integerString.size();
            stack.push_back(integerString);
            continue;
        } 

        if (jsonText[pos] == '{' || jsonText[pos] == '[') {
            stack.push_back(string() + jsonText[pos]);
        } else if (jsonText[pos] == 'r' && jsonText.substr(pos, 3) == "red") {
            stack.push_back("red");
        } else if (jsonText[pos] == '}' || jsonText[pos] == ']') {
            vector<string> subStack;

            // Evaluate substack for nested object / array
            while(stack[stack.size() - 1] != "{" && stack[stack.size() - 1] != "[") {
                subStack.push_back(stack[stack.size() - 1]);
                stack.pop_back();
            }
            stack.pop_back();

            stack.push_back(to_string(getSumOfStringStack(subStack, jsonText[pos] == '}', shouldNotCalculateIfRed)));
        }
        pos++;
    }

    return getSumOfStringStack(stack, false, false);
}

// Returns the integer string at position startPos
// If there is a negative sign the position before, the number returned will also be negative
string getIntegerStringFromStartPosition(const string& jsonText, size_t startPos) {
    for (size_t endPos = startPos + 1; endPos < jsonText.size(); endPos++) {
        if (!isdigit(jsonText[endPos])) {
            string number = jsonText.substr(startPos, endPos - startPos);
            if (startPos > 0 && jsonText[startPos - 1] == '-') {
                return '-' + number;
            }
            return number;
        }
    }
    return "";
}

// Calculates the sum of integers in a stack of strings
int getSumOfStringStack(const vector<string>& stack, bool isObject, bool shouldNotCalculateIfRed) {
    int total = 0;
    for (const string& val: stack) {
        if (val == "red") {
            if (isObject && shouldNotCalculateIfRed) {
                return 0;
            }
            continue;
        }

        total += stoi(val);
    }

    return total;
}