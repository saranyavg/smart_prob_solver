import json
import os
import re
from dotenv import load_dotenv
from models import AgentOutput
from prompt import QUALIFIED_PROMPT
from openai import OpenAI

load_dotenv()

# Modern OpenAI client initialization 
# OpenRouter requires the base_url to route requests properly
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def run_agent(user_input: str):
    full_prompt = QUALIFIED_PROMPT + user_input

    # Updated to the modern client.chat.completions.create syntax
    response = client.chat.completions.create(
        model="google/gemini-2.5-flash",
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0.2,
        max_tokens=1000
    )

    raw_output = response.choices[0].message.content

    try:
        # Clean up markdown code blocks if the model includes them
        cleaned_output = re.sub(r"^```json\s*|\s*```$", "", raw_output.strip(), flags=re.MULTILINE)
        
        parsed = json.loads(cleaned_output)
        validated = AgentOutput(**parsed)
        return validated
    except Exception as e:
        return {"error": f"Invalid response format: {str(e)}", "raw": raw_output}