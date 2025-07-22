import tkinter as tk
from tkinter import messagebox, ttk
from gym_system import GymSystem
from login import verify_user

gym = GymSystem()  # Global Gym System

# ---------------- Login Window ----------------
def login_window():
    def attempt_login():
        user = username.get()
        pwd = password.get()
        if verify_user(user, pwd):
            messagebox.showinfo("Success", "Login successful")
            root.destroy()
            main_window()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    root = tk.Tk()
    root.title("Gym Login")
    root.geometry("600x380")
    tk.Label(root, text="Username").pack(pady=10)
    username = tk.Entry(root)
    username.pack()

    tk.Label(root, text="Password").pack(pady=10)
    password = tk.Entry(root, show="*")
    password.pack()

    tk.Button(root, text="Login", command=attempt_login).pack(pady=10)
    root.mainloop()


def main_window():
    def add_member():
        def save_member():
            success = gym.add_member(
                id_entry.get(),
                name_entry.get(),
                age_entry.get(),
                gender_var.get(),
                phone_entry.get()
            )
            if success:
                messagebox.showinfo("Done", "Member added.")
                win.destroy()
                view_members()
            else:
                messagebox.showerror("Error", "ID already exists")

        win = tk.Toplevel(app)
        win.title("Add Member")

        tk.Label(win, text="ID").pack()
        id_entry = tk.Entry(win)
        id_entry.pack()

        tk.Label(win, text="Name").pack()
        name_entry = tk.Entry(win)
        name_entry.pack()

        tk.Label(win, text="Age").pack()
        age_entry = tk.Entry(win)
        age_entry.pack()

        tk.Label(win, text="Gender").pack()
        gender_var = tk.StringVar(value="")
        tk.Entry(win, textvariable=gender_var).pack()

        tk.Label(win, text="Phone").pack()
        phone_entry = tk.Entry(win)
        phone_entry.pack()

        tk.Button(win, text="Save", command=save_member).pack(pady=5)

    def view_members():
        win = tk.Toplevel(app)
        win.title("All Members")
        tree = ttk.Treeview(win, columns=('ID', 'Name', 'Phone', 'Paid'), show='headings')
        tree.pack(fill='both', expand=True)

        tree.heading('ID', text='ID')
        tree.heading('Name', text='Name')
        tree.heading('Phone', text='Phone')
        tree.heading('Paid', text='Total Paid')

        for m in gym.get_all_members():
            tree.insert('', 'end', values=(m.member_id, m.name, m.phone, f"Rs. {m.total_paid()}"))

    def add_payment():
        def save_payment():
            try:
                amount = float(amount_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")
                return

            success = gym.add_payment(id_entry.get(), amount)
            if success:
                messagebox.showinfo("Success", "Payment added.")
                win.destroy()
            else:
                messagebox.showerror("Error", "Member not found.")

        win = tk.Toplevel(app)
        win.title("Add Payment")

        tk.Label(win, text="Member ID").pack()
        id_entry = tk.Entry(win)
        id_entry.pack()

        tk.Label(win, text="Amount").pack()
        amount_entry = tk.Entry(win)
        amount_entry.pack()

        tk.Button(win, text="Save Payment", command=save_payment).pack()

    # ----------- NEW FUNCTION TO DELETE MEMBER -----------
    def delete_member():
        def confirm_delete():
            member_id = id_entry.get()
            if gym.delete_member(member_id):
                messagebox.showinfo("Deleted", f"Member {member_id} removed.")
                win.destroy()
            else:
                messagebox.showerror("Error", "Member not found.")

        win = tk.Toplevel(app)
        win.title("Delete Member")

        tk.Label(win, text="Enter Member ID to Delete").pack()
        id_entry = tk.Entry(win)
        id_entry.pack()

        tk.Button(win, text="Delete", command=confirm_delete).pack(pady=5)

    # ---------------- Main UI ----------------
    app = tk.Tk()
    app.title("Gym Management System")
    app.geometry("400x350")

    tk.Label(app, text="Welcome to Gym Manager", font=('Arial', 16)).pack(pady=10)

    tk.Button(app, text="Add Member", width=30, command=add_member).pack(pady=5)
    tk.Button(app, text="View Members", width=30, command=view_members).pack(pady=5)
    tk.Button(app, text="Add Payment", width=30, command=add_payment).pack(pady=5)
    tk.Button(app, text="Delete Member", width=30, command=delete_member).pack(pady=5)  # ← NEW BUTTON
    tk.Button(app, text="Exit", width=30, command=app.quit).pack(pady=5)

    app.mainloop()

# Start App
if __name__ == "__main__":
    login_window()
