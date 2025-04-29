import tkinter as tk

class EraserApp:
    def __init__(self, root, grid_size=10, cell_size=30):
        self.root = root
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.canvas = tk.Canvas(root, width=grid_size * cell_size, height=grid_size * cell_size)
        self.canvas.pack()

        # Create grid of blue cells
        self.cells = {}
        for row in range(grid_size):
            for col in range(grid_size):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')
                self.cells[rect] = (row, col)

        # Create eraser rectangle
        self.eraser = self.canvas.create_rectangle(0, 0, cell_size, cell_size, fill='red', outline='black')

        # Bind mouse events for dragging the eraser
        self.canvas.bind("<B1-Motion>", self.drag_eraser)

    def drag_eraser(self, event):
        # Get the position of the mouse
        mouse_x, mouse_y = event.x, event.y

        # Calculate the top-left corner of the eraser rectangle based on mouse position
        eraser_x1 = (mouse_x // self.cell_size) * self.cell_size
        eraser_y1 = (mouse_y // self.cell_size) * self.cell_size
        eraser_x2 = eraser_x1 + self.cell_size
        eraser_y2 = eraser_y1 + self.cell_size

        # Move the eraser
        self.canvas.coords(self.eraser, eraser_x1, eraser_y1, eraser_x2, eraser_y2)

        # Erase the cells that the eraser is touching
        for rect, (row, col) in self.cells.items():
            rect_x1, rect_y1, rect_x2, rect_y2 = self.canvas.coords(rect)
            if eraser_x1 < rect_x2 and eraser_x2 > rect_x1 and eraser_y1 < rect_y2 and eraser_y2 > rect_y1:
                self.canvas.itemconfig(rect, fill='white')

# Create the tkinter root window
root = tk.Tk()
root.title("Eraser on Canvas")

# Create and run the EraserApp
app = EraserApp(root)

# Run the tkinter event loop
root.mainloop()
