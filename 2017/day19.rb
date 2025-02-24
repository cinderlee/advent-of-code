# Day 19: A Series of Tubes

INPUT_FILE_NAME = "./inputs/day19input.txt"

# Reads a file and returns the routing diagram for the network packet
# in the form of a nested array
def get_routing_diagram(file_nm)
  map = []
  File.open(file_nm).each do |line|
    map_row = line.chomp.split("")
    map << map_row
  end
  map
end

# Checks whether a character is a letter (uppercase only)
def is_alpha?(character)
  ("A".."Z").include?(character)
end

# Checks whether given row and col are valid positions in the routing digram
def is_within_diagram_bounds(row, col, routing_diagram)
  row >= 0 &&
  col >= 0 &&
  row < routing_diagram.length &&
  col < routing_diagram[0].length
end

# Traces the path the network packet will take and tracks the letters
# the packet will see. 
#
# The network packet will only turn a different direction if there is no other option
# Returns list of characters seen and number of steps taken to reach the end
def trace(routing_diagram)
  dir_row = 1
  dir_col = 0

  pos_row = 0
  pos_col = routing_diagram[0].find_index("|")

  characters = []
  steps = 0

  while (is_within_diagram_bounds(pos_row, pos_col, routing_diagram)) 
    if routing_diagram[pos_row][pos_col] == " "
      break
    end
  
    steps += 1
    characters << routing_diagram[pos_row][pos_col] if is_alpha?(routing_diagram[pos_row][pos_col])
     
    if routing_diagram[pos_row][pos_col] == "+"
      if dir_row.abs() == 1
        dir_row = 0
        dir_col = routing_diagram[pos_row][pos_col - 1] != " " ? -1 : 1
      else
        dir_col = 0
        dir_row = is_within_diagram_bounds(pos_row + 1, pos_col, routing_diagram) &&
          routing_diagram[pos_row + 1][pos_col] != " " ? 1 : -1
      end
    end
    pos_row += dir_row
    pos_col += dir_col
  end
  
  [characters, steps]
end

def main
  routing_diagram = get_routing_diagram(INPUT_FILE_NAME)
  characters, steps = trace(routing_diagram)
  
  puts "Part One: #{characters.join("")}"
  puts "Part Two: #{steps}"
end

if __FILE__==$0
  main
end