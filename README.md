# i_2021_10_21
# linear complexity missing number search

this project implements a linear time complexity search, with constant memory complexity, for a missing number in an array. the max search time grows linearly (1:1) with the size of the array being searched.

the algorithm is defined in find_missing/find_missing.py::find_missing_from_short_array

## a test set is included in the root directory, which can be run against the find_missing_from_short_array function as follows
```
krunch3r@ubuntu:~/i_2021_10_21$ ./go.py testlist1
loading a json_array of values from file 'testlist1'
Searching for missing element in list of length: 1000 with a presumed max value of 1000 in the theoretical inclusive sequence [0,1000]
searching for missing element...found...937
krunch3r@ubuntu:~/i_2021_10_21$ 
```

## the result may be confirmed with the following:
```
krunch3r@ubuntu:~/i_2021_10_21$ NUM=937; egrep "\<$NUM\>" testlist1; [[ $? = 1 ]] && echo "$NUM is the missing number!"
937 is the missing number!
krunch3r@ubuntu:~/i_2021_10_21$ 
```

## to generate a new test set and test:
```
krunch3r@ubuntu:~/i_2021_10_21$ ./generate_testlist.py testlist2
Shuffling a random sequence of 0 to 1000 excluding one random element and writing to testlist2
[468, 984, 239, 591, 645, 555, 27, 17, 306, 466, 511, 820, 434, 567, 758, 441, 51, 234, 448, 409, 975, 487, 539, 78, 89, 940, 954, 498, 186, 880, 969, 617, 696, 687, 750, 424, 399, 910, 538, 510, 367, 308, 817, 273, 786, 40, 184, 716, 263, 171, 616, 900, 204, 871, 683, 65, 618, 838, 384, 307, 576, 881, 68, 245, 143, 682, 823, 521, 442, 259, 782, 561, 600, 278, 189, 846, 153, 425, 684, 62, 776, 265, 50, 122, 292, 995, 614, 382, ...

krunch3r@ubuntu:~/i_2021_10_21$ ./go.py testlist2
loading a json_array of values from file 'testlist2'
Searching for missing element in list of length: 1000 with a presumed max value of 1000 in the theoretical inclusive sequence [0,1000]
searching for missing element...found...274

krunch3r@ubuntu:~/i_2021_10_21$ NUM=274; egrep "\<$NUM\>" testlist2; [[ $? = 1 ]] && echo "$NUM is the missing number!"
274 is the missing number!
```

## to test from the command line given a json array of numbers, pipe in via the - argument. ensure the set is from a theoretical set of 0 to maxval inclusive.
```
# suppose a theoretical set from 0 to 10 inclusive (11 elements originally)
krunch3r@ubuntu:~/i_2021_10_21$ echo "[0, 1, 2, 4, 5, 6, 7, 8, 9, 10]" | ./go.py -
loading a json_array of values from stdin
Searching for missing element in list of length: 10 with a presumed max value of 10 in the theoretical inclusive sequence [0,10]
the search space is: [0, 1, 2, 4, 5, 6, 7, 8, 9, 10]
searching for missing element...found...3
