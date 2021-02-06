import streamlit as st


class Toc:
    """
    Implementation found on https://discuss.streamlit.io/t/table-of-contents-widget/3470/8
    """

    def __init__(self):
        self._items = []
        self._placeholder = None

    def title(self, text):
        self._markdown(text, "h1")

    def header(self, text):
        self._markdown(text, "h2", " " * 2)

    def subheader(self, text):
        self._markdown(text, "h3", " " * 4)

    def placeholder(self, sidebar=True):
        self._placeholder = st.sidebar.empty() if sidebar else st.empty()

    def generate(self):
        if self._placeholder:
            self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)

    def _markdown(self, text, level, space=""):
        key = "".join(filter(str.isalnum, text)).lower()
        tags = {"h1": "bold", "h2": "", "h3": ""}
        st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)

        style = tags[level]

        self._items.append(
            f"{space}* <a style='color: #DB0007; font-weight: {style};' href='#{key}'>{text}</a>"
        )