import tkinter as tk
import pygame

def play():
    

# Initialize Pygame
    pygame.init()

# Load the OGG file
    ogg_file = "sahil.mp3"
    pygame.mixer.music.load(ogg_file)

# Play the audio
    pygame.mixer.music.play()
# Create the window
window = tk.Tk()
window.title("69")
window.geometry('200x200')
window.configure(bg='yellow')

# Create the label
label = tk.Label(window, text="HELLO JAGMEET SIR CLICK ME")
label.pack()

# Create the button
button = tk.Button(window, text="SAHIL ",command=play)
button.pack()

# Run the window loop
window.mainloop()


    
