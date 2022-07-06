
from base64 import b16decode
from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.tix import COLUMN
from turtle import color 
y=" "
x=2
player_1=[]
player_2=[]

def define_sign(number):
    global x,y
    global player_1,player_2
    from itertools import permutations
    set1=permutations([1,2,3])
    set2=permutations([3,5,7])
    set3=permutations([1,5,9])
    set4=permutations([4,5,6])
    set5=permutations([7,8,9])
    set6=permutations([1,4,7])
    set7=permutations([2,5,8])
    set8=permutations([3,6,9])
    
    for i in set1,set2,set3,set4,set5,set6,set7,set8:
        for j in list(i):
            plyr_1=all(elem in player_1 for elem in j)
            plyr_2=all(elem in player_2 for elem in j)
            if plyr_1==True:
                print("player 1 wins")
                showinfo ("game result","player 1 has won(congratulation)")
                break
            elif plyr_2==True:
                print("player 2 wins")
                showinfo("game result","player 2 has won(congratulation)")
                break
            else:
                pass
                
    if number==1:
        if x%2==0:
            y="X"
            player_1.append(number)
            print(player_1)
        elif x%2!=0:
            y="O"
            player_2.append(number)
            print(player_2)
        b1.config(text=y)
        x=x+1
        
    if number==2:
        if x%2==0:
            y="X"
            player_1.append(number)
            print(player_1)
        elif x%2!=0:
            y="O"
            player_2.append(number)
            print(player_2)
        b2.config(text=y)
        x=x+1
        
    if number==3:
        if x%2==0:
            y="X"
            player_1.append(number)
            print(player_1)
        elif x%2!=0:
            y="O"
            player_2.append(number)
            print(player_2)
        b3.config(text=y)
        x=x+1
        
    if number==4:
        if x%2==0:
            y="X"
            player_1.append(number)
            print(player_1)
        elif x%2!=0:
            y="O"
            player_2.append(number)
            print(player_2)
        b4.config(text=y)
        x=x+1
    
    if number==5:
        if x%2==0:
            y="X"
            player_1.append(number)
            print(player_1)
        elif x%2!=0:
            y="O"
            player_2.append(number)
            print(player_2)
        b5.config(text=y)
        x=x+1
        
    if number==6:
        if x%2==0:
            y="X"
            player_1.append(number)
            print(player_1)
        elif x%2!=0:
            y="O"
            player_2.append(number)
            print(player_2)
        b6.config(text=y)
        x=x+1
    
    if number==7:
        if x%2==0:
            y="X"
            player_1.append(number)
            print(player_1)
        elif x%2!=0:
            y="O"
            player_2.append(number)
            print(player_2)
        b7.config(text=y)
        x=x+1
        
    if number==8:
        if x%2==0:
            y="X"
            player_1.append(number)
            print(player_1)
        elif x%2!=0:
            y="O"
            player_2.append(number)
            print(player_2)
        b8.config(text=y)
        x=x+1
    
    if number==9:
        if x%2==0:
            y="X"
            player_1.append(number)
            print(player_1)
        elif x%2!=0:
            y="O"
            player_2.append(number)
            print(player_2)
        b9.config(text=y)
        x=x+1
        
root = Tk()
root.title("TIC-TEC-TOE GAME")

l1=Label(root,text="player 1 : X ")
l1.grid(row=0,column=1)

l2=Label(root,text="player 2 : O ")
l2.grid(row=0,column=2)

b1=Button(root,width=20,height=10,bg='light pink',activebackground='skyblue',command=lambda: define_sign(1))
b1.grid(row=1,column=1)

b2=Button(root,width=20,height=10,bg='light pink',activebackground='skyblue',command=lambda: define_sign(2))
b2.grid(row=1,column=2)

b3=Button(root,width=20,height=10,bg='light pink',activebackground='skyblue',command=lambda: define_sign(3))
b3.grid(row=1,column=3)

b4=Button(root,width=20,height=10,bg='light pink',activebackground='skyblue',command=lambda: define_sign(4))
b4.grid(row=4,column=1)

b5=Button(root,width=20,height=10,bg='light pink',activebackground='skyblue',command=lambda: define_sign(5))
b5.grid(row=4,column=2)

b6=Button(root,width=20,height=10,bg='light pink',activebackground='skyblue',command=lambda: define_sign(6))
b6.grid(row=4,column=3)

b7=Button(root,width=20,height=10,bg='light pink',activebackground='skyblue',command=lambda: define_sign(7))
b7.grid(row=8,column=1)

b8=Button(root,width=20,height=10,bg='light pink',activebackground='skyblue',command=lambda: define_sign(8))
b8.grid(row=8,column=2)

b9=Button(root,width=20,height=10,bg='light pink',activebackground='skyblue',command=lambda: define_sign(9))
b9.grid(row=8,column=3)

root.mainloop()

# import tkinter.massagebox
# p1_score=StringVar()
# p2_score=StringVar()
# ptr1=0
# ptr2=0
# flag=True
# ctr=1

# def play(btn):
#     global flag,ctr
#     if btn["text"]==" " and flag==True:
#         flag=False
#         btn["text"]="X"
#         ctr+=1
#         Check()
#     elif btn["text"]==" " and flag==False:
#         flag=True
#         btn["text"]="O"
#         ctr+=1
#         Check()
#     else:
#         tkinter.massagebox.showinfo("Learn TechTotech","Not Allowed")
# def ClearButton():
#     button1["text"]=" "
#     button2["text"]=" "
#     button3["text"]=" "
#     button4["text"]=" "
#     button5["text"]=" "
#     button6["text"]=" "
#     button7["text"]=" "
#     button8["text"]=" "
#     button9["text"]=" "

# def Check():
#     globle, ptr1,ptr2,p1_score,p2_score,ctr
#     if button1["text"] =="X" and button2["text"] == "X" and button3["text"] =="X" or 
#         button4["text"] =="X" and button5["text"] == "X" and button6["text"] =="X" or
#         button7["text"] =="X" and button8["text"] == "X" and button9["text"] =="X" or
#         button1["text"] =="X" and button4["text"] == "X" and button7["text"] =="X" or
#         button2["text"] =="X" and button5["text"] == "X" and button8["text"] =="X" or
#         button3["text"] =="X" and button6["text"] == "X" and button9["text"] =="X"
#         button1["text"] =="X" and button5["text"] == "X" and button9["text"] =="X"
#         button3["text"] =="X" and button5["text"] == "X" and button7["text"] =="X"
#         ClearButton()
#         tkinter.massagebox.showinfo("TIC-TAC-TOE", "Player 1 Win")
#         ptr1+=1
#         ctr=0
#         p1_score.set(ptr1)
        
        









