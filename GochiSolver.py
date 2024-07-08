import numpy as np
import pandas as pd
from ortoolpy import knapsack

class GochiSolver:
    def __init__(self):
        self.W = []
        self.C = 0
        self.ID = []
        self.Menu = []
        self.Size = []

        self.x = []

        self.total = 0
        self.order_ids = []

        self.menu_df = None
        self.order_df = None # 注文するメニューのデータフレーム

    def set_data(self, weight_df, capacity):
        self.W = weight_df['price'].tolist()
        self.C = capacity
        self.ID = weight_df['no'].tolist()
        self.Menu = weight_df['menu'].tolist()
        self.Size = weight_df['size'].tolist()
        # print(weight_df)
        # print(capacity)

    def show(self):
        print("W:", self.W)
        print("C: ", self.C)
        print("ID: ", self.ID)
        print("Menu: ", self.Menu)
        print("Size: ", self.Size)

    def solve(self):
        self.total, self.order_ids = knapsack(self.W, self.W, self.C)
        orders = np.zeros(len(self.ID), dtype=np.int64) # ゼロで初期化
        orders[self.order_ids] = 1 # 注文するメニューを設定
        self.menu_df = pd.DataFrame(
            {
                'no': self.ID,
                'menu': self.Menu,
                'size': self.Size,
                'price': self.W,
                'order' : orders
            }
        )
        self.order_df = self.menu_df[self.menu_df.order > 0]

if __name__ == "__main__":
    weight_df = pd.read_csv("gochi-menu.csv")
    capacity = 14800

    gochi = GochiSolver()
    gochi.set_data(weight_df, capacity)
    gochi.show()
    gochi.solve()
    print(gochi.total)
    print(gochi.order_ids)
    # print(gochi.menu_df)
    print(gochi.order_df)
