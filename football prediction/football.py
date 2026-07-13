import streamlit as st
import random

# Page settings
st.set_page_config(
    page_title="Football Match Predictor",
    page_icon="⚽",
    layout="centered"
)

# Title
st.title("⚽ Football Match Predictor")
st.write("Predict the winner of a football match!")

# Teams
teams = [
   "Spain",
   "Argentina",
   "moroco",
   "England",
   "suizerland",
   "france",
   "Norway",
   "Bejium",
   "Pakistan",
   "srilanka",
   "india",
   "Afghinsitan",
   "australia"


]

# Select teams
team1 = st.selectbox("Select Team 1", teams)
team2 = st.selectbox("Select Team 2", teams, index=1)

# Predict button
if st.button("Predict Match"):

    if team1 == team2:
        st.error("Please select two different teams.")
    else:
        score1 = random.randint(0, 5)
        score2 = random.randint(0, 5)

        st.subheader("🏟 Match Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(team1, score1)

        with col2:
            st.write("VS")

        with col3:
            st.metric(team2, score2)

        if score1 > score2:
            st.success(f"🏆 Winner: {team1}")
        elif score2 > score1:
            st.success(f"🏆 Winner: {team2}")
        else:
            st.warning("🤝 Match Draw")

# Footer
st.write("---")
st.caption("Created with ❤️ Muhammad Fawad ")