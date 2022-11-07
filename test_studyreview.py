import csv
from studyreview import Question, StudySession

mock_question = {
    "text": "text",
    "responses": ["response 1", "response-2"],
    "correct_res_index": 0,
    "topic_tags": ["topic_tag"]
}

class TestQuestion:
    def test_existence(self):
        TestQuestion.question = Question(*mock_question.values())

    def test_text(self):
        assert TestQuestion.question.text == mock_question["text"]

    def test_responses(self):
        assert TestQuestion.question.responses == mock_question["responses"]

    def test_correct_res_index(self):
        assert TestQuestion.question.correct_res_index == mock_question["correct_res_index"]

    def test_topic_tags(self):
        assert TestQuestion.question.topic_tags == mock_question["topic_tags"]

    def test_to_dict(self):
        assert TestQuestion.question.to_dict() == mock_question

class TestCSV:
    def test_add_question(self):
        TestCSV.session = StudySession()
        # TestCSV.session.add_question(TestQuestion.question)

        with open("./questions.csv", "r") as file:
            questions = list(csv.DictReader(file))

            print("questions in csv:", questions)
            questions_length = len(questions)
            print(questions_length)
            print(type(list(questions)))

            for question in questions:
                print(question)
            assert questions_length > 0

    def test_fetch_questions(self):
        questions = TestCSV.session.fetch_questions()

        assert type(questions) is list
        assert type(questions[0]) is Question
