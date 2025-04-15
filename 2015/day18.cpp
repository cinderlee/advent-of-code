// Day 18: Like a GIF For Your Yard

#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <tuple>
#include <cassert>
using namespace std;

const string INPUT_FILE_NM = "./inputs/day18input.txt";
const int GRID_SIZE = 100;
const int SIMULATION_NUMBER = 100;

map<tuple<int, int>, char> parseFile(const string& fileName);
map<tuple<int, int>, char> simulateAnimation(const map<tuple<int, int>, char>& grid, bool stuckOnCorners);
void solvePartOne(const map<tuple<int, int>, char>& grid);
void solvePartTwo(const map<tuple<int, int>, char>& grid);
int getNumNeighborsOn(const tuple<int, int> gridPosition, const map<tuple<int, int>, char>& grid);
void forceOnCorners(map<tuple<int, int>, char>& grid);
int getNumberOfLightsOn(const map<tuple<int, int>, char>& grid);

int main() {
    map<tuple<int, int>, char> grid = parseFile(INPUT_FILE_NM);
    solvePartOne(grid);
    solvePartTwo(grid);
}

void solvePartOne(const map<tuple<int, int>, char>& grid) {
    map<tuple<int, int>, char> animationResult = simulateAnimation(grid, false);
    int onLights = getNumberOfLightsOn(animationResult);

    cout << "Part One: " << onLights << endl;
}

void solvePartTwo(const map<tuple<int, int>, char>& grid) {
    map<tuple<int, int>, char> animationResult = simulateAnimation(grid, true);
    int onLights = getNumberOfLightsOn(animationResult);

    cout << "Part Two: " << onLights << endl;
}

// Returns number of lights that are on (#) in grid
int getNumberOfLightsOn(const map<tuple<int, int>, char>& grid) {
    int onLights = 0;
    for (const auto& [position, state] : grid) {
        if (state == '#') {
            onLights++;
        }
    }
    return onLights;
}

// Parse file for initial grid layout in the form of a map of tuple key (grid position) to light state
map<tuple<int, int>, char> parseFile(const string& fileName) {
    ifstream inputFile(fileName);
    map<tuple<int, int>, char> grid = {};
    string line;

    int row = 0;
    while (getline(inputFile, line)) {
        for (int col = 0; col < line.length(); col++) {
            grid[{row, col}] = line[col];
        }
        row++;
    }
    inputFile.close();
    return grid;
}

// Simulates animating for n number of times
// All lights update simultaneously, menaing that all consider the same current state before evaluating next
// An on light stays on if it has 2 or 3 neighbors that are on. Otherwise it will turn off.
// An off light will turn on if it has 3 neighbors that are on. Otherwise it will stay off.
// If stuckOnCorners is true, then the corner lights are permanently on.
map<tuple<int, int>, char> simulateAnimation(const map<tuple<int, int>, char>& grid, bool stuckOnCorners) {
    map<tuple<int, int>, char> currentGrid(grid);

    for (int i = 0; i < SIMULATION_NUMBER; i++) {
        if (stuckOnCorners) {
            forceOnCorners(currentGrid);
        }

        map<tuple<int, int>, char> newGrid = {};

        for (const auto& [position, state] : currentGrid) {
            bool isOn = state == '#';
            int onNeighbors = getNumNeighborsOn(position, currentGrid);

            char nextState = '.';
            if (!isOn && onNeighbors == 3) {
                nextState = '#';
            } else if (isOn && (onNeighbors == 3 || onNeighbors == 2)) {
                nextState = '#';
            }

            newGrid[position] = nextState;
        
        }

        currentGrid = newGrid;
    }

    if (stuckOnCorners) {
        forceOnCorners(currentGrid);
    }

    return currentGrid;
}

// Returns number of neighbors that are on given a grid position.
int getNumNeighborsOn(const tuple<int, int> gridPosition, const map<tuple<int, int>, char>& grid) {
    int onNeighbors = 0;
    auto& [row, col] = gridPosition;

    for (int r = row - 1; r <= row + 1; r++) {
        for (int c = col - 1; c <= col + 1; c++) {
            if (r == row && c == col) {
                continue;
            }

            if (r < 0 || c < 0 || r >= GRID_SIZE || c >= GRID_SIZE) {
                continue;
            }

            if (grid.at({r, c}) == '#') {
                onNeighbors++;
            }
        }
    }

    return onNeighbors;
}

// Forces the grid corners to be on
void forceOnCorners(map<tuple<int, int>, char>& grid) {
    grid[{ 0, 0 }] = '#';
    grid[{ 0, GRID_SIZE - 1 }] = '#';
    grid[{ GRID_SIZE - 1, 0 }] = '#';
    grid[{ GRID_SIZE - 1, GRID_SIZE - 1 }] = '#';
}