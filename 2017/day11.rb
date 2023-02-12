# Day 11: Hex Ed

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_FILE_NAME = "./inputs/day11input.txt"

TEST_STEPS_1 = ["ne", "ne", "ne"]
TEST_STEPS_2 = ["ne", "ne", "sw", "sw"]
TEST_STEPS_3 = ["ne", "ne", "s", "s"]
TEST_STEPS_4 = ["se", "sw", "se", "sw", "sw"]

MOVES = {
  "n" => [0, 2],
  "s" => [0, -2],
  "ne" =>  [1, 1],
  "se" => [1, -1],
  "nw" => [-1, 1],
  "sw" => [-1, -1]
}

def get_steps(file_nm)
  # Reads a file and returns the list of steps taken in the hex grid

  steps = nil
  File.open(file_nm).each do |line|
    steps = line.chomp.split(",")
  end
  return steps
end

def calculate_num_fewest_steps(loc_x, loc_y)
  # Returns the fewest number of steps away the current 
  # location is from the starting point [0, 0]

  num_steps = 0

  until (loc_x == 0 && loc_y == 0)
    direction = ""
    if (loc_x < 0 && loc_y < 0)
      direction = "sw"
    elsif (loc_x > 0 && loc_y < 0)
      direction = "se"
    elsif (loc_x > 0 && loc_y > 0)
      direction = "ne"
    elsif (loc_x < 0 && loc_y > 0)
      direction = "nw"
    elsif (loc_y > 0)
      direction = "n"
    else
      direction = "s"
    end

    disp_x, disp_y = MOVES[direction]
    loc_x -= disp_x
    loc_y -= disp_y
    num_steps += 1
  end

  num_steps
end 

def solve_part_one(steps)
  # Returns the fewest number of steps needed to reach the destination
  # after following the steps in the hex grid

  pos_x = 0
  pos_y = 0
  num_steps = 0
  steps.each do |step|
    move = MOVES[step]
    pos_x += move[0]
    pos_y += move[1]
  end

  calculate_num_fewest_steps(pos_x, pos_y)
end

def solve_part_two(steps)
  # Returns the furthest number of steps away traveled from the starting position

  pos_x = 0
  pos_y = 0
  furthest_num_steps = 0
  steps.each do |step|
    move = MOVES[step]
    pos_x += move[0]
    pos_y += move[1]
    num_steps = calculate_num_fewest_steps(pos_x, pos_y)
    furthest_num_steps = num_steps if num_steps > furthest_num_steps
  end

  furthest_num_steps
end

def main
  assert solve_part_one(TEST_STEPS_1) == 3
  assert solve_part_one(TEST_STEPS_2) == 0
  assert solve_part_one(TEST_STEPS_3) == 2
  assert solve_part_one(TEST_STEPS_4) == 3

  steps = get_steps(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(steps)}"
  puts "Part Two: #{solve_part_two(steps)}"
end

main