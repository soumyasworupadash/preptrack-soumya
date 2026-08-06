### 1. COLLECT STUDENT DETAILS

print("=" * 50)
print("              PREPTRACK")
print("=" * 50)

while True:
    student_name=input("enter student name")
    if student_name != "":
        break

    print("student name cannot be empty")
      
registration_number=input("enter registration number")
graduation_year=int(input("enter graduation year"))
while True:
    attendance_percentage=float(input("enter attendance percentage"))
    if attendance_percentage >=0 and attendance_percentage <=100:
        print("Attendance accepted")
        break
    print("attendance percentage must be between 0 and 100")

while True:
    project_input=input("Has the student completed the required project? Enter yes or no: ")
    if project_input=="yes" or project_input=="no":
        break
    print("Invalid input, Enter only yes or no")
if project_input=="no":
    project_completed=False
else:
    project_completed=True

while True:
    profile_input=input("Is the student profile verified?Enter yes or no :")
    if profile_input=="yes" or profile_input=="no":
        break
    print("Invalid input, Enter only yes or no")
if profile_input=="no":
    profile_verified=False
else:
    profile_verified=True


### 2. INITIALIZE COUNTERS AND VARIABLES
total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0


### 3. PROCESS SEVEN PRACTICE DAY
for day in range(1, 8):
    while True:
        score=int(input(f"Enter Day {day} score from 0 to 100, or -1 for absent : "))
        if score==-1 or (score >=0 and score <=100):
            break
        print("Invalid input, Enter only -1 or a score between 0 and 100")

    if score == -1:
        absent_days += 1
        print(f"Day {day} Result: Absent")
        continue
    attempted_days += 1
    total_score += score

    if not first_attempt_found:
        highest_score = score
        highest_score_day = day

        lowest_score = score
        lowest_score_day = day

        first_attempt_found = True

    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    if score >= 75:
        print(f"Day {day} Result: Strong")
        strong_days += 1

    elif score >= 60:
        print(f"Day {day} Result: Satisfactory")
        satisfactory_days += 1

    elif score >= 40:
        print(f"Day {day} Result: Needs Improvement")
        improvement_days += 1

    else:
        print(f"Day {day} Result: Critical")
        critical_days += 1

        if not critical_score_found:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score

    # Passed and Failed
    if score >= 60:
        passed_days += 1
    else:
        failed_days += 1

# 4. CALCULATE THE AVERAGE
        
if attempted_days > 0:
    average_score=total_score / attempted_days
else:
    average_score = 0

# 5. CREATE ELIGIBILITY CONDITIONS
graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

attendance_eligible = attendance_percentage >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)   
# 6. DETERMINE FINAL STATUS


if attempted_days == 0:
    final_status = "Practice Not Evaluated"
    primary_blocker = "No practice attempted"
    next_action = "Attempt the required coding practices"

elif critical_score_found:
    final_status = "Critical Support Required"
    primary_blocker = "Critical score found"
    next_action = "Revise the concepts from the first critical day"

elif attempted_days < 6:
    final_status = "Practice Incomplete"
    primary_blocker = "Fewer than six practices attempted"
    next_action = "Complete at least six practice days"

elif passed_days < 4:
    final_status = "Insufficient Passed Practices"
    primary_blocker = "Fewer than four passed practices"
    next_action = "Pass at least four coding practices"

elif average_score < 70:
    final_status = "Practice Improvement Required"
    primary_blocker = "Average score below 70"
    next_action = "Improve the average score to at least 70"

elif attendance_percentage < 75:
    final_status = "Attendance Improvement Required"
    primary_blocker = "Attendance below 75"
    next_action = "Improve attendance to at least 75 percent"

elif not graduation_eligible:
    final_status = "Graduation Criteria Not Met"
    primary_blocker = "Graduation year not eligible"
    next_action = "Check the eligible graduation-year requirement"

elif not project_completed:
    final_status = "Application On Hold"
    primary_blocker = "Project incomplete"
    next_action = "Complete the required project"

elif not profile_verified:
    final_status = "Application On Hold"
    primary_blocker = "Profile not verified"
    next_action = "Complete profile verification"

else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Proceed to placement mock interviews"


# Display Highest and Lowest Score

if attempted_days > 0:
    print(f"Highest Score          : {highest_score}")
    print(f"Highest Score Day      : Day {highest_score_day}")
    print(f"Lowest Score           : {lowest_score}")
    print(f"Lowest Score Day       : Day {lowest_score_day}")
else:
    print("Highest Score          : Not Available")
    print("Highest Score Day      : Not Available")
    print("Lowest Score           : Not Available")
    print("Lowest Score Day       : Not Available")


print()

# Display First Critical Score Information

if critical_score_found:
    print(f"Critical Score Found   : Yes")
    print(f"First Critical Day     : Day {first_critical_day}")
    print(f"First Critical Score   : {first_critical_score}")
else:
    print(f"Critical Score Found   : No")
    print("First Critical Day     : Not Applicable")
    print("First Critical Score   : Not Applicable")


print()
print(f"Final Status           : {final_status}")
print(f"Primary Blocker        : {primary_blocker}")
print(f"Next Action            : {next_action}")

print("=" * 50)