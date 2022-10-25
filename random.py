from tkinter import *
import random

root = Tk()
root.title("Random Color")
root.geometry("600x600")
root.config(bg="Slate Gray1")

color = Label(root,font=("Sylfaen",25),bg="Slate Gray1")
color.place(relx=0.5,rely=0.2,anchor=CENTER)

label_score = Label(root,text="Score: ")
label_score.place(relx=0.1,rely=0.1,anchor=CENTER)

text_input = Entry(root)
text_input.place(relx=0.5,rely=0.4,anchor=CENTER)

class game():
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["red","green","blue","yellow","pink","purple","orange","brown","black"]
        self.random_num_for_text = random.randint(0,8)
        self.color = ["red","green","blue","yellow","pink","purple","orange","brown","black"]
        self.random_num_for_color = random.randint(0,8)
        
        color["text"]=self.text[self.random_num_for_text]
        color["fg"]=self.color[self.random_num_for_color]
    
    def __updateScore(self,text_value):
        
        if(text_value==self.color[self.random_num_for_color]):
            print(self.color[self.random_num_for_color])
            self.__score = self.__score+random.randint(0,8)
            label_score["text"]="Score: "+str(self.__score)
    def get_user_value(self,text_value):
        self.__updateScore(text_value)
        

obj = game()
def get_input():
    value = text_input.get()
    obj.get_user_value(value)
    obj.updateGame()
    text_input.delete(0,END)

btn = Button(root,text="Start",command=obj.updateGame,bg="SteelBlue1",relief=FLAT,padx=5,pady=5)
btn.place(relx=0.3,rely=0.5,anchor=CENTER)
btn1 = Button(root,text="Check",command=get_input,bg="Green",relief=FLAT,padx=5,pady=5)
btn1.place(relx=0.7,rely=0.5,anchor=CENTER)
root.mainloop()