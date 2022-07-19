from main import *
from libraries import *

window = Window()

test_label = ctk.CTkLabel(master=window.frame_left, text='Test')
test_label.grid(row=0, column=0)