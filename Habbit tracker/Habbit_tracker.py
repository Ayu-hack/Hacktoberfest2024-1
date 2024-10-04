import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import os

# File to store habit data
DATA_FILE = 'habit_data.json'

class HabitTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Habit Tracker")
        self.habits = {}
        
        # Load saved habits from file
        self.load_data()

        # UI Components
        self.create_ui()

    def create_ui(self):
        # Input for new habit
        self.habit_label = tk.Label(self.root, text="Enter a new habit:")
        self.habit_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.habit_entry = tk.Entry(self.root)
        self.habit_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.add_button = tk.Button(self.root, text="Add Habit", command=self.add_habit)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        # List of habits
        self.habit_listbox = tk.Listbox(self.root, height=10, width=40)
        self.habit_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        # Habit Action Buttons
        self.track_button = tk.Button(self.root, text="Mark Today's Progress", command=self.mark_progress)
        self.track_button.grid(row=2, column=0, padx=10, pady=10)

        self.view_button = tk.Button(self.root, text="View Progress", command=self.view_progress)
        self.view_button.grid(row=2, column=1, padx=10, pady=10)

        self.streak_button = tk.Button(self.root, text="View Streaks", command=self.view_streak)
        self.streak_button.grid(row=2, column=2, padx=10, pady=10)

        # Populate the habit list
        self.update_habit_listbox()

    def add_habit(self):
        habit = self.habit_entry.get()
        if habit:
            if habit not in self.habits:
                self.habits[habit] = []
                self.update_habit_listbox()
                self.save_data()
                self.habit_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Duplicate Habit", "Habit already exists!")
        else:
            messagebox.showwarning("Input Error", "Please enter a habit!")

    def update_habit_listbox(self):
        self.habit_listbox.delete(0, tk.END)
        for habit in self.habits:
            self.habit_listbox.insert(tk.END, habit)

    def mark_progress(self):
        selected_habit = self.habit_listbox.curselection()
        if selected_habit:
            habit = self.habit_listbox.get(selected_habit)
            today = datetime.now().strftime("%Y-%m-%d")
            if today not in self.habits[habit]:
                self.habits[habit].append(today)
                self.save_data()
                messagebox.showinfo("Success", f"Progress marked for {habit}!")
            else:
                messagebox.showinfo("Already Marked", f"Progress already marked for {habit} today.")
        else:
            messagebox.showwarning("Selection Error", "Please select a habit to mark progress!")

    def view_progress(self):
        selected_habit = self.habit_listbox.curselection()
        if selected_habit:
            habit = self.habit_listbox.get(selected_habit)
            progress_dates = self.habits[habit]
            if progress_dates:
                messagebox.showinfo(f"Progress for {habit}", f"Dates completed: \n" + "\n".join(progress_dates))
            else:
                messagebox.showinfo("No Progress", f"No progress marked for {habit} yet.")
        else:
            messagebox.showwarning("Selection Error", "Please select a habit to view progress!")

    def view_streak(self):
        selected_habit = self.habit_listbox.curselection()
        if selected_habit:
            habit = self.habit_listbox.get(selected_habit)
            progress_dates = self.habits[habit]
            if progress_dates:
                streak = self.calculate_streak(progress_dates)
                messagebox.showinfo(f"Streak for {habit}", f"Your current streak is {streak} days!")
            else:
                messagebox.showinfo("No Streak", "No progress marked yet to calculate a streak.")
        else:
            messagebox.showwarning("Selection Error", "Please select a habit to view streak!")

    def calculate_streak(self, progress_dates):
        # Sort the dates to calculate streak
        progress_dates = sorted([datetime.strptime(date, "%Y-%m-%d") for date in progress_dates])
        streak = 0
        current_streak = 0
        for i in range(1, len(progress_dates)):
            delta = (progress_dates[i] - progress_dates[i - 1]).days
            if delta == 1:
                current_streak += 1
            else:
                current_streak = 0
            streak = max(streak, current_streak)
        return streak + 1  # Include the current day

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.habits, f)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                self.habits = json.load(f)

if __name__ == "__main__":
    root = tk.Tk()
    app = HabitTracker(root)
    root.geometry("400x400")
    root.mainloop()
