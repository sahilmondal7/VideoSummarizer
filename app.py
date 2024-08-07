import requests
import streamlit as st
from streamlit_lottie import st_lottie
from dotenv import load_dotenv

load_dotenv() ##load all the nevironment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """


## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        st.error("Enter a valid URL again with English Transcript")
        return None
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.set_page_config(page_title="Video Summarizer", page_icon="https://cdn-icons-png.flaticon.com/512/3242/3242257.png")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://lottie.host/85ff4ab5-590f-4fce-b819-8b71702b44a8/1ZyJrZvS0x.json")
lottie_coding2=load_lottieurl("https://lottie.host/d476042e-4dfd-4475-bf7c-5224b77fd65b/CclcM6q9DU.json")


with st.container():
    left_column, right_column = st.columns((2,1))

    with left_column:
        st.subheader("Hey, I am Sahil :wave:")

        st.title("Here You Can Get A Summary Of Your YouTube Video")

    with right_column:
        st_lottie(lottie_coding)

with st.container():
    youtube_link = st.text_input("Enter YouTube Video Link Here:")
    if youtube_link:
            video_id = youtube_link.split("=")[1]
            print(video_id)
            st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    if st.button("Click Me To Get The Summary"):
        transcript_text=extract_transcript_details(youtube_link)

        if transcript_text:
            summary=generate_gemini_content(transcript_text,prompt)
            st.markdown("## Here's A Detailed Summary:")
            st.write(summary)

with st.container():
    st_lottie(lottie_coding2)