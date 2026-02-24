import streamlit as st
from Solver import solve_24

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