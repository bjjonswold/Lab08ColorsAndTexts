# Lab08ColorsAndTexts
Functions Review Warmup Lab

# Introduction to Colorblindness
In this lab you will be learning about different types of colorblindness. The three types of colorblindness that we are addressing in this lab are protanopia, deuteranopia, and tritanopia. People with protanopia are unable to perceive ‘red’ light. People with deuteranopia are unable to perceive ‘green’ light. People with tritanopia are unable to perceive ‘blue’ light. All of these are oversimplifications of how colorblindness really works. This lab might suggest that a certain color palette may not work for a type of colorblindness when that is not really the case.

If you are curious about the different types of colorblindness you can click the following link:

https://www.colourblindawareness.org/colour-blindness/types-of-colour-blindness/#:~:text=People%20with%20protanopia%20are%20unable,blues%20and%20yellows%20stand%20out

The reason we are talking about colorblindness in this lab is because it is important to be aware of the colors you are using when developing something such as a website. This is when inclusive design comes into play. When developing a website, for example, you want to make sure to utilize specific colors in order to make sure the website’s visitors will be able to understand all the content.

If you are curious about hexadecimal, read this section. Otherwise, you can jump to step 1. If this is confusing, don’t worry too much about the values actually being stored by hexadecimal, but it can be helpful to have a grasp of alternate numbering schemes. In this lab, we will be utilizing hexadecimal to represent colors. A color can be represented using three values: red, green, and blue. Each of these are typically between 0 and 255, inclusive. A single hexadecimal character can represent a number 0-15, much like how a single decimal character can represent a number 0-9. Counting in hexadecimal looks like

0 1 2 3 4 5 6 7 8 9 A B C D E F 10 11 12 13 14 15 16 17 18 19 1A 1B … FD FE FF

FF is 255, the max value we will be using in this lab. Because each color (red, green, and blue) can be represented using two hexadecimal characters, a combination of these can be represented using six hexadecimal characters. For example, “FFFFFF” is white, as all three values are maxed at 255. You can experiment with creating colors using hexadecimal in the following link:

https://www.google.com/search?q=rgb+color+picker&rlz=1C1CHBF_enUS756US756&oq=rgb+color+picker&aqs=chrome..69i57j0l7.5322j0j1&sourceid=chrome&ie=UTF-8


# In ColorsAndTexts.py is some code
Review the code provided. Answer the following questions by adding comments to your code! You are free to talk with other students, and seek better understanding to these questions. See below for reminders on types, variables, and input

# Step One
Read the code in ColorsAndTexts.py. Complete the following questions in the comments at the top of your code. If your answer is multiple lines, use these: \``` around your answer:
1. Look at green(str). Why is the end index 4 and not 3? 
2. Look at blue(str) and red(str). Note that there is no end value for blue and no start value for red. What does this do?
3. Find the comment in main. What happens if we replace these three if statements with if, elif, and else? How does this change what the code does?
4. How does textToSpeech(txtlst) know what to translate the texts to?

# Step Two: Coding: tritanopiaSee(color)
Find the function tritanopiaSee(color). As a reminder, a function is a way to break up code into repeatable bits to be reused.

Write the code for tritanopiaSee(color) so that if the blue for the color is greater than 0, the red for the color is greater than 230, and the green for the color is greater than 230, it returns true. Otherwise, it should return false.

Ex: for
```
tritanopiaSee("E7F002") 
```
the function would return true
```
tritanopiaSee("03F002") 
```
the function would return false

# Step Three: Test tritanopiaSee(color)
How do you test code? You simply add the lines to your python file (in the future, you will have test lines in separate files).

As such, we would recommend adding the following just above def main().
```
print("TESTING", tritanopiaSee("E70F02"))
print("TESTING", tritanopiaSee("03F002"))
```
Also add your own tests!

# Submitting the Assignment
Make sure to submit the assignment for grading! If you haven't clicked through the canvas link in a while, we would suggest clicking through it again before submitting.

# Reminder on Substrings
Substrings are a way to cut apart strings or extract specific parts of them. We can do this with hardset numbers or with indexes.
# Harset Numbers
These work best when working with something of a set size
```
Ex: str = "Howdy, y'all" str[0:5] = "Howdy"
```
# Indexes
These work best if you don't know how long a section might be
```
Ex: str = "Howdy, y'all" str[0:str.index(",")] = "Howdy"
```
Remember that for both of these, you want your end value to be one more than where you want the end value to actually land because it is not right hand inclusive,
like ranges.
