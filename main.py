import streamlit as st
import random
from datetime import datetime

# Initialize session state to store random number, attempts, and success status
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.success = False

# App Title
st.title("Random Number Guessing Game")

# Instructions
st.write("Guess the random number (between 1 and 100). Enter your guess below!")

# Input box for user guess
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Button to submit guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1  # Increment attempts
    if user_guess == st.session_state.random_number:
        st.session_state.success = True  # Mark success if guessed correctly
    elif user_guess < st.session_state.random_number:
        st.write("Too low! Try again.")
    else:
        st.write("Too high! Try again.")

# Show success message with fireworks effect if guessed correctly
if st.session_state.success:
    st.balloons()  # Show fireworks/balloons
    st.write(f"Congratulations! You guessed the number {st.session_state.random_number} correctly.")
    st.write(f"It took you {st.session_state.attempts} attempts to guess the correct number.")

    # Reset game button
    if st.button("Play Again"):
        st.session_state.random_number = random.randint(1, 100)  # Reset random number
        st.session_state.attempts = 0  # Reset attempts
        st.session_state.success = False
