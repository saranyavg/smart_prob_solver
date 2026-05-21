# 🧠 Smart Problem Solver Agent

A lightweight AI-powered agent that uses a **Reasoning → Action → Result (ReAct)** workflow to solve user queries intelligently.  
Instead of directly answering like a chatbot, the agent reasons through problems, selects tools, and iterates to reach accurate results.

---

## 📺 Project Demo

> YouTube demo link
> https://youtu.be/AIbcn4LJzNw

---

## 🚀 Key Features

- Agentic workflow: **THOUGHT → ACTION → RESULT**
- Dynamic tool selection based on user query
- Transparent reasoning steps
- Modular and extensible design
- Lightweight browser-based UI

---

## ⚠️ Limitations

- Uses mock/static data
- No persistent memory (refresh clears state)
- No real external integrations yet

---

## 🚀 Future Improvements

- Add real API integrations
- Implement memory (chat history)
- Improve UI/UX
- Add more tools and capabilities

---

## 📁 Project Structure

```text
smart_prob_solver/
│
├── agent.py          # Core logic, OpenRouter client configuration, and string cleaning
├── models.py         # Pydantic schema enforcing the exact JSON response structure
├── prompt.py         # The qualified prompt injected with role and structural constraints
├── main.py           # CLI interface for user interaction
├── requirements.txt  # Project dependencies
└── .env              # Local environment variables (API keys)
```

---

## ⚙️ Installation & Setup

1. Download or clone the repository

2. Open `.env`

3. Add your API key:
```
const API_KEY = "your_api_key_here";
```

4. Run the project:
```command
python main.py
```

---

## ▶️ How It Works

1. User inputs a query  
2. Agent generates a **THOUGHT**  
3. Chooses an **ACTION (tool)**  
4. Executes and gets a **RESULT**  
5. Repeats until final answer  

---

## 💬 Example Queries

- A software team has a 4-day sprint to deploy a feature. Design takes 1 day. Development takes 2 days but cannot start until Design is complete. Testing takes 1 day and must happen after Development. If the team starts on Monday morning, on what day will the feature be fully tested? Is it possible to finish within the 4-day sprint?
    - Sample output: The final_answer should clearly state "Thursday" and confirm "Yes, it fits exactly in 4 days.
- A retail store buys a jacket wholesale for $50. They mark up the price by 80% for the retail shelf. After a month of no sales, they offer a 20% discount on the retail price. Finally, a customer buys it and has to pay an additional 8% sales tax on the discounted price. What is the final amount the customer paid, and did the store still make a profit compared to the wholesale cost?
    - The final_answer should be $77.76, explicitly noting that the store made a profit of $27.76.

---

## 🧠 Why This is an Agent

- Performs reasoning before responding  
- Uses tools dynamically  
- Iterates based on results  

This makes it an **agentic AI system**, not just a chatbot.

---

## 📌 Notes

- Runs entirely in the browser
- No backend required
- Easy to extend and customize
