import random
import requests
import json

parameters = {
    "amount": 10,
    "type": "boolean"

}

get_new_questions = requests.get(url="https://opentdb.com/api.php?", params=parameters)

get_new_questions.raise_for_status()
data = get_new_questions.json()
question_data = (data['results'])
print(question_data[0])
