import streamlit as st
from Solver import solve_24

import streamlit as st
from Solver import solve_24

# 页面配置，隐藏菜单、页脚 Streamlit 标志
st.set_page_config(
    page_title="24点计算器",
    page_icon="🃏",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 通过 CSS 隐藏右上角菜单和页脚
hide_streamlit_style = """
    <style>
    /* 隐藏右上角菜单 */
    #MainMenu {visibility: hidden;}
    /* 隐藏 Streamlit 页脚 */
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)




st.title("24点计算器")

cards = st.text_input("输入四张牌 (如: J Q K 2)")

if st.button("计算"):
    if cards:
        solutions = solve_24(cards.split())

        if solutions:
            st.success(f"找到 {len(solutions)} 个解")
            for s in solutions:
                st.write(s)
        else:
            st.error("无解")