import numpy as np
import pandas as pd
from ortoolpy import knapsack

class GochiSolver:
    def __init__(self):
        self.W = []
        self.C = 0

        self.x = []

        self.model = None

        self.total = 0
        self.order_ids = []

    def set_data(self, weight_df, capacity):
        self.W = weight_df['price'].tolist()
        self.C = capacity
        # print(weight_df)
        # print(capacity)

    def show(self):
        print("W:", self.W)
        print("C: ", self.C)

    def solve(self):
        self.total, self.order_ids = knapsack(self.W, self.W, self.C)

if __name__ == "__main__":
    weight_df = pd.read_csv("gochi-menu.csv")
    capacity = 14800

    gochi = GochiSolver()
    gochi.set_data(weight_df, capacity)
    gochi.show()
    gochi.solve()
    print(gochi.total)
    print(gochi.order_ids)
