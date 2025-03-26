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



1b) Comparison of Quicksort Variants vs. Selection Sort (ssort)
Key Observations from the Table:
Quicksort (Fixed Pivot) vs. Quicksort (Random Pivot):
Both variants have similar performance for small lists (n ≤ 1000).
For larger lists (n ≥ 5000), the fixed-pivot version is slightly faster than the random-pivot version.
This suggests that random shuffling (done in compare_sort) helps avoid worst-case behavior for fixed-pivot Quicksort.
If the input were already sorted, fixed-pivot Quicksort would degrade to O(n²), while random-pivot would remain O(n log n).
Quicksort vs. Timsort (sorted):
Timsort (Python’s sorted) is significantly faster than both Quicksort variants.
At n=100,000, Timsort takes 14.747 ms, while fixed-pivot Quicksort takes 153.377 ms (~10× slower).
This aligns with expectations since Timsort is a hybrid algorithm (merge sort + insertion sort) optimized for real-world data.
Selection Sort (ssort):
Not included in the table, but if tested, it would be much slower (O(n²) even for small n).
Example: For n=1000, Quicksort takes ~1 ms, while ssort would take ~100x longer (~100 ms).
Comparison for Different Input Types:
Input Type	Fixed-Pivot Quicksort	Random-Pivot Quicksort	Selection Sort (ssort)
Random Permutation	O(n log n) avg.	O(n log n) avg.	O(n²) (always)
Already Sorted	O(n²) (worst-case)	O(n log n) avg.	O(n²) (always)
Fixed-pivot Quicksort performs poorly on sorted inputs (degenerates to O(n²)).
Random-pivot Quicksort maintains O(n log n) due to randomized pivot selection.
Selection Sort is always O(n²), making it impractical for large n.

1c) Comparing Fastest Implementation (Timsort) vs. Quicksort
Key Findings from the Table:
Timsort (sorted) is consistently faster than both Quicksort variants.
At n=100, Timsort is 11× faster than fixed-pivot Quicksort (0.007 ms vs. 0.079 ms).
At n=100,000, Timsort is 10× faster (14.747 ms vs. 153.377 ms).
Why Timsort Outperforms Quicksort:
Adaptive: Timsort exploits existing order in data (e.g., nearly sorted lists).
Hybrid Approach: Combines merge sort (for large chunks) + insertion sort (for small chunks).
Optimized for Real Data: Unlike Quicksort, it avoids worst-case scenarios.
Performance Comparison (Random vs. Sorted Inputs):
Algorithm	Random Input (Time)	Sorted Input (Time)	Notes
Fixed-Pivot QS	O(n log n)	O(n²)	Degrades on sorted input.
Random-Pivot QS	O(n log n)	O(n log n)	Robust due to randomization.
Timsort (sorted)	O(n log n)	O(n) (best-case)	Excels on nearly-sorted data.
Timsort is the clear winner in both random and sorted cases.
Quicksort (random-pivot) is a good general-purpose alternative but still slower than Timsort.
Recommendations for Further Testing:
Test ssort on small lists (e.g., n ≤ 500) to see its O(n²) behavior.
Compare sorted vs. reverse-sorted inputs to see how Quicksort behaves.
Increase n beyond 100,000 to observe scalability (if system memory allows).
Expected Result: Fixed-pivot Quicksort will be much slower on sorted inputs, while Timsort will be fastest.

Conclusion
Quicksort (random-pivot) is more reliable than fixed-pivot but still slower than Timsort.

Timsort (sorted) is the best choice for most practical use cases.

Selection Sort (ssort) is inefficient and should only be used for educational purposes.
