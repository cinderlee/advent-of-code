// Day 6: Probably a Fire Hazard

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;

const string INPUT_FILE_NM = "./inputs/day6input.txt";
const int BOARD_SIZE = 1000;
const int TOGGLE = 0;
const int TURN_ON = 1;
const int TURN_OFF = 2;

vector<vector<int>> parseFile(const string& fileName);
vector<int> parseLine(const string& line);
vector<string> split(const string& str, char delimiter);
void solvePartOne(const vector<vector<int>>& instructions);
void solvePartTwo(const vector<vector<int>>& instructions);
vector<vector<int>> configureLights(const vector<vector<int>>& instructions, bool isSecondScoringSystem);
vector<vector<int>> generateLightsBoard();
int countLightValues(const vector<vector<int>>& lightsBoard);

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
    vector<string> parts = split(line, ' ');
    int instruction = 0;
    vector<string> startPosition;
    vector<string> endPosition;
    // turn on or off instruction
    if (parts.size() == 5) {
        instruction = parts[1] == "on" ? TURN_ON : TURN_OFF;
        startPosition = split(parts[2], ',');
        endPosition = split(parts[4], ',');
    } else {
        instruction = TOGGLE;
        startPosition = split(parts[1], ',');
        endPosition = split(parts[3], ',');
    }
    return {
        instruction,
        stoi(startPosition[0]),
        stoi(startPosition[1]),
        stoi(endPosition[0]),
        stoi(endPosition[1])
    };
}

void solvePartOne(const vector<vector<int>>& instructions) {
    vector<vector<int>> lights = configureLights(instructions, false);
    int count = countLightValues(lights);
    cout << "Part One: " << count << endl;
}

void solvePartTwo(const vector<vector<int>>& instructions) {
    vector<vector<int>> lights = configureLights(instructions, true);
    int count = countLightValues(lights);
    cout << "Part Two: " << count << endl;
}

// Returns the configured board of lights after following Santa's instructions for his ideal
// lighting configuration. 
//
// For part one (first scoring system)
// - turn on will turn on the light
// - turn off will turn off the light,
// - toggle will toggle on lights to off and vice versa. 
//
// For part two (second scoring system)
// - turn on means to increase the light brightness by 1
// - turn off means to decrease the light brightness by 1
// - toggle means to increase the light brightness by 2
vector<vector<int>> configureLights(const vector<vector<int>>& instructions, bool isSecondScoringSystem) {
    vector<vector<int>> lights = generateLightsBoard();

    for (const vector<int>& instruction: instructions) {
        int instr = instruction[0];
        int rowStart = instruction[1];
        int colStart = instruction[2];
        int rowEnd = instruction[3];
        int colEnd = instruction[4];

        for (int i = min(rowStart, rowEnd); i <= max(rowStart, rowEnd); i++) {
            for (int j = min(colStart, colEnd); j <= max(colStart, colEnd); j++) {
                if (instr == TURN_ON) {
                    lights[i][j] = isSecondScoringSystem ? lights[i][j] + 1 : 1;
                } else if (instr == TURN_OFF) {
                    lights[i][j] = isSecondScoringSystem ? lights[i][j] - 1 : 0;
                    if (lights[i][j] < 0) {
                        lights[i][j] = 0;
                    }
                } else {
                    lights[i][j] = isSecondScoringSystem ? lights[i][j] + 2 : 
                        lights[i][j] == 0 ? 1 : 0;
                }
            }
        }
    }

    return lights;
}

// Generates a board of lights where the values are 0s initially.
vector<vector<int>> generateLightsBoard() {
    vector<vector<int>> lights;
    for (int i = 0; i < BOARD_SIZE; i++) {
        vector<int> row;
        for (int j = 0; j < BOARD_SIZE; j++) {
            row.push_back(0);
        }
        lights.push_back(row);
    }

    return lights;
}

// Util function for splitting a string given a delimiter
vector<string> split(const string& str, char delimiter) {
    vector<string> tokens;
    stringstream ss(str);
    string token;
    while (getline(ss, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

// Returns the sum of the values in the board of lights
// For part one, this method will return the number of lights that are on (represented by 1, 0 is off)
// For part two, this method will return the total brightness of the lights.
int countLightValues(const vector<vector<int>>& lightsBoard) {
    int count = 0;
    for (int i = 0; i < BOARD_SIZE; i++) {
        for (int j = 0; j < BOARD_SIZE; j++) {
            count += lightsBoard[i][j];
        }
    }
    return count;
}