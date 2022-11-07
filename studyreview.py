# imports
import random
import csv
import os

questions = [] # temporary until csv storage complete

class Question():
    def __init__(self, text, responses, correct_res_index, topic_tags):
        self.text = text
        self.responses = responses
        self.correct_res_index = correct_res_index
        self.topic_tags = topic_tags

    def to_dict(self):
        return {
            "text": self.text,
            "responses": self.responses,
            "correct_res_index": self.correct_res_index,
            "topic_tags": self.topic_tags
        }

    def __repr__(self):
        return f"{{\ntext: {self.text},\nresponses: {self.responses},\ncorrect_res_index: {self.correct_res_index},\ntopic_tags: {self.topic_tags}\n}}"

# STUDY REVIEW PROJECT
class StudySession():
    def __init__(self, questions = []):
        self.questions = questions

    def startup_prompt(self):
        while True:
            response = input("Type B to begin a study session, Q to add a question or EXIT to end program:\n").upper()

            if response in ("B", "Q", "EXIT"): return response
            
            print("Input invalid.")

    def select_index(self, list, display_text):
        valid_index = False
        while not valid_index:
            selected_index = input(display_text + '\n')

            try:
                selected_index = int(selected_index)
            except(ValueError):
                pass
            
            valid_index = True
            if selected_index not in range(0, len(list)):
                    print("You must provid a valid index from 0 to", len(list) - 1)
                    valid_index = False

        return int(selected_index)

    def question_prompt(self):
        text = input("Provide question text:\n")
        responses = input("Provide comma (,) separated responses:\n").split(',')
        responses = [response.strip() for response in responses]
        for i, response in enumerate(responses):
            print(f"{i}: {response}")

        correct_res_index = self.select_index(responses, "Indicate which response is correct:")

        topic_tags = input("Provide comma (,) separated topic tags:\n").split(',')
        topic_tags = [topic_tag.strip() for topic_tag in topic_tags]

        return Question(text,  responses, int(correct_res_index), topic_tags)

    def add_question(self, question):
        dict_question = question.to_dict()
        fieldnames = list(dict_question.keys())

        if not os.path.exists("./questions.csv"):
            with open("./questions.csv", "w") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

        with open('questions.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames) # create a .to_dict() method
            writer.writerow(dict_question)

    def fetch_questions(self):
        # go into csv
        with open('questions.csv', 'r') as file:
            # retrieve questions as list of dictionaries
            questions = list(csv.DictReader(file))
            # convert dictionaries into Questions
            return [Question(*question.values()) for question in questions]

    def start_review(self):
        user_response = 'Y'
        while user_response.upper() in ('Y', 'YES'):    
            random_question = random.choice(self.fetch_questions())

            print(f"Questions:\n{random_question.text}")
            print("Choices:")
            for i, choice in enumerate(random_question.responses):
                print(f"{i}: {choice}")

            selected_index = self.select_index(random_question.responses, "Select your answer's index:")

            if (selected_index == random_question.correct_res_index):
                print("Correct!")
            else:
                print(f"Incorrect, the correct answer is {random_question.responses[random_question.correct_res_index]}.")

            user_response = input('Would you like to continue your review? (Y/N):\n')

    def start(self):
        response = ''

        while response != 'EXIT':
            response = self.startup_prompt()

            if response == "Q":
                new_question = self.question_prompt()
                self.add_question(new_question)
            elif response == "B":
                self.start_review()

# create new study session
study_session = StudySession()

study_session.start()
