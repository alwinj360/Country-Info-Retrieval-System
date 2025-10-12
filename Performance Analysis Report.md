# Performance Analysis Report
## Country Information Retrieval System

**Author:** Alwin Kowattu 
**Date:** October 2025

---

## 1. Overview

This report analyzes the performance of five data structure implementations for searching country development data. We tested each implementation with datasets ranging from 100 to 900 entries and query loads of 1,000 to 10,000 searches.

**Data Structures Tested:**
- **List** - Simple array (O(n) search)
- **BST Dict** - Binary Search Tree (O(log n) search)
- **LL Dict** - Linked List (O(n) search)
- **SL Dict** - Sorted List (O(n) search)
- **HT Dict** - Hash Table (O(1) search)

---

## 2. Key Results

### Performance Summary (900 entries, 10,000 queries)

| Implementation | Time | Speed vs HT |
|----------------|------|-------------|
| **Hash Table** | **0.47 ms** | **1x (fastest)** |
| BST Dict | 136 ms | 290x slower |
| List | 318 ms | 680x slower |
| LL Dict | 1,945 ms | 4,165x slower |
| SL Dict | 1,952 ms | 4,179x slower |

**Finding:** Hash Table outperforms all other implementations by **290-4,179x**.

---

### Scaling Behavior (1,000 queries)

| Entries | List | BST | HT |
|---------|------|-----|-----|
| 100 | 0.001s | 0.005s | 0.00003s |
| 500 | 0.014s | 0.015s | 0.00019s |
| 900 | 0.039s | 0.017s | 0.00012s |

**Key Observation:** 
- **List** grows 39x slower as data increases (poor scaling)
- **BST** grows only 3.4x slower (good scaling)
- **HT** grows 4x slower (excellent scaling)

---

## 3. Important Findings

### Finding 1: Hash Table Dominates
Hash Table is the clear winner at all dataset sizes, maintaining sub-millisecond response times even under heavy load (10,000 queries). This confirms the power of O(1) constant-time lookup.

### Finding 2: BST vs List Crossover Point
- **Small datasets (< 300 entries):** Simple List is faster due to lower overhead
- **Large datasets (> 500 entries):** BST becomes significantly faster
- **Crossover at ~300-500 entries:** Performance is nearly equal

At 500 entries with 1,000 queries:
- List: 0.014s
- BST: 0.015s (essentially tied)

At 900 entries with 1,000 queries:
- List: 0.039s
- BST: 0.017s (BST is 2.3x faster)

### Finding 3: Linear Structures Don't Scale
Linked List and Sorted List perform poorly at all scales, taking nearly 2 seconds for 10,000 queries on 900 entries. These are unsuitable for real-world applications.

### Finding 4: Algorithm Complexity Verified
Test results match theoretical complexity:
- **O(1) Hash Table:** Constant time, barely increases with dataset size
- **O(log n) BST:** Grows logarithmically, scales well
- **O(n) List/LL/SL:** Grows linearly, struggles with larger datasets

---

## 4. Visual Comparison

### Performance Ranking (900 entries, 10,000 queries)

```
Hash Table    ▓ 0.47ms                    [FASTEST]

BST Dict      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 136ms

List          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 318ms

LL Dict       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 1,945ms

SL Dict       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 1,952ms
```

---

## 5. Recommendations

### For Production Use
**✅ Use Hash Table** 
- 290-4,179x faster than alternatives
- Sub-millisecond performance even with 10,000 queries
- Best choice for real-world applications

**Note:** Current hash function can be improved for even better performance.

### For Educational/Learning Purposes
**✅ Use Binary Search Tree**
- Demonstrates important algorithm concepts
- Shows clear O(log n) scaling behavior
- More challenging and interesting to implement
- Good performance (second-best overall)

### Not Recommended
- ❌ **Linked List:** Poor performance, recursion limitations beyond 950 entries
- ❌ **Sorted List:** Worst performance at scale
- ⚠️ **Simple List:** Only suitable for very small datasets (< 100 entries)

---

## 6. Conclusion

This analysis confirms that algorithm choice significantly impacts performance:

1. **Hash Tables are unmatched** for lookup operations - even a simple implementation is 290-4,179x faster than alternatives

2. **Binary Search Trees scale well** and offer the best balance of performance and educational value

3. **The crossover point between List and BST occurs around 300-500 entries**, which is important for choosing the right structure

4. **For the 20-country production dataset**, any implementation would be fast enough (< 1ms). However, Hash Table or BST are recommended for scalability.

**Final Decision for Project:** BST was selected for the production implementation because it offers excellent performance while showcasing more complex algorithmic concepts than a simple List. Hash Table would be the optimal choice purely for speed.

---

**Test Environment:** Windows, Python 3.x  
**Test Limitation:** Maximum 900 entries due to Python recursion limit in LL implementation

---

## Appendix: Complete Test Data

| Run | Entries | Queries | List (s) | BST (s) | LL (s) | SL (s) | HT (s) |
|-----|---------|---------|----------|---------|--------|--------|--------|
| 1 | 100 | 1,000 | 0.000378 | 0.002566 | 0.002459 | 0.002145 | 0.000017 |
| 2 | 100 | 1,000 | 0.001154 | 0.004979 | 0.015598 | 0.010708 | 0.000033 |
| 3 | 100 | 1,000 | 0.002014 | 0.009249 | 0.020257 | 0.020287 | 0.000034 |
| 4 | 250 | 1,000 | 0.006101 | 0.012465 | 0.048738 | 0.050494 | 0.000083 |
| 5 | 500 | 1,000 | 0.013878 | 0.014529 | 0.114456 | 0.104126 | 0.000186 |
| 6 | 900 | 1,000 | 0.038964 | 0.016582 | 0.186150 | 0.180204 | 0.000119 |
| 7 | 500 | 10,000 | 0.263045 | 0.114142 | 1.038940 | 1.158473 | 0.000186 |
| 8 | 900 | 10,000 | 0.317631 | 0.135529 | 1.945269 | 1.951590 | 0.000467 |
