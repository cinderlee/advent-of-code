# Day 17: Spinlock

SPINLOCK_STEP = 303
PART_ONE_NUM_TIMES = 2017
PART_TWO_NUM_TIMES = 50_000_000

class Node
  attr_accessor :next
  attr_reader :value

  def initialize(value, nextNode)
    @value = value
    @next = nextNode
  end
end

class CircularBuffer
  def initialize(step)
    @length = 2
    @step = step

    # initialize linked list buffer array with 2 starting values [0, 1]
    second_node = Node.new(1, nil)
    @start = Node.new(0, second_node)
    second_node.next = @start
  end

  # The spinlock algorithm starts with a circular buffer which has 0, 1, with current position at 1.
  # Each turn of the spinlock (supposedly starts with [0]) steps forward # of steps and inserts 
  # the next value. 
  # The position of the next value is the current position for the next turn. 
  def spinlock(num_times)
    # start at 1
    current_node = @start.next

    (2..num_times).each do |number|
      step_forward = @step % @length
      step_forward.times { current_node = current_node.next }
      
      number_node = Node.new(number, current_node.next)
      current_node.next = number_node
      current_node = number_node
      @length = @length + 1
    end
  end

  # Returns the value that is after the specified number in the buffer
  def get_value_after(number)
    current_node = @start 
    @length.times do
      return current_node.next.value if current_node.value == number
      current_node = current_node.next
    end
  end
end

# Returns the value after the final spinlock number
def solve_part_one(spinlock_times, step)
  buffer = CircularBuffer.new(step)
  buffer.spinlock(spinlock_times)
  buffer.get_value_after(spinlock_times)
end

# The spinlock algorithm starts with a circular buffer which has 0, 1, with current position at 1.
# Each turn of the spinlock (supposedly starts with [0]) steps forward # of steps and inserts 
# the next value. 
# The position of the next value is the current position for the next turn. 

# Returns the value after 0
def solve_part_two(spinlock_times)
  # start at 1
  zero_location = 0
  next_number_after_zero = 1
  curr_length = 2
  curr_loc = 1

  (2..spinlock_times).each do |number|
    next_loc = (curr_loc + SPINLOCK_STEP) % curr_length

    # update the number that is after 0
    if next_loc == zero_location
      next_number_after_zero = number
    end

    curr_loc = next_loc + 1
    curr_length = curr_length + 1
  end
  
  next_number_after_zero
end

def main
  puts "Part One: #{solve_part_one(PART_ONE_NUM_TIMES, SPINLOCK_STEP)}"
  puts "Part Two: #{solve_part_two(PART_TWO_NUM_TIMES)}"
end

main
