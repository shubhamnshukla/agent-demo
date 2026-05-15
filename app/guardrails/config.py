from definable.agent.guardrail import Guardrails, max_tokens, pii_filter, tool_blocklist

from app.guardrails.custom import no_profanity

guardrails = Guardrails(
    input=[max_tokens(500), no_profanity()],
    output=[pii_filter()],
    tool=[tool_blocklist({"delete_all"})],
)
