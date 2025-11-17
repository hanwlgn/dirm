import streamlit as st
from PIL import Image, ImageDraw
import os

st.set_page_config(page_title="발로란트 맵 드로잉", layout="wide")

st.title("🎮 발로란트 맵 드로잉 사이트")
st.write("원하는 맵을 선택하고 그림을 그릴 수 있어요!")

maps = {
    "Ascent": "maps/ascent.png",
    "Bind": "maps/bind.png",
    "Haven": "maps/haven.png"
}

selected_map = st.selectbox("맵 선택", list(maps.keys()))

# 이미지 불러오기
img_path = maps[selected_map]
img = Image.open(img_path)
draw = ImageDraw.Draw(img)

# 그리기 옵션
color = st.color_picker("색 선택", "#ff0000")
size = st.slider("펜 사이즈", 1, 30, 5)

st.write("마우스로 그림을 그려요:")

# 그림 그리기 인터페이스
canvas = st.canvas(
    fill_color="rgba(0, 0, 0, 0)",
    stroke_width=size,
    stroke_color=color,
    background_image=img,
    height=img.height,
    width=img.width,
    drawing_mode="freedraw",
    key="canvas",
)

# 저장 버튼
if st.button("이미지 저장"):
    if canvas.image_data is not None:
        out = Image.fromarray(canvas.image_data)
        out.save("saved_image.png")
        st.success("saved_image.png 로 저장됐어요!")

st.write("다른 맵은 왼쪽 메뉴에서 선택할 수 있어요!")
