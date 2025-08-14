import random

def get_random_fortune(messages):
    """
    Returns a random fortune message from the given list.
    """
    return random.choice(messages)

def main():
    fortune_messages = [
        "Aaj ka din shubh hai!",
        "Kuch bada hone wala hai!",
        "Mehnat ka phal meetha hota hai.",
        "Naye logon se milne ka mauka milega.",
        "Apne sapno ka peecha karo.",
        "Luck tumhare sath hai!",
        "Kamyabi tumhare kadam chumegi.",
        "Har mushkil asaan banegi.",
        "Tumhara hard work nazar aa raha hai.",
        "Aaj coffee free mil sakti hai 😉",
        "Kal ka tension chhodo, aaj ka maza lo!",
        "Kisi purane dost ka message aane wala hai.",
        "Tumhe jaldi ek achi khabar milegi.",
        "Aaj tumhara smile kisi ka din bana dega 😊",
        "Unexpected paise mil sakte hain 💰",
        "Tumhare ideas aaj hit hone wale hain!",
        "Kisi ne tumhare liye dua maangi hai 🙏",
        "Tumhare efforts ka reward milne wala hai.",
        "Aaj ka mood: sirf positive vibes ✨",
        "Kuch tasty khane ka mauka mil sakta hai 🍕"
    ]

    print("🥠 Welcome to the Fortune Cookie Machine!")
    print("Type 'exit' to quit at any time.")

    while True:
        user_input = input("\nPress 'Enter' to open a cookie: ").strip().lower()

        if user_input == 'exit':
            print("✨ Thank you for visiting! Have a great day! ✨")
            break
        elif user_input == '':
            fortune = get_random_fortune(fortune_messages)
            print(f"\n🔮 Your Fortune:\n{fortune}")
        else:
            print("⚠ Invalid input. Press Enter for a fortune or type 'exit' to quit.")

if __name__ == "__main__":
    main()
