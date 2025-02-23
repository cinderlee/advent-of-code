# Day 20: Particle Swarm

require "set"

INPUT_FILE_NAME = "./inputs/day20input.txt"

class Particle
  attr_reader :x, :y, :z
  
  def initialize(x:, y:, z:, vx:, vy:, vz:, ax:, ay:, az:)
    @x = x
    @y = y
    @z = z

    @vx = vx
    @vy = vy
    @vz = vz

    @ax = ax
    @ay = ay
    @az = az
  end

  def move
    @vx += @ax
    @vy += @ay
    @vz += @az

    @x += @vx
    @y += @vy
    @z += @vz
  end

  def manhattan_distance
    @x.abs() + @y.abs() + @z.abs()
  end

  def ==(other)
    @x == other.x && @y == other.y && @z == other.z
  end
end

# Reads a file and returns list of particle data 
def get_particles_data(file_nm)
  particles = []
  File.open(file_nm).each do |line|
    particle_info = line.chomp.split(", ")
    particle_pos = particle_info[0][3, particle_info[0].length - 4]
    particle_velocity = particle_info[1][3, particle_info[1].length - 4]
    particle_acc = particle_info[2][3, particle_info[2].length - 4]

    x, y, z = particle_pos.split(',').map { |val| val.to_i }
    vx, vy, vz = particle_velocity.split(',').map { |val| val.to_i }
    ax, ay, az = particle_acc.split(',').map { |val| val.to_i }

    particles << {
      x: x, y: y, z: z,
      vx: vx, vy: vy, vz: vz,
      ax: ax, ay: ay, az: az
    }
  end

  particles
end

# Converts a list of particles data (hashes) into list of Particle objects
def convert_to_particles(particles_data)
  particles_data.map do |particle_data| 
    Particle.new(
      x: particle_data[:x],
      y: particle_data[:y],
      z: particle_data[:z],
      vx: particle_data[:vx],
      vy: particle_data[:vy],
      vz: particle_data[:vz],
      ax: particle_data[:ax],
      ay: particle_data[:ay],
      az: particle_data[:az],
    )
  end
end

# Returns the particle that will stay closest to position <0,0,0> in the long term 
# determined by the Manhattan distance
def get_closest(particles)
  500.times do
    particles.each { |particle| particle.move }
  end

  distances = particles.map { |particle| particle.manhattan_distance }
  distances.find_index(distances.min)
end

# Simulate particles movement. If particles collide, they will be removed.
# Returns the number of particles remaining after all colliding particles have
# been removed
def simulate_particles(particles)
  1000.times do
    particles.each { |particle| particle.move }

    clashes = Set.new
    (0...particles.length - 1).each do |pos_one|
      (pos_one + 1...particles.length).each do |pos_two|
        if particles[pos_one] == particles[pos_two]
          clashes.add(pos_one)
          clashes.add(pos_two)
        end
      end
    end

    new_list = []
    particles.each_with_index { |item, index| new_list << item unless clashes.include?(index)}
    particles = new_list
  end

  particles.length
end

def solve_part_one(particles_data)
  particles = convert_to_particles(particles_data)
  get_closest(particles)
end

def solve_part_two(particles_data)
  particles = convert_to_particles(particles_data)
  simulate_particles(particles)
end

def main
  particles_data = get_particles_data(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(particles_data)}"
  puts "Part Two: #{solve_part_two(particles_data)}"
end

main