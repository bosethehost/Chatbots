# Import OpenAI and supporting libraries
import os
from openai import OpenAI

def read_text_from_file(filename):
    """
    Reads the first 500 lines of content from a file and returns it as a string.
    Args: filename (str): The name of the file to read.
    Returns: str: The content of the file as a string, or an empty string if the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            return ''.join([next(file) for _ in range(500)])
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return ""

# Read content from the file
content = read_text_from_file("physics_lecture.txt")

# Set up the OpenAI client
client = OpenAI()

# Setting up the recommended model
model = "gpt-4o-mini"

system_prompt = "You are a quiz bot. Your purpose is to generate multiple choice questions from educational text and support educators by creating structured quizzes"

user_prompt = """Create quiz question on any topic. For each question provide 4 options and the answer. Have following sections for quiz question, "Question:", "Options:", and "Answer: <Correct Option>"""

quiz_data = []
def generate_quiz_questions():
    for i in range(5):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_completion_tokens=300,
            messages=[{"role": "system", "content": system_prompt}, 
                      {"role": "user", "content": user_prompt}])
        chatbot_reply = response.choices[0].message.content
        quiz_data.append(chatbot_reply)

generate_quiz_questions()
print(quiz_data)
