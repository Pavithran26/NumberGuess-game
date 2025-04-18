import streamlit as st
import random
background_url = "https://thumbs.dreamstime.com/z/vector-background-numbers-rainbow-colored-copyspace-38771719.jpg"

def add_bg_and_custom_info_style():
    st.markdown(
        f"""
        <style>
        /* Background image for the whole app */
        .stApp {{
            background-image: url("{background_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

       
        </style>
        """,
        unsafe_allow_html=True
    )

def start_new_game():
    st.session_state['target'] = random.randint(1, 100)
    st.session_state['tries'] = 0
    st.session_state['game_finished'] = False
    st.session_state['history'] = []

def main():
    add_bg_and_custom_info_style()

    st.title("🎯 Custom Number Guessing Game")
    st.write("Guess the secret number between 1 and 100!")

    if 'target' not in st.session_state:
        start_new_game()

    user_guess = st.number_input("Your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess") and not st.session_state['game_finished']:
        st.session_state['tries'] += 1
        st.session_state['history'].append(user_guess)
        if user_guess < st.session_state['target']:
            st.info("Try higher! ⬆️")
        elif user_guess > st.session_state['target']:
            st.info("Try lower! ⬇️")
        else:
            st.success(f"🎊 You got it in {st.session_state['tries']} tries!🎊")
            st.session_state['game_finished'] = True

    if st.session_state['history']:
        st.write("Your guesses so far:", st.session_state['history'])

    if st.button("®️Restart Game"):
        start_new_game()
        st.rerun()

if __name__ == "__main__":
    main()