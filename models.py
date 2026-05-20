from pydantic import BaseModel
from typing import List, Union

class Step(BaseModel):
    step: str
    explanation: str
    result: Union[str, float, int]

class AgentOutput(BaseModel):
    problem_type: str
    steps: List[Step]
    final_answer: str
    confidence: float
