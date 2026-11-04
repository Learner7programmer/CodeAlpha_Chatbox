# CodeAlpha_Chatbot

A rule-based console chatbot built for **CodeAlpha Python Programming Internship – Task 4**.

## Features
- Replies to greetings, "how are you", and goodbyes (`Hi!`, `I'm fine, thanks!`, `Goodbye!`)
- Regex-based intent detection, so messy input like `Hey!! how r u?` still works
- Handles multiple intents in one message
- Remembers your name (`my name is ...`)
- Tells the current time and date
- Fallback replies with a hint after repeated misunderstandings
- Clean exit on `bye`, `Ctrl+C`, or `Ctrl+D`

## Concepts Used
| Concept | Where |
|---|---|
| Functions | `normalize`, `extract_name`, `detect_intents`, `respond`, `chat` |
| if-elif | `respond()` |
| Loops | `while True` in `chat()` |
| Regex (`re`) | Intent matching with word boundaries |
| Dictionaries | `RESPONSES`, `memory` |
| Exception handling | `try/except` around `input()` |
| `random`, `datetime` | Varied replies, time and date |

## Project Structure
```
CodeAlpha_Chatbot/
├── chatbot.py        # main program
├── test_chatbot.py   # unit tests
├── README.md
└── .gitignore
```

## How to Run
Requires Python 3.8+ and no external libraries.

```bash
python chatbot.py
```

Run the tests:

```bash
python -m unittest test_chatbot.py -v
```

## Sample Conversation
```
Alpha: Hi! I'm Alpha. Type 'help' to see what I can do.
You: Hey!! how r u?
Alpha: Hey! Nice to see you. I'm fine, thanks!
You: my name is Tanvi
Alpha: Nice to meet you, Tanvi!
Tanvi: what's the time
Alpha: It's 04:15 PM.
Tanvi: bye
Alpha: Goodbye!
```

## Author
Tanvi – CodeAlpha Python Programming Intern
