import tkinter as tk
from tkinter import messagebox

HISTORY_FILE = "history.txt"

# ---------------- HISTORY FUNCTIONS ----------------
def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()


def show_history():
    try:
        file = open(HISTORY_FILE, "r")
        data = file.read()
        file.close()

        if data.strip() == "":
            messagebox.showinfo("History", "History not found")
        else:
            messagebox.showinfo("History", data)

    except FileNotFoundError:
        messagebox.showinfo("History", "History not found")


def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    messagebox.showinfo("History", "History cleared")


# ---------------- CALCULATION ----------------
def calculate():
    user_input = entry.get()
    parts = user_input.split()

    if len(parts) != 3:
        messagebox.showerror("Error", "Use format: number operator number\nExample: 8 + 8")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
        result = num1 / num2
    else:
        messagebox.showerror("Error", "Invalid operator")
        return

    if result.is_integer():
        result = int(result)

    result_label.config(text="Result: " + str(result))
    save_to_history(user_input, result)


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x250")

tk.Label(root, text="Enter calculation (e.g. 8 + 8)").pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate).pack(pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

tk.Button(root, text="Show History", command=show_history).pack(pady=3)
tk.Button(root, text="Clear History", command=clear_history).pack(pady=3)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()
