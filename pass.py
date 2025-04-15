import streamlit as st
import random

# Elo functions
def elo(playera, playerb):
    return 1 / (1 + 10 ** ((playerb - playera) / 400))

def elo_most(old_rating, opponent_rating, k_factor, actual_score):
    expected_score = elo(old_rating, opponent_rating)
    return old_rating + k_factor * (actual_score - expected_score)

# Initialize session state for ratings
if 'player_a' not in st.session_state:
    st.session_state.player_a = 1000
if 'player_b' not in st.session_state:
    st.session_state.player_b = 1000
if 'left_index' not in st.session_state:
    st.session_state.left_index = 0
if 'right_index' not in st.session_state:
    st.session_state.right_index = 1

# Generate image URLs for image_1.webp to image_100.webp
image_list = [f"https://raw.githubusercontent.com/MuhammadHamza123c/Rating/main/image_{i}.webp" for i in range(2, 101)]

# Display columns for left and right images
col1, _, col2 = st.columns([1, 0.1, 1])

with col1:
    st.image(image_list[st.session_state.left_index], caption="")
    if st.button("This"):
        # Update Elo ratings
        st.session_state.player_a = elo_most(st.session_state.player_a, st.session_state.player_b, 32, 1)
        st.session_state.player_b = elo_most(st.session_state.player_b, st.session_state.player_a, 32, 0)
        # Keep Left Girl, change Right Girl
        st.session_state.right_index = random.randint(0, len(image_list)-1)

with col2:
    st.image(image_list[st.session_state.right_index], caption="")
    if st.button("That"):
        # Update Elo ratings
        st.session_state.player_a = elo_most(st.session_state.player_a, st.session_state.player_b, 32, 0)
        st.session_state.player_b = elo_most(st.session_state.player_b, st.session_state.player_a, 32, 1)
        # Keep Right Girl, change Left Girl
        st.session_state.left_index = random.randint(0, len(image_list)-1)

display_button = st.button("Display Result")
if display_button:
    st.markdown("### 💯 Current Ratings")
    if st.session_state.player_a > st.session_state.player_b:
        st.image(image_list[st.session_state.left_index])
        st.write("Girl Rating:", round(st.session_state.player_a, 2))
    else:
        st.image(image_list[st.session_state.right_index])
        st.write("Right Girl Rating:", round(st.session_state.player_b, 2))
