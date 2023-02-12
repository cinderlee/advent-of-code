# Day 3: Spiral Memory

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_NUM = 325489

def get_circle_num(square_num)
  # Returns the circle number the data square is located in. 

  circle_root = (square_num ** 0.5).ceil
  circle_root = circle_root % 2 == 1 ? circle_root : circle_root + 1
  circle_num = (circle_root + 1) / 2 

  circle_num
end

def get_circle_corners(circle_num)
  # Returns the data square numbers at each corner for the specified circle

  max_num_in_circle = (2 * circle_num - 1) ** 2
  first_corner = max_num_in_circle - ((2 * circle_num - 2) * 3)
  second_corner = max_num_in_circle - ((2 * circle_num - 2) * 2)
  third_corner = max_num_in_circle - ((2 * circle_num - 2) * 1)
  fourth_corner = max_num_in_circle

  [first_corner, second_corner, third_corner, fourth_corner]
end

def get_side_index(target_num, circle_corners, circle_num)
  # Return the index position of a number found in a side of the 
  # circle in the grid. 

  first_corner, second_corner,third_corner, fourth_corner = circle_corners
  min_num_in_circle = ((circle_num - 1) * 2 - 2) ** 2 + 1

  if target_num >= first_corner && target_num <= second_corner
    (first_corner..second_corner).find_index(target_num)
  elsif target_num >= second_corner && target_num <= third_corner
    (second_corner..third_corner).find_index(target_num)
  elsif target_num >= third_corner && target_num <= fourth_corner
    (third_corner..fourth_corner).find_index(target_num)
  else
    # This side includes the max number as well. To account for this, the 
    # range is reverse to treat the max number as a last element.
    (min_num_in_circle..first_corner).to_a.reverse.find_index(target_num)
  end 
end

def get_manhattan_distance(square_num)
  # Returns the manhattan distance from the specified square to square 1. 
  # The squares are placed in a grid spiraling outward. 

  circle_num = get_circle_num(square_num)
  circle_corners = get_circle_corners(circle_num)
  side_index = get_side_index(square_num, circle_corners, circle_num)
  middle_index = (circle_num * 2 - 1) / 2

  (circle_num - 1) + (side_index - middle_index).abs()
end

def get_adjacent_sum(position, square_values)
  # Return the sum of the adjacent square values for the specified location

  row, col = position
  sum = 0

  (row - 1..row + 1).each do |r|
    (col - 1..col + 1).each do |c|
      sum += square_values.fetch([r, c], 0)
    end
  end

  sum
end

def get_next_direction(position, curr_direction)
  # Returns the next direction to go in given the position 
  # The value allocation in the grid happens in a spiral.

  row, col = position

  # Go up from the start of the spiral
  if (col == row + 1 && row >= 0 && col >= 0)
    [-1, 0]
  
  elsif (row == col * -1)
    # Go left if at the upper right corner
    if (row < 0)
      [0, -1]
    # Go right if at the lower left corner
    else
      [0, 1]
    end 
  # Go down if at the upper left corner
  elsif (row == col && row < 0)
    [1, 0]

  # No change in direction
  else 
    curr_direction
  end
end

def solve_part_one(square_num)
  get_manhattan_distance(square_num)
end

def solve_part_two(target_num)
  # Return the first value allocated that us greater than the specified number.
  # Value allocation occurs in a spiral with the value of 1 stored initial in 
  # square 1 (location 0, 0). 

  square_values = { [0, 0] => 1 }
  direction = [0, 1]
  position = [0, 1]

  while true
    adjacent_sum = get_adjacent_sum(position, square_values)
    if (adjacent_sum > target_num)
      return adjacent_sum
    end
    square_values[position] = adjacent_sum
    direction = get_next_direction(position, direction)
    position = [position[0] + direction[0], position[1] + direction[1]]
  end
end

def main
  assert solve_part_one(1) == 0
  assert solve_part_one(12) == 3
  assert solve_part_one(23) == 2
  assert solve_part_one(1024) == 31

  puts "Part One: #{solve_part_one(INPUT_NUM)}"
  puts "Part Two: #{solve_part_two(INPUT_NUM)}"
end

main