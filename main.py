import tkinter as tk
from PIL import ImageTk
from PIL import Image



'''
def Upload(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image=Image.open("hero_h.png")
        self.image_copy=self.image.copy()
    
    def _resize_image(self, event):
        new_width=event.width
        new_height = event.new_height
        self.image = self.image_copy.resize((new_width,new_height))
        self.image.grid(row = 0,column=3,rowspan=2,columnspan=5)

'''




width=900
height=500


def Upload():
    image = Image.open("hero_h.png")
    image_copy = image.copy()
    image = image_copy.resize((width-200, height))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.image=photo
    label.grid(row=0,column=3,rowspan = 8, columnspan = 9)
    

def load():
    image = Image.open("scenery.png")
    image_copy = image.copy()
    image = image_copy.resize((width-200, height))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.image=photo
    label.grid(row=0,column=3,rowspan = 8, columnspan = 9)
    
    


def default():
    image = Image.open("scenery.png")
    image_copy = image.copy()
    image = image_copy.resize((width-200, height))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.image=photo
    label.grid(row=0,column=3,rowspan = 8, columnspan = 9)
    


if __name__ == "__main__":
    width=900
    height=500
    window = tk.Tk()
    window.config(bg="black")
    window.title("Color_Detection")
    window.geometry("900x500") # Here x is not *

    default()
    


    load_btn = tk.Button(window, text="Load Image", width=25, activebackground="grey", activeforeground="blue",bg="red", command=load())
    load_btn.grid(row=0,column=1,columnspan=2, padx=10, pady=50)
    upload_btn = tk.Button(window, text="Upload Image", width=25, activebackground="grey", activeforeground="blue",bg="green", command=default())
    upload_btn.grid(row=1,column=1,columnspan=2,padx=10,pady = 50)

    window.mainloop()
