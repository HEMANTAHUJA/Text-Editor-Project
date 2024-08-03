import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfile(defaultextension=".txt",filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path,'r') as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path,'w') as file:
            file.write(text.get(1.0,tk.END))
            messagebox.showinfo("Info","File Saved!")

def set_theme(theme):
    if theme == "Light":
        text.config(bg="white", fg="black")
    elif theme == "Dark":
        text.config(bg="black", fg="white")

def change_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        try:
            start_index = text.index(tk.SEL_FIRST)
            end_index = text.index(tk.SEL_LAST)
            text.tag_add("color", start_index, end_index)
            text.tag_config("color", foreground=color)
        except tk.TclError:
            messagebox.showerror("Error", "No text selected")
        

root = tk.Tk()
root.title("Text Editor 1.0")
root.geometry("800x600")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
theme_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Themes",menu=theme_menu)
file_menu.add_cascade(label="New",command=new_file)
file_menu.add_cascade(label="Open",command=open_file)
file_menu.add_cascade(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_cascade(label="Exit",command=root.quit)
theme_menu.add_command(label="Light", command=lambda: set_theme("Light"))
theme_menu.add_command(label="Dark", command=lambda: set_theme("Dark"))

format_menu = tk.Menu(menu)
menu.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Change Text Color", command=change_text_color)

text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="black")
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()

