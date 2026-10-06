# ✈️ AI Travel Planner using CrewAI

An AI-powered travel planner built using **CrewAI** and **Streamlit**.
Enter a city name and the AI agent generates a personalized travel plan with tourist attractions, activities, accommodations, and dining recommendations.

## 🚀 Features

* 🤖 CrewAI-powered AI Travel Agent
* ✈️ Personalized travel recommendations
* 🏛️ Tourist attractions and activities
* 🏨 Accommodation suggestions
* 🍽️ Dining recommendations
* 🎨 Simple Streamlit user interface
* 🔐 Environment variable support for API keys

## 🛠️ Technologies Used

* Python
* CrewAI
* Streamlit
* OpenAI
* python-dotenv

## 📁 Project Structure

```text
crewai-ai-travel-planner/
│
├── 1.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/crewai-ai-travel-planner.git
```

### 2. Navigate to the project

```bash
cd crewai-ai-travel-planner
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Mac/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project directory:

```text
OPENAI_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file or API key to GitHub.

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run 1.py
```

The application will open in your browser.

## 💡 How It Works

```text
User enters city
       ↓
Streamlit UI
       ↓
CrewAI Travel Agent
       ↓
LLM
       ↓
Personalized Travel Plan
       ↓
Streamlit displays the result
```

## 📸 Example

Enter:

```text
Chennai
```

The AI Travel Planner can provide recommendations for:

* Tourist places
* Activities
* Accommodation
* Restaurants
* Nearby attractions

## 🔮 Future Improvements

* 🌐 Real-time web search
* 🗺️ Google Maps integration
* 🏨 Real-time hotel information
* 🍽️ Restaurant recommendations
* 💰 Travel budget planning
* 📅 Multi-day itinerary generation
* 🤖 Multiple CrewAI agents
* 💾 Conversation memory

## 👨‍💻 Author

**Prakash R**

Exploring **Generative AI, Agentic AI, CrewAI, RAG, and Data Engineering**.
