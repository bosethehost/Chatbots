# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

instruction_prompt = 'You are a tour guide. You must answer questions of tourists'

corrected_text = ['How far away is the Louvre from the Eiffel Tower (in miles only) if you are driving?', 'Where is the Arc de Triomphe?', 'What are the must-see artworks at the Louvre Museum?']


# Start coding here
conversation = []
for i in range(3):
    conversation.append({"role": "system", "content": instruction_prompt})
    conversation.append({"role": "user", "content": corrected_text[i]})
    
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": instruction_prompt},{"role": "user", "content": corrected_text[i]}],
        max_completion_tokens=100,
        temperature = 0.0)
    
    text = response.choices[0].message.content
    conversation.append({'role':'assistant','content':text})
# Add as many cells as you like
