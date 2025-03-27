# CMPS 2200 Reciation 5
## Answers

**Name:** Lulu Sawaf


Place all written answers from `recitation-05.md` here for easier grading.

|      n |   qsort-fixed-pivot |   qsort-random-pivot |   tim_sort |
|--------|---------------------|----------------------|------------|
|    100 |               0.133 |                0.152 |      0.010 |
|    200 |               0.159 |                0.213 |      0.014 |
|    500 |               0.479 |                0.592 |      0.039 |
|   1000 |               1.047 |                1.412 |      0.131 |
|   2000 |               2.222 |                2.802 |      0.187 |
|   5000 |               6.036 |                8.956 |      0.567 |
|  10000 |              12.998 |               16.573 |      1.253 |
|  20000 |              27.351 |               33.859 |      2.576 |
|  50000 |              77.143 |               88.521 |      7.576 |
| 100000 |             174.074 |              197.214 |     15.551 |



1b)

pre sorted quicksort vs. random quicksort:
Both variants have similar performance for small lists (n ≤ 1000).
For larger lists (n ≥ 5000), the pre sorted version is slightly faster than the random version.
This suggests that random shuffling (done in compare_sort) helps avoid worst-case behavior for pre sorted Quicksort.
If the input were already sorted, pre sorted Quicksort would changeto O(n²), while random would remain O(n log n).

Quicksort vs. Timsort (sorted):
Timsort is significantly faster than both Quicksort variants.
At n=100,000, Timsort takes 15.551 ms, while fixed-pivot Quicksort takes 174.074 ms (~10× slower).
This aligns with expectations since Timsort is a hybrid algorithm (of merge sort + insertion sort) optimized for real-world data.

ssort:
Not in the table, but if it was, it would be much slower (O(n²) even for small n).
So for n=1000, Quicksort takes ~1 ms, while ssort would take ~100x longer (~100 ms).

Comparison for Different Input Types:
Input Types:	pre sorted, random, ssort
Random Permutation	O(n log n) avg.	O(n log n) avg.	O(n²) (always)
Already Sorted	O(n²) (worst-case)	O(n log n) avg.	O(n²) (always)
Pre sorted quicksort performs poorly on sorted inputs (degenerates to O(n²)).
Random quicksort maintains O(n log n) due to randomized pivot selection.
Selection Sort is always O(n²), making it impractical for large n.

1c)
Timsort (sorted) is consistently faster than both quicksorts.
At n=100, timsort is 11× faster than pre sorted quicksort (0.010 ms vs. 0.133 ms).
At n=100,000, timsort is 10× faster (15.551 ms vs. 174.074 ms).

Timsort outperforms quicksort because it is-
  Adaptive: Timsort exploits existing order in data (e.g., nearly sorted lists).
  Hybrid Approach: Combines merge sort (for large chunks) + insertion sort (for small chunks).
  Optimized for Real Data: Unlike Quicksort, it avoids worst-case scenarios.
  Performance Comparison (Random vs. Sorted Inputs):

Pre sorted quicksort	O(n log n)	O(n²)	Degrades on sorted input.
Random quicksort	O(n log n)	O(n log n)	Robust due to randomization.
Timsort (sorted)	O(n log n)	O(n) (best-case)	Excels on nearly-sorted data.
Timsort is the clear winner in both random and sorted cases.
Quicksort (random) is a good general-purpose alternative but still slower than timsort.