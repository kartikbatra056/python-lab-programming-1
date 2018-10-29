from easygui import*
import sys
sum=0
while 1:
  msgbox("WELCOME,ENTER PROMO CODE AND GET 50% OFF.")
  msg=("What  type you wanna eat ?")
  title=("Craving something,Have Something.")
  choices=["Breakfast","Indian","Chinese","Italian"]
  choice=choicebox(msg,title,choices)
  if choice=="Breakfast":
        msg1=("What  type you wanna eat,Choose a hotel ?")
        title1=("Craving something,Have Something.")
        choices1=["A1 Pizza","Smokin Joe's camp","Roll Bites"]
        choice1=choicebox(msg1,title1,choices1)
        if choice1="A1 Pizza":
           msg10=("Select your meal.")
           title10=("A1 Pizza") 
           choices10=["Veg cheese Pizza","Special veg  paneer cheese Pizza","Special veg  paneer cheese Pizza"]
            
