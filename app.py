# convert emoji converter to a function

def emoji_converter(str):
    words = str.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😔"
    }
    output = ""

    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")

print(emoji_converter(message))