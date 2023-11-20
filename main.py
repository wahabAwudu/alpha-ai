import tools.pet_names_tool as pt
import tools.youtube_tool as yt
import tools.general_tool as gt
import streamlit as st
import textwrap


st.title("Alpha AI project")
utility = st.sidebar.selectbox(
    label="Select utility",
    options=[
        "General Utility",
        "Pet Names Utility",
        "YouTube Utility",
    ]
)
st.sidebar.divider()

response = ""
if utility == "General Utility":
    st.sidebar.subheader(
        "Ask us anything. Provide a context and then a request for a better output."
    )
    query = st.sidebar.text_area(label="Ask a question", placeholder="What's on your mind?")

    if query:
        response = gt.generate_output(query)["data"]
        
elif utility == "Pet Names Utility":
    st.sidebar.subheader("Give us your pet details and let's suggest some cool names for them!")
    animal_type = st.sidebar.selectbox("What is the type of your pet?", ["cat", "dog", "hamster"])

    animal_color = st.sidebar.text_input(label=f"What is the color of your {animal_type}?", max_chars=20)

    if animal_color:
        response = pt.generate_pet_names(animal_type, animal_color)["data"]

elif utility == "YouTube Utility":
    st.sidebar.subheader("Give us a youtube video url and ask questions about the video.")
    youtube_url = st.sidebar.text_area(
        label="What is the video URL?",
        max_chars=100
    )
    query = st.sidebar.text_area(
        label="Ask me about the video",
        max_chars=150
    )
    
    if youtube_url and query:
        db = yt.get_youtube_transcript(youtube_url)
        response = yt.get_response_from_query(db, query)
        response = textwrap.fill(response, width=80)

if response:
    st.subheader("Answer:")
    st.text(response)
