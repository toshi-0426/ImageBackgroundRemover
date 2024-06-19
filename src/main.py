import os
import requests
import tkinter as tk
import tkmacosx as tkm 

from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD

# global variable, api key
api_key = os.getenv("X-Api-Key")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Image Backgroud Remover")
        # get the width and height of the screen
        # place the window in the middle of the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 600
        window_height = 600
        x_position = int(screen_width/2 - window_width/2)
        y_position = int(screen_height/2 - window_height/1.7)
        self.master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.master.configure(bg="#CBC5B7")
        self.pack()
        # main frame that occupies the entire window
        self.top_frame = tk.Frame(self.master, bg="#CBC5B7")
        self.top_frame.pack(fill=tk.BOTH, expand=True)  # Fill the entire window
        self.filepath = None
        self.create_widget()


    def create_widget(self):
        self.create_header()
        self.create_drag_and_drop_box()
        self.create_buttons()


    def create_header(self):
        # place the text onto the upper middle  
        header_label = tk.Label(self.top_frame, text="Image Backgroud Remover", font='Helvetica 28 bold', fg="black", bg="#CBC5B7")
        header_label.pack(pady=30)
        
    
    def create_drag_and_drop_box(self):
        # frame for drag and drop 
        self.dnd_frame = tk.Frame(self.top_frame, relief=tk.RIDGE, width=400, height=350, bg="#D9D9D9") 
        self.dnd_frame.pack(pady=10)
        self.dnd_frame.drop_target_register(DND_FILES)
        self.dnd_frame.dnd_bind("<<Drop>>", self.drop_image_handler)  
        #Instructional Text
        sentence = "Drag and drop or select your file"
        self.instructions = tk.Label(self.dnd_frame, text=sentence, bg="#D9D9D9", font='Helvetica 18 bold', fg="grey")
        self.instructions.place(relx=0.5, rely=0.3, anchor="center")
        self.or_label = tk.Label(self.dnd_frame, text="or", bg="#D9D9D9", font='Helvetica 18 bold', fg="grey")
        self.or_label.place(relx=0.5, rely=0.5, anchor="center")
        #Select file button
        self.select_file = tkm.Button(self.dnd_frame, text="Select image", command=self.upload_image_handler) 
        self.select_file.place(relx=0.5, rely=0.7, anchor="center")
        
    
    def create_buttons(self):
        # one is a button to open new window to show exmaple image transformation
        # the second one is a download button
        # the last is a cancel button
        self.buttons_frame = tk.Frame(self.top_frame, width=400, height=70, bg="#CBC5B7")  
        self.buttons_frame.pack(pady=10)
        # add buttons
        self.create_button(self.buttons_frame, "View Example", "blue", self.open_example_window)
        self.create_button(self.buttons_frame, "Download", "red", self.start_download)
        self.create_button(self.buttons_frame, "Cancel", "grey", self.cancel_upload)

    def create_button(self, frame, btn_text, btn_color, function):
        btn = tkm.Button(frame, text=btn_text, command=function, fg="white", bg=btn_color,
                         font=("Helvetica", 14, "bold"), padx=10, pady=10, anchor=tk.CENTER, 
                         borderwidth=0, borderless=1)
        btn.pack(side=tk.LEFT, padx=5)  


    def drop_image_handler(self, event):
        # if file path is already uploaded or dropped, it's deleted
        if self.filepath:
            self.clear_image()
        # remove potential curly bracket
        self.filepath = event.data.strip('{}')
        if not self.filepath.lower().endswith(('.jpg', '.png')):
            self.clear_image()
            self.display_error_message("Pleasse upload .jpg or .png file")
        else: 
            messagebox.showinfo("", "Image uploaded successfully")


    def upload_image_handler(self):
        # if file path is already uploaded or dropped, it's deleted
        if self.filepath:
            self.clear_image()
        self.filepath = filedialog.askopenfilename()
        if not self.filepath.lower().endswith(('.jpg', '.png')):
            self.clear_image()
            self.display_error_message("Pleasse upload .jpg or .png file")
        else: 
            messagebox.showinfo("", "Image uploaded successfully")
    

    def clear_image(self):
        self.filepath = None;
        
    
    def open_example_window(self):
        pass

    def start_download(self):
        if not self.filepath:
            self.display_error_message("No image file selected.")
            self.clear_image()
            return
        try:
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': open(self.filepath, 'rb')},
                data={'size': 'auto'},
                headers={'X-Api-Key': api_key},
            )
        except Exception as e:
            self.display_error_message(f"Failed to upload image: {e}")
            self.clear_image()
            return
        
        if response.status_code == requests.codes.ok:
            save_dir = os.path.join(os.path.expanduser("~"), "Downloads")  # Save to the Downloads directory
            save_path = os.path.join(save_dir, 'no-bg.png')
            with open('no-bg.png', 'wb') as out:
                out.write(response.content)
                messagebox.showinfo("", "Image processed and downloaded successfully!")
        else:
            self.display_error_message(f"{response.status_code} {response.text}")
        self.clear_image()
    
    
    def cancel_upload(self):
        if self.filepath:
            if messagebox.askokcancel("Confirmation", "Are you sure you want to delete this image?"):
                self.clear_image(self)
            else:
                messagebox.showinfo("", "Deletion canceled")


    def display_error_message(self, message):
        messagebox.showerror("Error", message)



def main():
    root = TkinterDnD.Tk()
    app = Application(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()

