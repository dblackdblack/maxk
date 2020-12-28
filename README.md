read a file of ints and print out the greatest K ints from that file.

assumptions:
1. our random "number" is a random int, not a random float. It's trivial to switch to floats but you get into weird edge cases comparing floats and imperfect precision for storing floating point numbers when the two numbers you're comparing are very together.
1. We care about *distinct* top-K numbers.  I perform a de-dupe by doing a set lookup before adding to the heap.  If we don't care about de-duping, it is trivial to remove that check. But it makes the output slightly less interesting when you're generating a long list of random ints and you end up getting the same value K times in the top-K list.


Example usage:
1. `docker build --tag=maxk .`
1. `docker run --rm -ti maxk bash`

Inside of the docker container (step 2 above):
1. `python3 maxk.py -k 3 ints.txt`  # print out top 3 elements from ints.txt
1. `sort -nru ints.txt | head -n 3`  # verify that the top 3 elements are correct using `sort`
1. `pytest` # tests both max-K as well as flatten
