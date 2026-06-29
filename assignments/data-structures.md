# Data Structures Assignments

# List

## 1. Find Second Largest Number
Write a program to find the second largest number in a list of integers.

**Requirements:**
- Take a list of integers as input (from user or hardcoded)
- Find and print the second largest number in the list
- Handle edge cases (e.g., list with fewer than 2 elements)
- Do not use built-in sorting functions

**Example:**
- Input: [10, 5, 8, 20, 15]
- Output: 15

## 2. Remove Duplicates from List
Write a program to remove duplicate elements from a list while preserving order.

**Requirements:**
- Take a list as input
- Remove all duplicate elements
- Preserve the original order of first occurrences
- Do not use sets directly

**Example:**
- Input: [1, 2, 3, 2, 4, 1, 5, 3]
- Output: [1, 2, 3, 4, 5]

## 3. Rotate List
Write a program to rotate a list by k positions to the right.

**Requirements:**
- Take a list and an integer k as input
- Rotate the list to the right by k positions
- Handle cases where k is greater than list length

**Example:**
- Input: [1, 2, 3, 4, 5], k = 2
- Output: [4, 5, 1, 2, 3]

# Dictionary

## 1. Word Frequency Counter
Write a program to count the frequency of each word in a given text.

**Requirements:**
- Take a string of text as input
- Split into words (ignore punctuation and case)
- Use a dictionary to count word occurrences
- Print the word counts in alphabetical order

**Example:**
- Input: "hello world hello python world"
- Output: {"hello": 2, "python": 1, "world": 2}

## 2. Inventory Management System
Write a program to manage an inventory using dictionaries.

**Requirements:**
- Create a dictionary with item names as keys and quantities as values
- Implement functions to:
  - Add items to inventory
  - Remove items from inventory
  - Update item quantities
  - Check if an item is in stock
  - Display all items with low stock (below threshold)

**Example:**
```python
inventory = {"apple": 10, "banana": 5, "orange": 8}
# Add: "grape": 15
# Remove: "banana": 3 (remaining: 2)
# Low stock (threshold 3): banana
```

## 3. Nested Dictionary Operations
Write a program to work with nested dictionaries representing student data.

**Requirements:**
- Create a nested dictionary structure with student info (name, age, grades, subjects)
- Implement functions to:
  - Find the average grade for each student
  - Find the student with the highest average
  - Calculate class average for each subject
  - Add a new student with their data

**Example:**
```python
students = {
    "Alice": {"age": 20, "grades": {"math": 90, "science": 85, "english": 88}},
    "Bob": {"age": 21, "grades": {"math": 78, "science": 92, "english": 80}}
}
# Alice's average: 87.67
# Highest average: Alice
# Math class average: 84.0
```

# Set

## 1. Find Common Elements
Write a program to find common elements between two sets.

**Requirements:**
- Take two sets as input
- Find and print the intersection (common elements)
- Find and print the union (all unique elements)
- Find and print the difference (elements in first but not in second)

**Example:**
- Input: {1, 2, 3, 4}, {3, 4, 5, 6}
- Intersection: {3, 4}
- Union: {1, 2, 3, 4, 5, 6}
- Difference: {1, 2}

## 2. Remove Duplicates from Multiple Lists
Write a program to find unique elements across multiple lists using sets.

**Requirements:**
- Take 3 or more lists as input
- Find elements that appear in at least one list (union)
- Find elements that appear in all lists (intersection)
- Find elements that appear in exactly one list (symmetric difference)

**Example:**
- Input: [1, 2, 3], [2, 3, 4], [3, 4, 5]
- Union: {1, 2, 3, 4, 5}
- Intersection: {3}
- Exactly one: {1, 5}

## 3. Set Operations for Text Analysis
Write a program to analyze text using set operations.

**Requirements:**
- Take two paragraphs of text as input
- Extract unique words from each paragraph (ignoring case and punctuation)
- Find:
  - Words common to both paragraphs
  - Words unique to each paragraph
  - All unique words combined

**Example:**
- Paragraph 1: "The quick brown fox"
- Paragraph 2: "The quick blue dog"
- Common: {"the", "quick"}
- Unique to P1: {"brown", "fox"}
- Unique to P2: {"blue", "dog"}
- All unique: {"the", "quick", "brown", "fox", "blue", "dog"}

# Tuple

## 1. Coordinate Operations
Write a program to perform operations on 2D coordinates stored as tuples.

**Requirements:**
- Store coordinates as tuples (x, y)
- Implement functions to:
  - Calculate distance between two points
  - Find the midpoint between two points
  - Check if a point lies within a bounding box
  - Find the point closest to the origin

**Example:**
```python
point1 = (3, 4)
point2 = (0, 0)
# Distance: 5.0
# Midpoint: (1.5, 2.0)
# Distance from origin: 5.0
```

## 2. Student Records with Tuples
Write a program to manage student records using tuples.

**Requirements:**
- Store student records as tuples: (name, age, grade)
- Implement functions to:
  - Sort students by grade
  - Find students above a certain age
  - Calculate average grade
  - Find the student with the highest grade

**Example:**
```python
students = [
    ("Alice", 20, 85),
    ("Bob", 21, 92),
    ("Charlie", 19, 78)
]
# Sorted by grade: [("Charlie", 19, 78), ("Alice", 20, 85), ("Bob", 21, 92)]
# Above age 20: [("Bob", 21, 92)]
# Highest grade: Bob with 92
```

## 3. Tuple Unpacking and Swapping
Write a program to demonstrate tuple unpacking and swapping.

**Requirements:**
- Use tuples to store RGB color values
- Implement functions to:
  - Convert RGB to HSL using tuple unpacking
  - Swap color channels
  - Find complementary colors
  - Check if two colors are the same

**Example:**
```python
red = (255, 0, 0)
blue = (0, 0, 255)
# Swap red and blue: (0, 0, 255) -> (255, 0, 0)
# Unpack: r, g, b = red
# Complementary of red: (0, 255, 255)
```

# Array (using array module or lists as arrays)

## 1. Array Rotation
Write a program to rotate an array by k positions using array operations.

**Requirements:**
- Use the array module or list as an array
- Rotate the array left or right by k positions
- Do it in-place with O(1) extra space
- Handle edge cases

**Example:**
- Input: [1, 2, 3, 4, 5], k = 2 (left)
- Output: [3, 4, 5, 1, 2]

## 2. Find Missing Number
Write a program to find the missing number in an array of consecutive integers.

**Requirements:**
- Take an array containing n-1 integers from 1 to n
- Find the missing number
- Do not use sorting
- Solve in O(n) time

**Example:**
- Input: [1, 2, 4, 5, 6] (n = 6)
- Output: 3

## 3. Merge Two Sorted Arrays
Write a program to merge two sorted arrays into one sorted array.

**Requirements:**
- Take two sorted arrays as input
- Merge them into a single sorted array
- Do not use built-in sort functions
- Maintain O(n + m) time complexity

**Example:**
- Input: [1, 3, 5], [2, 4, 6]
- Output: [1, 2, 3, 4, 5, 6]
