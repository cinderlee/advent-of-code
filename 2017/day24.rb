# Day 24: Electromagnetic Moat

INPUT_FILE_NAME = "./inputs/day24input.txt"

# Gets list of magentic components that can be used to build the bridge
def get_magenetic_components(file_nm)
  nodes = []
  File.open(file_nm).each do |line|
    nodes << line.chomp.split("/").map { |num_string| num_string.to_i }
  end

  nodes
end

# Get list of magentic components that could be the start of the bridge
# The first port must of be of type 0
def get_start_components(components)
  components.select { |component| component.include?(0) }
end

def get_strongest_and_longest_bridge(bridges)
  longest_bridge_length = bridges.map{ |bridge| bridge[1] }.max
  max_bridge_strength = bridges
    .select { |bridge| bridge[1] == longest_bridge_length }
    .map { |bridge| bridge[0] }.max
  [max_bridge_strength, longest_bridge_length]
end

def build_strongest_bridge(component_options, last_port_number, find_longest = false)
  possible_next_components = component_options.select { |component| component.include?(last_port_number) }

  if possible_next_components.length == 0
    # return [strength total, bridge length]
    return [0, 0]
  end

  # map next components to resulting sub bridge built from that component
  possible_sub_bridges = possible_next_components.map do |next_component|
    next_last_port_number = last_port_number == next_component[0] ? next_component[1] : next_component[0]
    remaining_components_options = component_options.reject { |option| option == next_component }
    sub_bridge_details = build_strongest_bridge(remaining_components_options, next_last_port_number, find_longest)
    [sub_bridge_details[0] + next_component.sum, sub_bridge_details[1] + 1]
  end

  # determine which sub bridge has the greatest strength
  # if find longest is true, finds the strongest and longest sub bridge
  if find_longest
    get_strongest_and_longest_bridge(possible_sub_bridges)
  else
    max_sub_bridge_strength = possible_sub_bridges.map { |bridge| bridge[0] }.max
    possible_sub_bridges.find { |bridge| bridge[0] == max_sub_bridge_strength}
  end
end

# Returns list of possible strong bridges that can be built from initial list of components
# First component must be able to connect to zero-pin port
def get_possible_strongest_bridges(components, find_longest = false)
  get_start_components(components).map do |start_node|
    last_port_number = start_node[0] == 0 ? start_node[1] : start_node[0]
    component_options = components.reject { |component| component == start_node }
    bridge = build_strongest_bridge(component_options, last_port_number, find_longest)
    [bridge[0] + start_node.sum, bridge[1] + 1]
  end
end

def solve_part_one(components)
  bridges = get_possible_strongest_bridges(components)
  bridges.map { |bridge| bridge[0] }.max
end

def solve_part_two(components)
  bridges = get_possible_strongest_bridges(components, true)
  get_strongest_and_longest_bridge(bridges)[0]
end

def main
  components = get_magenetic_components(INPUT_FILE_NAME)

  puts "Part One: #{solve_part_one(components)}"
  puts "Part Two: #{solve_part_two(components)}"
end

if __FILE__==$0
  main
end