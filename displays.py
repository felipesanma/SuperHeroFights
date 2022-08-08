from itertools import cycle

import streamlit as st


def display_5_vs_5_teams(members_team_1, members_team_2) -> None:

    images_team_1 = [member.images["sm"] for member in members_team_1]
    captions_team_1 = [member.name for member in members_team_1]

    images_team_2 = [member.images["sm"] for member in members_team_2]
    captions_team_2 = [member.name for member in members_team_2]
    cols = cycle(st.columns(11))
    vs_image = ["vs_transparent.png"]
    vs_caption = ["Versus"]
    images = images_team_1 + vs_image + images_team_2

    captions = captions_team_1 + vs_caption + captions_team_2
    for idx, image in enumerate(images):
        next(cols).image(image, width=100, caption=captions[idx])
