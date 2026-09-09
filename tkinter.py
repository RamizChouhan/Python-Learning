import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter Layout Managers Comparison")
root.geometry("800x400")

# --- 1. PACK DEMO (Top / Vertical Stacking) ---
frame_pack = ttk.LabelFrame(root, text="1. pack() Demo", padding=20)
frame_pack.pack(side="left", fill="both" , expand=True, padx=20, pady=10)

tk.Button(frame_pack, text="Button 1 (default)", bg="lightblue").pack(
    fill="x", pady=5)
# pady adds outer vertical space; ipadx/ipady expand internal button size
tk.Button(frame_pack, text="Button 2 (padded)", bg="lightgreen").pack(
    fill="x", padx=15, pady=15, ipadx=10, ipady=5
)
tk.Button(frame_pack, text="Button 3 (bottom)", bg="lightcoral").pack(
    side="bottom", fill="x"
)

# --- 2. GRID DEMO (Row & Column Matrix) ---
frame_grid = ttk.LabelFrame(root, text="2. grid() Demo", padding=10)
frame_grid.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Row 0
tk.Label(frame_grid, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Entry(frame_grid).grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Row 1
tk.Label(frame_grid, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Entry(frame_grid).grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Row 2 (Spanning 2 columns with internal padding)
tk.Button(frame_grid, text="Submit Grid Form", bg="gold").grid(
    row=2, column=0, columnspan=2, pady=15, ipadx=20, ipady=5
)

# --- 3. PLACE DEMO (Absolute/Relative Coordinates) ---
frame_place = ttk.LabelFrame(root, text="3. place() Demo", padding=10)
frame_place.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Absolute positioning using exact pixels (x, y)
btn1 = tk.Button(frame_place, text="Fixed (x=20, y=30)", bg="plum")
btn1.place(x=20, y=30, width=150, height=35)

# Relative positioning using percentage of parent frame (relx, rely)
btn2 = tk.Button(frame_place, text="Relative (50% Center)", bg="orange")
btn2.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.7)

root.mainloop()
