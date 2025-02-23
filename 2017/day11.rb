# Day 11: Hex Ed

INPUT_FILE_NAME = "./inputs/day11input.txt"

MOVES = {
  "n" => [0, 2],
  "s" => [0, -2],
  "ne" =>  [1, 1],
  "se" => [1, -1],
  "nw" => [-1, 1],
  "sw" => [-1, -1]
}

# Reads a file and returns the list of steps taken in the hex grid
def get_steps(file_nm)
  steps = nil
  File.open(file_nm).each do |line|
    steps = line.chomp.split(",")
  end
  return steps
end

# Returns the fewest number of steps away the current 
# location is from the starting point [0, 0]
def calculate_num_fewest_steps(loc_x, loc_y)
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

# Returns the fewest number of steps needed to reach the destination
# after following the steps in the hex grid
def solve_part_one(steps)
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

# Returns the furthest number of steps away traveled from the starting position
def solve_part_two(steps)
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
  steps = get_steps(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(steps)}"
  puts "Part Two: #{solve_part_two(steps)}"
end

if __FILE__==$0
  main
end