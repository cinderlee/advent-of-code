// Day 10: Elves Look, Elves Say

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cassert>
using namespace std;

const string INPUT = "1113222113";
const string TEST_INPUT_1 = "1";
const string TEST_INPUT_2 = "11";
const string TEST_INPUT_3 = "21";
const string TEST_INPUT_4 = "1211";
const string TEST_INPUT_5 = "111221";

string generateSequence(const string& input, int repeatTimes);
void solvePartOne(const string& input);
void solvePartTwo(const string& input);

int main() {
    assert(generateSequence(TEST_INPUT_1, 1) == "11");
    assert(generateSequence(TEST_INPUT_2, 1) == "21");
    assert(generateSequence(TEST_INPUT_3, 1) == "1211");
    assert(generateSequence(TEST_INPUT_4, 1) == "111221");
    assert(generateSequence(TEST_INPUT_5, 1) == "312211");
    solvePartOne(INPUT);
    solvePartOne(INPUT);
}

void solvePartOne(const string& input){
    string sequence = generateSequence(input, 40);
    cout << sequence.size() << endl;
}

void solvePartTwo(const string& input){
    string sequence = generateSequence(input, 50);
    cout << sequence.size() << endl;
}

// Generates a look-and-say sequence after repeating a process n number of times. 
// To generate the sequence, convert the current sequence by reading aloud 
// Example: 211 is read as "one two, two ones" -> 1221
string generateSequence(const string& input, int repeatTimes) {
    vector<char> characters;
    for (const char& c: input) {
        characters.push_back(c);
    }

    for (int i = 0; i < repeatTimes; i++) {
        vector<char> sequence;
        char current = characters[0];
        int count = 1;
        for (size_t index = 1; index < characters.size(); index++) {
            if (characters[index] == current) {
                count++;
                continue;
            } 

            sequence.push_back(count + '0');
            sequence.push_back(current);

            current = characters[index];
            count = 1;
        }

        sequence.push_back(count + '0');
        sequence.push_back(current);

        characters = sequence;
    }

    return string(characters.begin(), characters.end());
}
