from google import genai

client = genai.Client(api_key="AQ.Ab8RN6IkY9jL1IVqse6CYdoJtWF5bZOWzOLrjaX7b13g8TRmAg")

for model in client.models.list():
    print(model.name)