#!/usr/bin/env python3
"""
🐕 Rover.exe - Reviving Windows XP Nostalgia
A nostalgic recreation of the iconic Windows XP search dog.
Now with drag & drop and improved visuals!
"""

import tkinter as tk
from tkinter import messagebox
import random

class Rover:
    """The legendary Windows XP search dog, now in Python."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rover.exe - Windows XP Search Dog")
        self.root.geometry("400x300")
        self.root.configure(bg='white')
        self.root.attributes('-topmost', True)
        
        # Rover state
        self.x = 150
        self.y = 100
        self.vx = random.choice([-1, 1])
        self.vy = random.choice([-1, 1])
        self.mood = "happy"
        self.energy = 100
        self.is_dragging = False
        self.drag_start_x = 0
        self.drag_start_y = 0
        
        # Create canvas with transparent-like appearance
        self.canvas = tk.Canvas(
            self.root, 
            width=400, 
            height=300, 
            bg='white',
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Button-3>", self.on_right_click)
        
        # Status bar
        self.status_frame = tk.Frame(self.root, bg='#e0e0e0', height=25)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="Rover is ready! 🐕 | Mood: HAPPY | Energy: 100%",
            bg='#e0e0e0',
            font=("MS Sans Serif", 8)
        )
        self.status_label.pack(side=tk.LEFT, padx=5, pady=2)
        
        # Keyboard bindings
        self.root.bind("<Escape>", lambda e: self.root.quit())
        self.root.bind("<space>", self.bark)
        
        # Start animation loop
        self.animate()
    
    def draw_rover_improved(self):
        """Draw Rover closer to the original Windows XP design."""
        self.canvas.delete("rover")
        
        # Body - Main shape (yellow/golden)
        body_color = '#FFD700'  # Golden yellow like XP Rover
        highlight_color = '#FFF8DC'  # Light yellow highlight
        shadow_color = '#DAA520'  # Darker gold for shadow
        
        # Back leg
        self.canvas.create_oval(
            self.x - 18, self.y + 30, self.x - 8, self.y + 50,
            fill=body_color, outline=shadow_color, width=1, tags="rover"
        )
        
        # Front leg
        self.canvas.create_oval(
            self.x + 8, self.y + 30, self.x + 18, self.y + 50,
            fill=body_color, outline=shadow_color, width=1, tags="rover"
        )
        
        # Body
        self.canvas.create_oval(
            self.x - 22, self.y + 5, self.x + 22, self.y + 35,
            fill=body_color, outline=shadow_color, width=2, tags="rover"
        )
        
        # Highlight on body
        self.canvas.create_oval(
            self.x - 18, self.y + 8, self.x - 8, self.y + 15,
            fill=highlight_color, outline="", tags="rover"
        )
        
        # Neck
        self.canvas.create_oval(
            self.x - 15, self.y - 5, self.x + 15, self.y + 10,
            fill=body_color, outline=shadow_color, width=2, tags="rover"
        )
        
        # Head
        self.canvas.create_oval(
            self.x - 18, self.y - 30, self.x + 18, self.y + 2,
            fill=body_color, outline=shadow_color, width=2, tags="rover"
        )
        
        # Snout/Nose area
        self.canvas.create_oval(
            self.x - 8, self.y - 8, self.x + 8, self.y + 2,
            fill=highlight_color, outline=shadow_color, width=1, tags="rover"
        )
        
        # Ears
        # Left ear
        self.canvas.create_polygon(
            self.x - 12, self.y - 15, self.x - 18, self.y - 35, self.x - 8, self.y - 20,
            fill=body_color, outline=shadow_color, width=1, tags="rover"
        )
        # Right ear
        self.canvas.create_polygon(
            self.x + 12, self.y - 15, self.x + 18, self.y - 35, self.x + 8, self.y - 20,
            fill=body_color, outline=shadow_color, width=1, tags="rover"
        )
        
        # Eyes
        self.canvas.create_oval(
            self.x - 8, self.y - 20, self.x - 2, self.y - 12,
            fill='black', tags="rover"
        )
        self.canvas.create_oval(
            self.x + 2, self.y - 20, self.x + 8, self.y - 12,
            fill='black', tags="rover"
        )
        
        # Eye shine
        self.canvas.create_oval(
            self.x - 6, self.y - 18, self.x - 4, self.y - 16,
            fill='white', tags="rover"
        )
        self.canvas.create_oval(
            self.x + 4, self.y - 18, self.x + 6, self.y - 16,
            fill='white', tags="rover"
        )
        
        # Nose
        self.canvas.create_oval(
            self.x - 3, self.y - 8, self.x + 3, self.y - 2,
            fill='black', tags="rover"
        )
        
        # Mouth
        self.canvas.create_arc(
            self.x - 6, self.y - 2, self.x + 6, self.y + 4,
            start=0, extent=180, fill='', outline='black', width=1, tags="rover"
        )
        
        # Tail
        tail_x = self.x - 25
        tail_y = self.y + 15
        self.canvas.create_arc(
            tail_x - 12, tail_y - 8, tail_x + 12, tail_y + 16,
            start=0, extent=180, fill='', outline=shadow_color, width=3, tags="rover"
        )
    
    def animate(self):
        """Animation loop."""
        if not self.is_dragging:
            # Move Rover
            self.x += self.vx
            self.y += self.vy
            
            # Bounce off walls
            if self.x <= 25 or self.x >= 375:
                self.vx *= -1
                self.x = max(25, min(375, self.x))
            if self.y <= 25 or self.y >= 250:
                self.vy *= -1
                self.y = max(25, min(250, self.y))
        
        # Decrease energy slightly
        self.energy = max(0, self.energy - 0.05)
        
        # Random mood changes
        if random.random() < 0.01:
            self.mood = random.choice(["happy", "playful", "searching"])
        
        # Draw
        self.draw_rover_improved()
        self.update_status()
        
        # Continue animation
        self.root.after(50, self.animate)
    
    def on_click(self, event):
        """Handle mouse click on Rover."""
        distance = ((self.x - event.x) ** 2 + (self.y - event.y) ** 2) ** 0.5
        
        if distance < 50:
            self.is_dragging = True
            self.drag_start_x = event.x - self.x
            self.drag_start_y = event.y - self.y
            self.mood = "playful"
            self.energy = min(100, self.energy + 15)
    
    def on_drag(self, event):
        """Handle dragging Rover."""
        if self.is_dragging:
            self.x = event.x - self.drag_start_x
            self.y = event.y - self.drag_start_y
            self.vx = 0
            self.vy = 0
    
    def on_release(self, event):
        """Handle release after dragging."""
        self.is_dragging = False
        self.vx = random.choice([-1, 1])
        self.vy = random.choice([-1, 1])
    
    def on_right_click(self, event):
        """Handle right-click menu."""
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="🐕 Pet Rover", command=self.pet)
        menu.add_command(label="🦴 Feed Rover", command=self.feed)
        menu.add_command(label="🎾 Play", command=self.play)
        menu.add_command(label="📍 About Rover", command=self.about)
        menu.add_separator()
        menu.add_command(label="❌ Exit", command=self.root.quit)
        
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()
    
    def pet(self):
        """Pet Rover."""
        self.mood = "happy"
        self.energy = min(100, self.energy + 10)
        messagebox.showinfo("Rover", "🐕 Rover wags his tail happily!")
    
    def feed(self):
        """Feed Rover."""
        self.energy = min(100, self.energy + 40)
        self.mood = "happy"
        messagebox.showinfo("Rover", "Rover is eating... nom nom nom! 🦴")
    
    def play(self):
        """Play with Rover."""
        self.energy = max(0, self.energy - 20)
        self.mood = "playful"
        self.vx *= 2
        self.vy *= 2
        messagebox.showinfo("Rover", "Let's play! 🎾\n\nRover is running around!")
    
    def bark(self, event=None):
        """Make Rover bark."""
        self.mood = "playful"
        self.energy = max(0, self.energy - 5)
        messagebox.showinfo("Rover", "🐕 WOOF! WOOF!\n\nRover is barking!")
    
    def about(self):
        """Show about dialog."""
        messagebox.showinfo(
            "About Rover",
            "🐕 Rover.exe - Windows XP Nostalgia\n\n"
            "The legendary search dog is back!\n\n"
            "Controls:\n"
            "• Click & Drag: Move Rover\n"
            "• Right-click: Menu\n"
            "• SPACE: Bark\n"
            "• ESC: Exit\n\n"
            "Made with Python & nostalgia ❤️\n"
            "Compiled with GitHub Actions"
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
