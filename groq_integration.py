from groq import Groq

def use_groq(text):
    groq = Groq()
    response = groq.process(text)
    return response

if __name__ == "__main__":
    text = "Find the nearest washroom in Italy."
    print("Groq Response:", use_groq(text))
