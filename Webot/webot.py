##  Streamlit-based ========================================================================
##  please comment out this code before running and comment the code of Python-based console which is below this code 


# import openai
# import requests
# from bs4 import BeautifulSoup
# import streamlit as st
# from dotenv import load_dotenv
# import os


# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")  #create a .env fie and put there OPENAI_API_KEY from openaiapi

# # Function to scrape website content
# def scrape_website(url):
#     try:
#         response = requests.get(url, timeout=10)  
#         response.raise_for_status()  
#         soup = BeautifulSoup(response.content, "html.parser")
#         paragraphs = soup.find_all('p')
#         text = "\n".join([para.get_text(strip=True) for para in paragraphs if para.get_text(strip=True)])
#         return text
#     except requests.exceptions.RequestException as e:
#         return f"Failed to fetch the website: {e}"
#     except Exception as e:
#         return f"An error occurred: {e}"
# #function for response
# def get_response_from_openai(website_content, user_input):
#     messages = [
#         {"role": "system", "content": "You are a helpful assistant that answers questions based on website content."},
#         {"role": "user", "content": f"Website content:\n{website_content}\n\nQuestion: {user_input}"}
#     ]
    
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",  # you can use gpt-4,4 ....any
#             messages=messages,
#             max_tokens=150,
#             temperature=0.7
#         )
#         return response.choices[0].message['content'].strip()
#     except Exception as e:
#         return f"Error generating response from OpenAI: {e}"

# # Streamlit for interface
# st.title("Website-based Chatbot")
# #input for website url
# url = st.text_input("Enter the website URL:", "")

# if url:
#     website_content = scrape_website(url)
#     if website_content.startswith("Failed") or website_content.startswith("An error"):
#         st.error(website_content)
#     elif website_content.strip() == "":
#         st.warning("No content found on the website.")
#     else:
#         st.success("Website content scraped successfully!")

#         # Input for quary
#         user_input = st.text_input("Ask a question related to the website:", "")

#         if user_input:
#             with st.spinner("Generating response..."):
#                 response = get_response_from_openai(website_content, user_input)
#                 st.write(f"**Chatbot Response:** {response}")




# This code is Python-based console =========================================================================================================


import openai
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Load API key in .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  

# Function for scrape website content
def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all('p')
        text = "\n".join([para.get_text(strip=True) for para in paragraphs if para.get_text(strip=True)])
        return text
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch the website: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

# Function for get response 
def get_response_from_openai(website_content, user_input):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that answers questions based on website content."},
        {"role": "user", "content": f"Website content:\n{website_content}\n\nQuestion: {user_input}"}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", #use anyb model of openai
            messages=messages,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error generating response from OpenAI: {e}"

# Main function for console-based chatbot
def main():
    print("===** Website-based Chatbot **===")
    url = input("Enter the website URL: ").strip()
    
    website_content = scrape_website(url)
    if website_content.startswith("Failed") or website_content.startswith("An error"):
        print(website_content)
        return
    
    if not website_content.strip():
        print("No content found on the website.")
        return

    print("Website content scraped successfully!")
    
    while True:
        user_input = input("\nAsk a question related to the website (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = get_response_from_openai(website_content, user_input)
        print(f"Chatbot Response: {response}")

if __name__ == "__main__":
    main()





