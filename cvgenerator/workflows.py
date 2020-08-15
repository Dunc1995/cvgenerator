from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt
import cvgenerator.classes as classes
import yaml
import json

# def add_value():
#     questions = [{
#         'type': 'input',
#         'name': 'name',
#         'message': 'What is an important value you\'d attribute to your work? (e.g. creativity)\n Please enter a name here:',
#     },
#     {
#         'type': 'input',
#         'name': 'weighting',
#         'message': 'On a scale of 1 to 10, 10 being of most importance to you, what would you rate this value?\n Enter here:',
#     }]
#     answers = prompt(questions)
#     va.VALUES.append(value(answers['name'], int(answers['weighting'])).__dict__)

def remove_value():
    print('not yet implemented')

def on_start():
    print('not yet implemented')

def on_exit():
    print('Route not yet implemented...')

def write_variables():
    print('Route not yet implemented...')

def placeholder():
    print('Route not yet implemented...')

def create_work_experience_template():
    questions = {
        'type': 'input',
        'name': 'name',
        'message': 'Enter a job title...',
    }
    answers = prompt(questions)

    with open('./work_experience/{}.yaml'.format(answers['name']), 'w') as file:
        yaml.dump(classes.work_experience(answers['name']), file)