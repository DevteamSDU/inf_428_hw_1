# inf_428_hw_1

# Homework 1 Report

This is the report for Homework 1, divided into three days of work. Each task was completed and documented over separate days.

## Day 1: Completed Task 1
On the first day, I worked on Task 1, which involved solving three algorithmic problems and documenting them. Here’s the breakdown:

- **1. Longest Continuous Increasing Subsequence**
  - Implemented a solution using a single pass with two variables to track the longest sequence.
  - Documented the approach in `doc.txt` explaining the use of current and max length variables.
  - Code: `/homework1/1/first/code.py`

- **2. Merge Sorted Array**
  - Used a three-pointer approach to merge arrays in-place, filling from the end.
  - Documented the thought process in `doc.txt`.
  - Code: `/homework1/1/second/code.py`

- **3. Intersection of Two Arrays**
  - Solved using sets to simplify finding unique elements in both arrays.
  - Documented the approach of using sets in `doc.txt`.
  - Code: `/homework1/1/third/code.py`

## Day 2: Completed Task 2
On the second day, I focused on Task 2, which required calculating an aggregated user threat score for multiple departments.

- **Generated Random Data**: 
  - Used the provided `generate_random_data` function to simulate threat scores for each department.
  
- **Calculated Aggregated Threat Score**:
  - Implemented `calculate_aggregated_threat_score` to weight each department’s average threat score by its importance.
  - Normalized the final score to a range of 0–90.
  - Code: `/homework/2/code.py`

- **Testing**:
  - Wrote tests for different cases (equal importance, high/low threat, etc.) in `test.py`.
  - Documented the thought process and test cases in `doc.txt`.
  - Test file: `/homework/2/test.py`

## Day 3: Completed Task 3
On the third day, I worked on Task 3, transforming time data into cyclic features for better use in machine learning models.

- **Implemented Cyclic Transformation**:
  - Created `transform_time_to_cyclic` using sine and cosine to represent time on a 24-hour cycle.
  - This approach enables the model to correctly interpret the cyclic nature of time.

- **Testing**:
  - Added unit tests for various time points (e.g., midnight, noon, near midnight).
  - Verified that times like 23:00 and 01:00 are close in the transformed cyclic space.
  - Code: `/homework/3/code.py`
  - Test file: `/homework/3/test.py`

Each task was completed with accompanying documentation (`doc.txt` files) to explain the solution approach and design decisions.
