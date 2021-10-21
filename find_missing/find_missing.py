
def find_missing_from_short_array(short_array):
# pre: short array is a "subset" from a "set" of integers from 0 to some value inclusive
# with a cardinality of -1 vs the original set
# inputs:                               process:                                  output
# array with missing (short_array)      candidate=*short_array                   candidate as missing
#                                       [ candidate in short_array ] continue


    def test_candidate_in_array(candidate, thearray):
        # iterate over array until either end or number seen
        result=False # number not seen yet
        offset=0
        thearraylen = len(thearray)
        while result==False and offset < thearraylen:
            if candidate == thearray[offset]:
                result=True
            else:
                offset+=1
        return result


    candidate=0
    identified_missing=False
    short_array_len = len(short_array)
    while candidate < short_array_len and not identified_missing:
        if not test_candidate_in_array(candidate, short_array):
            identified_missing=True
        else:
            candidate+=1

    return candidate

