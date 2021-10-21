import random

def build_random_list_short_one_of_integers_from_zero_up_to_and_including(maxval):

    ordered_list = [ num for num in range(maxval+1) ] # inclusive of maxvalue
    return random.sample(ordered_list, maxval) # since maxval is from a zero based list this implies short one

