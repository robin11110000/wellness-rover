from ai_ml_api import AI_ML_API

def use_ai_ml_api(text):
    api = AI_ML_API()
    response = api.text_completion(text)
    return response

if __name__ == "__main__":
    text = "Find the nearest washroom in Italy."
    print("AI/ML API Response:", use_ai_ml_api(text))
