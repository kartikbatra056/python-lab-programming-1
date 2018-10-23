from easygui import *
import sys
sum=0
while 1:
  msgbox("WElCOME.")
  msg ="What's your Wish list? "
  title = "CATEGORY"
  choices = ["Mobile and Electronics", "All Books", "Bags", "Sports"]
  choice = choicebox(msg, title, choices)
  if choice=="Mobile and Electronics":
     msgbox("mobile and electronics")
     msg_1="What's your Wish list? "
     title_1= "CATEGORY OF MOBILE AND ELECTRONICS"
     choices_1= ["Samsung j6", "Apple Xs", "Redmi note 5 pro", "Redmi 4"]
     choice_1= choicebox(msg_1, title_1, choices_1) 
     if choice_1=="Samsung j6":
          msg_2="PRICE IS 12000 "
          title_2= "SAMSUNG J6"
          choices_2= ["BUY","CANCEL"]
          choice_2= boolbox(msg_2, title_2, choices_2) 
          if choice_2==1:
                a=12000
                sum+=a
     elif choice_1=="Apple Xs":
          msg_2="PRICE IS 15000 "
          title_2= "APPLE XS"
          choices_2= ["BUY","CANCEL"]
          choice_2= boolbox(msg_2, title_2, choices_2) 
          if choice_2==1:
                b=15000
                sum+=b    
     elif choice_1=="Redmi note 5 pro":
          msg_2="PRICE IS 11500 "
          title_2= "REDMI NOTE 5 PRO"
          choices_2= ["BUY","CANCEL"]
          choice_2= boolbox(msg_2, title_2, choices_2) 
          if choice_2==1:
                c=115000
                sum+=c                    
     elif choice_1=="Redmi 4":  
          msg_2="PRICE IS 9500 "
          title_2= "REDMI 4"
          choices_2= ["BUY","CANCEL"]
          choice_2= boolbox(msg_2, title_2, choices_2) 
          if choice_2==1:
                d=9500
                sum+=d             
  elif choice=="All Books":
     msg_11="What's your Wish list? "
     title_11= "CATEGORY OF BOOKS"
     choices_11= ["Wikipedia", "Encyclopedia", "A girl on the train", "Wings of fire"]
     choice_11= choicebox(msg_11, title_11, choices_11) 
     if choice_11=="Wikipedia":
          msg_22="PRICE IS 300 "
          title_22= "Wikipedia"
          choices_22= ["BUY","CANCEL"]
          choice_22= boolbox(msg_22, title_22, choices_22) 
          if choice_22==1:
                e=300
                sum+=e           
     elif choice_11=="Encyclopedia":
          msg_22="PRICE IS 200 "
          title_22= "Encyclopedia"
          choices_22= ["BUY","CANCEL"]
          choice_22= boolbox(msg_22, title_22, choices_22) 
          if choice_22==1:
                f=200
                sum+=f      
     elif choice_11=="A girl on the train":
          msg_22="PRICE IS 250 "
          title_22= "A girl on the train"
          choices_22= ["BUY","CANCEL"]
          choice_22= boolbox(msg_22, title_22, choices_22) 
          if choice_22==1:
                g=250
                sum+=g                             
     elif choice_11=="Wings of fire":  
          msg_22="PRICE IS 350 "
          title_22= "Wings of fire"
          choices_22= ["BUY","CANCEL"]
          choice_22= boolbox(msg_22, title_22, choices_22) 
          if choice_22==1:
                h=350
                sum+=h
  elif choice=="Bags":
     msg_111="What's your Wish list? "
     title_111= "CATEGORY OF BAGS"
     choices_111= ["Nike","Young","Skybags","Adidas"]
     choice_111= choicebox(msg_111, title_111, choices_111) 
     if choice_111=="Nike":
          msg_222="PRICE IS 3000 "
          title_222= "Nike"
          choices_222= ["BUY","CANCEL"]
          choice_222= boolbox(msg_222, title_222, choices_222) 
          if choice_222==1:
                i=3000
                sum+=i           
     elif choice_111=="Young":
          msg_222="PRICE IS 2000 "
          title_222= "Young"
          choices_222= ["BUY","CANCEL"]
          choice_222= boolbox(msg_222, title_222, choices_222) 
          if choice_222==1:
                j=2000
                sum+=j      
     elif choice_111=="Skybags":
          msg_222="PRICE IS 2500 "
          title_222= "Skybags"
          choices_222= ["BUY","CANCEL"]
          choice_222= boolbox(msg_222, title_222, choices_222) 
          if choice_222==1:
                k=2500
                sum+=k                             
     elif choice_111=="Adidas":  
          msg_222="PRICE IS 3500 "
          title_222= "Adidas"
          choices_222= ["BUY","CANCEL"]
          choice_222= boolbox(msg_222, title_222, choices_222) 
          if choice_222==1:
                l=3500
                sum+=l
  elif choice=="Sports":
     msg_1111="What's your Wish list? "
     title_1111= "CATEGORY OF Sports"
     choices_1111= ["Cricket kit","volleyball kit","Badminton kit "]
     choice_1111= choicebox(msg_1111, title_1111, choices_1111) 
     if choice_1111=="Cricket kit":
          msg_2222="PRICE IS 3000 "
          title_2222= "Cricket kit"
          choices_2222= ["BUY","CANCEL"]
          choice_2222= boolbox(msg_2222, title_2222, choices_2222) 
          if choice_2222==1:
                m=3000
                sum+=m           
     elif choice_1111=="volleyball kit":
          msg_2222="PRICE IS 1500 "
          title_2222= "volleyball kit"
          choices_2222= ["BUY","CANCEL"]
          choice_2222= boolbox(msg_2222, title_2222, choices_2222) 
          if choice_2222==1:
                n=1500
                sum+=n      
     elif choice_1111=="Badminton kit":
          msg_2222="PRICE IS 2500 "
          title_2222= "Badminton kit"
          choices_2222= ["BUY","CANCEL"]
          choice_2222= boolbox(msg_2222, title_2222, choices_2222) 
          if choice_2222==1:
                o=2500
                sum+=o 
                
  msg = "Do you want to continue?"
  title = "Please Confirm"
  if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
  else:
	msg="Your total is:"+str(sum)
	title="BILL DESK"
	textbox(msg,title)
        sys.exit(0)  
    
 
