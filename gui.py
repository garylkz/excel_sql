import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk
from tkinter.constants import BOTH, BOTTOM, DISABLED, END, LEFT, NORMAL, X

import lib


def set_label(widget: ttk.Label, text: str) -> None:
    widget.config(text=text)


def set_text(widget: st.ScrolledText, text: str) -> None:
    state = widget["state"]
    if state == DISABLED:
        widget.config(state=NORMAL)
    widget.delete(1.0, END)
    widget.insert(END, text)
    if state == DISABLED:
        widget.config(state=DISABLED)


root = tk.Tk()
root.title("XL2Q")

style = ttk.Style()
style.configure("BGRed.TFrame", background="red")
style.configure("BGGreen.TFrame", background="green")

# body
bodyLabel = ttk.Label(text="Page")
body = ttk.LabelFrame(root, labelwidget=bodyLabel)

# result
result = ttk.LabelFrame(root, labelwidget=ttk.Label(text="Result"))
resultValueFrame = ttk.Frame(result)
resultValue = st.ScrolledText(resultValueFrame)
resultValue.config(height=8, state=DISABLED)
resultActions = ttk.Frame(result)
resultCopy = ttk.Button(resultActions, text="Copy")

# home page
# homePage = ttk.Frame(body)

# insert page
insertPage = ttk.Frame(body)
insertTableFrame = ttk.Frame(insertPage)
insertTableLabel = ttk.Label(insertTableFrame, text="Table:")
insertTable = ttk.Entry(insertTableFrame)
## insert data
insertDataLabel = ttk.Label(
    insertPage, text="Paste the data copied from the Excel sheet here:"
)
insertDataFrame = ttk.Frame(insertPage)
insertData = st.ScrolledText(insertDataFrame)
insertData.config(height=8)
## insert data format
insertFormat = ttk.Frame(insertPage)
### insert data format labels
insertFormatLabels = ttk.Frame(insertFormat)
insertIgnoreLabel = ttk.Label(insertFormatLabels, text="Ignore column(s):")
insertNoTrimLabel = ttk.Label(insertFormatLabels, text="Don't trim column(s):")
### insert data format entries
insertFormatEntries = ttk.Frame(insertFormat)
insertIgnore = ttk.Entry(insertFormatEntries)
insertNoTrim = ttk.Entry(insertFormatEntries)
## insert options
insertOptions = ttk.Frame(insertPage)
insertVarHeader = tk.BooleanVar(value=True)
insertVarAtomic = tk.BooleanVar(value=True)
insertOptionHeader = ttk.Checkbutton(
    insertOptions, text="Has header", variable=insertVarHeader
)
insertOptionAtomic = ttk.Checkbutton(
    insertOptions, text="Atomic execution", variable=insertVarAtomic
)
## insert actions
insertActions = ttk.Frame(insertPage)
insertOk = ttk.Button(insertActions, text="Generate")
insertClear = ttk.Button(insertActions, text="Clear")


# navigation section
nav = ttk.LabelFrame(root, labelwidget=ttk.Label(text="Functions"))
navFrame = ttk.Frame(nav)
# navigation buttons
# navHome = ttk.Button(navFrame, text="Home", padding=8)
navInsert = ttk.Button(navFrame, text="INSERT from Excel", padding=8)


def insert_ok():
    table = lib.table_name_of(insertTable.get())
    data = insertData.get(1.0, END)
    ignores = {int(val) for val in insertIgnore.get().split() if val.isnumeric()}
    nostrips = {int(val) for val in insertNoTrim.get().split() if val.isnumeric()}
    if table == "":
        set_text(resultValue, "Table name can't be empty!")
        return
    elif data.strip() == "":
        set_text(resultValue, "Data field can't be empty!")
        return
    try:
        result = lib.excel_insert(
            table,
            data,
            ignores=ignores,
            nostrips=nostrips,
            hasHeader=insertVarHeader.get(),
            atomic=insertVarAtomic.get(),
        )
        set_text(resultValue, result)
    except Exception as e:
        set_text(resultValue, f"Error generating query!\n{e}")


def insert_clear():
    insertTable.delete(0, END)
    insertData.delete(1.0, END)


def clear_result():
    set_text(resultValue, "")


def copy_result():
    root.clipboard_clear()
    root.clipboard_append(resultValue.get(1.0, END))


# def goto_home():
#     clear_result()
#     set_label(bodyLabel, "Home")
#     insertPage.pack_forget()
#     homePage.pack(fill=BOTH, expand=1)


# navigation functions
def goto_insert():
    clear_result()
    set_label(bodyLabel, "INSERT from Excel")
    # homePage.pack_forget()
    insertPage.pack(fill=BOTH, expand=1, anchor="n")


# binding command to buttons
navInsert.config(command=goto_insert)
insertOk.config(command=insert_ok)
insertClear.config(command=insert_clear)
resultCopy.config(command=copy_result)

# packing ui
# nav.pack(fill=X, padx=12, pady=4)
# navFrame.pack(fill=X, padx=3)
# # navHome.pack(side=LEFT, fill=X, expand=1, padx=1)
# navInsert.pack(side=LEFT, fill=X, expand=1, padx=1)
# ttk.Frame(nav).pack(side=BOTTOM, fill=X, expand=1, pady=2)

body.pack(fill=BOTH, expand=1, padx=12, pady=4)

# ttk.Frame(homePage).pack(pady=16)

insertTableFrame.pack(fill=X, padx=4)
insertTableLabel.pack(side=LEFT)
ttk.Frame(insertTableFrame).pack(side=LEFT, padx=4)
insertTable.pack(side=LEFT)
ttk.Frame(insertPage).pack(pady=2)

insertDataLabel.pack(fill=X, padx=4, pady=2)
insertDataFrame.pack(fill=X)
ttk.Frame(insertDataFrame).pack(side=LEFT, padx=2)
insertData.pack(side=LEFT, fill=X, expand=1)
ttk.Frame(insertPage).pack(pady=2)

insertOptions.pack(fill=X, padx=3)
insertOptionHeader.pack(side=LEFT, padx=1)
insertOptionAtomic.pack(side=LEFT, padx=1)
ttk.Frame(insertPage).pack(pady=2)

insertFormat.pack(fill=X, padx=4)
insertFormatLabels.pack(side=LEFT)
insertIgnoreLabel.pack(fill=X)
ttk.Frame(insertFormatLabels).pack(pady=1)
insertNoTrimLabel.pack()
ttk.Frame(insertFormat).pack(side=LEFT, padx=2)
insertFormatEntries.pack(side=LEFT)
insertIgnore.pack()
ttk.Frame(insertFormatEntries).pack(pady=1)
insertNoTrim.pack()

ttk.Frame(insertPage).pack(expand=1, pady=2)

insertActions.pack(fill=X, padx=3)
insertOk.pack(side=LEFT, padx=1)
insertClear.pack(side=LEFT, padx=1)

ttk.Frame(body).pack(side=BOTTOM, pady=2)

result.pack(fill=X, padx=12, pady=4)
resultValueFrame.pack(fill=X)
ttk.Frame(resultValueFrame).pack(side=LEFT, padx=2)
resultValue.pack(side=LEFT, fill=X, expand=1)
ttk.Frame(result).pack(pady=2)
resultActions.pack(fill=X, padx=4)
resultCopy.pack(side=LEFT)
ttk.Frame(result).pack(pady=2)

ttk.Frame(root).pack(pady=2)

goto_insert()  # set initial page

root.mainloop()
