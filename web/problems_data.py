problems = [

# =========================
# EASY (10)
# =========================

{
    "slug": "two-sum",
    "title": "Two Sum",
    "difficulty": "easy",
    "description": """Given an array of integers and a target value,
return the indices of the two numbers that add up to the target.

Example:
nums = [2,7,11,15]
target = 9

Output:
[0,1]
""",

    "function_name": "two_sum",

    "starter_code": """class Solution:
    def two_sum(self, nums, target):
        # Write your logic below
        pass
""",

    "visible_tests": [
        {
            "input": ([2,7,11,15], 9),
            "expected": [0,1]
        }
    ],

    "hidden_tests": [
        {
            "input": ([3,2,4], 6),
            "expected": [1,2]
        },
        {
            "input": ([3,3], 6),
            "expected": [0,1]
        }
    ]
},

{
    "slug": "palindrome-number",
    "title": "Palindrome Number",
    "difficulty": "easy",
    "description": """Return True if the integer is a palindrome, else False.

Example:
Input: 121
Output: True
""",
    "starter_code": """def is_palindrome(x):
    # Write your code here
    pass

print(is_palindrome(121))"""
},

{
    "slug": "valid-parentheses",
    "title": "Valid Parentheses",
    "difficulty": "easy",
    "description": """Given a string containing just (), {}, [],
determine if the input string is valid.""",
    "starter_code": """def is_valid(s):
    # Write your code here
    pass

print(is_valid("()[]{}"))"""
},

{
    "slug": "max-subarray",
    "title": "Maximum Subarray",
    "difficulty": "easy",
    "description": """Find the contiguous subarray with the largest sum.""",
    "starter_code": """def max_subarray(nums):
    # Write your code here
    pass

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))"""
},

{
    "slug": "climbing-stairs",
    "title": "Climbing Stairs",
    "difficulty": "easy",
    "description": """You are climbing stairs. You can take 1 or 2 steps.
Return number of distinct ways to reach top.""",
    "starter_code": """def climb_stairs(n):
    # Write your code here
    pass

print(climb_stairs(5))"""
},

{
    "slug": "merge-sorted-arrays",
    "title": "Merge Sorted Arrays",
    "difficulty": "easy",
    "description": "Merge two sorted arrays into one sorted array.",
    "starter_code": """def merge_arrays(a, b):
    # Write your code here
    pass

print(merge_arrays([1,3,5], [2,4,6]))"""
},

{
    "slug": "remove-duplicates",
    "title": "Remove Duplicates",
    "difficulty": "easy",
    "description": "Remove duplicates from sorted array.",
    "starter_code": """def remove_duplicates(nums):
    # Write your code here
    pass

print(remove_duplicates([1,1,2,2,3]))"""
},

{
    "slug": "reverse-string",
    "title": "Reverse String",
    "difficulty": "easy",
    "description": "Reverse a string.",
    "starter_code": """def reverse_string(s):
    # Write your code here
    pass

print(reverse_string("hello"))"""
},

{
    "slug": "fibonacci",
    "title": "Fibonacci Number",
    "difficulty": "easy",
    "description": "Return nth Fibonacci number.",
    "starter_code": """def fib(n):
    # Write your code here
    pass

print(fib(7))"""
},

{
    "slug": "binary-search",
    "title": "Binary Search",
    "difficulty": "easy",
    "description": "Implement binary search.",
    "starter_code": """def binary_search(nums, target):
    # Write your code here
    pass

print(binary_search([1,2,3,4,5], 4))"""
},

# =========================
# MEDIUM (10)
# =========================

{
    "slug": "longest-substring",
    "title": "Longest Substring Without Repeating Characters",
    "difficulty": "medium",
    "description": """Given a string s, find the length of the longest substring 
without repeating characters.

A substring is a contiguous sequence of characters within the string.

Return the length of the longest possible substring that contains only unique characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with length 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with length 3.

Constraints:
• 0 <= s.length <= 5 * 10^4
• s consists of English letters, digits, symbols, and spaces.
""",

    "function_name": "length_of_longest_substring",

    "starter_code": """class Solution:
    def length_of_longest_substring(self, s):
        # Write your logic below
        pass
""",

    "visible_tests": [
        {"input": ("abcabcbb",), "expected": 3}
    ],

    "hidden_tests": [
        {"input": ("bbbbb",), "expected": 1},
        {"input": ("pwwkew",), "expected": 3}
    ]
},

{
    "slug": "3sum",
    "title": "3Sum",
    "difficulty": "medium",
    "description": "Find all unique triplets that sum to zero.",
    "starter_code": """def three_sum(nums):
    # Write your code here
    pass

print(three_sum([-1,0,1,2,-1,-4]))"""
},

{
    "slug": "group-anagrams",
    "title": "Group Anagrams",
    "difficulty": "medium",
    "description": "Group words that are anagrams.",
    "starter_code": """def group_anagrams(strs):
    # Write your code here
    pass

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))"""
},

{
    "slug": "container-water",
    "title": "Container With Most Water",
    "difficulty": "medium",
    "description": "Find max water container.",
    "starter_code": """def max_area(height):
    # Write your code here
    pass

print(max_area([1,8,6,2,5,4,8,3,7]))"""
},

{
    "slug": "rotate-matrix",
    "title": "Rotate Matrix",
    "difficulty": "medium",
    "description": "Rotate matrix 90 degrees.",
    "starter_code": """def rotate(matrix):
    # Write your code here
    pass"""
},

{
    "slug": "product-array",
    "title": "Product of Array Except Self",
    "difficulty": "medium",
    "description": "Return array where each element is product of others.",
    "starter_code": """def product_except_self(nums):
    # Write your code here
    pass

print(product_except_self([1,2,3,4]))"""
},

{
    "slug": "top-k",
    "title": "Top K Frequent Elements",
    "difficulty": "medium",
    "description": "Return k most frequent elements.",
    "starter_code": """def top_k(nums, k):
    # Write your code here
    pass

print(top_k([1,1,1,2,2,3], 2))"""
},

{
    "slug": "coin-change",
    "title": "Coin Change",
    "difficulty": "medium",
    "description": "Minimum coins to make amount.",
    "starter_code": """def coin_change(coins, amount):
    # Write your code here
    pass

print(coin_change([1,2,5], 11))"""
},

{
    "slug": "validate-bst",
    "title": "Validate Binary Search Tree",
    "difficulty": "medium",
    "description": "Validate if tree is BST.",
    "starter_code": """def is_valid_bst(root):
    # Write your code here
    pass"""
},

{
    "slug": "kth-largest",
    "title": "Kth Largest Element",
    "difficulty": "medium",
    "description": "Find kth largest element.",
    "starter_code": """def find_kth_largest(nums, k):
    # Write your code here
    pass

print(find_kth_largest([3,2,1,5,6,4], 2))"""
},

# =========================
# HARD (10)
# =========================

{
    "slug": "lru-cache",
    "title": "LRU Cache",
    "difficulty": "hard",
    "description": "Design LRU Cache.",
    "starter_code": """class LRUCache:
    def __init__(self, capacity):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass"""
},

{
    "slug": "median-two-sorted",
    "title": "Median of Two Sorted Arrays",
    "difficulty": "hard",
    "description": "Find median of two sorted arrays in O(log n).",
    "starter_code": """def find_median(nums1, nums2):
    # Write your code here
    pass"""
},

{
    "slug": "word-ladder",
    "title": "Word Ladder",
    "difficulty": "hard",
    "description": "Shortest transformation sequence.",
    "starter_code": """def word_ladder(begin, end, word_list):
    # Write your code here
    pass"""
},

{
    "slug": "serialize-tree",
    "title": "Serialize and Deserialize Binary Tree",
    "difficulty": "hard",
    "description": "Serialize and deserialize tree.",
    "starter_code": """class Codec:
    def serialize(self, root):
        pass

    def deserialize(self, data):
        pass"""
},

{
    "slug": "n-queens",
    "title": "N-Queens",
    "difficulty": "hard",
    "description": "Solve N-Queens problem.",
    "starter_code": """def solve_n_queens(n):
    # Write your code here
    pass"""
},

{
    "slug": "trapping-rain-water",
    "title": "Trapping Rain Water",
    "difficulty": "hard",
    "description": "Calculate trapped rain water.",
    "starter_code": """def trap(height):
    # Write your code here
    pass"""
},

{
    "slug": "largest-rectangle",
    "title": "Largest Rectangle in Histogram",
    "difficulty": "hard",
    "description": "Find largest rectangle area.",
    "starter_code": """def largest_rectangle(heights):
    # Write your code here
    pass"""
},

{
    "slug": "merge-k-lists",
    "title": "Merge K Sorted Lists",
    "difficulty": "hard",
    "description": "Merge k sorted linked lists.",
    "starter_code": """def merge_k_lists(lists):
    # Write your code here
    pass"""
},

{
    "slug": "minimum-window",
    "title": "Minimum Window Substring",
    "difficulty": "hard",
    "description": "Find minimum window substring.",
    "starter_code": """def min_window(s, t):
    # Write your code here
    pass"""
},

{
    "slug": "regex-matching",
    "title": "Regular Expression Matching",
    "difficulty": "hard",
    "description": "Implement regex matching with . and *.",
    "starter_code": """def is_match(s, p):
    # Write your code here
    pass"""
},

]