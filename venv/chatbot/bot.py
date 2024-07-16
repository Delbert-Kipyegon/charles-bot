# chatbot/bot.py
import vertexai  

# import gemeniaai
from .config import VERTEXAI_API_KEY, GEMENIAAI_API_KEY

vertexai.init(api_key=VERTEXAI_API_KEY)
# gemeniaai.init(api_key=GEMENIAAI_API_KEY)


def get_response_from_vertexai(message):
    # Implement VertexAI response logic
    response = vertexai.Completion.create(prompt=message)
    return response.choices[0].text


# def get_response_from_gemeniaai(message):
#     # Implement GeminiAI response logic
#     response = gemeniaai.Completion.create(prompt=message)
#     return response.choices[0].text


def get_chatbot_response(message):
    response_vertexai = get_response_from_vertexai(message)
    # response_gemeniaai = get_response_from_gemeniaai(message)
    # return f"VertexAI: {response_vertexai}\nGeminiAI: {response_gemeniaai}"
    return f"VertexAI: {response_vertexai}"
