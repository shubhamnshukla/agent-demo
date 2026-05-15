from definable.agent.events import RunContext
from definable.agent.guardrail import GuardrailResult, input_guardrail


def no_profanity(banned_words: set[str] | None = None):
    """Factory for an input guardrail that blocks banned words."""
    words = banned_words or {"badword1", "badword2"}

    @input_guardrail(name="no_profanity")
    async def _guard(text: str, _context: RunContext) -> GuardrailResult:
        lowered = text.lower()
        for word in words:
            if word in lowered:
                return GuardrailResult.block(f"Contains banned word: {word}")
        return GuardrailResult.allow()

    return _guard
