from os.path import basename
import sys
import datetime
from blockchain.blockexplorer import get_latest_block

if __name__ == "__main__":
    try:
        number_of_raffles = int(sys.argv[1])
    except:
        print('Wrong arguments!')
        print('Usage: {} number_of_raffles'.format(sys.argv[0]))
        exit(1)
    block = get_latest_block()
    print('Block Time:')
    print(datetime.datetime.fromtimestamp(block.time))
    print('')
    hash_str = block.hash
    print('Hash (hex): {}'.format(hash_str))
    hash_int = int(block.hash, 16)
    print('Hash (int): {}'.format(hash_int))
    hash_mod = hash_int%number_of_raffles
    print('Result (hash%{}): {}'.format(number_of_raffles, hash_mod))
