#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;

const string INPUT_FILE_NM = "day6input.txt";
const int TOGGLE = 0;
const int TURN_ON = 1;
const int TURN_OFF = 2;

vector<vector<int>> parseFile(const string& fileName);
vector<int> parseLine(const string& line);
void solvePartOne(const vector<vector<int>>& instructions);
void solvePartTwo(const vector<vector<int>>& instructions);


int main() {
    vector<vector<int>> instructions = parseFile(INPUT_FILE_NM);
    solvePartOne(instructions);
    solvePartTwo(instructions);
}

vector<vector<int>> parseFile(const string& fileName) {
    ifstream inputFile(fileName);
    vector<vector<int>> instructions;
    string line;

    while (getline(inputFile, line)) {
        instructions.push_back(parseLine(line));
    }
    inputFile.close();
    return instructions;
}

vector<int> parseLine(const string& line) {
    stringstream lineStream;
    string instruction; 
    int rowStart;
    int colStart; 
    int rowEnd;
    int colEnd;
    string filler;
    char comma;

    lineStream << line;
    if (line.find("turn") == 0) {
        lineStream >> instruction >> instruction;
    } else {
        lineStream >> instruction;
    }
    lineStream >> rowStart >> comma >> colStart >> filler >> rowEnd >> comma >> colEnd;

    vector<int> instrVec;
    if (instruction == "on") {
        instrVec.push_back(TURN_ON);
    } else if (instruction == "off") {
        instrVec.push_back(TURN_OFF);
    } else {
        instrVec.push_back(TOGGLE);
    }

    instrVec.insert(instrVec.end(), { rowStart, rowEnd, colStart, colEnd });

    return instrVec;
}

void solvePartOne(const vector<vector<int>>& instructions) {
    vector<vector<bool>> lights;
    for (int i = 0; i < 1000; i++) {
        vector<bool> row;
        for (int j = 0; j < 1000; j++) {
            row.push_back(false);
        }
        lights.push_back(row);
    }

    for (const vector<int>& instruction: instructions) {
        int instr = instruction[0];
        int rowStart = instruction[1];
        int rowEnd = instruction[2];
        int colStart = instruction[3];
        int colEnd = instruction[4];

        for (int i = rowStart; i <= rowEnd; i++) {
            for (int j = colStart; j <= colEnd; j++) {
                if (instr == TURN_ON) {
                    lights[i][j] = true;
                } else if (instr == TURN_OFF) {
                    lights[i][j] = false;
                } else {
                    lights[i][j] = !lights[i][j];
                }
            }
        }
    }

    int count = 0;
    for (int i = 0; i < 1000; i++) {
        for (int j = 0; j < 1000; j++) {
            if (lights[i][j]) {
                count++;
            }
        }
    }
    cout << count << endl;
}

int countLights

void solvePartTwo(const vector<vector<int>>& instructions) {
    vector<vector<int>> lights;
    for (int i = 0; i < 1000; i++) {
        vector<int> row;
        for (int j = 0; j < 1000; j++) {
            row.push_back(0);
        }
        lights.push_back(row);
    }

    for (const vector<int>& instruction: instructions) {
        int instr = instruction[0];
        int rowStart = instruction[1];
        int rowEnd = instruction[2];
        int colStart = instruction[3];
        int colEnd = instruction[4];

        for (int i = rowStart; i <= rowEnd; i++) {
            for (int j = colStart; j <= colEnd; j++) {
                if (instr == TURN_ON) {
                    lights[i][j]++;
                } else if (instr == TURN_OFF) {
                    if (lights[i][j] != 0) {
                        lights[i][j]--;
                    }
                } else {
                    lights[i][j] += 2;
                }
            }
        }
    }

    int count = 0;
    for (int i = 0; i < 1000; i++) {
        for (int j = 0; j < 1000; j++) {
            count += lights[i][j];
        }
    }
    cout << count << endl;
}
