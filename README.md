# PrepTrack — Placement Preparation Performance Analyzer

## Overview

PrepTrack is a Python-based placement readiness assessment system that helps evaluate whether a student is prepared for a placement mock interview. The application analyzes student attendance, project completion status, profile verification, and seven days of coding practice performance to generate a comprehensive readiness report with personalized recommendations.

The system validates user inputs, processes practice scores, performs performance analysis, and determines placement eligibility based on predefined criteria.

---

## Features

### Student Information Management

- Student Name Validation
- Registration Number Input
- Graduation Year Validation
- Attendance Validation
- Project Completion Verification
- Profile Verification

### Practice Score Processing

- Processes coding scores for 7 practice days
- Supports absent days using `-1`
- Validates all score inputs
- Calculates:
  - Attempted Days
  - Absent Days
  - Passed Days
  - Failed Days

### Performance Classification

| Score Range | Classification |
|-------------|---------------|
| 75 – 100 | Strong |
| 60 – 74 | Satisfactory |
| 40 – 59 | Needs Improvement |
| 0 – 39 | Critical |

### Performance Analysis

- Total Score Calculation
- Average Score Calculation
- Highest Score Identification
- Lowest Score Identification
- First Critical Score Detection

### Placement Readiness Evaluation

The system verifies:

- Graduation Year (2025–2027)
- Attendance ≥ 75%
- At Least 6 Practice Attempts
- Average Score ≥ 70
- No Critical Scores
- Minimum 4 Passed Practices
- Project Completion Status
- Profile Verification Status

### Final Decision System

The application provides:

- Final Placement Status
- Primary blocker
- Recommended Next Action

---

## Technologies Used

- Python 3
- Loops (`for`, `while`)
- Conditional Statements (`if`, `elif`, `else`)
- Boolean Expressions
- Input Validation
- Counters and Accumulators
- Arithmetic Operators

---

## Project Structure

```text
PrepTrack/
│
├── preptrack-soumya.py
├── README.md
```

---

## Sample Execution

```text
================================================== 
              PREPTRACK
==================================================

enter student name soumya dash
enter registration numberkcse2003
enter graduation year2026
enter attendance percentage75

Attendance accepted
Has the student completed the required project? Enter yes or no: yes

Is the student profile verified?Enter yes or no :yes
Enter Day 1 score from 0 to 100, or -1 for absent : 78
Day 1 Result: Strong
Enter Day 2 score from 0 to 100, or -1 for absent : 99
Day 2 Result: Strong
Enter Day 3 score from 0 to 100, or -1 for absent : 34
Day 3 Result: Critical
Enter Day 4 score from 0 to 100, or -1 for absent : 56
Day 4 Result: Needs Improvement
Enter Day 5 score from 0 to 100, or -1 for absent : -1
Day 5 Result: Absent
Enter Day 6 score from 0 to 100, or -1 for absent : 3
Day 6 Result: Critical
Enter Day 7 score from 0 to 100, or -1 for absent : 45
Day 7 Result: Needs Improvement

Highest Score          : 99
Highest Score Day      : Day 2
Lowest Score           : 3
Lowest Score Day       : Day 6

Critical Score Found   : Yes
First Critical Day     : Day 3
First Critical Score   : 34

Final Status           : Critical Support Required
Primary Blocker        : Critical score found
Next Action            : Revise the concepts from the first critical day

==================================================
```

---

## Placement Readiness Criteria

A student is considered **Ready for Mock Interview** only if all of the following conditions are satisfied:

- Graduation Year between 2025 and 2027
- Attendance ≥ 75%
- Attempted Days ≥ 6
- Average Score ≥ 70
- No Critical Scores
- Passed Days ≥ 4
- Project Completed
- Profile Verified

---

## Output Report

The generated report includes:

### Student Profile

- Student Name
- Registration Number
- Graduation Year
- Attendance Percentage
- Project Completion Status
- Profile Verification Status

### Practice Summary

- Total Practice Days
- Attempted Days
- Absent Days
- Passed Days
- Failed Days

### Performance Analysis

- Total Score
- Average Score
- Highest Score
- Lowest Score

### Critical Score Information

- Critical Score Found
- First Critical Day
- First Critical Score

### Final Decision

- Placement Status
- Primary Blocker
- Recommended Next Action

---

## Learning Outcomes

This project demonstrates:

- Input Validation
- Conditional Logic
- Looping Structures
- Data Processing
- Performance Analysis
- Decision-Making Algorithms
- Report Generation
- Problem Solving using Python

---

# Individual Contribution

**Name:** Soumya Sworupa Dash

**Repository URL:** https://github.com/<your-username>/preptrack-soumya

### My Contribution

I independently developed the Placement Preparation Performance Analyzer by implementing the complete application workflow—from collecting and validating student information to generating the final placement readiness report. The project focuses on evaluating a student's overall preparation for placement interviews using multiple performance indicators.

### Features I Implemented

- Student information collection and validation
- Attendance percentage validation
- Graduation year eligibility check
- Project completion verification
- Profile verification
- Seven-day coding practice score processing
- Handling absent days using `-1`
- Performance classification (Strong, Satisfactory, Needs Improvement, Critical)
- Calculation of total score, average score, highest score, lowest score, passed days, and failed days
- Final placement readiness evaluation
- Generation of recommendations based on the student's performance

### Python Concepts Used

During this project, I applied several core Python concepts, including:

- Variables and Data Types
- Input Validation
- Conditional Statements (`if`, `elif`, `else`)
- `for` and `while` Loops
- Boolean Logic
- Counters and Accumulators
- Arithmetic and Comparison Operators
- Nested Decision Making
- Formatted Output

### Most Challenging Part

The most challenging part was designing the placement readiness evaluation logic. Since the final result depends on multiple conditions such as attendance, graduation year, practice attempts, average score, project completion, and profile verification, I had to carefully combine these conditions to ensure the correct status and recommendation were generated.

### Challenges Faced

One challenge was handling absent practice days without affecting performance calculations. Another was correctly identifying performance statistics such as the highest score, lowest score, and first critical score while ignoring absent entries.

### How I Solved It

I solved these challenges by maintaining separate counters for attempted and absent days and using conditional checks to skip score calculations for absent entries. I also used control variables to accurately update the highest score, lowest score, and first critical score only for valid practice attempts. This ensured that the generated performance report was accurate and reliable.
