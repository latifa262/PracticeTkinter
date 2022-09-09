from tkinter import *
import easyocr

from tkinter import filedialog
from PIL import ImageTk, Image
import re

root = Tk()
root.title('Extract text from image') 

newline= Label(root)
uploaded_img=Label(root)

def extract(path):
    reader = easyocr.Reader(['en'])
    RST = reader.readtext(path)
    res2=str(RST)       
    res = re.findall(r'[^\d\W]+', res2)
    
    x=' '
    for i in res:
        x+=' '+i
    Label(root,text=x).pack()

def show_extract_button(path):
    extractBtn= Button(root,text="Extract text",command=lambda: extract(path),pady=15,padx=15,font=('Times',15))
    extractBtn.pack()

def upload():
    try:
        path=filedialog.askopenfilename()
        image=Image.open(path)
        img=ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        show_extract_button(path)
    except:
        pass  

uploadbtn = Button(root,text="Upload an image",command=upload,pady=15,padx=15,font=('Times',15)).pack()
newline.configure(text='\n')
newline.pack()
uploaded_img.pack()
newline.pack()

root.mainloop()