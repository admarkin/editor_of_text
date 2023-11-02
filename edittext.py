import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font, colorchooser
from tkinter import *
from tkinter import ttk



class EditMenu:
    def __init__(self, root, text_editor):
        self.root = root
        self.text_editor = text_editor
        self.menu = tk.Menu(self.root, tearoff= 0)
        self.menu.add_command(label="Вырезать", command=self.cut_text)
        self.menu.add_command(label="Копировать", command=self.copy_text)
        self.menu.add_command(label="Вставить", command=self.paste_text)
        self.menu.add_separator()
        self.menu.add_command(label="Найти один раз", command=self.find_once)
        self.menu.add_command(label="Найти все", command=self.find_text)
        self.menu.add_command(label="Заменить", command=self.replace_text)

    def cut_text(self, event=None):
        self.text_editor.event_generate("<<Cut>>")

    def copy_text(self, event=None):
        self.text_editor.event_generate("<<Copy>>")

    def paste_text(self, event=None):
        self.text_editor.event_generate("<<Paste>>")

    def find_once(self):
        search_text = simpledialog.askstring("Найти", "Что хочешь найти?:")
        if search_text:
            text_content = self.text_editor.get("1.0", tk.END)
            index = text_content.find(search_text)
            if index != -1:
                start = f"1.{index}"
                end = f"1.{index + len(search_text)}"
                self.text_editor.tag_add(tk.SEL, start, end)
                self.text_editor.focus_set()
                self.text_editor.tag_config(tk.SEL, background="blue")
            else:
                messagebox.showinfo("Поиск", "Текст не найден.")
    def find_text(self):
        search_text = simpledialog.askstring("Найти", "Что хочешь найти?:")
        if search_text:
            text_content = self.text_editor.get("1.0", tk.END)
            self.text_editor.tag_remove("yellow", "1.0", tk.END)
            start_index = "1.0"
            while True:
                start_index = self.text_editor.search(search_text, start_index, stopindex=tk.END)
                if not start_index:
                    break
                end_index = self.text_editor.index(f"{start_index}+{len(search_text)}c")
                self.text_editor.tag_add("yellow", start_index, end_index)
                start_index = end_index
                self.text_editor.tag_config("yellow", background="yellow")
                self.text_editor.focus_set()

    def replace_text(self):
        search_text = simpledialog.askstring("Замена", "Введите что заменить:")
        if search_text:
            replace_text = simpledialog.askstring("Замена", "Введите на что заменить:")
            if replace_text:
                current_content = self.text_editor.get("1.0", tk.END)
                new_content = current_content.replace(search_text, replace_text)
                self.text_editor.delete("1.0", tk.END)
                self.text_editor.insert("1.0", new_content)

class Shrift_and_fone_change:
    def __init__(self, root, text_editor, font):
        self.root = root
        self.text_editor = text_editor
        self.font = font
        self.menu = tk.Menu(self.root, tearoff = 0)
        self.menu.add_command(label="Шрифт", command=self.change_font)
        self.menu.add_command(label="Размер шрифта", command=self.change_font_size)
        self.menu.add_separator()
        self.menu.add_command(label="Цвет шрифта", command=self.change_text_color)
        self.menu.add_command(label="Цвет фона", command=self.change_fon_color)

    def change_font(self):
        new_font = font.nametofont(self.text_editor.cget("font"))
        font_family = simpledialog.askstring("Шрифт", "Выбери шрифт", initialvalue=new_font.actual("family"))
        if font_family:
            new_font.configure(family=font_family)
            self.text_editor.configure(font=new_font)

    def change_font_size(self):
        new_font = font.nametofont(self.text_editor.cget("font"))
        font_size = simpledialog.askinteger("Размер шрифта", "Выбери размер шрифта", initialvalue=new_font.actual("size"))
        if font_size:
            new_font.configure(size=font_size)
            self.text_editor.configure(font=new_font)
    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        self.text_editor.config(fg=color)
    def change_fon_color(self):
        color = colorchooser.askcolor()[1]
        self.text_editor.config(bg=color)
