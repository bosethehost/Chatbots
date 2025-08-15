import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

audio_file = open("data/sample.wav","rb")

transcription_response = client.audio.transcriptions.create(model="whisper-1",file=audio_file)

transcription_text = transcription_response.text

# Extract translated text
target_language = "French"

translation_response = client.chat.completions.create(model="gpt-4o-mini",
                                                      max_completion_tokens=300,
                                                      messages=[{"role": "user", "content": f"""Translate {transcription_text} to {target_language}: """}])

translated_text = translation_response.choices[0].message.content

grammar_response = client.chat.completions.create(model="gpt-4o-mini",
                                                  max_completion_tokens=300,
                                                  messages=[{"role": "user", 
                                                             "content": f"""Analyze {translated_text} for grammatical errors and provide corrections"""}])

grammar_feedback = grammar_response.choices[0].message.content

target_text = "Heat brings out flavor, cold restores, salt complements ham, tacos are a favorite, and hot cross buns are zestful."

pronunciation_response = client.chat.completions.create(model="gpt-4o-mini",
                                                        max_completion_tokens=300,
                                                        messages = [{"role": "user", "content": f"""Compare original transcription {transcription_text} with user defined target pronunciation {target_text}. Provide suggestions for improvement: """}])

pronunciation_feedback = pronunciation_response.choices[0].message.content
print(pronunciation_feedback)
