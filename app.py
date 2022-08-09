import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

from battle import Battle
from displays import display_5_vs_5_teams

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


def create_battle(name_1, name_2):
    battle = Battle(name_team_1=name_1, name_team_2=name_2)
    battle.create_teams()
    battle.prepare_teams_to_fight()
    return battle


row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3 = st.columns(
    (0.1, 0.5, 0.05, 0.5, 0.1)
)
with row2_1:

    team_1 = st.text_input("Team 1", value="Marvel", key="team_1")
    fast_agree = st.checkbox("Fast Mode")
    button1 = st.button("Start Battle")


with row2_spacer2:
    st.write("")
    st.write("")
    st.subheader("VS")

with row2_2:

    team_2 = st.text_input("Team 2", value="Capcom", key="team_2")


if not st.session_state.get("button1"):

    st.session_state["button1"] = button1

if st.session_state["button1"]:

    # Haciendo algunos check's

    if not team_1 or not team_2:

        st.warning("Put names to the teams")
        st.stop()

    with st.spinner("Creating teams...."):

        try:

            st.session_state.battle = create_battle(team_1, team_2)
        except Exception as e:

            st.error("Something went grong...")
            st.exception(e)
            st.stop()

    # ROW 3 ------------------------------------------------------------------------
    row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3 = st.columns(
        (1.0, 1.5, 2.0, 1.0, 1.0)
    )
    with row2_1:
        st.header(st.session_state.battle._team_1.name)

    with row2_2:
        st.header(st.session_state.battle._team_2.name)

    # ROW 4 ------------------------------------------------------------------------
    display_5_vs_5_teams(
        st.session_state.battle._team_1.members,
        st.session_state.battle._team_2.members,
    )
    if fast_agree:

        with st.spinner("Fighting in fast mode...."):
            try:
                (
                    battle_info,
                    battle_history,
                ) = st.session_state.battle.streamlit_fast_battle_start()
            except Exception as e:
                st.error("You need to create the teams first")
                print(e)
    else:
        try:
            battle_info, battle_history = st.session_state.battle.streamlit_start()
        except Exception as e:
            st.error("You need to create the teams first")
            print(e)

    # ROW 5 ------------------------------------------------------------------------

    ###not working
    # display_json_battle_details(battle_info, battle_history)

    st.write(battle_info)

    total_fights = len(battle_history)
    fights_names = []
    for i in range(total_fights):
        fights_names.append(f"Fight N°: {i+1}")
    tabs = st.tabs(fights_names)

    for tab, fight_info in zip(tabs, battle_history):

        with tab:
            st.write(fight_info)
