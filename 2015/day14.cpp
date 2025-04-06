// Day 14: Reindeer Olympics

#include <iostream>
#include <string>
#include <fstream>
#include <cassert>
#include <sstream>
#include <map>
using namespace std;

const string INPUT_FILE_NM = "./inputs/day14input.txt";
const int SECONDS_ELAPSED = 2503;

const map<string, vector<int>> TEST_REINDEERS = {
    { "Comet", { 14, 10, 127 } },
    { "Dancer", { 16, 11, 162 } },
};
const int TEST_SECONDS_ELAPSED = 1000;

void solvePartOne(const map<string, vector<int>>& reindeers);
void solvePartTwo(const map<string, vector<int>>& reindeers);
map<string, vector<int>> parseFile(const string& fileName);
vector<string> split(const string& str, char delimiter);
int getWinningReindeerScore(const map<string, vector<int>>& reindeers, int totalNumSecondsElapsed);
int getWinningReindeerDistance(const map<string, vector<int>>& reindeers, int numSecondsElapsed);
int getDistanceTraveled(const vector<int>& reindeerDetails, int numSecondsElapsed);

int main() {
    map<string, vector<int>> reindeers = parseFile(INPUT_FILE_NM);
    solvePartOne(reindeers);
    solvePartTwo(reindeers);
}

void solvePartOne(const map<string, vector<int>>& reindeers) {
    assert(getWinningReindeerDistance(TEST_REINDEERS, TEST_SECONDS_ELAPSED) == 1120);

    int maxDistanceTraveled = getWinningReindeerDistance(reindeers, SECONDS_ELAPSED);
    cout << "Part One: " << maxDistanceTraveled << endl;
}

void solvePartTwo(const map<string, vector<int>>& reindeers) {
    assert(getWinningReindeerScore(TEST_REINDEERS, TEST_SECONDS_ELAPSED) == 689);

    int maxScore = getWinningReindeerScore(reindeers, SECONDS_ELAPSED);
    cout << "Part Two: " << maxScore << endl;
}

// Parses file and returns a mapping of reindeer to travel data: [rate km/s, flight duration, rest duration]
map<string, vector<int>> parseFile(const string& fileName) {
    ifstream inputFile(fileName);
    vector<vector<int>> instructions;
    string line;

    map<string, vector<int>> reindeers;

    while (getline(inputFile, line)) {
        vector<string> parts = split(line, ' ');
        reindeers[parts[0]] = { stoi(parts[3]), stoi(parts[6]), stoi(parts[parts.size() - 2]) };
    }
    inputFile.close();
    return reindeers;
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

// Returns the winning reindeer score given n number of seconds
// At each second, the reindeer in the lead gets a point and if there are multiple
// reindeers in the lead, they each get a point.
int getWinningReindeerScore(const map<string, vector<int>>& reindeers, int totalNumSecondsElapsed) {
    map<string, int> scores;
    for (const auto& pair : reindeers) {
        scores[pair.first] = 0;
    }

    for (int i = 1; i <= totalNumSecondsElapsed; i++) {
        int winningDistance = getWinningReindeerDistance(reindeers, i);
        
        for (const auto& pair : reindeers) {
            vector<int> reindeerDetails = pair.second;
            int distance = getDistanceTraveled(reindeerDetails, i);
    
            if (distance == winningDistance) {
                scores[pair.first] += 1;
            }
        }
    }

    int maxScore = 0;
    for (const auto& pair : scores) {
        maxScore = max(maxScore, pair.second);
    }
    return maxScore;
}

// Returns the winning reindeer distance given the number of seconds elapsed
int getWinningReindeerDistance(const map<string, vector<int>>& reindeers, int numSecondsElapsed) {
    int maxDistance = 0;

    for (const auto& pair : reindeers) {
        vector<int> reindeerDetails = pair.second;
        int distance = getDistanceTraveled(reindeerDetails, numSecondsElapsed);

        maxDistance = max(maxDistance, distance);
    }

    return maxDistance;
}

// Returns the distance traveled given how many seconds has elapsed
int getDistanceTraveled(const vector<int>& reindeerDetails, int numSecondsElapsed) {
    int rate = reindeerDetails[0];
    int travelDuration = reindeerDetails[1];
    int restDuration = reindeerDetails[2];

    // determine how many travel + rest time segments there are
    int travelAndRestSegments = numSecondsElapsed / (travelDuration + restDuration);
    int distance = travelAndRestSegments * rate * travelDuration;

    // determine how far the reindeer can still travel with the remaining time left
    int leftOverTravelSeconds = min(numSecondsElapsed % (travelDuration + restDuration), travelDuration); 
    distance += rate * leftOverTravelSeconds;

    return distance;
}
