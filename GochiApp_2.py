import streamlit as st
import pandas as pd

st.title("ゴチバトルソルバー")

# サイドバー
st.sidebar.header("CSVファイルのアップロード")
weight_file = st.sidebar.file_uploader("メニューデータ", ["csv"])

# タブ
tab1, tab2, tab3 = st.tabs(
  [
    "メニュー情報",
    "予算の設定",
    "注文の作成"
  ]
)

with tab1:
  if weight_file is None:
    st.markdown("- メニューデータをアップロードしてください")
  else:
    st.markdown('### メニュー情報')
    weight_file = pd.read_csv(weight_file)
    st.table(weight_file)

with tab2:
  st.markdown('### 予算の設定')

with tab3:
  st.markdown('### 注文の作成')
