// Day 2: I Was Told There Would Be No Math

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cassert>
using namespace std;

const string TEST_INPUT_1 = "2x3x4";
const string TEST_INPUT_2 = "1x1x10";

const string INPUT_FILE_NM = "./inputs/day2input.txt";

int calculatePresentWrappingPaper(const string& dimensions);
int calculatePresentWrappingPaper(int length, int width, int height);
int calculatePresentRibbon(const string& dimensions);
int calculatePresentRibbon(int length, int width, int height);
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
    assert(calculatePresentWrappingPaper(TEST_INPUT_1) == 58);
    assert(calculatePresentWrappingPaper(TEST_INPUT_2) == 43);

    string dimensions;
    int totalWrappingPaper = 0;
    while (getline(inputFile, dimensions)) {
        totalWrappingPaper += calculatePresentWrappingPaper(dimensions);
    }
    
    cout << "Part One: " << totalWrappingPaper << endl;
}

void solvePartTwo(ifstream& inputFile) {
    assert(calculatePresentRibbon(TEST_INPUT_1) == 34);
    assert(calculatePresentRibbon(TEST_INPUT_2) == 14);

    string dimensions;
    int totalRibbon = 0;
    while (getline(inputFile, dimensions)) {
        totalRibbon += calculatePresentRibbon(dimensions);
    }
    
    cout << "Part Two: " << totalRibbon << endl;
}

// Returns the amount of ribbon needed to wrap a present and make a ribbow bow
// given the dimensions (ex: 2x3x4)
int calculatePresentRibbon(const string& dimensions) {
    stringstream dimensionsStream;
    dimensionsStream << dimensions;
    int length;
    int width;
    int height;
    char x;
    dimensionsStream >> length >> x >> width >> x >> height;
    return calculatePresentRibbon(length, width, height);
}

// Returns the amount of ribbon needed to wrap a present -- the shortest distance
// around the sides or smallest perimeter. 
// A bow is also needed, to which the measurement is equal to the cubic volume of the present 
int calculatePresentRibbon(int length, int width, int height) {
    int perimeterOne = 2 * length + 2 * width;
    int perimeterTwo = 2 * width + 2 * height;
    int perimeterThree = 2 * length + 2 * height;

    int ribbonLength = min(min(perimeterOne, perimeterTwo), perimeterThree);
    int bowRibbonLength = length * width * height;
    return ribbonLength + bowRibbonLength;
}

// Returns the amount of wrapping paper needed to wrap a rectangular prism present
// Example of dimensions input: 2x3x4
int calculatePresentWrappingPaper(const string& dimensions) {
    stringstream dimensionsStream;
    dimensionsStream << dimensions;
    int length;
    int width;
    int height;
    char x;
    dimensionsStream >> length >> x >> width >> x >> height;
    return calculatePresentWrappingPaper(length, width, height);
}

// Returns the amount of wrapping paper needed to wrap a rectangular prism present
// given the length, width, and height. A little extra paper is also needed, which
// the area of the smallest side
int calculatePresentWrappingPaper(int length, int width, int height) {
    int sideOneArea = length * width;
    int sideTwoArea = width * height;
    int sideThreeArea = length * height;

    int surfaceArea = 2 * sideOneArea + 2 * sideTwoArea + 2 * sideThreeArea;
    int smallestSideArea = min(min(sideOneArea, sideTwoArea), sideThreeArea);
    return surfaceArea + smallestSideArea;
}
