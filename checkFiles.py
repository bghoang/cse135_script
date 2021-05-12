#!/usr/bin/env python
import json
import os
import sys
import time
import csv


# check if student submitted required files
CHECK_STUDENT_SUBMITTED_CODE_FILES = True
CHECK_STUDENT_SUBMITTED_NON_CODE_FILES = True
TERMINATE_SCRIPT_IF_MISSING_CODE_FILE = False

# code files required for grading, format as [filename:str,]
REQUIRED_CODE_FILES = \
    [
        "database.html",
        "hellodataviz.html",
        "postman.png",
        "REST.png",
        "database.png",
        "routes.pdf"
    ]

# non-code files required for grading, format as [filename:str,]
REQUIRED_NON_CODE_FILES = \
    [

    ]

# files to copy to working dir from student submission before running grading
# this is usually a list of extra credit file
OPTIONAL_FILES = \
    [
    ]

# Modified to simulate submission environment
STUDENT_SUBMISSION_PATH = 'submission'

OUTPUT_JSON = {'output': ''}


def append_visible_output(line):
    OUTPUT_JSON['output'] += line
    OUTPUT_JSON['output'] += '\n'


def write_json_and_quit():
    # write to results.json
    OUTPUT_JSON['score'] = 0

    path = 'results/'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, 'results.json'), 'w') as outfile:
        json.dump(OUTPUT_JSON, outfile)
    sys.exit()


def check_files():
    # check whether all non-code files exist
    '''for filename in REQUIRED_NON_CODE_FILES:
        print(f'{STUDENT_SUBMISSION_PATH}/{filename}')
        if os.path.exists(f'{STUDENT_SUBMISSION_PATH}/{filename}'):
            append_visible_output(f'[     FOUND     ] {filename}')
            print(f'[     FOUND     ] {filename}')
        else:
            append_visible_output(f'[    MISSING    ] {filename}')
            print(f'[    MISSING    ] {filename}')
    '''

    # check whether all code files exist
    all_code_file_exists = True
    for filename in REQUIRED_CODE_FILES:
        # print(f'{STUDENT_SUBMISSION_PATH}/{filename}')
        if os.path.exists(f'{STUDENT_SUBMISSION_PATH}/{filename}'):
            append_visible_output(f'[     FOUND     ] {filename}')
            print(f'[     FOUND     ] {filename}')
        else:
            append_visible_output(f'[    MISSING    ] {filename}')
            print(f'[    MISSING    ] {filename}')
            all_code_file_exists = False

    # terminate the grading script if source codes are missing and the
    # TERMINATE_SCRIPT_IF_MISSING_CODE_FILE boolean is set to true
    if not all_code_file_exists and TERMINATE_SCRIPT_IF_MISSING_CODE_FILE:
        print('[grade.py] Missing code file, exit')
        write_json_and_quit()


if __name__ == '__main__':
    # print(os.path.exists('/autograder/submission/test.txt'))
    check_files()
    write_json_and_quit()
