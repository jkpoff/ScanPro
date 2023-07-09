from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import scanner

# Main Window
Root = Tk()
Root.title("ScanPro")
Root.geometry("500x500")
Root.resizable(False, False)
Root.configure(bg="midnight blue")

# ScanPro Image
image = Image.open("receipt_emoji.png")
resized_image = image.resize((120, 120))
image1 = ImageTk.PhotoImage(resized_image)
image_lbl = Label(image=image1)
image_lbl.configure(bg="midnight blue")
image_lbl.place(relx=0.5, rely=0.2, anchor=CENTER)

# ScanPro Title
title = Label(Root, 
            text="ScanPro", 
            font="Courier 75",
            width=500
            )
title.configure(bg="dark slate blue")
title.place(relx=0.5, rely=0.435, anchor=CENTER)
# ScanPro Subtitle
subtitle = Label(Root, 
                text="The Receipt Scanner", 
                font="Courier 20"
                )
subtitle.configure(bg="midnight blue")
subtitle.place(relx=0.5, rely=0.55, anchor=CENTER)

# ScanPro user information
info = Label(Root, 
    text=" • Select image of receipt\n • Adjust image settings \n • Select file location \n • Re-optimize if necessary", 
    font=("Courier", 12, "italic")
    )
info.configure(bg="midnight blue")
info.place(relx=0.5, rely=0.65, anchor=CENTER)

# Tag
creator = Label(Root,
                text="@jkpoff"
                )
creator.configure(bg="midnight blue")
creator.place(relx=0.9, rely=0.95, anchor=CENTER)

# Accept User File
b1 = Button(Root, 
            text='Upload File', height=1,
            highlightbackground="midnight blue",
            width=20,
            command = lambda:upload_file(),
            )
b1.place(relx=0.5, rely=0.765, anchor=CENTER)

# Command for b1 to allow users to upload photo
def upload_file():
    global img
    f_types = [('Jpeg Files', '*.jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = filename
    if img:
        grayscale_window(img)

def grayscale_window(image, threshold = 150):
    Preview = Toplevel()
    Preview.title("Grayscale Preview")
    Preview.geometry("700x700")
    Preview.resizable(False, False)
    Preview.configure(bg="midnight blue")

    # CV, Gray Scale
    cv_object = scanner.CV(image)
    cv_image = cv_object.grayscale(threshold)
    print(cv_image)
    user_image = Image.open(cv_image)
    resized_image = user_image.resize((400,500))
    user_image = ImageTk.PhotoImage(resized_image)
    pic = Label(Preview, image=user_image)
    pic.place(relx=0.5, rely=0.4, anchor=CENTER)

    def get_current_value():
        return current_value.get()

    def slider_changed(event):
        value_label.configure(text=get_current_value())

    current_value = IntVar()
    slider_label = Label(
        Preview,
        text='Threshold Value:',
        bg='gray70'
    )
    slider_label.grid(
        row=0,
        column=0,
        padx=5,
    )
    slider_label.place(
        relx=0.5,
        rely=0.8,
        anchor=CENTER
    )
    slider = Scale(Preview,
        from_=0,
        to=255,
        bg="gray70",
        orient='horizontal',
        length=150,
        command=slider_changed,
        variable=current_value
    )
    slider.grid(
        row=0,
        column=1,
        ipadx=25,
    )
    slider.place(
        relx=0.5,
        rely=0.85,
        anchor=CENTER
    )
    value_label = Label(Preview,
        text=get_current_value()
    )
    next_btn = Button(Preview,
        text="Next",
        highlightbackground="midnight blue",
        height=2,
        width=10,
        command=lambda: [Preview.destroy(), noisecontrol_window(cv_image)]
    )
    next_btn.place (
        relx=0.9,
        rely=0.95,
        anchor=CENTER
    )
    reload_btn = Button(Preview,
        text="Reload",
        highlightbackground="midnight blue",
        height=1,
        width=20,
        command=lambda: [Preview.destroy(), grayscale_window(image, get_current_value())]
    )
    reload_btn.place(
        relx=0.5,
        rely=0.915,
        anchor=CENTER
    )

    Preview.mainloop()

def noisecontrol_window(image):
    Preview = Toplevel()
    Preview.title("Noise Control Preview")
    Preview.geometry("700x700")
    Preview.resizable(False, False)
    Preview.configure(bg="midnight blue")

    
    cv_object = scanner.CV(image)
    cv_image = cv_object.noise_reduction()
    print(cv_image)
    user_image = Image.open(cv_image)
    resized_image = user_image.resize((400,500))
    user_image = ImageTk.PhotoImage(resized_image)
    pic = Label(Preview, image=user_image)
    pic.place(relx=0.5, rely=0.4, anchor=CENTER)

    next_btn = Button(Preview,
        text="Next",
        highlightbackground="midnight blue",
        height=2,
        width=10,
        command=lambda: [Preview.destroy(), noisecontrol_window(cv_image)]
    )
    next_btn.place (
        relx=0.9,
        rely=0.95,
        anchor=CENTER
    )
    Preview.mainloop()


Root.mainloop()


