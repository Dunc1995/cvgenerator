from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt, Separator
from examples import custom_style_2
import cvgenerator as cv

# from PyInquirer import style_from_dict, Token, prompt, print_json
# from PyInquirer import Validator, ValidationError

class choice():
    def __init__(self, name, method=None):
        self.name = name
        self.connector = method

    def call_connector(self):
        '''calls the method assigned to the choice object'''
        try:
            self.connector()
        except Exception as e:
            print(str(e))

class menu():
    def __init__(self, name, message, escapable=True, exitable=True):
        self.type = 'list'
        self.name = name
        self.message = message
        self.choices = []
        self.has_been_shown = False
        self.include_back_option = escapable
        self.include_exit_option = exitable
        self.back_option = choice('<<< Back', method=self.__escape_loop)
        self.exit_option = choice('<X> Exit', method=self.__exit)
        
    def show(self):
        '''displays the list menu'''
        output = None
        self.escaped = False
        
        if self.has_been_shown == False:
            self.choices.append(Separator())
            if self.include_back_option == True:
                self.choices.append(self.back_option)
            if self.include_exit_option == True:
                self.choices.append(self.exit_option)
            self.has_been_shown = True

        while self.escaped == False and cv.IS_EXITED == False:
            answer = prompt({
                'type': self.type,
                'name': self.name,
                'message': self.message,
                'choices': self.__get_choice_names()
            }, style=custom_style_2)
            choice = self.__return_choice(answer[self.name])
            output = choice.name
            if not choice == None and not choice.connector == None:
                choice.call_connector()
            else:
                self.escaped = True
        return output

    def add_option(self, input: choice):
        self.choices.append(input)

    def add_options(self, input: list):
        for i in input:
            self.add_option(i)

    def __get_choice_names(self):
        '''takes the choice objects in self.choices and creates a list of their names'''
        output = []
        for choice in self.choices:
            if hasattr(choice, 'name'):
                output.append(choice.name)
            else:
                output.append(choice)
        return output
    
    def __return_choice(self, choice_name):
        '''simply a filter to retrieve the choice object with the choice_name input'''
        output = None
        for x in self.choices:
            try:
                if x.name == choice_name:
                    output = x
            except Exception as e:
                pass
        return output                                

    def __escape_loop(self):
        '''when called, this breaks the while loop in self.show'''
        self.escaped = True

    def __exit(self):
        '''instructs all forms to exit'''
        cv.IS_EXITED = True

class prompts():
    '''
    Dicts for PyInquirer affect the readability of user workflows.
    This class abstracts them away so questions take up little space for complex methods.
    '''
    @staticmethod
    def input_prompt(name: str, message: str, prompt_now=True, default=None):
        '''
        If the prompt is used at invocation, input_prompt will return the user's selection;
        if not it returns the question dict for later use.
        '''
        output = None
        question = {
            'type': 'input',
            'name': name,
            'message': message,
            'default': default
        }
        if prompt_now == True:
            answer = prompt(question)
            output = answer[name]
        else:
            output = question #? Returns the question dict if the question is not asked immediately.
        return output

    @staticmethod
    def list_prompt(name: str, message: str, list_array: list, prompt_now=True):
        '''
        If the prompt is used at invocation, list_prompt will return the user's selection;
        if not it returns the question dict for later use.
        '''
        output = None
        question = {
            'type': 'list',
            'name': name,
            'message': message,
            'choices': list_array
        }
        if prompt_now == True:
            answer = prompt(question)
            output = answer[name]
        else:
            output = question #? Returns the question dict if the question is not asked immediately.
        return output

    @staticmethod
    def question_sequence(questions: list):
        '''
        Simple wrapper for the 'prompt' method. This will return a dict containing user inputs.
        '''
        return prompt(questions)
        
    @staticmethod
    def editor():
        questions = [
            {
                'type': 'editor',
                'name': 'bio',
                'message': 'Edits:\n',
                'eargs': {
                    'editor':'nano',
                    'filename': './config/schemas_hierarchy.yaml'
                }
            }
        ]

        answers = prompt(questions, style=custom_style_2)
        pprint(answers)

    @staticmethod
    def checkbox():
        questions = [
            {
                'type': 'checkbox',
                'qmark': '😃',
                'message': 'Select toppings',
                'name': 'toppings',
                'choices': [ 
                    Separator('= The Meats ='),
                    {
                        'name': 'Ham'
                    },
                    {
                        'name': 'Ground Meat'
                    },
                    {
                        'name': 'Bacon'
                    },
                    Separator('= The Cheeses ='),
                    {
                        'name': 'Mozzarella',
                        'checked': True
                    },
                    {
                        'name': 'Cheddar'
                    },
                    {
                        'name': 'Parmesan'
                    },
                    Separator('= The usual ='),
                    {
                        'name': 'Mushroom'
                    },
                    {
                        'name': 'Tomato'
                    },
                    {
                        'name': 'Pepperoni'
                    },
                    Separator('= The extras ='),
                    {
                        'name': 'Pineapple'
                    },
                    {
                        'name': 'Olives',
                        'disabled': 'out of stock'
                    },
                    {
                        'name': 'Extra cheese'
                    }
                ],
                'validate': lambda answer: 'You must choose at least one topping.' \
                    if len(answer) == 0 else True
            }
        ]

        answers = prompt(questions, style=custom_style_2)
        pprint(answers)

    @staticmethod
    def confirm(message: str, default=False):
        '''Confirms whether a user wants to continue.'''
        answer = prompt({
                'type': 'confirm',
                'message': message,
                'name': 'confirm',
                'default': default,
            }, style=custom_style_2)
        
        return answer['confirm']

    @staticmethod
    def get_separator(input=None):
        return Separator(input)