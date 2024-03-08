import streamlit as st

st.set_page_config(
    page_title="Decembaek_library",
    page_icon="images\Original.png",
    layout="centered",
)
st.page_link("main.py", label="Home", icon="🏠")

st.title("Decembaek Library")

# 명함 카드 ------
card_container = st.container(border=True)
col1, col2, col3 = card_container.columns([0.5, 0.8, 0.1])

col1.image(
    "images/circle_profile.png",
    caption="",
    width=130,
    # use_column_width="always",
)
col1.subheader("")
col1.subheader("Decembaek")

col2.subheader("백승규 Seunggyu Baek")
col2.write("경력 1년 Python 백엔드 개발자")
col2.write("Email : tmdrbpp123@gmail.com")
col2.write("SKill : Python, Django, deploy, Streamlit, Dart, Flutter")
github, blog, _ = col2.columns([6, 6, 8])
github.link_button(
    "Go to Blog", "https://wingyu-story.tistory.com/", help="블로그 이동"
)
blog.link_button("Go to Blog", "https://wingyu-story.tistory.com/", help="블로그 이동")
# 명함 카드 ------
