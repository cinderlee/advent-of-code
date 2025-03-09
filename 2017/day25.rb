# Day 25: The Halting Problem

def main
  state = 'A'
  current_slot = 0

  slots = {
    0 => 0
  }

  # Translated day 25 input
  12964419.times do 
    next_state = ''
    case state
    when 'A'
      value = slots.fetch(current_slot, 0)
      slots[current_slot] = value == 0 ? 1 : 0
      current_slot += 1
      next_state = value == 0 ? 'B' : 'F'
    when 'B'
      value = slots.fetch(current_slot, 0)
      current_slot -= 1
      next_state = value == 0 ? 'B' : 'C'
    when 'C'
      value = slots.fetch(current_slot, 0)
      slots[current_slot] = value == 0 ? 1 : 0
      current_slot = value == 0 ? current_slot - 1 : current_slot + 1
      next_state = value == 0 ? 'D' : 'C'
    when 'D'
      value = slots.fetch(current_slot, 0)
      slots[current_slot] = 1
      current_slot = value == 0 ? current_slot - 1 : current_slot + 1
      next_state = value == 0 ? 'E' : 'A'
    when 'E'
      value = slots.fetch(current_slot, 0)
      slots[current_slot] = value == 0 ? 1 : 0
      current_slot -= 1
      next_state = value == 0 ? 'F' : 'D'
    when 'F'
      value = slots.fetch(current_slot, 0)
      slots[current_slot] = value == 0 ? 1 : 0
      current_slot = value == 0 ? current_slot + 1 : current_slot - 1
      next_state = value == 0 ? 'A' : 'E'
    end

  state = next_state
  end

  puts "Part One: #{slots.values.to_a.count(1)}"
end

main