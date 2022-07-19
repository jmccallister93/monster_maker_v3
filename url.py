import webbrowser
from data.combobox_options import *
from data.label_options import *
from data.url_links import *


#Define a callback function
def callback(url):
    webbrowser.open_new_tab(url)

