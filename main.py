import tkinter as tk
from PIL import ImageTk
from PIL import Image
from tkinter import filedialog as fd 
import cv2


width=900
height=500
flag = False

def Upload():
    name = fd.askopenfilename(title = "Select file", filetypes = ((("png files","*.png"),("jpeg files","*.jpg"))))
    #print(name)
    show_image(name)
    

def Capture(flag = False):
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    loop = True
    while(loop):
        ret,frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Camera",frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            cv2.destroyAllWindows()
            break
        elif(key == ord('s')):
            cv2.imwrite("captured_image.png",frame)
            cv2.destroyAllWindows()
            show_image("captured_image.png")
            break
        else:
            continue
    
            
    
    


def show_image(image_name):
    flag = True
    image = Image.open(image_name)
    image_copy = image.copy()
    image = image_copy.resize((width-200, height))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.image=photo
    label.grid(row=0,column=3,rowspan = 8, columnspan = 9)
    


def main():
    width=900
    height=500
    window = tk.Tk()
    window.config(bg="black")
    window.title("Color_Detection")
    window.geometry("900x500") # Here x is not *
    
    show_image("hero_2.png")


    load_btn = tk.Button(window, text="Load Image", width=25, activebackground="grey", activeforeground="blue",bg="red", command=lambda:Upload())
    load_btn.grid(row=0,column=1,columnspan=2, padx=10, pady=50)
    capture_btn = tk.Button(window, text="Take Image", width=25, activebackground="grey", activeforeground="blue",bg="green", command=lambda:Capture())
    capture_btn.grid(row=1,column=1,columnspan=2,padx=10,pady = 50)
    process_btn = tk.Button(window, text="Process Colors", width=25, activebackground="grey", activeforeground="blue",bg="purple", command=lambda:Process())
    process_btn.grid(row=2,column=1,columnspan=2,padx=10,pady = 50)
    window.mainloop()



if __name__ == "__main__":
    main()    
