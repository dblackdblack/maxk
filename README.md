read a file of ints and print out the greatest K ints from that file.


Example usage:
1. `docker build --tag=maxk .`
1. `docker run --rm -ti maxk bash`

Inside of the docker container (step 2 above):
1. `perl -e "for(0..10000){print int(rand(2**32)).\"\n\"}" > ints.txt`  # 10,000 random ints into ints.txt
1. `python3 maxk.py -k 3 ints.txt`  # print out top 3 elements from ints.txt
1. `sort -nru ints.txt | head -n 3`  # verify that the top 3 elements are correct using `sort`
