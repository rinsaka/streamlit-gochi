import numpy as np
import pandas as pd
from ortoolpy import knapsack
import argparse

class GochiSolver:
    """
    ゴチのソルバー
    """
    def __init__(self):
        self.W = [] # 価格
        self.C = 0  # 予算
        self.ID = []
        self.Menu = []
        self.Size = []

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

    def show(self):
        print("W:", self.W)
        print("C: ", self.C)
        print("ID: ", self.ID)
        print("Menu: ", self.Menu)
        print("Size: ", self.Size)

    def solve(self):
        # 問題を解く
        self.total, self.order_ids = knapsack(self.W, self.W, self.C)
        # 注文するかしないか
        orders = np.zeros(len(self.ID), dtype=np.int64) # ゼロで初期化
        orders[self.order_ids] = 1 # 注文するメニューを設定
        # 全メニューのデータフレームに注文データ(0-1変数)も追加する
        self.menu_df = pd.DataFrame(
            {
                'no': self.ID,
                'menu': self.Menu,
                'size': self.Size,
                'price': self.W,
                'order' : orders
            }
        )
        # 注文メニューだけのデータフレーム
        self.order_df = self.menu_df[self.menu_df.order > 0]


def get_args():
    """
    コマンドライン引数を取り出す処理を行う関数
    """
    # オブジェクトを生成する
    parser = argparse.ArgumentParser()
    # 予算はオプショナル引数
    parser.add_argument("-c", "--capacity", type=int, help="Capacity")
    args = parser.parse_args()
    return(args)

if __name__ == "__main__":
    args = get_args()
    if args.capacity:
        capacity = args.capacity
    else:
        capacity = 2980
        # capacity = 31560
        # capacity = 31453

    url = "https://github.com/rinsaka/sample-data-sets/blob/master/gochi-menu.csv?raw=true"
    # url = "gochi-menu.csv"  # カレントディレクトリから読み込む場合
    weight_df = pd.read_csv(url)

    gochi = GochiSolver()
    gochi.set_data(weight_df, capacity)
    # gochi.show()  # 確認のために読み込んだデータを表示する
    gochi.solve()

    if gochi.C == gochi.total:
        print("解が見つかりました")
    else:
        print("解は見つかりませんでした")
        print(f"- 差額: {gochi.total - gochi.C}")
    print(f"- 予算額: {gochi.C}")
    print(f"- 注文合計額: {gochi.total}")
    print("")
    print(gochi.order_df)
