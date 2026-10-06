
import streamlit as st
import time

from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# --------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="centered"
)


# --------------------------------------------------
# Application UI
# --------------------------------------------------

st.title("✈️ AI Travel Planner")

st.write(
    "Enter a city below to get a personalized travel itinerary "
    "with top attractions, activities, stays, and dining options."
)


# --------------------------------------------------
# User Input
# --------------------------------------------------

city = st.text_input(
    "Which city do you want to explore?",
    placeholder="e.g. Kyoto, Paris, Cape Town"
)


# --------------------------------------------------
# Generate Travel Plan
# --------------------------------------------------

if st.button("Generate Travel Plan", type="primary"):

    if not city.strip():

        st.warning("Please enter a city name first.")

    else:

        try:

            # ------------------------------------------
            # Step 1: Create LLM
            # ------------------------------------------

            llm = LLM("gpt-4o-mini")


            # ------------------------------------------
            # Step 2: Create Travel Agent
            # ------------------------------------------

            travel_agent = Agent(

                role="Travel Planner",

                goal=(
                    "Help users discover famous tourist places in and around "
                    "the city they provide and give useful travel recommendations."
                ),

                backstory=(
                    "You are an experienced travel planner with good knowledge "
                    "of tourist destinations, attractions, hill stations, "
                    "historical places, temples, waterfalls, and scenic locations. "
                    "You help travelers discover interesting places based on "
                    "their chosen city. You provide clear, practical, and "
                    "easy-to-understand travel recommendations and avoid "
                    "making up information."
                ),

                llm=llm,

                verbose=False
            )


            # ------------------------------------------
            # Step 3: Create Task
            # ------------------------------------------

            travel_task = Task(

                description=(
                    "Create a personalized travel plan for a trip to {city}. "

                    "Include famous tourist places, activities, "
                    "accommodations, and dining options. "

                    "Explain briefly why each recommendation "
                    "is worth considering."
                ),

                expected_output=(
                    "A detailed travel plan for {city} containing "
                    "recommended tourist places, activities, "
                    "accommodations, and dining options."
                ),

                agent=travel_agent
            )


            # ------------------------------------------
            # Step 4: Create Crew
            # ------------------------------------------

            crew = Crew(

                agents=[travel_agent],

                tasks=[travel_task],

                verbose=False
            )


            # ------------------------------------------
            # Step 5: Run CrewAI
            # ------------------------------------------

            with st.spinner(f"AI is planning your trip to {city}..."):

                result = crew.kickoff(
                    inputs={"city": city}
                )


            # ------------------------------------------
            # Step 6: Get Final Answer
            # ------------------------------------------

            answer = result.raw


            # ------------------------------------------
            # Step 7: Live Line-by-Line Display
            # ------------------------------------------

            st.success(f"Travel Plan for {city}:")

            output_placeholder = st.empty()

            lines = answer.split("\n")

            displayed_text = ""

            for line in lines:

                displayed_text += line + "\n"

                output_placeholder.markdown(displayed_text)

                time.sleep(0.08)


        except Exception as e:

            st.error(
                f"An error occurred while generating the plan: {str(e)}"
            )
