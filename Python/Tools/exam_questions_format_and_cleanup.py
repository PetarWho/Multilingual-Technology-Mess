# This project will format questions and remove repeating questions and export it as JSON
# If there are 2 or more same questions with different answer,
# they will be displayed, so you know there are such occurances
# How it works:
# You should have a dot at the start of the question, or numbered order like this:
# 31. What color is a banana  or this .What color is a banana
# The possible answer options should be all on a new line and the correct one should have this symbol in front "~"
# Here is an example
# 31. What color is a banana
# a) red
# orange
# - black
# ~4) yellow
# As you can see it doesn't matter if your options are ordered by numbers/letters/hyphens or nothing, all you have
# to do is put this "~" in front of the correct answer
# If there are open questions to answer, you should put "o" in front of it, and if this is an exam that you want
# to check and study from, you can put the correct answer below it like this:
# o13. What is your height:
# My height is a secret!!
# And now finally, to separate one question from another, put empty line between questions, here is an example:
# o16. What is your credit card info:
# 2345 5432 1234 1234
#
# 17. Is there enough money for me to buy a bike?
# a) yes
# b) no
#
#
# Now save all the questions to one txt file called "questions.txt"


import json
import re


class Question:
    def __init__(self, question: str, possible_answers: list, correct_answer: str):
        self.question = question
        self.possible_answers = possible_answers
        self.correct_answer = correct_answer

    def to_dict(self):
        return {
            "question": self.question,
            "possible_answers": self.possible_answers,
            "correct_answer": self.correct_answer
        }


def normalize_answer(answer: str) -> str:
    # Remove ordering symbols and brackets at the beginning of the answer
    return re.sub(r'^[).-]|^\w+[)}\]\/.]+| +', '', answer.lower().strip(), flags=re.UNICODE)


def normalize_answer_display(answer: str) -> str:
    # Remove ordering symbols and brackets at the beginning of the answer
    return re.sub(r'^[).-]|^\w+[)}\]\/.]+', '', answer.strip(), flags=re.UNICODE)


def normalize_question(text: str) -> str:
    # Convert to lowercase, remove all non-alphanumeric Unicode characters, and strip whitespace
    return re.sub(r'[\W]| ', '', text.lower().strip(), flags=re.UNICODE)


def parse_questions(file_content):
    questions = []
    repeating_with_different_answers = []
    same_question_same_answer_count = 0
    question_map = {}

    current_question = None
    current_answers = []
    correct_answer = None

    lines = file_content.splitlines()

    for line in lines:
        line = line.strip()

        if not line:
            # End of a question block
            if current_question:
                normalized_question = normalize_question(current_question)
                normalized_answers = [normalize_answer(ans) for ans in current_answers]
                normalized_answers_display = [normalize_answer_display(ans) for ans in current_answers]
                q_obj = Question(current_question, normalized_answers_display, correct_answer)
                if normalized_question in question_map:
                    existing_question = question_map[normalized_question]
                    if existing_question.correct_answer and correct_answer:
                        if set([normalize_answer(answ) for answ in existing_question.possible_answers]) == set(normalized_answers):
                            # Check if possible answers are the same
                            if normalize_answer(existing_question.correct_answer.lower()) != normalize_answer(correct_answer.lower()):
                                repeating_with_different_answers.append(q_obj)
                            else:
                                same_question_same_answer_count += 1
                else:
                    questions.append(q_obj)
                    question_map[normalized_question] = q_obj

                current_question = None
                current_answers = []
                correct_answer = None
            continue

        if re.match(r'^(\d+\.\s*|\.)', line) or re.match(r'^o\d+\.\s*', line):
            # New question
            if re.match(r'^o\d+\.\s*', line):
                current_question = re.sub(r'^o\d+\.\s*', '', line)
                correct_answer = None  # No correct answer for open questions
            else:
                current_question = re.sub(r'^\d+\.\s*', '', line)
        else:
            if line.startswith('~'):
                correct_answer = normalize_answer_display(line[1:].strip())
                current_answers.append(correct_answer)
            else:
                current_answers.append(normalize_answer_display(line))

    # Final check if the file does not end with a blank line
    if current_question:
        normalized_question = normalize_question(current_question)
        normalized_answers = [normalize_answer(ans) for ans in current_answers]
        normalized_answers_display = [normalize_answer_display(ans) for ans in current_answers]
        q_obj = Question(current_question, normalized_answers_display, correct_answer)
        if normalized_question in question_map:
            existing_question = question_map[normalized_question]
            if existing_question.correct_answer and correct_answer:
                if existing_question.correct_answer.lower() != correct_answer.lower():
                    if set(existing_question.possible_answers) == set(normalized_answers):
                        repeating_with_different_answers.append(q_obj)
                    else:
                        questions.append(q_obj)
                else:
                    if set(existing_question.possible_answers) == set(normalized_answers):
                        same_question_same_answer_count += 1
            else:
                questions.append(q_obj)
        else:
            questions.append(q_obj)
            question_map[normalized_question] = q_obj

    return questions, repeating_with_different_answers, same_question_same_answer_count



def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    file_content = read_file("questions.txt")
    questions, repeating_with_different_answers, same_question_same_answer_count = parse_questions(file_content)

    questions_dict = [q.to_dict() for q in questions]
    repeating_dict = [q.to_dict() for q in repeating_with_different_answers]

    # Remove ordering symbols from answers and correct answers
    for q in questions_dict:
        q["possible_answers"] = [normalize_answer_display(ans) for ans in q["possible_answers"]]
        q["correct_answer"] = normalize_answer_display(q["correct_answer"]) if q["correct_answer"] else q["correct_answer"]
    for q in repeating_dict:
        q["possible_answers"] = [normalize_answer_display(ans) for ans in q["possible_answers"]]
        q["correct_answer"] = normalize_answer_display(q["correct_answer"]) if q["correct_answer"] else q["correct_answer"]

    output_data = {
        "questions": questions_dict,
        "repeating_with_different_answers": repeating_dict,
        "same_question_same_answer_count": same_question_same_answer_count
    }

    write_json(output_data, "questions.json")

    # Print the same_question_same_answer_count
    print(f"Removed {same_question_same_answer_count} same questions with same answers")

    # Generate JSON file for questions with different answers
    different_answers_data = {
        "questions": [q.to_dict() for q in repeating_with_different_answers if q.to_dict() not in questions_dict]
    }

    # Remove ordering symbols from answers in the different answers file
    for q in different_answers_data["questions"]:
        q["possible_answers"] = [normalize_answer_display(ans) for ans in q["possible_answers"]]
        q["correct_answer"] = normalize_answer_display(q["correct_answer"]) if q["correct_answer"] else q["correct_answer"]

    write_json(different_answers_data, "questions_different_answers.json")


if __name__ == "__main__":
    main()

