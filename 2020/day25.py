# Day 25: Combo Breaker

CARD_PUB_TEST_KEY = 5764801
DOOR_PUB_TEST_KEY = 17807724
CARD_PUB_KEY = 8252394
DOOR_PUB_KEY = 6269621
INITIAL_SUBJECT = 7

def get_loop_size(pub_key):
    '''
    The handshake operation transforms a subject number. 
    Steps:
        start at value of 1
        repeat number of times (loop size):
            set the value to itself multiplied by subject number
            set the value to remainder from dividing by 20201227

    Returns the loop size given a public key
    '''
    value = 1
    loop_size = 0
    while value != pub_key:
        value = (value * INITIAL_SUBJECT) % 20201227
        loop_size += 1
    return loop_size

def get_encryption_key(loop_size, pub_key):
    '''
    Returns the encryption key given a loop size and a public key.

    Note:
    The card transforms the door's public key using the card's loop size.
    The door transforms the card's public key using the door's loop size.
    '''
    encr_key = 1
    for i in range(loop_size):
        encr_key = (encr_key * pub_key) % 20201227
    return encr_key

def solve_part_one(card_pub_key, door_pub_key):
    '''
    Reverse engineer cryptographic handshake and return encryption key.
    '''
    card_loop_size = get_loop_size(card_pub_key)
    door_loop_size = get_loop_size(door_pub_key)

    encryption_key = get_encryption_key(card_loop_size, door_pub_key)
    encryption_check_key = get_encryption_key(door_loop_size, card_pub_key)

    assert(encryption_key == encryption_check_key)
    return encryption_key

def main():
    assert(solve_part_one(CARD_PUB_TEST_KEY, DOOR_PUB_TEST_KEY) == 14897079)
    print('Part One:', solve_part_one(CARD_PUB_KEY, DOOR_PUB_KEY))

main()