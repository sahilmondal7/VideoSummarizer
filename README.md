**YT Video Summarizer**

__Description__

This project provides a Streamlit-based web application that leverages the power of Google's Gemini API to generate concise summaries of YouTube videos. 
By inputting a YouTube video URL, users can quickly obtain key takeaways from the video content.

__Installation__

1. Clone the repository:

   git clone https://github.com/sahilmondal7/VideoSummarizer.git

3. Create a virtual environment

   conda create -p venv python==3.10 -y

   conda activate venv/

5. Install dependencies:

   pip install -r requirements.txt

7. Set up API keys. Create a .env file in the project root and add your Gemini API key:

   GEMINI_API_KEY=your_api_key

__Usage__

1. Run the Streamlit app:

   streamlit run app.py

3. Paste a YouTube video URL into the input field and hit enter.
4. Click the "Click Me To Get The Summary" button.
5. The generated summary will be displayed.

__Dependencies__

1. youtube_transcript_api
2. streamlit
3. streamlit_lottie
4. google-generativeai
5. python-dotenv
6. pathlib

__Notes__

1. Ensure you have a Gemini API key and have enabled the necessary services.
2. The performance of the summarization may vary depending on the video content and the complexity of the language.
3. Consider implementing error handling for API calls and potential exceptions.
