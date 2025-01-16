import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

"""# リーマン和"""

"""___"""

formula = st.selectbox(
    "式を選んでください",
    ("1", "2", "3"),
)

tub_dict = {"指定する":0,"∞":1}
selected_cbox = st.radio(label="分割数を選んでください", options = tub_dict.keys(),horizontal=True)

if tub_dict[selected_cbox] == 0 :
    n = st.number_input("分割数を入力してください", value=0, step=1)
    a = st.number_input("区域の始まり入力してください", value=0, step=1)
    b = st.number_input("区域の終わりを入力してください", value=0, step=1)

    st.write("n = ", n)
    st.write("a = ", a)
    st.write("b = ", b)

elif tub_dict[selected_cbox] == 1 :
    a = st.number_input("区域の始まり入力してください", value=0, step=1)
    b = st.number_input("区域の終わりを入力してください", value=0, step=1)
    n = abs(b-a) * 1000
    
    st.write("n = ∞")
    st.write("a = ", a)
    st.write("b = ", b)

#関数
def f(x):
    return np.sin(x) + 10
#区間・分割数
if n!=0 and a<b:
    if st.button("結果の表示"):    


        # 区間の分割
        x = np.linspace(a, b, n+1)  # n+1に均等に分ける
        x_right = x[1:]  # 右端点 2番目以降を取り出す
        y_right = f(x_right)

        # 棒グラフのデータ
        bar_x = x_right - (b-a)/n/2  # 棒の中心
        bar_width = (b-a)/n  # 棒の幅

        # 関数の曲線データ
        x_curve = np.linspace(a, b, 500)  # 曲線用のx
        y_curve = f(x_curve)  # 曲線用のy

        # グラフの作成
        fig = go.Figure()

        # 関数の曲線
        fig.add_trace(go.Scatter(x=x_curve, y=y_curve, mode='lines', name='f(x) = sin(x)+10'))

        # 棒グラフ (右リーマン和)
        fig.add_trace(go.Bar(
            x=bar_x, 
            y=y_right, 
            width=bar_width, 
            name='右リーマン和', 
            marker=dict(color='rgba(200, 50, 50, 0.6)')
        ))

        # レイアウトを設定
        fig.update_layout(
            title="右リーマン和 (f(x) = sin(x)+10)",
            xaxis_title="x",
            yaxis_title="f(x)",
            barmode='overlay',
            template="plotly_white"
        )
        right_riemann = np.sum(y_right * bar_width)
        st.write(fig)
        st.write(right_riemann)


        # 左リーマン和

        x = np.linspace(a, b, n+1)  # n+1に均等に分ける
        x_left = x[:-1]  # 右端点 2番目以降を取り出す
        y_left = f(x_left)

        # 棒グラフのデータ
        bar_x = x_left + (b-a)/n/2 # 棒の中心
        bar_width = (b-a)/n  # 棒の幅

        # 関数の曲線データ
        x_curve = np.linspace(a, b, 500)  # 曲線用のx
        y_curve = f(x_curve)  # 曲線用のy

        # グラフの作成
        fig = go.Figure()

        # 関数の曲線
        fig.add_trace(go.Scatter(x=x_curve, y=y_curve, mode='lines', name='f(x) = sin(x)+10'))

        # 棒グラフ 
        fig.add_trace(go.Bar(
            x=bar_x, 
            y=y_left, 
            width=bar_width, 
            name='左リーマン和', 
            marker=dict(color='rgba(200, 50, 50, 0.6)')
        ))

        # レイアウトを設定
        fig.update_layout(
            title="左リーマン和 (f(x) = sin(x)+10)",
            xaxis_title="x",
            yaxis_title="f(x)",
            barmode='overlay',
            template="plotly_white"
        )

        left_riemann = np.sum(y_left * bar_width)

        st.write(fig)
        st.write(left_riemann)

        # 中央リーマン和
        x_mid = x_left + (b-a)/n/2
        y_mid = f(x_mid)

        # グラフの作成
        fig = go.Figure()

        # 関数の曲線
        fig.add_trace(go.Scatter(x=x_curve, y=y_curve, mode='lines', name='f(x) = sin(x)+10'))

        # 棒グラフ 
        fig.add_trace(go.Bar(
            x=x_mid, 
            y=y_mid, 
            width=bar_width, 
            name='中央リーマン和', 
            marker=dict(color='rgba(200, 50, 50, 0.6)')
        ))

        # レイアウトを設定
        fig.update_layout(
            title="中央リーマン和 (f(x) = sin(x)+10)",
            xaxis_title="x",
            yaxis_title="f(x)",
            barmode='overlay',
            template="plotly_white"
        )

        mid_riemann = np.sum(y_mid * bar_width)
        st.write(fig)
        st.write(mid_riemann)

        # 上リーマン和

        # 各区間の上リーマン和の計算
        x_intervals = [(x[i], x[i+1]) for i in range(n)]  # 各区間 [x[i], x[i+1]]
        y_top = np.array([max(f(np.linspace(start, end, 10))) for start, end in x_intervals])  # 各区間での最大値

        # グラフの作成
        fig = go.Figure()

        # 関数の曲線
        fig.add_trace(go.Scatter(x=x_curve, y=y_curve, mode='lines', name='f(x) = sin(x)+10'))

        # 棒グラフ 
        fig.add_trace(go.Bar(
            x=bar_x, 
            y=y_top, 
            width=bar_width, 
            name='上リーマン和', 
            marker=dict(color='rgba(200, 50, 50, 0.6)')
        ))

        # レイアウトを設定
        fig.update_layout(
            title="上リーマン和 (f(x) = sin(x)+10)",
            xaxis_title="x",
            yaxis_title="f(x)",
            barmode='overlay',
            template="plotly_white"
        )
        top_riemann = np.sum(y_top * bar_width)
        st.write(fig)
        st.write(top_riemann)


        # 下リーマン和
        y_bottom = np.array([min(f(np.linspace(start, end, 10))) for start, end in x_intervals])  # 各区間での最大値
        # グラフの作成
        fig = go.Figure()

        # 関数の曲線
        fig.add_trace(go.Scatter(x=x_curve, y=y_curve, mode='lines', name='f(x) = sin(x)+10'))

        # 棒グラフ 
        fig.add_trace(go.Bar(
            x=bar_x, 
            y=y_bottom, 
            width=bar_width, 
            name='下リーマン和', 
            marker=dict(color='rgba(200, 50, 50, 0.6)')
        ))

        # レイアウトを設定
        fig.update_layout(
            title="下リーマン和 (f(x) = sin(x)+10)",
            xaxis_title="x",
            yaxis_title="f(x)",
            barmode='overlay',
            template="plotly_white"
        )
        bottom_riemann = np.sum(y_bottom * bar_width)
        st.write(fig)
        st.write(bottom_riemann)