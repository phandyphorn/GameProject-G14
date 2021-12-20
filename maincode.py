import tkinter as tk
root = tk.Tk()
root.geometry("600x600")
surface = tk.Frame()
surface.master.title("G14 Master Eat")
canvas = tk.Canvas(surface)



canvas.pack(expand=True, fill= "both")
surface.pack(expand=True, fill = "both")
surface.mainloop()
