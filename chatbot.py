#CodeAlpha Python Internship - Task 4: Rule-Based Chatbot.
import re
import random
from datetime import datetime

BOT = "Alpha"

RESPONSES = {
    "greet":  ["Hi!", "Hello there!", "Hey! Nice to see you."],
    "status": ["I'm fine, thanks!", "Doing great, thanks for asking!","I am great!! what is your name?"],
    "bye":    ["Goodbye!", "See you later, take care!"],
    "thanks": ["You're welcome!", "Happy to help!"],
}

HELP_TEXT = (
    "I understand: greetings, 'how are you', 'my name is ...', "
    "'time', 'date', 'thanks', and 'bye'."
)


def normalize(text: str) -> str:
    text = re.sub(r"[^a-z0-9\s']", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def extract_name(raw: str):
 
    match = re.search(r"\b([a-zA-Z]+)" or r"\b(my name is) ([a-zA-Z]+)", raw, re.IGNORECASE)
    return match.group(1).capitalize() if match else None


def detect_intents(text: str) -> list:
    intents = []
    if re.search(r"\b(hello|hi|hey|hola)\b", text):
        intents.append("greet")
    if re.search(r"\bhow (are|r) (you|u)\b", text):
        intents.append("status")
    if re.search(r"\b(thanks|thank you|thx)\b", text):
        intents.append("thanks")
    if re.search(r"\b(time|clock)\b", text):
        intents.append("time")
    if re.search(r"\b(date|today)\b", text):
        intents.append("date")
    if re.search(r"\bhelp\b", text):
        intents.append("help")
    if re.search(r"\b(bye|goodbye|exit|quit|see you)\b", text):
        intents.append("bye")
    return intents


def respond(intent: str, memory: dict) -> str:
    if intent == "greet":
        name = f" {memory['name']}" if memory["name"] else ""
        return random.choice(RESPONSES["greet"]).replace("!", f"{name}!", 1)
    elif intent == "status":
        return random.choice(RESPONSES["status"])
    elif intent == "thanks":
        return random.choice(RESPONSES["thanks"])
    elif intent == "time":
        return "It's " + datetime.now().strftime("%I:%M %p") + "."
    elif intent == "date":
        return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."
    elif intent == "help":
        return HELP_TEXT
    elif intent == "bye":
        return random.choice(RESPONSES["bye"])
    return "Hmm, I didn't get that."


def chat():
    memory = {"name": None, "misses": 0}
    print(f"{BOT}: Hi! I'm {BOT}. Tell me your name! or Type 'help' to see what I can do.")

    while True:
        try:
            raw = input(f"{memory['name'] or 'You'}: ")
        except (EOFError, KeyboardInterrupt):
            print(f"\n{BOT}: Goodbye!")
            break

        text = normalize(raw)
        if not text:
            print(f"{BOT}: Say something, I'm listening.")
            continue

        name = extract_name(raw)
        if name:
            memory["name"] = name
            print(f"{BOT}: Nice to meet you, {name}!")
            continue

        intents = detect_intents(text)

        if not intents:
            memory["misses"] += 1
            reply = "Sorry, I didn't understand that."
            if memory["misses"] >= 2:
                reply += " Type 'help' to see what I can do."
            print(f"{BOT}: {reply}")
            continue

        memory["misses"] = 0
        print(f"{BOT}: " + " ".join(respond(i, memory) for i in intents))

        if "bye" in intents:
            break


if __name__ == "__main__":
    chat()
