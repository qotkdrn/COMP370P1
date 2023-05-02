# Name: pa1.py
# Author(s): Kennedy Castillon Jimenez
# Date last modified: Feb 22, 2022
# Description: Implement Gale Shapley algorithm to produce matchings of hospitals and students

# 3 3     Number of hospitals/Number of students
# 1 1 1   Number of positions at each hospital
# -----   
# 2 0 1   Hospital 0 : Preference:[2,0,1]
# 1 2 0   Hospital 1 : Preference:[1,2,0]
# 1 0 2   Hospital 2 : Preference:[1,0,2]
# -----     
# 0 1 2   Student 0 : Preference: [0,1,2]
# 1 0 2   Student 1 : Preference: [1,0,2]
# 2 0 1   Student 2 : Preference: [2,0,1]

import sys

def gale_shapley(filename):
    """
    Runs Gale-Shapley algorithm on input
    from file filename.  Format of input file
    given in problem statement.
    Returns a list containing hospitals assigned to each 
    student, or None if a student is not assigned to a hospital.
    """

    # file open and read
    with open(filename, "r") as file:
        lines = file.readlines()

    # getting data ready and loaded
    num_hospitals = int(lines[0].split()[0])
    num_students = int(lines[0].split()[1])
    openings = [int(i) for i in lines[1].split()]

    # allows one to get an array for the preferences of the hospitals
    hospital_preferences = [[] for i in range(num_hospitals)]
    student_preferences = [[] for i in range(num_students)]

    # initiates lists that will be changing during G-S algorithm
    hospital_matches = [None for i in range(num_hospitals)]
    student_matches = [None for i in range(num_students)]
    unassigned_Hospitals = [int(i) for i in range(num_hospitals)]

    current_line = 2 
    #saves for each hospital's preference
    for hospital in range(num_hospitals):
        preferences = list(map(int, lines[current_line].split()))
        for i in range(num_hospitals):
            hospital_preferences[hospital].append(preferences[i])
        current_line += 1
        
    for student in range(num_students):
        preferences = list(map(int, lines[current_line].split()))
        for i in range(num_students):
            student_preferences[student].append(preferences[i])
        current_line += 1
        
    hospital_matches = [None for i in range(num_hospitals)]
    student_matches = [None for i in range(num_students)]

    while None in hospital_matches:
        for hospital in range(num_hospitals):
            if hospital_matches[hospital] is None:
                for student in hospital_preferences[hospital]:
                    if student_matches[student] is None:
                        hospital_matches[hospital] = student
                        student_matches[student] = hospital
                        break
                    else:
                        current_match = student_matches[student]
                        if student_preferences[student].index(hospital) < student_preferences[student].index(current_match):
                            hospital_matches[current_match] = None
                            hospital_matches[hospital] = student
                            student_matches[student] = hospital
                            break

    return student_matches

    # while None in student_matches:
    #     for student in range(num_students):
    #         if student_matches[student] is None:
    #             for hospital in student_preferences[student]:
    #                 if hospital_matches[hospital] is None:
    #                     student_matches[student] = hospital
    #                     hospital_matches[hospital] = student
    #                     break
    #                 else:
    #                     current_match = hospital_matches[hospital]
    #                     if hospital_preferences[hospital].index(student) < hospital_preferences[hospital].index(current_match):
    #                         student_matches[current_match] = None
    #                         student_matches[student] = hospital
    #                         hospital_matches[hospital] = student
    #                         break
    # return student_matches

# filename = 'input1.txt'
# gale_shapley(filename)

if __name__ == "__main__":
    print(gale_shapley("input1.txt"))