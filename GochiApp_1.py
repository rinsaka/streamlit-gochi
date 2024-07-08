import streamlit as st

st.title("ゴチバトルソルバー")

st.sidebar.header("CSVファイルのアップロード")

# タブ
tab1, tab2, tab3 = st.tabs(
  [
    "メニュー情報",
    "予算の設定",
    "注文の作成"
  ]
)

with tab1:
  st.markdown('### メニュー情報')

with tab2:
  st.markdown('### 予算の設定')

with tab3:
  st.markdown('### 注文の作成')
