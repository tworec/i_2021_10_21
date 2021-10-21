#!/usr/bin/env python3

import random
import fileinput
import sys
import json
from find_missing import find_missing_from_short_array
from random_ import build_random_list_short_one_of_integers_from_zero_up_to_and_including






if __name__ == '__main__':
    # in: max last value or comma delimited list of numbers
    # out: a number from the theoretical complete sequence of numbers from 0 to and including max
    # pre: number list is originally a sequence of numbers from 0, excluding one member
    f_input = None
    line_decoded = None
    if len(sys.argv) !=1 and len(sys.argv) >2:
        print(len(sys.argv))
        print(f"usage: {sys.argv[0]} [ <maxvalue=1000> | <file or '-' for stdin> ]")
        print("note, file or stdin must contain a json array of a short list of values from a theoretical consecutive list starting from 0")
        print("e.g. '[0, 2, 3, 4, 5, 6, 7, 8, 9, 10]' is from a theoretical list of 11 elements including the missing 1")
        sys.exit(1)

    if len(sys.argv) == 1:
        maxval=1000
    else:
        maxval_argument=sys.argv[1]
        try:
            maxval=int(maxval_argument)
        except ValueError:
            maxval=None

    if not maxval:
        # input is a file not a max value number
        f_input = fileinput.input()

    # have maxval or f_input

    if not f_input: # just have maxval or default maxval but no other input, so, generate a random sequence sans 1 element
        random_integer_sequence_short_one = build_random_list_short_one_of_integers_from_zero_up_to_and_including(maxval)
        print(f"generated random array of numbers 0 and {maxval} inclusive ({maxval+1} elements) but removed an element at random")
    else:
        print("loading a json_array of values from ", end="")
        if sys.argv[1]=='-':
            print("stdin")
        else:
            print(f"file '{sys.argv[1]}'")

        line=next(f_input).rstrip("\r\n")
        try:
            line_decoded=json.JSONDecoder().decode(line)
        except json.decoder.JSONDecodeError:
            print(type(line))
            print("the input was not a valid json array")
            sys.exit(2)
        else:
            if not isinstance(line_decoded, list):
                print("the input was not a valid json array")
                sys.exit(3)

        random_integer_sequence_short_one = line_decoded

        print(f"Searching for missing element in list of length: {len(random_integer_sequence_short_one)}"
                f" with a presumed max value of {len(random_integer_sequence_short_one)}"
                f" in the theoretical inclusive sequence [0,{len(random_integer_sequence_short_one)}]"
                )

    if len(random_integer_sequence_short_one) <= 11:
        print(f"the search space is: {random_integer_sequence_short_one}")
    print(f"searching for missing element...", end="")
    missing_number=find_missing_from_short_array(random_integer_sequence_short_one) 
    print(f"found...{missing_number}")


