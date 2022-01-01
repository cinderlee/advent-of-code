#include <iostream>
#include <string>
#include <fstream>
using namespace std;

// test inputs for part 1
const string TEST_INPUT_1A = "(())";
const string TEST_INPUT_1B = "()()";
const string TEST_INPUT_2A = "(((";
const string TEST_INPUT_2B = "(()(()(";
const string TEST_INPUT_3 = "))(((((";
const string TEST_INPUT_4A = "())";
const string TEST_INPUT_4B = "))(";
const string TEST_INPUT_5A = ")))";
const string TEST_INPUT_5B = ")())())";

// test inputs for part 2
const string TEST_INPUT_6 = ")";
const string TEST_INPUT_7 = "()())";

const string INPUT_FILE_NM = "day1input1.txt";

int calculateFloor(const string& directions);
int determineFirstBasementPosition(const string& directions);
void solvePartOne(const string& directions);
void solvePartTwo(const string& directions);

int main() {
    ifstream inputFile(INPUT_FILE_NM);
    string directions;
    inputFile >> directions;
    inputFile.close();

    solvePartOne(directions);
    solvePartTwo(directions);
}

void solvePartOne(const string& directions) {
    assert(calculateFloor(TEST_INPUT_1A) == 0);
    assert(calculateFloor(TEST_INPUT_1B) == 0);
    assert(calculateFloor(TEST_INPUT_2A) == 3);
    assert(calculateFloor(TEST_INPUT_2B) == 3);
    assert(calculateFloor(TEST_INPUT_3) == 3);
    assert(calculateFloor(TEST_INPUT_4A) == -1);
    assert(calculateFloor(TEST_INPUT_4B) == -1);
    assert(calculateFloor(TEST_INPUT_5A) == -3);
    assert(calculateFloor(TEST_INPUT_5B) == -3);
    cout << calculateFloor(directions) << endl;
}

void solvePartTwo(const string& directions) {
    assert(determineFirstBasementPosition(TEST_INPUT_6) == 1);
    assert(determineFirstBasementPosition(TEST_INPUT_7) == 5);
    cout << determineFirstBasementPosition(directions) << endl;
}

int calculateFloor(const string& directions) {
    int floor = 0;
    for (const char& c: directions) {
        if (c == '(') {
            floor++;
        } else {
            floor--;
        }
    }
    return floor;
}

int determineFirstBasementPosition(const string& directions) {
    int floor = 0;
    for (int i = 0; i < directions.length(); i++) {
        if (directions[i] == '(') {
            floor++;
        } else {
            floor--;
        }
        if (floor < 0) {
            return i + 1;
        }
    }
    return 0;
}
