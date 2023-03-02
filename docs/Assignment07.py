# ---------------------------------------------------------------------------- #
# Title: Assignment07
# Description: Demonstrates Structured Error Handling and Use of Pickling
# ChangeLog (Who,When,What):
# JJepson, 2.27.2023, Created File
# ---------------------------------------------------------------------------- #
import pickle
# Data ---------------------------------------------------------------------- #
# Declare variables and constants
GradeBook = [{'Name': 'Linus', 'Grade': 89.00},
             {'Name': 'Lucy', 'Grade': 96.35},
             {'Name': 'Sally', 'Grade': 92.27},
             {'Name': 'Charlie Brown', 'Grade': 72.59},
             {'Name': 'Joe Cool', 'Grade': 100.00},
             {'Name': 'Patty', 'Grade': 87.05},
             {'Name': 'Marci', 'Grade': 98.23}]

GradeBookFile = 'StudentGrades.pickle'


# Processing  --------------------------------------------------------------- #
def write_grades(data, file):
    """  Serializes a msg in binary and uploads it to a file

    :param data: {dict} with student grades data:
    :param file: (string) containing name of the file:
    :return nothing
    """
    print('*Pickling data to binary form.*')
    with open(file, 'wb') as file:
        pickle.dump(data, file)
    print('Data saved in binary form!')


def read_grades(file_name):
    """  unpickles a binary file.

    :param file_name: (string) containing name of the file:
    :return data: (list) of dictionary rows with student grades
    """
    try:
        print('*Trying to read file as regular file.*')
        with open(file_name, 'r') as file:
            print(file.read())

    except:
        print('Error: data is in binary form!\n'
              '*Now unpickling from binary form.*')
        with open(file_name, 'rb') as file:
            data = pickle.load(file)
        print('Data unpickled from binary form!')
    return data


# Presentation (Input/Output)  -------------------------------------------- #
def display_grades(data):
    """  Displays Student Name and their Grade
    :param data: (list) of student grades you want to show:
    :return nothing
    """
    print('*****STUDENT GRADES*****')
    print(' Name | Grade   ')
    for row in data:
        print(row['Name'] + ' | ' + str(row['Grade']))
    print('************************')


# Main Script -------------------------------------------------------------#
print('---------------Action Log---------------')
print('*Running write_grades function.*')
write_grades(GradeBook, GradeBookFile)
print('*Running read_grades function.*')
GradeBook = read_grades(GradeBookFile)
print('*Now printing unpickled data.*')
display_grades(GradeBook)
print('----------------------------------------')
