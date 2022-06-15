textTranslations = {
    "lol" : "laughing out loud",
    "ttyl" : "talk to you later",
    "nvm" : "nevermind",
    "brb" : "be right back",
    "smh" : "shaking my head",
    "idk" : "I don't know",
    "btw" : "by the way"

}

#reads in files and puts the items into lists--if the files have sentences, it separates the words in the list
def readFile(fileName):
    lst = []
    with open(fileName) as file:
        for lines in file:
            for word in lines.split():
                lst.append(word)
    return lst

#input: a list of words from a text
#output: the text with the abbrieviations from textTranslations elongated
def textToSpeech(txtlst):
    str = ""
    for word in txtlst:
        if word.lower() in textTranslations:
            str += " " + textTranslations[word.lower()]
        else:
            str += " " + word
    return "Translated: " + str

#input: string of RGB values
#output: the red value
def red(str):
    return int(str[:2], 16)

#input: string of RGB values
#output: the green value
def green(str):
    return int(str[2: 4], 16) #Why 4?

#input: string of RGB values
#output: the blue value
def blue(str):
    return int(str[4:], 16) #what happens when we don't put the second value?

# input: color as RGB code
#output: true or false depending on if a person with protanopia could see it
def protanopiaSee(color):
    return red(color) < 64

# input: color as RGB code
#output: true or false depending on if a person with deuteranopia could see it
def deuteranopiaSee(color):
    return green(color) < 64

# input: color as RGB code
#output: true or false depending on if a person with tritanopia could see it
def tritanopiaSee(color):
    #student code
    return False

def main():
    text = readFile("text.txt")
    print(textToSpeech(text))
    colors = readFile("colors.txt")
    for color in colors:
        str = "Can see: "
        if protanopiaSee(color):
            str += "protanopia "
        if deuteranopiaSee(color): #What might happen if we used an elif here? and the next was an else?
            str += "deuteranopia "
        if tritanopiaSee(color):
            str += "tritanopia"
        if not protanopiaSee(color) and not deuteranopiaSee(color) and not tritanopiaSee(color):
            str += "None"
        print(str)

if __name__ == "__main__":
    main()

