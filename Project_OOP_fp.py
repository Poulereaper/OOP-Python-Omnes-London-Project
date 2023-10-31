#First Page of the Project test repository
import tkinter as tk
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tk.Tk()
        self.main_window.title("Home Page")
        self.main_window.geometry("900x500")
        # Create a frame at the top for buttons
        self.top_frame = tk.Frame(self.main_window)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Create buttons
        self.my_button_Log = tk.Button(self.top_frame, text='Sign In or Sign Up', command=self.do_something_one)
        self.my_button_Search = tk.Button(self.top_frame, text='Advanced Search', command=self.do_something_two)

        # Pack the 'Sign In or Sign Up' button to the left (west)
        self.my_button_Log.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=10, pady=10)
        # Pack the 'Advanced Search' button to the right (east)
        self.my_button_Search.pack(ipadx=5, ipady=5, side=tk.RIGHT, padx=10, pady=10)

        #Creat a list box of the days of the week
        self.label = tk.Label(self.main_window, text="Select your favorite day")
        self.listbox = tk.Listbox(self.main_window, height=0, width=0)
        self.listbox.pack()
        day=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        for item in day:
            self.listbox.insert(tk.END, item) 
        #I want to select one ittem in the list by using the selectmode
         
        #Now I want to create a button that will print the selected item in the listbox
         #self.my_button = tkinter.Button(self.main_window, text='Click Me!', command=self.do_something)
        tk.mainloop()

    def do_something_one(self):
        tk.messagebox.showinfo('Response', 'Thanks for clicking the button.')
        #print("You clicked the button!")
    def do_something_two(self):
        tk.messagebox.showinfo('Response', 'Thanks for clicking the button.')
        #print("You clicked the button!")

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
    