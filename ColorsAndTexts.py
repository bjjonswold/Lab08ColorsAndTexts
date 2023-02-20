'''
1. This is because it indexes to up to 4 non-inclusive. So really, it only indexes to 3, which is what we want. 
2. When there is no start value, it will start at default index value 0 and when there is no end, it will index to the end of the list. 
3. As it is written now, every if statement is checked. If they were changed to if, elif, and else, only one statement would be executed. 
4. This code searches each element in txtlist to see if it is found in the "text" list, and if it is, it will index this location, and call the 
same location in the textTranslations list to append the translation to the translated string. 
'''

texts = ["lol", "ttyl", "nvm", "brb", "smh", "idk", "btw"]
textTranslations = ["laughing out loud", "talk to you later", "nevermind", "be right back", "shaking my head", "I don't know", "by the way"]

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
        if word.lower() in texts:
            num = texts.index(word.lower())
            str += " " + textTranslations[num]
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
    return (blue(color) > 0 and red(color) > 230 and green(color) > 230)

print("TESTING", tritanopiaSee("E7F002"))
print("TESTING", tritanopiaSee("03F002"))

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

