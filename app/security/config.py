from definable.agent.security import (
    ContentDefenseConfig,
    EnvSanitizeConfig,
    RateLimitConfig,
    SecurityConfig,
    SSRFGuardConfig,
    ToolPolicy,
)


security = SecurityConfig(
    tool_policy=ToolPolicy(mode="allowlist", allowed_tools={"escalate_to_human"}),
    rate_limit=RateLimitConfig(max_requests=10, window_seconds=60),
    content_defense=ContentDefenseConfig(injection_detection=True),
    ssrf_guard=SSRFGuardConfig(enabled=True),
    env_sanitize=EnvSanitizeConfig(),
)
