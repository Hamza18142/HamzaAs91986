from tkinter import *

names=[]


class GUIWindow:
    def __init__(self, parent):
        
      background_color = "OldLace"
    
      #frame set up
      self.quiz_frame=Frame(parent, bg=background_color, padx=100, pady=100)
      self.quiz_frame.grid()
      #Create a label widget for the heading
      self.heading_label= Label(self.quiz_frame, text="WARZONE", bg=background_color)
      self.heading_label.grid(row=0, padx=20)

      self.user_label=Label(self.quiz_frame, text="Please enter your name: ", bg=background_color)
      self.user_label.grid(row=1, padx=20)

      #Entry Box
      self.entry_box=Entry(self.quiz_frame)
      self.entry_box.grid(row=2, padx=20, pady=20)

      #Create a Button
      self.continue_button=Button (self.quiz_frame, text="Continue", bg="lime",command=self.name_collection)
      self.continue_button.grid(row=3, padx=20, pady=20)

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to nameslist declared at the beggining
        self.quiz_frame.destroy()



#starting point of the program
if __name__ =="__main__":
    root = Tk()#creating a window
    root.title("WARZONE")#title of the window
    open_quiz=GUIWindow(root)
    root.mainloop() #keep showing the window untill we close import
  