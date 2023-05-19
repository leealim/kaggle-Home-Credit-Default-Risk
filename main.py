import tkinter as tk
import pandas as pd


class MainWindow:
    def __init__(self, mw) -> None:
        self.mainWindow = mw
        self.mainWindow.title("Credit Risk Evalution")
        self.mainWindow.geometry("800x500")
        self.labels_entrys = dict()

    def createUI(self):
        self.create_button()
        scrollbar = tk.Scrollbar(mainWindow)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas = tk.Canvas(mainWindow, yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        max_len=50
        ite = pd.read_csv("ui_item_res.csv")
        for row_index, row in ite.iterrows():
            lines = [row["Description"][i:i+max_len] for i in range(0, len(row["Description"]), max_len)]
            wrapped_text = "\n".join(lines)
            # 创建标签
            label = tk.Label(frame, text=row["Row"])
            label.grid(row=row_index, column=0)
            # 创建文本框
            entry = tk.Entry(frame)
            entry.insert(0, str(row["Example"]))
            entry.grid(row=row_index, column=1)
            label = tk.Label(frame, text=wrapped_text,anchor='w')

            label.grid(row=row_index, column=2)
            self.labels_entrys[row["Row"]] = entry
            

        frame.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))
        scrollbar.config(command=canvas.yview)

    def create_button(self):
        def on_submit():
            # app_te_path = "data\\home-credit-default-risk\\application_test.csv"
            # app_te = pd.read_csv(app_te_path)
            # test_example=app_te.iloc[0, :]
            # todo
            pass

        submit_button = tk.Button(mainWindow, text="Submit", command=on_submit)
        submit_button.pack()


mainWindow = tk.Tk()
MainWindow(mainWindow).createUI()
mainWindow.mainloop()
