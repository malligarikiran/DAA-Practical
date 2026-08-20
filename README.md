# DAA Practical – Searching Algorithms

## Practical Title

**Implementation and Time Analysis of Linear Search and Binary Search Algorithms**

---

## Aim

To implement **Linear Search** and **Binary Search** algorithms using Python and analyze their time complexity.

---

## Objectives

- To understand the working of searching algorithms.
- To implement Linear Search using Python.
- To implement Binary Search using Python.
- To calculate the number of comparisons.
- To measure the execution time of both algorithms.
- To analyze their best, average, and worst-case time complexities.

---

## Algorithms Covered

### 1. Linear Search

Linear Search checks each element of the array one by one until the required element is found or the end of the array is reached.

### Algorithm

1. Start from the first element of the array.
2. Compare the current element with the target element.
3. If both are equal, return the position of the element.
4. If they are not equal, move to the next element.
5. Repeat until the element is found or the array ends.
6. If the element is not found, return "Element Not Found".

### Time Complexity

| Case | Complexity |
|---|---|
| Best Case | O(1) |
| Average Case | O(n) |
| Worst Case | O(n) |

### Space Complexity

**O(1)**

---

## 2. Binary Search

Binary Search works on a **sorted array**. It repeatedly divides the search range into two halves.

### Algorithm

1. Sort the array.
2. Set `low = 0`.
3. Set `high = n - 1`.
4. Find the middle element using:
   `mid = (low + high) // 2`
5. Compare the middle element with the target.
6. If the middle element is equal to the target, return its position.
7. If the target is greater than the middle element, search the right half.
8. If the target is smaller than the middle element, search the left half.
9. Repeat until the element is found or the search range becomes empty.

### Time Complexity

| Case | Complexity |
|---|---|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

### Space Complexity

**O(1)**

---

# Project Structure

```text
DAA-Practical/
│
├── linear_search.py
├── binary_search.py
└── README.md
