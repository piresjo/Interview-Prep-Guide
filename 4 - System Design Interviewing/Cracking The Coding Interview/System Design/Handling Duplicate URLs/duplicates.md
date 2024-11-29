
## Question

> You have 10 billion urls. How do you detect duplicate URLs?

### Background Info

Assuming an average URL is 100 chars long, and the average character is four bytes, we're looking at a total of four terabytes of data.

With that in mind, our solution is based off what we assume about how this is stored. We can't store a 4 TB file into memory. So we'll need to split this file into chunks (4000 to be specific). We can do this by putting them into one of the many chunks we've allocated (what chunk the url goes to is based on the hash of the url mod 4000; similar or same urls will then be in the same file because the hash value is the same)

### Solution 1
This solution involves those chunks being a 1 GB file. The first pass we do is to separate the urls into their appropriate file, based off the hash value modulo 4000. Then, for each file, we load it into memory, and look for duplicates (hash table would be a good idea)

### Solution 2
This solution involves us allocating 4000 different machines. Each url will be organized into one of the machines based off its hash value modulo 4000. Each machine, in parallel, can then set up a hash table, and look for duplicates.

However, we now need to worry about if one of the machines fails. We'll need to have a lookup table mapping the machine being used to what (hash % 4000) it was tasked to do. We might need this lookup table in multiple machines, in case one of the machines that has the lookup table fails as well. Then, we can just have a working machine also handle the urls with the same (hash % 4000) value.

### Analysis

In terms of reliability, solution 1 is the better solution, due to there being fewer parts that can break (1 machine vs. 4000 machines). In solution 2, we have to factor in what happens if one of the machines fail (in our case, just have one of the working ones do the check). We'll also need a lookup table mapping machine to the (hash % 4000) value.

In terms of speed, however, solution 2 would be the better solution. Since you're parallelizing the process, potentially all 4000 chunks get processed at once.
