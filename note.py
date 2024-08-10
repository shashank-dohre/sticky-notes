import tkinter as tk
from tkinter import simpledialog

class StickyNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sticky Notes")
        self.notes = []

        self.new_note_button = tk.Button(root, text="New Note", command=self.create_new_note)
        self.new_note_button.pack(pady=10)

    def create_new_note(self):
        note_window = tk.Toplevel(self.root)
        note_window.title("Sticky Note")
        note_window.geometry("200x200")
        text_widget = tk.Text(note_window, wrap="word")
        text_widget.pack(expand=True, fill="both")
        self.notes.append(note_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = StickyNoteApp(root)
    root.mainloop()