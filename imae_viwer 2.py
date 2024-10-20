from tkinter import *

#To make python able to work with images
from PIL import ImageTk,Image

root=Tk()
root.title('lets learn together')#the title
root.iconbitmap('C:\\Users\\user\\Downloads\\frog.ico')#to add an icon to your app

#defining the image stored in your folders, you can change the directory to your own x
my_img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\OneDrive\\Pictures\\1000026974.jpg"))#ImageTk.PhotoImage is used when dealing with an image
my_img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\OneDrive\\Pictures\\1000026971.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\OneDrive\\Pictures\\1000026972.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\OneDrive\\Pictures\\1000026973.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\OneDrive\\Pictures\\1000026975.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

#Relief is used to sink the label in the box, anchor is used to take the label to the extreme end according to compass readings(W,E,N,S)
status= Label(root, text='image 1 of '+str(len (image_list)), bd=1, relief=SUNKEN,anchor=E)

#columnspan is used to tell how many columns the widget should occupy
my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

#every button must have a function
def foward(image_number):
    global my_label
    global button_foward
    global button_back
    
    my_label.grid_forget()#.forget is used so that when moving to the next image it lyk deletes the old one to prevent overlapping
    my_label=Label(image=image_list[image_number-1])#???
    button_foward=Button(root, text='>>',command=lambda: foward(image_number+1))#labda is used to pass an argument inside a button
    button_back=Button(root, text='<<', command=lambda: backward(image_number-1))
    
    #once the number reaches 5 the button is disabled
    if image_number==5:
        button_foward=Button(root, text='>>', state = DISABLED)
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1, column=0)
    button_foward.grid(row=1,column=2)
    
    status= Label(root, text="image " + str(image_number) +  "of  "+str(len (image_list)), bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)
    
def backward(image_number):
    global my_label
    global button_foward
    global button_back
    
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_foward=Button(root, text='>>',command=lambda: foward(image_number+1))
    button_back=Button(root, text='<<', command=lambda: backward(image_number-1))

    if image_number==1:
        button_back=Button(root, text='<<',state=DISABLED)
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1, column=0)
    button_foward.grid(row=1,column=2)
    
    status= Label(root, text="image " + str(image_number) +  "of  "+str(len (image_list)), bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)

button_back= Button(root, text='<<',command=backward, state=DISABLED)
button_exit=Button(root, text= 'exit program', command=root.quit)
button_foward= Button(root, text='>>',command=lambda: foward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_foward.grid(row=1,column=2, pady=10)

status.grid(row=2,column=0,columnspan=3, sticky=W+E)




root.mainloop()#mainloop can be used