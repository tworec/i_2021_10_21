
def find_missing_from_short_array(short_array):
# pre: short array is a "subset" or 1-short-list from a "set" of integers
#  from a domain of consecutive integers 0 to some max value inclusive
#  with a cardinality of -1 vs the original set
#
# inputs:                               process:                                  output
# array with missing (short_array)      candidate=*[0,len(short_array)]           candidate as missing
#                                       [ candidate in short_array ] continue

# comments: the maxval is implied by the cardinality (n) of the short array, or (N-1), b/c it is a from a zero based list of len N
# e.g. original [ 1, 0, 2, 4, 3, 5 ] len=6, note maxvalue=5
# remove '0' [ 1, 2, 4, 3, 5 ] len=5 corresponding to max value
# or remove '5' [ 1, 0, 2, 4, 3 ] len=5 &c.
# the instruction count is defined linearly by n + f(n-1) + 1 where f(1)=2 and n is the number of elements in the short list

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


def find_missing_number_linear(array):
    for i, _ in enumerate(array):
        if i not in array:
            return i
    return len(array)


def find_missing_number_by_sum(array):
    n = len(array)
    # total_sum = n * (n+1) / 2
    # array_sum = 0
    # for i in array:
    #     array_sum += i
    #
    # return int(total_sum - array_sum)

    # shorter version
    return (n * (n+1)) // 2 - sum(array)

