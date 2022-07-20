
import requests

with requests.get(url="https://opentdb.com/api.php?amount=10&category=22&type=boolean") as response:
    response.raise_for_status()
    question_data = response.json()['results']








