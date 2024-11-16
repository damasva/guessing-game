import streamlit as st
import random

st.title("Number Guessing Game")

# Initialize session state variables
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.feedback = ""

# Display instructions
st.write("I'm thinking of a number between 1 and 100. Try to guess it!")

# User input
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Submit button
if st.button("Submit guess"):
    st.session_state.attempts += 1
    if user_guess < st.session_state.target:
        st.session_state.feedback = "Your guess is too low! Try a higher number."
    elif user_guess > st.session_state.target:
        st.session_state.feedback = "Your guess is too high! Try a lower number."
    else:
        st.session_state.feedback = (
            f"Correct! You guessed the number in {st.session_state.attempts} attempts."
        )
        st.balloons()
        # Reset the game
        st.session_state.target = random.randint(1, 100)
        st.session_state.attempts = 0

# Display feedback
st.write(st.session_state.feedback)
