from tkinter import *
from PIL import ImageTk, Image #this import to use images

names=[]


class GUIWindow:
    def __init__(self, parent):
        
      background_color = "OldLace"
          #frame set up
      self.quiz_frame=Frame(parent, bg=background_color)
      self.quiz_frame.grid()

      #open image
      self.start_image = Image.open("start.png")
      self.start_image = self.start_image.resize((650,550), Image.ANTIALIAS)
      self.start_image = ImageTk.PhotoImage(self.start_image)
      #display image in a label
      self.image_label = Label(self.quiz_frame, image=self.start_image)
      self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
   
      #Entry Box
      self.entry_box=Entry(self.quiz_frame)
      self.entry_box.grid(row=2, padx=250, pady=200)

      #Create a Button
      self.continue_button=Button (self.quiz_frame, text="Continue", bg="lime",command=self.name_collection)
      self.continue_button.grid(row=3, padx=20)

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to nameslist declared at the beggining
        self.quiz_frame.destroy()



#starting point of the program
if __name__ =="__main__":
    root = Tk()#creating a window
    root.title("CALL OF DUTY WARZONE")#title of the window
    open_quiz=GUIWindow(root)
    root.mainloop() #keep showing the window untill we close import
  