import random

import requests
from pyfiglet import Figlet
from termcolor import COLORS, cprint


class Joke:
    URL = 'https://icanhazdadjoke.com'

    def __init__(self):
        self._topic = None
        self._total_jokes = None
        self._joke = None
        self.print_intro()
        self.ask_topic()
        self.save_joke_data(self.search_joke())
        self.print(self.get_text())

    @staticmethod
    def print_intro():
        cprint(Figlet().renderText('Dad Joke 3000'),
               random.choice(tuple(COLORS.keys())), attrs=['blink'])

    def ask_topic(self):
        self._topic = input('Let me tell you a joke! Give me a topic: ')

    def search_joke(self):
        return requests.get(
            self.URL + '/search', headers={"accept": "application/json"}, params={'term': self._topic, 'limit': 30}).json()

    def save_joke_data(self, data):
        self._topic = data['search_term']
        self._total_jokes = data['total_jokes']
        if self._total_jokes:
            self._joke = random.choice(data['results'])['joke']

    def get_text(self):
        if not self._total_jokes:
            return f"Sorry, I don't have any jokes about {self.topic}! Please try again"

        if self._total_jokes is 1:
            return f"I've got one joke about {self.topic}. Here it is: \n{self.joke}"

        return f"I've got {self.total_jokes} jokes about {self.topic}. Here's one: \n{self.joke}"

    @staticmethod
    def print(text):
        print(text)


if __name__ == '__main__':
    Joke()
