# raffle_picker_blockchain

Picks a random number based on the hash of the latest block on the bitcoin blockchain

## Install

Requires python3 and pip3
Install dependencies like this:
```sh
pip install -r requirements.txt
```

## Usage

```sh
python3 raffle_picker_blockchain.py 100

Block Time:
2019-03-15 09:49:49

Hash (hex): 00000000000000000017a074e2a049863684fcc977ed1c8199cbfb5c4c2c3747
Hash (int): 2262996275056157707289898579720968612408508058925020999
Result (hash%100): 99
```
