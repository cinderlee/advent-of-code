# Day 22: Sporifica Virus

INPUT_FILE_NAME = "./inputs/day22input.txt"

DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def get_nodes(file_nm)
  row_num = 0
  nodes = []
  File.open(file_nm).each do |line|
    nodes << line.chomp.split("")
  end

  center_row = nodes.length / 2
  center_col = nodes[0].length / 2
  [nodes, center_row, center_col]
end

# Converts 2D-list of nodes into a mapping
# Each node key is represented by [node row, node column]
# Each value is converted into 'C' (for clean - .) or 'I' (for infected - #)
def convert_nodes_to_map(nodes)
  nodes_map = {}
  nodes.each_with_index do |row, row_index|
    row.each_with_index do |node_value, col_index|
      nodes_map[[row_index, col_index]] = node_value == '.' ? 'C' : 'I'
    end
  end
  nodes_map
end

# Returns the next node value
# If visiting evolved node
# - a cleaned node will become weakened
# - a weakened node will become infected
# - an infected node will become flagged
# - a flagged node will become clean
# Otherwise, a clean node will become infected and an infected node will become clean.
def next_node_value(node_val, is_evolved_node = false)
  case node_val
  when 'C'
    is_evolved_node ? 'W' : 'I'
  when 'W'
    'I'
  when 'I'
    is_evolved_node ? 'F' : 'C'
  when 'F'
    'C'
  else
    ''
  end
end

# Returns next virus direction
# If the virus is on
# - a clean node, it will turn left
# - a weakened node, it will not turn
# - an infected node, it will turn right
# - a flagged node, it will reverse direction
def get_next_virus_direction(node_val, current_direction)
  virus_direction = current_direction
  current_direction_index = DIRECTIONS.find_index(virus_direction)
  case node_val
  when 'C'
    next_direction_index = current_direction_index - 1
    virus_direction = DIRECTIONS[next_direction_index]
  when 'I'
    next_direction_index = (current_direction_index + 1) % DIRECTIONS.length
    virus_direction = DIRECTIONS[next_direction_index]
  when 'F'
    virus_direction = virus_direction.map { |dir| dir * -1 }
  end

  virus_direction
end

# Returns the number of nodes that were infected after n number of bursts
# The virus starts in the middle of the map facing up. During each burst,
# the virus will convert the current node and then move in the next direction depending
# on the current node value.
def simulate_bursts(num_bursts, nodes_information, has_evolved_nodes = false)
  infected_count = 0
  nodes, virus_position_row, virus_position_col = nodes_information
  node_mappings = convert_nodes_to_map(nodes)
  virus_direction = DIRECTIONS[0]
  num_bursts.times do 
    node_value = node_mappings.fetch([virus_position_row, virus_position_col], 'C')
    new_node_value = next_node_value(node_value, has_evolved_nodes)
    node_mappings[[virus_position_row, virus_position_col]] = new_node_value

    if (new_node_value == 'I')
      infected_count += 1
    end

    virus_direction = get_next_virus_direction(node_value, virus_direction)
    virus_position_row += virus_direction[0]
    virus_position_col += virus_direction[1]
  end

  infected_count
end

def solve_part_one(nodes_information)
  simulate_bursts(10000, nodes_information)
end

def solve_part_two(nodes_information)
  simulate_bursts(10000000, nodes_information, true)
end

def main
  nodes_information = get_nodes(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(nodes_information)}"
  puts "Part Two: #{solve_part_two(nodes_information)}"
end

if __FILE__==$0
  main
end