from tkinter import *
from PIL import Image, ImageTk

# Initialize the main window
root = Tk()
root.title("Wordiee")
root.geometry("800x600")  # Set window size

# Load and resize the main background image
bg_image = Image.open("assets/background.png")  # Replace with your image path
bg_image = bg_image.resize((800, 600), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Canvas to display the background image
canvas = Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Load and resize the welcome message background image
welcome_bg_image = Image.open("assets/message.png")  # Replace with your image path
welcome_bg_image = welcome_bg_image.resize((400, 200), Image.LANCZOS)
welcome_bg_photo = ImageTk.PhotoImage(welcome_bg_image)

# Create a Label to act as the background for the welcome frame
welcome_bg_label = Label(canvas, image=welcome_bg_photo, borderwidth=0)
canvas.create_window(400, 300, window=welcome_bg_label)  # Center the image

# Add welcome message and start button on top of the background image
welcome_label = Label(canvas, text="Welcome to the Game!", font=("Arial", 24), fg="black", bg="#ffffff")
canvas.create_window(400, 250, window=welcome_label)  # Adjust Y-coordinate to place it higher

def start_game():
    # Clear welcome screen items when the game starts
    canvas.delete("all")
    # You can add code here to create the game screen
    print("Game Started!")

start_button = Button(canvas, text="Start", font=("Arial", 18), command=start_game)
canvas.create_window(400, 350, window=start_button)  # Place start button below the label

# Run the application
root.mainloop()
