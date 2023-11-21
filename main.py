import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font, colorchooser
from tkinter import ttk
from edittext import *
from filechange import *
class TextEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Текстовый редактор")
        self.root.geometry('700x500')
        self.text = tk.Frame(self.root)
        self.text.pack(fill=tk.BOTH, expand =0)
        self.listbox = tk.Listbox()
        self.text_editor = tk.Text(self.root, bg='#FFF5EE',fg='#181716',padx=10,pady=10,wrap=tk.WORD,
        insertbackground='#AB274F', selectbackground='#AFEEEE',spacing3= 7,width=10)
        self.text_editor.pack(fill=tk.BOTH, expand = 1, side=tk.LEFT)
        self.menu_bar = tk.Menu(self.root)
        self.scroll = ttk.Scrollbar(orient="vertical", command=self.text_editor.yview)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_editor.config(yscrollcommand=self.scroll.set)
        self.font = font.Font(family="Helvetica", size=12)
        self.file_menu = FileMenu(self.root, self.text_editor)
        self.edit_menu = EditMenu(self.root, self.text_editor)
        self.format_menu = Shrift_and_fone_change(self.root, self.text_editor, self.font)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu.menu)
        self.menu_bar.add_cascade(label="Инструменты", menu=self.edit_menu.menu)
        self.menu_bar.add_cascade(label="Шрифт", menu=self.format_menu.menu)
        self.root.config(menu=self.menu_bar)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    text_editor = TextEditor()
    text_editor.run()