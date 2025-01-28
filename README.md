# websiet_scrabber_bot
This is a webot which can scarab the knowledge from given website and give response according to that  
Website-based webot using OpenAI
This is a Streamlit-based and Python-based console webot application that interacts with users by answering their questions based on the content of a specified website. The webot uses OpenAI's GPT model to generate responses.

Features
Scrape content from any website.
Use OpenAI GPT model to answer user queries based on the scraped content.
User-friendly interface built with Streamlit.
Error handling for invalid URLs or failed website scraping.
Prerequisites
Python 3.8 or higher installed on your system.
OpenAI API key (you can get one from OpenAI).
Internet connection to access the website and call the ChatGPT API.
Create a virtual environment (optional):
bash python -m venv venv source venv/bin/activate # On Windows, use venv\Scripts\activate

Install the dependencies:
bash pip install -r requirements.txt

Create a .env file in the project directory and add your OpenAI API key:
 OPENAI_API_KEY=your_openai_api_key
Usage For Python-based console
1. Run the script:
python webbot.py
2. Enter a website URL when prompted. For example:
plaintext Enter the website URL: https://example.com

3. Ask questions based on the website's content. Example:
plaintext Ask a question related to the website (or type 'exit' to quit): What is this website about?

4. To exit the webot, type exit.
Example Interaction
plaintext ===** Website-based webot **=== Enter the website URL: https://example.com Website content scraped successfully!

Ask a question related to the website (or type 'exit' to quit): What is the main focus of the website? webot Response: .............................

Ask a question related to the website (or type 'exit' to quit): exit Goodbye!

Usage For Python-based console
1. Run the script:
streamlit run webbot.py You can now view your Streamlit app in your browser. Local URL: http://localhost:8501 Network URL: http://:8501

Website-based Chatbot Enter the website URL: https://example.com

Website content scraped successfully!

Ask a question related to the website: What is the main focus of the website? webot Response: .............................
