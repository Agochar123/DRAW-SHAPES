import turtle
import random

dict1={"Shape1":"square","Shape2":"triangle","Shape3":"circle"}
colors=["orange","red","green","blue","yellow"]

#Take user input for the shape and use variable name as user_input

#Fill colors using random function
turtle.begin_fill()

if dict1.get("Shape1")==user_input:
    #Write the code for drawing a square having side = 100
elif #use the get function using key==user_input:
    #Write the code for drawing a triangle having side = 100
elif #use the get function using key==user_input:
    #Draw a square of radius = 100
else:
    print("Enter a value between square, circle and rectangle")
    
turtle.end_fill()