import streamlit as st
from PIL import Image
st.title("▶ Ascent 맵")

st.write("이 페이지에서도 그림 그릴 수 있어요!")

img = Image.open("maps/ascent.png")

canvas = st.canvas(
    fill_color="rgba(0, 0, 0, 0)",
    stroke_width=5,
    stroke_color="#00ff00",
    background_image=img,
    height=img.height,
    width=img.width,
    drawing_mode="freedraw",
)
