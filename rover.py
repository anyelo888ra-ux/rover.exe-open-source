#!/usr/bin/env python3
"""
🐕 Rover.exe - Reviving Windows XP Nostalgia
A nostalgic recreation of the iconic Windows XP search dog.
Built with Python | Compiled to .exe with GitHub Actions
"""

import tkinter as tk
from tkinter import messagebox
import random
import os
import sys
from pathlib import Path

class Rover:
    """The legendary Windows XP search dog, now in Python."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rover.exe - Windows XP Search Dog")
        self.root.geometry("300x200")
        self.root.config(bg='white')
        
        # Rover state
        self.x = 100
        self.y = 100
        self.vx = random.choice([-2, 2])
        self.vy = random.choice([-2, 2])
        self.mood = "happy"
        self.energy = 100
        
        # Create canvas
        self.canvas = tk.Canvas(
            self.root, 
            width=300, 
            height=200, 
            bg='white',
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        
        # Draw Rover
        self.rover_id = None
        
        # Status bar
        self.status_frame = tk.Frame(self.root, bg='lightgray', height=30)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.status_label = tk.Label(
            self.status_frame,
            text=f"Rover is ready! 🐕 | Mood: {self.mood.upper()} | Energy: {self.energy}%",
            bg='lightgray',
            font=("MS Sans Serif", 8)
        )
        self.status_label.pack(side=tk.LEFT, padx=5)
        
        # Keyboard bindings
        self.root.bind("<Escape>", lambda e: self.root.quit())
        self.root.bind("<space>", self.bark)
        
        # Start animation loop
        self.animate()
    
    def draw_rover(self):
        """Draw the cute Rover dog on canvas."""
        self.canvas.delete(self.rover_id)
        
        # Tail
        tail_x = self.x - 30
        tail_y = self.y + 10
        self.canvas.create_arc(
            tail_x - 15, tail_y - 5, tail_x + 15, tail_y + 20,
            start=0, extent=180, fill='brown', width=3, tags="rover"
        )
        
        # Body
        self.canvas.create_oval(
            self.x - 20, self.y, self.x + 20, self.y + 40,
            fill='#D2691E', width=2, tags="rover"
        )
        
        # Head
        self.canvas.create_oval(
            self.x - 15, self.y - 25, self.x + 15, self.y - 5,
            fill='#8B4513', width=2, tags="rover"
        )
        
        # Ears
        self.canvas.create_polygon(
            self.x - 10, self.y - 20, self.x - 5, self.y - 35, self.x, self.y - 20,
            fill='#654321', tags="rover"
        )
        self.canvas.create_polygon(
            self.x + 10, self.y - 20, self.x + 5, self.y - 35, self.x, self.y - 20,
            fill='#654321', tags="rover"
        )
        
        # Eyes
        self.canvas.create_oval(
            self.x - 6, self.y - 18, self.x - 2, self.y - 14,
            fill='black', tags="rover"
        )
        self.canvas.create_oval(
            self.x + 2, self.y - 18, self.x + 6, self.y - 14,
            fill='black', tags="rover"
        )
        
        # Nose
        self.canvas.create_oval(
            self.x - 2, self.y - 10, self.x + 2, self.y - 6,
            fill='black', tags="rover"
        )
        
        # Legs
        leg_y = self.y + 40
        for leg_x in [self.x - 12, self.x - 4, self.x + 4, self.x + 12]:
            self.canvas.create_rectangle(
                leg_x - 2, leg_y, leg_x + 2, leg_y + 15,
                fill='#8B4513', width=1, tags="rover"
            )
        
        self.rover_id = "rover"
    
    def animate(self):
        """Animation loop."""
        # Move Rover
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off walls
        if self.x <= 20 or self.x >= 280:
            self.vx *= -1
            self.x = max(20, min(280, self.x))
        if self.y <= 20 or self.y >= 160:
            self.vy *= -1
            self.y = max(20, min(160, self.y))
        
        # Decrease energy slightly
        self.energy = max(0, self.energy - 0.1)
        
        # Random mood changes
        if random.random() < 0.02:
            self.mood = random.choice(["happy", "playful", "searching"])
        
        # Draw
        self.draw_rover()
        self.update_status()
        
        # Continue animation
        self.root.after(50, self.animate)
    
    def on_click(self, event):
        """Handle mouse click on Rover."""
        distance = ((self.x - event.x) ** 2 + (self.y - event.y) ** 2) ** 0.5
        
        if distance < 40:  # Clicked on Rover
            self.mood = "playful"
            self.energy = min(100, self.energy + 20)
            self.bark()
            # Make Rover jump
            self.vy -= 5
    
    def on_right_click(self, event):
        """Handle right-click menu."""
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Feed Rover", command=self.feed)
        menu.add_command(label="Play", command=self.play)
        menu.add_separator()
        menu.add_command(label="About Rover", command=self.about)
        menu.add_separator()
        menu.add_command(label="Exit", command=self.root.quit)
        
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()
    
    def bark(self, event=None):
        """Make Rover bark."""
        self.mood = "playful"
        self.energy = max(0, self.energy - 10)
        # In a real version, we'd play a sound here
        print("🐕 WOOF! WOOF!")
    
    def feed(self):
        """Feed Rover."""
        self.energy = min(100, self.energy + 30)
        self.mood = "happy"
        messagebox.showinfo("Rover", "Rover is eating... nom nom nom! 🦴")
    
    def play(self):
        """Play with Rover."""
        self.energy = max(0, self.energy - 20)
        self.mood = "playful"
        self.vx *= 1.5
        self.vy *= 1.5
        messagebox.showinfo("Rover", "Let's play! 🎾")
    
    def about(self):
        """Show about dialog."""
        messagebox.showinfo(
            "About Rover",
            "🐕 Rover.exe - Windows XP Nostalgia\n\n"
            "The legendary search dog is back!\n\n"
            "Controls:\n"
            "• Click: Interact with Rover\n"
            "• Right-click: Menu\n"
            "• SPACE: Bark\n"
            "• ESC: Exit\n\n"
            "Made with Python & nostalgia ❤️"
        )
    
    def update_status(self):
        """Update status bar."""
        status_text = f"Rover is here! 🐕 | Mood: {self.mood.upper()} | Energy: {int(self.energy)}%"
        self.status_label.config(text=status_text)
    
    def run(self):
        """Start Rover."""
        self.root.mainloop()


if __name__ == "__main__":
    app = Rover()
    app.run()
    
