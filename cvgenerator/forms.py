from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2
import cvgenerator as va

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
        self.escaped = False
        
        if self.has_been_shown == False:
            self.choices.append(Separator())
            if self.include_back_option == True:
                self.choices.append(self.back_option)
            if self.include_exit_option == True:
                self.choices.append(self.exit_option)
            self.has_been_shown = True

        while self.escaped == False and va.IS_EXITED == False:
            answer = prompt({
                'type': self.type,
                'name': self.name,
                'message': self.message,
                'choices': self.__get_choice_names()
            }, style=custom_style_2)
            choice = self.__return_choice(answer[self.name])
            if not choice == None:
                choice.call_connector()

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
        va.IS_EXITED = True

def input_prompt(name: str, message: str, return_immediately=True):
    output = None
    question = {
        'type': 'input',
        'name': name,
        'message': message
    }
    if return_immediately == True:
        answer = prompt(question)
        output = answer[name]
    else:
        output = question #? Returns the question dict if the question is not asked immediately.
    return output
