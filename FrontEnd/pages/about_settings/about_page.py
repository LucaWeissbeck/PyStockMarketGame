# PAGE IMPORTS
import pages.side_bar as side_bar
import streamlit as st
import pages.about_settings.helperfunctions as hf


def run(session_state):
    side_bar.run(session_state)
    st.title("Settings")

    st.header("Transaction Fee")
    # Slider for setting the transaction fee (step size = 0.5)
    transaction_fee_current = hf.get_transaction_fees(session_state.auth_key)
    transaction_fee = st.slider("Gebühren:", 1.0, 30.0, step=0.5, value=float(transaction_fee_current))

    if st.button("Apply"):
        hf.post_new_transaction_fees(session_state.auth_key, transaction_fee)
        st.success("The transaction fee has been changed successfully!")
    st.write("---")

    # Set GIF Topic
    st.header("Loading Screen GIF selection")
    gifs = ["AustinPowers", "TheOffice", "Cats", "Dogs", "Cute_Animals"]
    gif_selected = st.selectbox("GIF Topic:", gifs, index=session_state.gif_tag[1])
    session_state.gif_tag = (gif_selected, gifs.index(gif_selected))
    st.write("---")

    # Delete User
    st.header("Delete Profile")
    if st.button("Delete User"):
        st.warning("This action cannot be reversed")
        if st.checkbox("I am sure", value=False):
            hf.delete_user(session_state.auth_key)
            session_state.page = "login"
            st.experimental_rerun()
    st.write("---")

    # Print possible sustainability warnings
    st.title("About")
    hf.write_sustainability_warning()