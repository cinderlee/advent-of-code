# Day 23: Coprocessor Conflagration

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_FILE_NAME = "./inputs/day20input.txt"

def get_paths(file_nm)
  # Reads a file and returns the paths after 100 turns

  line_num = 0

  paths = {}
  File.open(file_nm).each do |line|
    path_info = line.chomp.split(", ")
    path_pos = path_info[0][3, path_info[0].length - 4]
    path_velocity = path_info[1][3, path_info[1].length - 4]
    path_acc = path_info[2][3, path_info[2].length - 4]

    x, y, z = path_pos.split(',').map { |val| val.to_i }
    vx, vy, vz = path_velocity.split(',').map { |val| val.to_i }
    ax, ay, az = path_acc.split(',').map { |val| val.to_i }
    
  # x + vx + n/2 * (n-1) * ax = x1 + vx1 + (n/2 * (n-1) * ax1) 

  #  x1 + vx1 - x - vx = n/2 * n-1 (ax - ax1)  
    #  next_x = x + vx + (500 / 2 * (500-1) * ax)
    #  next_y = y + vy + (500 / 2 * (500-1) * ay)
    #  next_z = z + vz + (500 / 2 * (500-1) * az)
     paths[line_num] = {
      x: x, y: y, z: z,
      vx: vx, vy: vy, vz: vz,
      ax: ax, ay: ay, az: az
    }
      # p paths
      line_num += 1
  end

  paths
end

def get_closest(paths)
  distance = nil
  path = nil
  paths.each do |path_num, location|
    future_x = location[:x] + location[:vx] + (500 / 2 * (500-1) * location[:ax])
    future_y = location[:y] + location[:vy] + (500 / 2 * (500-1) * location[:ay])
    future_z = location[:z] + location[:vz] + (500 / 2 * (500-1) * location[:az])
    dist = future_x.abs() + future_y.abs() + future_z.abs()
    if distance.nil?
      distance = dist
      path = path_num
    elsif dist < distance 
      distance = dist
      path = path_num
    end
  end
  p path
  p distance
  path 
end

def remove_overlaps(paths)
  remove = []
  num_paths = paths.length

  (0...num_paths).each do |path_num|
    (path_num + 1...num_paths) do |path_num_2|
      path1 = paths[path_num]
      path2 = paths[path_num_2]
    end
  end
end

def main
  paths = get_paths(INPUT_FILE_NAME)
  p get_closest(paths)
  # puts "Part One: #{solve_part_one(registers, instructions)}"
  # puts "Part Two: #{solve_part_two}"
end

main