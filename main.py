import streamlit as st
import time # 時間を扱う機能

st.title("streamlitの基礎")
st.write("Hello World")

col1, col2 = st.columns(2) # レイアウトとして２列を定義

# 1列目をwithで囲む
with col1:
    st.write("列1がここに表示されます")

# 2列目をwithで囲む
with col2:
    st.write("列2がここに表示されます")

st.sidebar.write("hello world") #.sidebar付けるとサイトバーに出力されます。
st.text_input("ここに文字が入力できます") 

slider_text = st.slider("スライダーで数字を決定できます。", 0, 100, 5) # (最小、最大値、デフォルト値)の順で設定されます。
"スライダーの数字", slider_text

st.button("ボタン")

x = st.empty()
bar = st.progress(0)

for i in range(100):
    time.sleep(0.1)
    x.text(i)
    bar.progress(i)
    i += 1

st.selectbox("選んでください", ["選択肢1", "選択肢2", "選択肢3"])

output_text = "この文字がダウンロードできます。"

st.download_button(label='記事内容 Download',
                   data=output_text,
                   file_name='out_put.txt',
                   mime='text/plain'
                   )

faile_upload = st.file_uploader("ここに音声認識したファイルをアップロードしてください", type=["png", "jpg"])

if(faile_upload !=None):
    st.image(faile_upload)

import numpy as np
import pandas as pd

def rand_df(r=10, c=5):
    df = pd.DataFrame(
        np.random.randn(r,c),
        columns=('col %d' % i for i in range(c)))
    return df

dataframe = rand_df(r=10, c=3)

st.dataframe(dataframe.head(n=3))
st.line_chart(dataframe)