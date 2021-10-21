#!/usr/bin/env python3
import json

from random_ import build_random_list_short_one_of_integers_from_zero_up_to_and_including

import sys
# generate a random json array of 1000 numbers and write to the specified file

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <output-file>")
    sys.exit(1)

print(f"Shuffling a random sequence of 0 to 1000 excluding one random element and writing to {sys.argv[1]}")
randomized_sequence_less_1 = build_random_list_short_one_of_integers_from_zero_up_to_and_including(1000)
as_json=json.JSONEncoder().encode(randomized_sequence_less_1)
print(as_json)
with open(sys.argv[1], mode="w+") as f:
    f.write(str(as_json))
