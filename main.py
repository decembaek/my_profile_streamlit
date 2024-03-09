import streamlit as st

from features.my_card import my_card

# import emoji

# 이모티콘 목록 출력
# print(emoji.EMOJI_DATA)


def project_card(st, title, descript, image_path, github):
    card_container = st.container(border=True)
    card_container.subheader(title)
    card_container.write(descript)


# 자기소개
def introduce_card(st):
    st.subheader("win or Learn, 이기거나 배워")
    st.write(
        """안녕하세요, Python 백엔드 개발자 백승규라고 합니다.
             마음껏 구경해주세요"""
    )
    # st.write("""안녕하세요, Python 백엔드 개발자 백승규라고 합니다.""")


# 💌💾📝


# 명함 카드 ------
def main():
    st.title("Decembaek Library")
    st.write("Python으로 제작되었습니다.")
    # 명함
    my_card(st)

    # 자기소개
    introduce_card(st)

    # 프로젝트 카드
    project_card(
        st,
        title="airbnb 에어비앤비 클론코딩",
        descript="Python Django로 에어비앤비 클론코딩을 진행했습니다.",
        image_path="",
        github=[
            {
                "dev": "Frontend",
                "name": "airbnb Frontend",
                "skill": [""],
            },
            {
                "dev": "Backend",
                "name": "airbnb Backend",
                "skill": [""],
            },
        ],
    )


if __name__ == "__main__":
    st.set_page_config(
        page_title="Decembaek_library",
        page_icon="images/Original.png",
        initial_sidebar_state="expanded",
        layout="centered",
        menu_items={
            # "Get Help": "https://www.extremelycoolapp.com/help",
            # "Report a bug": "https://www.extremelycoolapp.com/bug",
            "About": "# 오직 Python으로만 만들었습니다. skill : Streamlit ",
        },
    )
    st.sidebar.subheader("Profile")
    st.sidebar.page_link("main.py", label="Instagram", icon="💌")
    st.sidebar.page_link("main.py", label="Github", icon="💾")
    st.sidebar.page_link("main.py", label="Blog", icon="📝")
    main()
