# Day 13: Packet Scanners

INPUT_FILE_NAME = "./inputs/day13input.txt"

# Reads a file and returns a list representing the firewall
# ranges for scanners at each depth (index represents the depth)
def get_firewall_info(file_nm)
  firewall_scanner_range = []
  File.open(file_nm).each do |line|
    layer_info = line.chomp.split(": ")
    firewall_scanner_range[layer_info[0].to_i] = layer_info[1].to_i
  end
  return firewall_scanner_range
end

# Returns the trip severity from a packet traversing through the firewall
# layers. The severity is the sum of the product of depth and ranges
# where the packet would get caught.

# How traversal works per picosecond:
# The packet moves a layer forward and then the scanners at each layer 
# move (moves back and forth from ends of range). The packet is caught
# if the packet moves when the scanner is at the top of the layer. 
def get_trip_severity(firewall_scanner_range)
  severity = 0
  firewall_scanner_range.each_with_index do |range, depth|
    # The scanner is at the top of the layer every (range - 1) * 2 picoseconds
    next if range.nil?
    scanner_position = depth % ((range - 1) * 2)
    severity += depth * range if scanner_position == 0
  end
  severity
end

# Returns the number of picoseconds to delay by for a packet to 
# successfully pass through the firewall undetected

# How traversal works per picosecond:
# The packet moves a layer forward and then the scanners at each layer 
# move (moves back and forth from ends of range). The packet is caught
# if the packet moves when the scanner is at the top of the layer. 
def get_num_delayed_seconds_for_success(firewall_scanner_range)
  num_delayed_seconds = 1
  
  while true
    is_caught = false
    firewall_scanner_range.each_with_index do |range, depth|
      next if range.nil?
      scanner_position = (num_delayed_seconds + depth) % ((range - 1) * 2)
      if scanner_position == 0
        is_caught = true
        break
      end
    end
  
    return num_delayed_seconds unless is_caught
    num_delayed_seconds += 1
  end
end

def solve_part_one(firewall_scanner_range)
  get_trip_severity(firewall_scanner_range)
end

def solve_part_two(firewall_scanner_range)
  get_num_delayed_seconds_for_success(firewall_scanner_range)
end

def main
  firewall_scanner_range = get_firewall_info(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(firewall_scanner_range)}"
  puts "Part Two: #{solve_part_two(firewall_scanner_range)}"
end

if __FILE__==$0
  main
end