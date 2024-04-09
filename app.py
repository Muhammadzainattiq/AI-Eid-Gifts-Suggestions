import openai
import streamlit as st
import os
openai.api_key = st.secrets["OPENAI_API_KEY"]
import json


created_style = """
    color: #888888; /* Light gray color */
    font-size: 99px; /* Increased font size */
"""
header_style = """
    text-align: center;
    color: white;
    background-color: #008000;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 30px;
"""


@st.cache_data(show_spinner=False)
def generate_response(budget, age, gender, relation, personality_type, hobbies, profession,):
    system_content = '''
You are a Eid-ul-Fitr personalized Gift Suggestions assistant. You will help me decide gifts which I can give to someone dear to me. I will give you my budget in Pkr and also the age, gender, my relation with him/her, his/her personality type, his/her hobbies and his/her profession and his/her some additonal information to which I want to give a gift and you will suggest me a personalized gift according to the mentioned things about the person.
and you have to keep in mind my budget and all the details about the person  age, gender, personality type, hobbies and profession then give me five gift suggestions in the form of a list.
         '''
    user_content = {f"My budget is : \"{budget}\", His/her age is \"{age}\" the gender is \"{gender}\". He/She is my \"{relation}\" his/her personality_type is \"{personality_type}\" his  hobbies are \"{hobbies}\" and his profession is \"{profession}\"."}
    user_content = str(user_content)
    messages = [
        {'role': 'system', 'content': system_content},
        {'role': 'user', 'content': user_content}
    ]
    response = openai.chat.completions.create(model='gpt-3.5-turbo-0125', messages=messages, temperature=0.9)
    return response

def main():
    st.set_page_config(page_title="Eid Gift Suggestions LLM", page_icon="🌙")
    st.markdown("<p style='{}'>➡️created by 'Muhammad Zain Attiq'</p>".format(created_style), unsafe_allow_html=True)
    st.markdown(f"<h1 style='{header_style}'>🎉Eid Gift🎁 Suggestions LLM</h1>", unsafe_allow_html=True)
    with st.expander("About the app:"):
        st.markdown("**What can this app do?**")
        st.info("This app is designed to provide personalized Eid gift suggestions based on the recipient's budget, age, gender, relationship, personality type, hobbies, and profession.")
        st.markdown("**How to use the app?**")
        st.warning('''To use the app:
                    1. Adjust the slider to select your budget in PKR.
                    2. Enter the recipient's age.
                    3. Choose the recipient's gender, relationship, personality type, hobbies, and profession from the dropdown menus.
                    4. Click the 'Get AI Suggestions' button to receive personalized gift suggestions based on the provided information.''')

    # Check if response is already stored in session state
    budget = st.slider("Select your budget in Pkr", min_value=100, max_value=100000,step =100)
    age = st.number_input("Enter his/her age:", min_value=1, max_value=120)
    gender = st.selectbox("Enter his/her gender:", ["Male", "Female"])
    relation = st.selectbox("Enter his/her relation:", ["Friend",
    "Father",
    "Mother",
    "Grandfather",
    "Grandmother",
    "Son",
    "Daughter",
    "Sister",
    "Brother",
    "Cousin",
    "Husband",
    "Wife",
    "Uncle",
    "Aunt",
    "Nephew",
    "Niece",
    "Grandson",
    "Granddaughter",
    "In-Laws",
    "Godfather",
    "Godmother",
    "Stepfather",
    "Stepmother",
    "Stepson",
    "Stepdaughter",
    "Stepbrother",
    "Stepsister",
    "Foster Parent",
    "Foster Child",
    "Guardian"
])
    personality_type = st.selectbox("Enter his/her personality type:", ["The Outgoing One",
    "The Outgoing One (The Life of the Party)",
    "The Quiet Observer (The Wallflower)",
    "The Leader (The Boss)",
    "The Helper (The Caregiver)",
    "The Thinker (The Brainiac)",
    "The Creative (The Artist)",
    "The Organized One (The Neat Freak)",
    "The Easygoing One (The Go-with-the-Flow)",
    "The Grumpy One (The Debbie Downer)",
    "The Funny One (The Comedian)"])
    hobbies = st.multiselect("Enter his/her hobbies:", [
    "Reading",
    "Cooking",
    "Gardening",
    "Painting/Drawing",
    "Photography",
    "Writing",
    "Traveling",
    "Hiking",
    "Playing musical instruments",
    "Crafting",
    "Fishing",
    "Playing sports",
    "Collecting",
    "Yoga",
    "Gaming",
    "Birdwatching",
    "Dancing",
    "Watching movies/TV shows",
    "Volunteering",
    "DIY projects/Home improvement",
    "Knitting/Crochet",
    "Running",
    "Cycling",
    "Meditation",
    "Swimming",
    "Surfing",
    "Climbing",
    "Horseback riding",
    "Sailing"])
    profession = st.selectbox("Enter his/her profession:", ["Doctor",
    "Engineer",
    "Teacher",
    "House Wife",
    "Nurse",
    "Software Developer",
    "Accountant",
    "Lawyer",
    "Manager",
    "Salesperson",
    "Marketing Specialist",
    "Architect",
    "Scientist",
    "Financial Analyst",
    "Consultant",
    "Pharmacist",
    "Psychologist",
    "Dentist",
    "Chef",
    "Police Officer",
    "Artist",
    "Musician",
    "Writer",
    "Graphic Designer",
    "Entrepreneur",
    "Economist",
    "Social Worker",
    "Pilot",
    "Veterinarian",
    "Electrician",
    "Construction Worker"])
    submit = st.button("Get AI Suggestions")
    if submit:
        if budget and age and gender and relation and personality_type and hobbies and profession: 
            response = generate_response(budget, age, gender, relation, personality_type, hobbies, profession)
            response = response.choices[0].message.content
            st.write(response)
        else:
            st.error("You have missed some input field.")
if __name__ == "__main__":
    try:
        main()  
    except Exception as e:
        st.error(f"An error occurred: {e}")
