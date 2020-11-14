# Follow Us On Twitter @PY4ALL

from tkinter import *
import tkinter as tk
import random


class gui(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        parent.title('Rock Paper Scissor Game')
        parent.resizable(False, False)
        parent.configure(background = 'white')
        self.canvas =  tk.Canvas(parent, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)

        self.choices = ['Rock','Paper','Scissor']
        self.winlist = [('Rock','Scissor'),('Paper','Rock'),('Scissor','Paper')]
        
        self.r = PhotoImage(file="images/rock.png")
        self.p = PhotoImage(file="images/paper.png")
        self.s = PhotoImage(file="images/scissors.png")
        self.rock_user = self.canvas.create_image(150,150, anchor=CENTER, image=self.r, tags=('rock',))
        self.paper_user = self.canvas.create_image(150,150, anchor=CENTER, image=self.p, tags=('paper',))
        self.scissors_user = self.canvas.create_image(150,150, anchor=CENTER, image=self.s, tags=('scissors',))
        
        self.r2 = self.r.subsample(3)
        self.p2 = self.p.subsample(3)
        self.s2 = self.s.subsample(3)
        self.r_user = self.canvas.create_image(200,350, anchor=CENTER, image=self.r2, tags=('rock',))
        self.p_user = self.canvas.create_image(300,350, anchor=CENTER, image=self.p2, tags=('paper',))
        self.s_user = self.canvas.create_image(400,350, anchor=CENTER, image=self.s2, tags=('scissors',))
        
        self.r_pc = PhotoImage(file="images/rock2.png")
        self.p_pc = PhotoImage(file="images/paper2.png")
        self.s_pc = PhotoImage(file="images/scissors2.png")
        self.rock_pc = self.canvas.create_image(450,150, anchor=CENTER, image=self.r_pc, tags=('rock',))
        self.paper_pc = self.canvas.create_image(450,150, anchor=CENTER, image=self.p_pc, tags=('paper',))
        self.scissors_pc = self.canvas.create_image(450,150, anchor=CENTER, image=self.s_pc, tags=('scissors',))


        self.canvas.create_text(150,30,font='Times 40 bold',text='User', fill='blue')
        self.canvas.create_text(450,30,font='Times 40 bold',text='PC', fill='blue')
        
        self.canvas.tag_bind(self.r_user, "<Button-1>", lambda x: self.run(self.rock_user,'Rock'))
        self.canvas.tag_bind(self.p_user, "<Button-1>", lambda x: self.run(self.paper_user,'Paper'))
        self.canvas.tag_bind(self.s_user, "<Button-1>", lambda x: self.run(self.scissors_user,'Scissor'))
        self.user_count = 0 
        self.pc_count = 0
        self.text_id = self.canvas.create_text(300,295,font='Times 40 bold',text=f'{self.user_count} - {self.pc_count}', fill='blue')
        self.text_pc = self.canvas.create_text(300,260,font='Times 40 bold',text="PC Win This Game!", fill='red')
        self.text_user = self.canvas.create_text(300,260,font='Times 40 bold',text="You Win This Game!", fill='red')
        self.hideall()
        
    def hideall(self):
        self.canvas.itemconfigure(self.rock_pc, state='hidden')
        self.canvas.itemconfigure(self.rock_user, state='hidden')
        self.canvas.itemconfigure(self.paper_pc, state='hidden')
        self.canvas.itemconfigure(self.paper_user, state='hidden')        
        self.canvas.itemconfigure(self.scissors_pc, state='hidden')
        self.canvas.itemconfigure(self.scissors_user, state='hidden')

        self.canvas.itemconfigure(self.text_pc, state='hidden')
        self.canvas.itemconfigure(self.text_user, state='hidden')
        
    def run(self, item, user):
        self.hideall()
        self.canvas.itemconfigure(item, state='normal')
        pc = random.choice(self.choices)
        if pc == 'Rock':
            self.canvas.itemconfigure(self.rock_pc, state='normal')
        elif pc == 'Paper':
            self.canvas.itemconfigure(self.paper_pc, state='normal')
        else:
            self.canvas.itemconfigure(self.scissors_pc, state='normal')


        if user == pc:
            self.canvas.itemconfig(self.text_id, text=f"{self.user_count} - {self.pc_count}")
        elif (user,pc) in self.winlist:
            self.user_count += 1
            self.canvas.itemconfig(self.text_id, text=f"{self.user_count} - {self.pc_count}")
        else:
            self.pc_count += 1
            self.canvas.itemconfig(self.text_id, text=f"{self.user_count} - {self.pc_count}")

        if self.user_count == 10:
            self.canvas.itemconfigure(self.text_user, state='normal')
            self.pc_count = 0
            self.user_count = 0
        elif self.pc_count == 10:
            self.canvas.itemconfigure(self.text_pc, state='normal')
            self.pc_count = 0
            self.user_count = 0
            
    
if __name__ == "__main__":
    root = tk.Tk()
    gui(root)
    root.mainloop()
