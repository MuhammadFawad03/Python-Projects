import streamlit as st

st.set_page_config(
    page_title="Cricket Score Predictor",
    page_icon="🏏"
)

st.title("🏏 Cricket Score Predictor")
st.write("Predict the final score of a cricket innings.")

team = st.text_input("Enter Team Name")

current_score = st.number_input(
    "Current Score",
    min_value=0,
    max_value=500,
    value=100
)

overs = st.number_input(
    "Overs Completed",
    min_value=0.0,
    max_value=20.0,
    value=10.0
)

wickets = st.slider(
    "Wickets Lost",
    0,
    10,
    2
)

if st.button("Predict Final Score"):
    if overs > 0:
        run_rate = current_score / overs
        predicted = int(current_score + run_rate * (20 - overs))

        if wickets >= 7:
            predicted -= 20

        st.success(
            f"{team}'s predicted final score: {predicted}"
        )
    else:
        st.error("Overs must be greater than zero.")