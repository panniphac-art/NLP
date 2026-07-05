import re

def eliza_response(user_input):
    rules = [
        # I am depressed / sad
        (
            re.compile(r".*\bI'?M\s+(DEPRESSED|SAD)\b.*", re.IGNORECASE),
            lambda m: f"I AM SORRY TO HEAR YOU ARE {m.group(1).upper()}."
        ),

        # I am ...
        (
            re.compile(r".*\bI'?M\s+(.+)", re.IGNORECASE),
            lambda m: f"WHY DO YOU THINK YOU ARE {m.group(1).upper()}?"
        ),

        # all
        (
            re.compile(r".*\bALL\b.*", re.IGNORECASE),
            lambda m: "IN WHAT WAY?"
        ),

        # always
        (
            re.compile(r".*\bALWAYS\b.*", re.IGNORECASE),
            lambda m: "CAN YOU THINK OF A SPECIFIC EXAMPLE?"
        ),

        # my boyfriend
        (
            re.compile(r".*\bMY BOYFRIEND\b.*", re.IGNORECASE),
            lambda m: "YOUR BOYFRIEND MADE YOU COME HERE?"
        ),

        # my girlfriend
        (
            re.compile(r".*\bMY GIRLFRIEND\b.*", re.IGNORECASE),
            lambda m: "YOUR GIRLFRIEND MADE YOU COME HERE?"
        ),
    ]

    for pattern, response in rules:
        match = pattern.match(user_input)
        if match:
            return response(match)

    return "PLEASE TELL ME MORE."


def main():
    print("=" * 40)
    print("         ELIZA Chatbot")
    print("Type 'quite' เพื่อออกจากโปรแกรม")
    print("=" * 40)

    while True:
        user = input("\nYou : ")

        if user.lower() == "quite":
            print("ELIZA : GOODBYE.")
            break

        print("ELIZA :", eliza_response(user))


if __name__ == "__main__":
    main()
