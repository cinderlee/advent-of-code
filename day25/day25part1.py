CARD_PUB_TEST_KEY = 5764801
DOOR_PUB_TEST_KEY = 17807724
CARD_PUB_KEY = 8252394
DOOR_PUB_KEY = 6269621
INITIAL_SUBJECT = 7

def get_loop_size(pub_key):
    value = 1
    loop_size = 0
    while value != pub_key:
        value = (value * INITIAL_SUBJECT) % 20201227
        loop_size += 1
    return loop_size

def get_encryption_key(loop_size, pub_key):
    encr_key = 1
    for i in range(loop_size):
        encr_key = (encr_key * pub_key) % 20201227
    return encr_key

def solve(card_pub_key, door_pub_key):
    card_loop_size = get_loop_size(card_pub_key)
    door_loop_size = get_loop_size(door_pub_key)

    encryption_key = get_encryption_key(card_loop_size, door_pub_key)
    encryption_check_key = get_encryption_key(door_loop_size, card_pub_key)

    assert(encryption_key == encryption_check_key)
    return encryption_key

def main():
    assert(solve(CARD_PUB_TEST_KEY, DOOR_PUB_TEST_KEY) == 14897079)
    print(solve(CARD_PUB_KEY, DOOR_PUB_KEY))

main()