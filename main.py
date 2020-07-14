import tkinter as tk
from PIL import ImageTk
from PIL import Image
from tkinter import filedialog as fd 
import pyautogui
import cv2



window = tk.Tk()
window.config(bg="black")
window.title("Color_Detection")
window.geometry("900x500")
width=900
height=500
window_list = []


def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list


def Upload():
    try:
        window.unbind('<Motion>')
        window.unbind('<Button-1>')
        window.unbind_all('<F1>')
    except:
        a=1
    name = fd.askopenfilename(title = "Select file", filetypes = ((("png files","*.png"),("jpeg files","*.jpg"))))
    #print(name)
    show_image(name)
    

def Capture():
    try:
        window.unbind('<Motion>')
        window.unbind('<Button-1>')
        window.unbind_all('<F1>')
    except:
        a=1
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
    


def open_window():
    list_of_tops.append(tk.Toplevel(root))
    list_of_tops[-1].geometry("100x100")


            
def pressed2(event):
        x, y = event.x_root, event.y_root
        x_r, y_r = window.winfo_x(), window.winfo_y()
        MOUSE_X, MOUSE_Y = pyautogui.position()
        PIXEL = pyautogui.screenshot(region=(MOUSE_X, MOUSE_Y, 1, 1))
        COLOR = PIXEL.getcolors()
        if(x>x_r+250 and y > y_r and x<x_r + window.winfo_width() and y < y_r + window.winfo_height()):
            try:
                del_win = window_list.pop()
                del_win.destroy()
                #color_window.destroy()

            except:
                a=1
            color_window = tk.Tk()
            color_window.title("Colors")
            position = '180x20+'+str(x+10)+'+'+str(y-10)
            color_window.geometry(str(position))
            window_list.append(color_window)
            win = tk.Label(color_window, text = "RGB: %s" % (COLOR[0][1].__str__())).grid(row=1,column=0,columnspan=3)
            

def Motion(event):

    x, y = event.x_root, event.y_root
    x_r, y_r = window.winfo_x(), window.winfo_y()
    #print("X = ", x, " Y = ", y)
    #print("X_R = ", x_r," Y_R = ", y_r)
    if x > x_r + window.winfo_width() or x < x_r+250 or y > y_r + window.winfo_height() or y < y_r:
        a = 1
    else:
        window.bind('<Button-1>',pressed2)




def Process(window):
    window.bind('<Motion>',Motion)


def show_image(image_name):
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
    # Here x is not *
    
    show_image("hero_2.png")


    load_btn = tk.Button(window, text="Load Image", width=25, activebackground="grey", activeforeground="blue",bg="red", command=lambda:Upload())
    load_btn.grid(row=0,column=1,columnspan=2, padx=10, pady=50)
    capture_btn = tk.Button(window, text="Take Image", width=25, activebackground="grey", activeforeground="blue",bg="green", command=lambda:Capture())
    capture_btn.grid(row=1,column=1,columnspan=2,padx=10,pady = 50)
    process_btn = tk.Button(window, text="Process Colors", width=25, activebackground="grey", activeforeground="blue",bg="purple", command=lambda:Process(window))
    process_btn.grid(row=2,column=1,columnspan=2,padx=10,pady = 50)
    window.mainloop()



if __name__ == "__main__":
    main()    
