import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ------------------------------
# Sample Questions
# ------------------------------
rooms = [
    {
        "title": "Room 1: Password Security",
        "question": "Which of these is the strongest password?",
        "options": ["123456", "password", "MyP@ssw0rd!2025", "qwerty"],
        "answer": "MyP@ssw0rd!2025"
    },
    {
        "title": "Room 2: Phishing Awareness",
        "question": "What should you check in a suspicious email?",
        "options": ["Sender email", "Spelling mistakes", "Links", "All of the above"],
        "answer": "All of the above"
    },
    {
        "title": "Room 3: Secure Practices",
        "question": "Which action improves online security?",
        "options": ["Reusing passwords", "Using 2FA", "Ignoring updates", "Sharing credentials"],
        "answer": "Using 2FA"
    }
]

# ------------------------------
# Main Application
# ------------------------------
class CyberAdventure:
    def __init__(self, root):
        self.root = root
        self.root.title("🌸 Cybersecurity Adventure 🌸")
        self.root.geometry("700x500")
        self.root.configure(bg="#FFF0F5")  # pastel lavender background

        self.score = 0
        self.current_room = 0

        # Single variable for all radiobuttons
        self.option_var = tk.StringVar()

       

        self.create_widgets()
        self.show_room()

    def create_widgets(self):
        self.title_label = tk.Label(
            self.root, text="", font=("Arial", 20, "bold"),
            bg="#FFF0F5", fg="#FF69B4"
        )
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(
            self.root, text="", font=("Arial", 16),
            wraplength=600, bg="#FFF0F5"
        )
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                self.root, text="", variable=self.option_var,
                value="", font=("Arial", 14),
                bg="#FFFAF0", indicatoron=0, width=30, pady=10
            )
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.next_button = tk.Button(
            self.root, text="Next", command=self.next_room,
            bg="#FFB6C1", width=15, pady=5
        )
        self.next_button.pack(pady=20)


    def show_room(self):
        if self.current_room < len(rooms):
            room = rooms[self.current_room]
            self.title_label.config(text=room["title"])
            self.question_label.config(text=room["question"])
            for i, option in enumerate(room["options"]):
                self.option_buttons[i].config(text=option, value=option)
            self.option_var.set(None)  # Clear previous selection
        else:
            messagebox.showinfo(
                "Game Over",
                f"🎉 Adventure Complete! Your final score: {self.score} / {len(rooms)}"
            )
            self.root.destroy()

    def next_room(self):
        selected = self.option_var.get()
        if not selected:
            messagebox.showwarning("Choose an option", "Please select an answer before proceeding.")
            return

        correct_answer = rooms[self.current_room]["answer"]
        if selected == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "✅ Correct answer!")
        else:
            messagebox.showinfo("Wrong!", f"❌ Wrong! Correct answer: {correct_answer}")

        self.current_room += 1
        self.show_room()

# ------------------------------
# Run Application
# ------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = CyberAdventure(root)
    root.mainloop()
