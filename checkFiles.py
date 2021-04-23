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
        "test.txt"
    ]

# non-code files required for grading, format as [filename:str,]
REQUIRED_NON_CODE_FILES = \
    [
        "environment-setup.png"
    ]

# files to copy to working dir from student submission before running grading
# this is usually a list of extra credit file
OPTIONAL_FILES = \
    [
    ]

# Modified to simulate submission environment
STUDENT_SUBMISSION_PATH = '/autograder/submission/'

OUTPUT_JSON = {'output': '', "score": 0.0}


def execute(command):
    return os.system(command)


def cp(fr, to, flag='', quiet=False):
    cmd = f'cp {flag} {fr} {to}'
    if not quiet:
        print(cmd)
    return execute(cmd)


def rm(path, flag='', quiet=False):
    cmd = f'rm {flag} {path}'
    if not quiet:
        print(cmd)
    return execute(cmd)


def append_visible_output(line):
    OUTPUT_JSON['output'] += line
    OUTPUT_JSON['output'] += '\n'


def write_json_and_quit():
    # floor each case to 0, ceiling each case to max_score
    for case in OUTPUT_JSON['tests']:
        if case['score'] < 0:
            case['score'] = 0
        if case['score'] > case['max_score']:
            case['score'] = case['max_score']

    # sum points
    OUTPUT_JSON['score'] = 0
    '''for test_result in OUTPUT_JSON['tests']:
        if not PRE_DEPLOYMENT or test_result['visibility'] == 'visible':
            test_score = test_result['score']
            OUTPUT_JSON['score'] += test_score

    if PRINT_JSON_BEFORE_EXIT:
        print_section_title('results.json')
        pprint(OUTPUT_JSON, width=150)

    print(f'[grade.py] Final score = [{OUTPUT_JSON["score"]}]')'''

    # write to results.json
    with open('results.json', 'w') as outfile:
        json.dump(OUTPUT_JSON, outfile)
    sys.exit()


def check_files():
    # check whether all non-code files exist
    for filename in REQUIRED_NON_CODE_FILES:
        if os.path.exists(f'{STUDENT_SUBMISSION_PATH}/{filename}'):
            append_visible_output(f'[     FOUND     ] {filename}')
            print(f'[     FOUND     ] {filename}')
        else:
            append_visible_output(f'[    MISSING    ] {filename}')
            print(f'[    MISSING    ] {filename}')

    # check whether all code files exist
    all_code_file_exists = True
    for filename in REQUIRED_CODE_FILES:
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
    #STUDENT_SUBMISSION_PATH = sys.argv[1]

    # copy required code file from submission path to working dir
    # print('Copying over files from student submission, '
    #                    'there can be errors if students are missing file(s)')
    '''for filename in REQUIRED_CODE_FILES:
        # for each required file, if the file already exists in the working
        # dir, remove it, then copy the file from the submission dir
        if os.path.exists(filename):
            rm(filename, '-f')
        cp(f'{STUDENT_SUBMISSION_PATH}/{filename}', '.')

    for filename in OPTIONAL_FILES:
        if os.path.exists(filename):
            rm(filename, '-f')
        cp(f'{STUDENT_SUBMISSION_PATH}/{filename}', '.')
    '''
    # print(os.path.exists('test1.txt'))
    check_files()
    write_json_and_quit()
