// Day 16: Aunt Sue

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cassert>
#include <map>
using namespace std;

const string INPUT_FILE_NM = "./inputs/day16inputlist.txt";
const string TICKER_TAPE_FILE_NM = "./inputs/day16tickertape.txt";

void solvePartOne(const map<string, int>& tickerTape, const map<int, map<string, int>>& auntSues);
void solvePartTwo(const map<string, int>& tickerTape, const map<int, map<string, int>>& auntSues);
bool isValidRangeValue(const string& componentName, int count, int tickerTapeComponentValue);
bool isRangeComponent(const string& componentName);
int getAuntSueNumber(
    const map<string, int>& tickerTape,
    const map<int, map<string, int>>& auntSues,
    bool hasRangeComponents
);
map<string, int> parseTickerTapeFile(const string& fileName);
map<int, map<string, int>> parseInputAuntSueFile(const string& fileName);
vector<string> split(const string& str, char delimiter);

int main() {
    map<string, int> tickerTape = parseTickerTapeFile(TICKER_TAPE_FILE_NM);
    map<int, map<string, int>> auntSues = parseInputAuntSueFile(INPUT_FILE_NM);

    solvePartOne(tickerTape, auntSues);
    solvePartTwo(tickerTape, auntSues);
}

void solvePartOne(const map<string, int>& tickerTape, const map<int, map<string, int>>& auntSues) {
    int auntNumber = getAuntSueNumber(tickerTape, auntSues, false);
    cout << "Part One: " << auntNumber << endl;
}

void solvePartTwo(const map<string, int>& tickerTape, const map<int, map<string, int>>& auntSues) {
    int auntNumber = getAuntSueNumber(tickerTape, auntSues, true);
    cout << "Part Two: " << auntNumber << endl;
}

// Returns the Aunt Sue that sent the gift with matching details to what is listed on the ticker tape.
// For part two, the ticker tape details are as follows:
// - cats and trees values represent a greater than range (ex: greater than 50)
// - pomeranians and dogs represent a less than range (ex: less than 40)
// - otherwise other values must match the values on the ticker tape
int getAuntSueNumber(
    const map<string, int>& tickerTape,
    const map<int, map<string, int>>& auntSues,
    bool hasRangeComponents
) {
    for (const auto& pair : auntSues) {
        int auntNumber = pair.first;
        map<string, int> components = pair.second;
    
        bool matches = true;
        for (const auto& componentPair : components) {
            string componentName = componentPair.first;
            int count = componentPair.second;
            int tickerTapeComponentValue = tickerTape.at(componentName);
           
            if (hasRangeComponents && isRangeComponent(componentName)) {
                if (!isValidRangeValue(componentName, count, tickerTapeComponentValue)) {
                    matches = false;
                    break;
                } else {
                    continue;
                }
            }

            if (tickerTapeComponentValue != count) {
                matches = false;
                break;
            }

        }

        if (matches) {
            return auntNumber;
        }
    }
    return 0;
}

// Determines whether given value for a component falls within the range specified on the ticker tape
bool isValidRangeValue(const string& componentName, int count, int tickerTapeComponentValue) {
    if (componentName == "cats" || componentName == "trees") {
        return count > tickerTapeComponentValue;
    }

    if (componentName == "pomeranians" || componentName == "goldfish") {
        return count < tickerTapeComponentValue;
    }

    // not a range component -- default to true
    return true;
}

// Returns whether a component name is one of the components that has range values
bool isRangeComponent(const string& componentName) {
    vector<string> rangeComponentNames = { "cats", "trees", "pomeranians", "goldfish" };
    return find(rangeComponentNames.begin(), rangeComponentNames.end(), componentName) != rangeComponentNames.end();
}

// Parses ticker tape file into a map of { component: count value }
map<string, int> parseTickerTapeFile(const string& fileName) {
    ifstream tickerTapeFile(fileName);
    map<string, int> tickerTape;
    string line;

    while (getline(tickerTapeFile, line)) {
        stringstream info;
        info << line;
        string component;
        int count;
        info >> component >> count;

        // when inserting into map, omit the : character from component
        tickerTape[component.substr(0, component.size() - 1)] = count;
    }

    tickerTapeFile.close();
    return tickerTape;
}

// Parses input Aunt Sue file details into a nested map of { aunt number : { component : count value }}
map<int, map<string, int>> parseInputAuntSueFile(const string& fileName) {
    ifstream inputFile(fileName);
    map<int, map<string, int>> auntSueData;
    string line;

    while (getline(inputFile, line)) {
        vector<string> parts = split(line, ' ');

        int auntNumber = stoi(parts[1]);
        map<string, int> components;

        for(size_t index = 2; index < parts.size(); index += 2) {
            string component = parts[index].substr(0, parts[index].size() - 1);

            int count = 0;
            // the last number in list will not have a comma following it
            if (index + 1 == parts.size() - 1) {
                count = stoi(parts[index + 1]);
            } else {
                count = stoi(parts[index + 1].substr(0, parts[index + 1].size() - 1));
            }

            components[component] = count;
        }

        auntSueData[auntNumber] = components;
    }

    inputFile.close();
    return auntSueData;
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

