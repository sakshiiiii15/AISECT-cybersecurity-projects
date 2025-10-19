import string  # To access string constants like punctuation
import tkinter as tk  # Tkinter library for GUI
from tkinter import messagebox  # For popup messages

# Function to check if password length is at least 8 characters
def check_length(password):
    return len(password) >= 8

# Function to check if password contains at least one uppercase letter
def has_upper(password):
    return any(c.isupper() for c in password)

# Function to check if password contains at least one lowercase letter
def has_lower(password):
    return any(c.islower() for c in password)

# Function to check if password contains at least one digit
def has_digit(password):
    return any(c.isdigit() for c in password)

# Function to check if password contains at least one special character
def has_special(password):
    special_chars = string.punctuation
    return any(c in special_chars for c in password)

# Function to calculate password strength by checking criteria and scoring
def password_strength(password):
    score = 0
    if check_length(password):
        score += 1
    if has_upper(password):
        score += 1
    if has_lower(password):
        score += 1
    if has_digit(password):
        score += 1
    if has_special(password):
        score += 1

    # Return strength label and corresponding color for display
    if score <= 2:
        return "Weak", "red"
    elif score == 3 or score == 4:
        return "Moderate", "orange"
    else:
        return "Strong", "green"

# Event handler function when user clicks "Check Strength"
def check_password():
    pwd = entry.get()  # Get password from input field
    if not pwd:  # If empty, show warning message
        messagebox.showwarning("Input Error", "Please enter a password")
        return
    strength, color = password_strength(pwd)  # Get strength and color
    # Update result label with strength text and color
    result_label.config(text=f"Password Strength: {strength}", fg=color)

# GUI setup starts here
root = tk.Tk()
root.title("Password Strength Checker")  # Window title

root.config(bg="#282c34")  # Set dark background color for the window
root.geometry("350x220")  # Set window size

# Label widget to indicate input field purpose
label = tk.Label(root, text="Enter Password:", fg="#61dafb", bg="#282c34", font=("Helvetica", 14))
label.pack(pady=10)

# Entry widget for password input; "show='*'" hides characters
entry = tk.Entry(root, width=30, show="*", font=("Helvetica", 12))
entry.pack(pady=5)

# Button widget to trigger strength check when clicked
check_button = tk.Button(root, text="Check Strength", command=check_password, bg="#61dafb", fg="#282c34", font=("Helvetica", 12, "bold"))
check_button.pack(pady=15)

# Label widget to display password strength result
result_label = tk.Label(root, text="Password Strength: ", fg="white", bg="#282c34", font=("Helvetica", 14, "bold"))
result_label.pack(pady=5)

# Start the GUI event loop, which waits for user interaction
root.mainloop()
