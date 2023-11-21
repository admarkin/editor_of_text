import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font, colorchooser
from tkinter import ttk

class FileMenu:
    def __init__(self, root, text_editor):
        self.root = root
        self.text_editor = text_editor
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Новый документ", command=self.new_file)
        self.menu.add_command(label="Открыть", command=self.open_file)
        self.menu.add_command(label="Сохранить", command=self.save_file)
        self.menu.add_command(label="Сохранить как", command=self.save_as_file)
        self.menu.add_separator()
        self.menu.add_command(label="Выйти", command=self.exit_editor)
        self.root.bind('<Control-s>', self.save_file)

    def new_file(self):
        self.text_editor.delete("1.0", tk.END)

    def open_file(self):
        filepath = filedialog.askopenfilename (filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filepath:
            with open(filepath, "r") as file:
                self.text_editor.delete("1.0", tk.END)
                self.text_editor.insert(tk.END, file.read())

    def save_file(self):
        current_file = self.text_editor.get("1.0", tk.END)
        with open(self.current_filepath, "w") as file:
            file.write(current_file)

    def save_as_file(self):
        current_file = self.text_editor.get("1.0", tk.END)
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filepath:
            with open(filepath, "w") as file:
                file.write(current_file)
                self.current_filepath = filepath

    def exit_editor(self):
        if messagebox.askokcancel("Выход", "Бро, точно хочешь выйти?"):
            self.root.destroy()