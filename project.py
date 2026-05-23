def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey", "sup"]:
        return "Hello! How can I help you today?"

    elif user_input in ["how are you", "hru", "how are you?"]:
        return "I'm just a bot, but I'm doing great! Thanks for asking 😊"

    elif "your name" in user_input or "who are you" in user_input:
        return "I'm RuleBot 🤖! A simple rule-based chatbot!"

    elif user_input in ["help", "help me", "what can you do", "what can you do?"]:
        return ("I can respond to:\n"
                "  - Greetings (hi, hello, hey)\n"
                "  - Questions about me (who are you, your name)\n"
                "  - Small talk (how are you, tell me a joke)\n"
                "  - Type 'quit' or 'bye' to exit")

    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? Because light attracts bugs! xD"

    elif "time" in user_input or "date" in user_input:
        from datetime import datetime
        now = datetime.now()
        return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

    elif "weather" in user_input:
        return "I wish I could check the weather, but I have no internet access! Try meteo.com 🌤️"

    elif user_input in ["thanks", "thank you", "thnx", "ty"]:
        return "You're welcome!"

    elif user_input in ["quit", "exit", "bye", "goodbye", "q"]:
        return "EXIT"

    else:
        return "Hmm, I don't understand that. Type 'help' to see what I can do"


def main():
    print("=" * 45)
    print("       Welcome to RuleBot 🤖")
    print("  Type 'help' to see available commands.")
    print("  Type 'quit' or 'bye' to exit.")
    print("=" * 45)

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                print("RuleBot: Please type something!")
                continue

            response = get_response(user_input)

            if response == "EXIT":
                print("RuleBot: Goodbye! Have a great day! 👋")
                break

            print(f"RuleBot: {response}")

        except KeyboardInterrupt:
            print("\nRuleBot: Goodbye! Have a great day! 👋")
            break


if __name__ == "__main__":
    main()