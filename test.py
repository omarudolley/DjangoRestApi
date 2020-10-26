import requests


resp = requests.get('http://localhost:8000/api/task-list/',headers={'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAzNTk1NDk3LCJqdGkiOiJjYzgyMjIxY2I3NjI0OGEwOGJhMWEwYjFlZDEwMzFjZCIsInVzZXJfaWQiOjF9.LTVHhLYImulBEzwJpzxIGUmNidWo8gTze_unsRWTyxo'})

data = resp.json()


print(data)
