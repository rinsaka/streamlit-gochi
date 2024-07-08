import streamlit as st
import pandas as pd
from GochiSolver import GochiSolver


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
    st.markdown('- 下限は最も安い料理だけを注文する場合')
    st.markdown('- 上限はすべての料理を注文する場合')
    if weight_file is None:
        st.markdown("- メニューデータをアップロードしてください")
    else:
        min_weight = weight_file['price'].min()
        sum_weight = weight_file['price'].sum()
        capacity = st.slider('スライドさせて予算を設定してください', min_value=min_weight, max_value=sum_weight)  # スライダー

with tab3:
    if weight_file is None:
        st.markdown("- メニューデータをアップロードしてください")
    else:
        st.markdown('### 注文の作成')
        solver_button = st.button("注文を作成する")
        if solver_button:
            gochi = GochiSolver()
            gochi.set_data(weight_file, capacity)
            gochi.solve()

            if gochi.C == gochi.total :
                st.markdown("#### 解が見つかりました")
            else:
                st.markdown("#### 解は見つかりませんでした")
                st.markdown(f"- 差額: {gochi.total - gochi.C}")
            st.markdown(f"- 予算額: {gochi.C}")
            st.markdown(f"- 注文合計額: {gochi.total}")
            # st.markdown(f"- 注文メニュー: {gochi.order_ids}")

            st.table(gochi.order_df)
