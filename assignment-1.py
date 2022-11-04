# %%
# imports
import random

# %%
questions = [] # temporary until csv storage complete

# %%
class Question():
    def __init__(self, text, responses, correct_res_index, topic_tags):
        self.text = text
        self.responses = responses
        self.correct_res_index = correct_res_index
        self.topic_tags = topic_tags

    def __repr__(self):
        return f"{{\ntext: {self.text},\nresponses: {self.responses},\ncorrect_res_index: {self.correct_res_index},\ntopic_tags: {self.topic_tags}\n}}"

# %%
# STUDY REVIEW PROJECT
class Study_Session():
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
        questions.append(question)

    def start_review(self):
        user_response = 'Y'
        while user_response.upper() in ('Y', 'YES'):    
            random_question = random.choice(questions)

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

# %%
# create new study session
study_session = Study_Session()

# %%
study_session.start()


