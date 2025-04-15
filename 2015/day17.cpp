// Day 17: No Such Thing as Too Much

#include <iostream>
#include <string>
#include <fstream>
#include <cassert>
using namespace std;

const string INPUT_FILE_NM = "./inputs/day17input.txt";
const int VOLUME = 150;

vector<vector<int>> getIndicesSubsets(int numContainers);
int getNumSubsetsWithVolume(const vector<vector<int>>& indicesSubsets, const vector<int>& containers);
vector<int> parseFile(const string& fileName);
void solvePartOne(const vector<vector<int>>& indicesSubsets, const vector<int>& containers);
void solvePartTwo(const vector<vector<int>>& indicesSubsets, const vector<int>& containers);
int getNumSubsetsWithVolumeAndLowestNumberContainers(const vector<vector<int>>& indicesSubsets, const vector<int>& containers);

int main() {
    vector<int> containers = parseFile(INPUT_FILE_NM);
    vector<vector<int>> indicesSubsets = getIndicesSubsets(containers.size());
    solvePartOne(indicesSubsets, containers);
    solvePartTwo(indicesSubsets, containers);
}

void solvePartOne(const vector<vector<int>>& indicesSubsets, const vector<int>& containers) {
    int numSubsets = getNumSubsetsWithVolume(indicesSubsets, containers);
    cout << "Part One: " << numSubsets << endl;
}

void solvePartTwo(const vector<vector<int>>& indicesSubsets, const vector<int>& containers) {
    int numSubsets = getNumSubsetsWithVolumeAndLowestNumberContainers(indicesSubsets, containers);
    cout << "Part One: " << numSubsets << endl;
}

// Parses into a list of container sizes
vector<int> parseFile(const string& fileName) {
    ifstream inputFile(fileName);
    int number;
    vector<int> containerSizes;
    while (inputFile >> number) {
        containerSizes.push_back(number);
    }

    inputFile.close();
    return containerSizes;
}

// Returns number of ways we can use the least number of containers to hold VOLUME of eggnog
int getNumSubsetsWithVolumeAndLowestNumberContainers(const vector<vector<int>>& indicesSubsets, const vector<int>& containers) {
    size_t numContainers = containers.size();
    int count = 0;

    for (const vector<int>& subset: indicesSubsets) {
        int total = 0;
        for (int index: subset) {
            total += containers[index];
        }

        if (total == VOLUME) {
            if(subset.size() == numContainers) {
                count++;
            } else {
                numContainers = min(numContainers, subset.size());
                if (numContainers == subset.size()) count = 1;
            }
        }
    }

    return count;
}

// Returns the number of differnet combinations of containers to fit VOLUME of eggnog
int getNumSubsetsWithVolume(const vector<vector<int>>& indicesSubsets, const vector<int>& containers) {
    int count = 0;

    for (const vector<int>& subset: indicesSubsets) {
        int total = 0;
        for (int index: subset) {
            total += containers[index];
        }

        if (total == VOLUME) {
            count++;
        }
    }

    return count;
}

// Returns all possible indices subsets given the number of containers
// Used to then map to all possible combinations of container sizes.
vector<vector<int>> getIndicesSubsets(int numContainers) {
    vector<vector<int>> subsets;

    for (int i = 0; i < numContainers; i++) {
        size_t currentSubsetsSize = subsets.size();
        for (size_t index = 0; index < currentSubsetsSize; index++) {
            vector<int> nextSubset = subsets[index];
            nextSubset.push_back(i);

            subsets.push_back(nextSubset);
        }

        subsets.push_back({ i });
    }

    return subsets;
}
