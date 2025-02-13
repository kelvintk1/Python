alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l",
"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l","m", "n", "o",
 "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
end = True
while end == True:
    direction = input("Type 'Encrypt / Encode' to encrypt or 'Decode / Decrypt' to decrypt\n").lower()
    text = input("Type your message.\n").lower()
    shift = int(input("What is your shift number?\n"))

    def Caeser(Plain_text, shift_N, Direction):
        if direction == "encrypt" or direction == "encode":
            cypher_text = ""
            for letter in Plain_text:
                if letter in alphabets:
                    position = alphabets.index(letter)
                    shift_N = shift % 25
                    New_position = position + shift_N
                    new_letter = alphabets[New_position]
                    cypher_text += new_letter
                else:
                    cypher_text += letter
            print(f"This is your encrypted text🕵️‍♂️🥷: \n{cypher_text}")
        elif direction == "decode" or direction == "decrypt":
            Cypher_text = ""
            for letter in Plain_text:
                if letter in alphabets:
                    position = alphabets.index(letter)
                    shift_N = shift % 25
                    New_position = position - shift_N
                    new_letter = alphabets[New_position]
                    Cypher_text += new_letter
                else:
                    Cypher_text += letter
            print(f"This is your decoded text🔎💻: \n{Cypher_text}")
        else:
            print("Your input is incorrect.")
    Caeser(Plain_text=text, shift_N=shift, Direction=direction)
    questions = input("Do you wants to restart? \n").lower()
    if questions == "yes":
        end = True
    elif questions == "no":
        end = False
        print("Goodbye👋")
    else:
        end = False
        print("Check your input well.❌")

