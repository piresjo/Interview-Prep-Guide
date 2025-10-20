# Notes On Hashing

- Whether worst or average case, space will always be `O(n)` complexity.
- In the worst case, insert, search, and delete are all `O(n)` complexity
- However, in the average case, it's constant

Most hashing functions have collisions in buckets. With linear probing, a significanty large enough number of collisions will kill performance

More efficient than search trees

Need hash function to best distribute values and prevent collisions

Load factor: `n/k` (`n` refers to number of entries and `k` refers to number of buckets). The larger the factor, the worse the performance.

## Links
