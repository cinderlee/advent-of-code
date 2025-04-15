// Day 7: Some Assembly Required

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <cctype>
#include <set>
using namespace std;

const string INPUT_FILE_NM = "./inputs/day7input.txt";

int solvePartOne(const vector<vector<string>>& instructions);
void solvePartTwo(const vector<vector<string>>& instructions);
void runInstructions(map<string, int>& registers, const vector<vector<string>>& instructions);
vector<vector<string>> parseInstructions(const string& fileName);
int getRegisterValueOrIntegerValue(const string& str, map<string, int>& registers);
vector<string> split(const string& str, const string& delimiter);
bool hasInputValue(const string& str, map<string, int>& registers);

int main() {
    vector<vector<string>> instructions = parseInstructions(INPUT_FILE_NM);
    int registerA = solvePartOne(instructions);

    // find instruction that instantiates b to an integer value and set to value of previous a
    for(size_t index = 0; index < instructions.size(); index++) {
        if (instructions[index].size() == 2 && instructions[index][1] == "b") {
            instructions[index][0] = to_string(registerA);
            break;
        }
    }
    solvePartTwo(instructions);
}

int solvePartOne(const vector<vector<string>>& instructions) {
    map<string, int> registers;
    runInstructions(registers, instructions);
    cout << "Part One: " << registers["a"] << endl;
    return registers["a"];
}

void solvePartTwo(const vector<vector<string>>& instructions) {
    map<string, int> registers;
    runInstructions(registers, instructions);
    cout << "Part Two: " << registers["a"] << endl;
}

// Runs a set of instructions. A register provides no signal until all of its inputs have a signal and
// all registers connected in some way.

// Because the instructions are not ordered, the instructions are looped over and over again 
// running instructions that have all input signals first until all instructions run.
void runInstructions(map<string, int>& registers, const vector<vector<string>>& instructions) {
    set<size_t> seenInstructionIndices;

    while(seenInstructionIndices.size() != instructions.size()) {
        for (size_t index = 0; index < instructions.size(); index++) {
            if (seenInstructionIndices.count(index)) {
                continue;
            }

            vector<string> instruction = instructions[index];
            // num -> register
            if(instruction.size() == 2 && hasInputValue(instruction[0], registers)) {
                registers[instruction[1]] = getRegisterValueOrIntegerValue(instruction[0], registers);
                seenInstructionIndices.insert(index);
            }
            // NOT register -> register
            else if (instruction.size() == 3 && hasInputValue(instruction[1], registers)) {
                registers[instruction[2]] = ~getRegisterValueOrIntegerValue(instruction[1], registers);
                seenInstructionIndices.insert(index);
            }
            
            // register instr register -> register
            else {
                if (!hasInputValue(instruction[0], registers) || !hasInputValue(instruction[2], registers)) {
                    continue;
                }

                int registerOne = getRegisterValueOrIntegerValue(instruction[0], registers);
                int registerTwo = getRegisterValueOrIntegerValue(instruction[2], registers);
    
                if (instruction[1] == "AND") {
                    registers[instruction[3]] = registerOne & registerTwo;
                }
                if (instruction[1] == "LSHIFT") {
                    registers[instruction[3]] = registerOne << registerTwo;
                }
                if (instruction[1] == "RSHIFT") {
                    registers[instruction[3]] = registerOne >> registerTwo;
                }
                if (instruction[1] == "OR") {
                    registers[instruction[3]] = registerOne | registerTwo;
                }

                seenInstructionIndices.insert(index);
            }
        }
    }
}

// Determines whether the register has a signal value or if the input is an integer
bool hasInputValue(const string& str, map<string, int>& registers) {
    if (isdigit(str[0])) {
        return true;
    }

    return registers.count(str);
}

// Returns either the integer value or register value
int getRegisterValueOrIntegerValue(const string& str, map<string, int>& registers) {
    if (isdigit(str[0])) {
        return stoi(str);
    }

    return registers.at(str);
}

// Parses the instructions into a list
vector<vector<string>> parseInstructions(const string& fileName) {
    ifstream inputFile(fileName);
    vector<vector<string>> instructions;
    string line;

    while (getline(inputFile, line)) {
        vector<string> parts = split(line, " -> ");
        vector<string> instruction = split(parts[0], " ");
        instruction.push_back(parts[1]);

        instructions.push_back(instruction);
    }

    inputFile.close();
    return instructions;
}

// Util function for splitting a string given a delimiter
vector<string> split(const string& str, const string& delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    string token;
    vector<string> result;

    while ((pos_end = str.find(delimiter, pos_start)) != std::string::npos) {
        token = str.substr (pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        result.push_back (token);
    }

    result.push_back(str.substr (pos_start));
    return result;
}