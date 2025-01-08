import streamlit as st
import random
import json
import os

# File to store leaderboard data
LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    """Load leaderboard data from a file."""
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []  # Return empty list if JSON is invalid
    return []

def save_leaderboard(leaderboard):
    """Save leaderboard data to a file."""
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file)

# Initialize session state to store random number, attempts, and success status
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.success = False
    if "leaderboard" not in st.session_state:
        st.session_state.leaderboard = load_leaderboard()

# Page navigation
page = st.sidebar.selectbox("Select a page", ["Game", "Leaderboard"])

if page == "Game":
    # Game Page
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

    # Reset game button (always available)
    if st.button("Reset Game"):
        st.session_state.random_number = random.randint(1, 100)  # Reset random number
        st.session_state.attempts = 0  # Reset attempts
        st.session_state.success = False
        st.write("Game has been reset. Start guessing again!")

    # Show success message with fireworks effect if guessed correctly
    if st.session_state.success:
        st.balloons()  # Show fireworks/balloons
        st.write(f"Congratulations! You guessed the number {st.session_state.random_number} correctly.")
        st.write(f"It took you {st.session_state.attempts} attempts to guess the correct number.")

        # Add result to leaderboard
        player_name = st.text_input("Enter your name for the leaderboard:")
        if st.button("Submit to Leaderboard") and player_name:
            if "leaderboard" not in st.session_state:
                st.session_state.leaderboard = []
            st.session_state.leaderboard.append({"name": player_name, "attempts": st.session_state.attempts})
            st.session_state.leaderboard = sorted(st.session_state.leaderboard, key=lambda x: x["attempts"])  # Sort by attempts
            save_leaderboard(st.session_state.leaderboard)
            st.write("Leaderboard updated! Reset the game to play again.")

elif page == "Leaderboard":
    # Leaderboard Page
    st.title("Leaderboard")

    # Display leaderboard
    leaderboard = st.session_state.get("leaderboard", [])
    if leaderboard:
        for idx, entry in enumerate(leaderboard, start=1):
            st.write(f"{idx}. {entry['name']} - {entry['attempts']} attempts")
    else:
        st.write("No entries in the leaderboard yet. Play the game to add your name!")
