// Day 3: Perfectly Spherical Houses in a Vacuum

#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <tuple>
#include <cassert>
using namespace std;

const string TEST_INPUT_1 = ">";
const string TEST_INPUT_2 = "^>v<";
const string TEST_INPUT_3 = "^v^v^v^v^v";
const string TEST_INPUT_4 = "^v";
const string INPUT_FILE_NM = "./inputs/day3input.txt";

const map<char, tuple<int, int>> moves = {
    {'>', {1, 0}},
    {'<', {-1, 0}},
    {'^', {0, 1}},
    {'v', {0, -1}}
};

int countVisitedHouses(const string& directions);
int countVisitedHousesWithRoboSanta(const string& directions);
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
    assert(countVisitedHouses(TEST_INPUT_1) == 2);
    assert(countVisitedHouses(TEST_INPUT_2) == 4);
    assert(countVisitedHouses(TEST_INPUT_3) == 2);

    cout << "Part One: " << countVisitedHouses(directions) << endl;
}

void solvePartTwo(const string& directions) {
    assert(countVisitedHousesWithRoboSanta(TEST_INPUT_4) == 3);
    assert(countVisitedHousesWithRoboSanta(TEST_INPUT_2) == 3);
    assert(countVisitedHousesWithRoboSanta(TEST_INPUT_3) == 11);

    cout << "Part Two: " << countVisitedHousesWithRoboSanta(directions) << endl;
}

// Returns number of houses Santa visits given a list of directions 
// Each move is exactly a house visit to the north, south, east, or west.
int countVisitedHouses(const string& directions) {
    set<tuple<int, int>> visitedHouses;
    int x = 0;
    int y = 0;
    visitedHouses.insert({0, 0});
    for (const char& c: directions) {
        tuple<int, int> move = moves.at(c);
        x += get<0>(move);
        y += get<1>(move);
        visitedHouses.insert({x, y});
    }
    return visitedHouses.size();
}

// Returns number of houses Santa and Robo-Santa visits given a list of directions 
// Each move is exactly a house visit to the north, south, east, or west.
// Santa and Robo-Santa take turns moving based on instructions
int countVisitedHousesWithRoboSanta(const string& directions) {
    set<tuple<int, int>> visitedHouses;
    int santaX = 0;
    int santaY = 0;
    int roboX = 0;
    int roboY = 0;
    bool santaTurn = true;
    visitedHouses.insert({0, 0});
    for (const char& c: directions) {
        tuple<int, int> move = moves.at(c);
        if (santaTurn) {
            santaX += get<0>(move);
            santaY += get<1>(move);
            visitedHouses.insert({santaX, santaY});
        } else {
            roboX += get<0>(move);
            roboY += get<1>(move);
            visitedHouses.insert({roboX, roboY});
        }
        santaTurn = !santaTurn;
    }
    return visitedHouses.size();
}
