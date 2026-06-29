# Mixed Data Structures Assignments

## 1. Student Gradebook System
Write a comprehensive student gradebook system using multiple data structures.

**Requirements:**
- Use a **dictionary** to store student data (name as key, grades as value)
- Use a **list** to store all student names in order
- Use a **set** to track unique subjects offered
- Use a **tuple** to store grade ranges (min, max) for each subject
- Implement functions to:
  - Add a student with their grades for multiple subjects
  - Calculate each student's average grade
  - Find the top performer in each subject
  - Get all students who failed (grade < 60) in any subject
  - Generate a class report showing averages per subject

**Example:**
```python
# Dictionary for student data
students = {
    "Alice": {"math": 85, "science": 90, "english": 78},
    "Bob": {"math": 92, "science": 88, "english": 95},
    "Charlie": {"math": 65, "science": 72, "english": 58}
}

# List for ordered student names
student_list = ["Alice", "Bob", "Charlie"]

# Set for unique subjects
subjects = {"math", "science", "english"}

# Tuple for grade ranges
grade_ranges = {
    "math": (0, 100),
    "science": (0, 100),
    "english": (0, 100)
}

# Alice's average: 84.33
# Top in math: Bob (92)
# Failed in english: Charlie (58)
```

**Data Structures Used:** Dictionary, List, Set, Tuple

## 2. E-commerce Shopping Cart
Write a program to manage an e-commerce shopping cart with inventory tracking.

**Requirements:**
- Use a **dictionary** for product catalog (product_id → {name, price, stock})
- Use a **list** for shopping cart items (each item as a dictionary)
- Use a **set** to track out-of-stock products
- Use a **tuple** for order confirmation (order_id, total, items_count)
- Implement functions to:
  - Add products to cart (check stock availability)
  - Remove items from cart
  - Calculate cart total with discounts
  - Apply coupon codes (stored in a set)
  - Generate order summary as a tuple
  - Update inventory after purchase

**Example:**
```python
# Product catalog
catalog = {
    1: {"name": "Laptop", "price": 999.99, "stock": 10},
    2: {"name": "Mouse", "price": 29.99, "stock": 50},
    3: {"name": "Keyboard", "price": 79.99, "stock": 0}
}

# Shopping cart
cart = [
    {"product_id": 1, "quantity": 1},
    {"product_id": 2, "quantity": 2}
]

# Out of stock
out_of_stock = {3}

# Valid coupons
coupons = {"SAVE10", "SUMMER20"}

# Order confirmation
order = (1001, 1059.97, 3)  # (order_id, total, items_count)
```

**Data Structures Used:** Dictionary, List, Set, Tuple

## 3. Social Network Analysis
Write a program to analyze a social network using graph-like structures.

**Requirements:**
- Use a **dictionary** for the adjacency list (user → set of friends)
- Use a **list** to store all users in the network
- Use a **set** to find mutual friends between users
- Use a **tuple** to store user profiles (name, age, location)
- Use a **dictionary** to store user statistics (friends_count, posts_count)
- Implement functions to:
  - Add a new user with their profile
  - Add friendship between two users (bidirectional)
  - Find mutual friends between two users
  - Find friends of friends (people 2 degrees away)
  - Calculate network density
  - Find the most connected user (highest degree)
  - Detect if the network has isolated users

**Example:**
```python
# Adjacency list (graph)
network = {
    "alice": {"bob", "charlie", "david"},
    "bob": {"alice", "charlie"},
    "charlie": {"alice", "bob", "david"},
    "david": {"alice", "charlie"}
}

# User list
users = ["alice", "bob", "charlie", "david"]

# User profiles
profiles = {
    "alice": ("Alice Smith", 25, "NYC"),
    "bob": ("Bob Jones", 30, "LA"),
    "charlie": ("Charlie Brown", 28, "Chicago"),
    "david": ("David Lee", 35, "Boston")
}

# User statistics
stats = {
    "alice": {"friends_count": 3, "posts_count": 45},
    "bob": {"friends_count": 2, "posts_count": 20},
    "charlie": {"friends_count": 3, "posts_count": 35},
    "david": {"friends_count": 2, "posts_count": 15}
}

# Mutual friends of alice and bob: {"charlie"}
# Friends of friends of alice: {"david"} (already friend) + {} new
# Most connected: alice or charlie (3 friends)
```

**Data Structures Used:** Dictionary, List, Set, Tuple
