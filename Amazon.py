from easygui import *
import sys
while 1:
    msgbox("WElCOME.")
    msg ="What's your Wish list? "
    title = "CATEGORY"
    choices = ["Mobile and Electronics", "All Books", "Bags", "Sports","Cars"]
    choice = choicebox(msg, title, choices)
if choice=="Mobile and Electronics":
     msgbox("mobile and electronics")
     msg ="What's your Wish list? "
     title = "CATEGORY OF MOBILE AND ELECTRONICS"
     choices = ["Mobile phones", "Mobile accesories", "laptops", "Computer appliances","Cameras"]
     choice1 = choicebox(msg, title, choices) 

