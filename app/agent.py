from pathlib import Path

from definable.agent import Agent
from definable.agent.tracing import JSONLExporter, Tracing
from definable.memory import Memory, SQLiteStore
from definable.skill import Calculator, DateTime

from app.guardrails import guardrails
from app.security import security
from app.skills import customer_support_reply

KB_DIR = str(Path(__file__).parent / "kb")

agent = Agent(
    name="luumen-support",
    model="gpt-5.4-nano",
    memory=Memory(store=SQLiteStore("./memory.db")),
    thinking=True,
    tracing=Tracing(
        enabled=True,
        exporters=[JSONLExporter("./traces")],
    ),
    skills=[Calculator(), DateTime(), customer_support_reply],
    knowledge=KB_DIR,
    debug=True,
    instructions=(
        "You are a customer support agent for Luumen (luumen.ai), an AI-powered SSH client. "
        "Answer user questions using ONLY the provided knowledge base. "
        "If the answer is not in the knowledge base, say so and offer to escalate. "
        "Be concise, friendly, and accurate."
    ),
    observability=True,
    security=security,
    guardrails=guardrails,
)

