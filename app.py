from itertools import cycle

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

from battle import Battle

# SETUP ------------------------------------------------------------------------
favicon = Image.open("favicon.ico")
st.set_page_config(
    page_title="Super Hero Battle",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="auto",
)


# ROW 1 ------------------------------------------------------------------------

Title_html = """
    <style>
        .title h1{
          user-select: none;
          font-size: 43px;
          color: white;
          background: repeating-linear-gradient(-45deg, red 0%, yellow 7.14%, rgb(0,255,0) 14.28%, rgb(0,255,255) 21.4%, cyan 28.56%, blue 35.7%, magenta 42.84%, red 50%);
          background-size: 300vw 300vw;
          -webkit-text-fill-color: transparent;
          -webkit-background-clip: text;
          animation: slide 10s linear infinite forwards;
        }
        @keyframes slide {
          0%{
            background-position-x: 0%;
          }
          100%{
            background-position-x: 600vw;
          }
        }
    </style> 
    
    <div class="title">
        <h1>Super Hero Battle</h1>
    </div>
    """
st.markdown(
    "_Random **5 vs 5** team battle using [SuperHeroAPI](https://akabab.github.io/superhero-api/api/)_"
)
st.markdown(
    "Hecho con :heartbeat: por [Pipe](https://www.linkedin.com/in/pipesanmartin/)"
)
components.html(Title_html)


# ROW 2 ------------------------------------------------------------------------
with st.form("Teams_names"):

    row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3 = st.columns(
        (0.1, 0.5, 0.05, 0.5, 0.1)
    )
    with row2_1:

        team_1 = st.text_input("Team 1", value="Marvel", key="team_1")
        boton = st.form_submit_button("Create Teams")

    with row2_spacer2:
        st.write("")
        st.write("")
        st.subheader("VS")

    with row2_2:

        team_2 = st.text_input("Team 2", value="Capcom", key="team_2")


if boton:

    # Haciendo algunos check's

    if not team_1 or not team_2:

        st.warning("Put names to the teams")
        st.stop()

    with st.spinner("Creating teams...."):

        try:

            battle = Battle(name_team_1=team_1, name_team_2=team_2)
            battle.create_teams()

            # ROW 3 ------------------------------------------------------------------------
            row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3 = st.columns(
                (1.0, 1.5, 2.0, 1.0, 1.0)
            )
            with row2_1:
                st.header(battle._team_1.name)

            with row2_2:
                st.header(battle._team_2.name)

            # ROW 4 ------------------------------------------------------------------------
            images_team_1 = [member.images["sm"] for member in battle._team_1.members]
            captions_team_1 = [member.name for member in battle._team_1.members]

            images_team_2 = [member.images["sm"] for member in battle._team_2.members]
            captions_team_2 = [member.name for member in battle._team_2.members]
            cols = cycle(st.columns(11))
            vs_image = ["vs_transparent.png"]
            vs_caption = ["Versus"]
            images = images_team_1 + vs_image + images_team_2

            captions = captions_team_1 + vs_caption + captions_team_2
            for idx, image in enumerate(images):
                next(cols).image(image, width=100, caption=captions[idx])

        except Exception as e:

            st.error("Something went grong...")
            st.exception(e)
            st.stop()

        with st.spinner("Preparing teams to fight"):

            try:

                battle.prepare_teams_to_fight()

            except Exception as e:

                st.error("Something went grong...")
                st.exception(e)
                st.stop()

    st.session_state.battle = battle

if st.button("Start Battle"):
    try:

        st.session_state.battle.start()
    except Exception as e:

        st.error("You need to create the teams first")
        print(e)
    st.success("Battle ends!")

else:
    st.caption("You should create teams first")
