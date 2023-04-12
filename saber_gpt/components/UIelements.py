import streamlit as st
from saber_gpt.components import config

import streamlit as st

class CycleTextInput:
    def __init__(self, label, options):
        self.label = label
        self.options = options
        self.option_index = st.session_state.get(f'{self.label}_option_index', 0)
        self.preamble = ""

    def render(self):
        # Render the left and right arrow buttons
        col1, col3, col2 = st.columns(3)
        if col1.button('←'):
            self.option_index = (self.option_index - 1) % len(self.options)
        if col3.button('→'):
            self.option_index = (self.option_index + 1) % len(self.options)

        # Get the current option string
        current_option = self.options[self.option_index]

        # Add a text input with the current option
        self.preamble = st.text_area(self.label, current_option)

        # Save the current option index to session state
        st.session_state[f'{self.label}_option_index'] = self.option_index