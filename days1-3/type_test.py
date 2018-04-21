from bs4 import BeautifulSoup
import requests
from datetime import datetime


def print_header():
    print('------------------------------------')
    print('            TYPE TEST')
    print('------------------------------------')


def get_test_text():
    text_request = requests.get('http://www.randomtextgenerator.com/')
    soup = BeautifulSoup(text_request.text, "html.parser")
    random_text = soup.find(id='generatedtext').get_text().split('\n')[0]
    return random_text

def display_test_text(text):
    print(text)
    return


def process_test_text(text):
    return [x.strip() for x in text.split()]


def take_test():
    input("When you're ready to begin, press <enter>.")
    test_start_time = datetime.today()
    user_text = input()
    test_stop_time = datetime.today()
    test_time = test_stop_time - test_start_time
    return process_test_text(user_text), test_time


def grade_test():
    pass


def display_test_results():
    pass


def main():
    print_header()
    test_text = get_test_text()
    display_test_text(test_text)
    test_key = process_test_text(test_text)
    user_text, test_time = take_test()
    print(test_key, user_text, test_time)
    grade_test()
    display_test_results()


if __name__ == '__main__':
    main()
