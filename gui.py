import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, BOTTOM, CENTER, LEFT, X

page = 0


def set_label(label: ttk.Label, text: str) -> None:
    label.config(text=text)


root = tk.Tk()
root.title("XL2Q")

# main functions
bodyLabel = ttk.Label(text="Page")
body = ttk.LabelFrame(root, labelwidget=bodyLabel)

# home page
homePage = ttk.Frame(body)

# insert page
insertPage = ttk.Frame(body)


def goto_home():
    set_label(bodyLabel, "Home")
    homePage.lift()


# navigation functions
def goto_insert():
    set_label(bodyLabel, "INSERT from Excel")
    insertPage.lift()


# navigation ui
nav = ttk.LabelFrame(root, labelwidget=ttk.Label(text="Functions"))
navFrame = ttk.Frame(nav)
# navigation buttons
navHome = ttk.Button(navFrame, text="Home", padding=8, command=goto_home)
navInsert = ttk.Button(
    navFrame, text="INSERT from Excel", padding=8, command=goto_insert
)
navPadding = ttk.Frame(nav)

# packing ui
nav.pack(fill=X, pady="8", padx="12")
navFrame.pack(fill=X, padx="3")
navHome.pack(side=LEFT, fill=X, expand=True, padx="1")
navInsert.pack(side=LEFT, fill=X, expand=True, padx="1")
navPadding.pack(side=BOTTOM, fill=X, expand=True, pady=2)
body.pack(fill=BOTH, expand=True, padx="12")
homePage.pack(fill=BOTH, expand=True, anchor=CENTER)
insertPage.pack(fill=BOTH, expand=True, anchor=CENTER)
ttk.Frame().pack(pady=4)

goto_home()  # set initial page

root.mainloop()
