# crewai-multimail

CrewAI tools for [MultiMail](https://multimail.dev) — give your CrewAI agents email capabilities with graduated human oversight.

## Installation

```bash
pip install crewai-multimail
```

## Quick Start

```python
from crewai import Agent, Task, Crew
from crewai_multimail import MultiMailToolkit

# Create tools from your API key
toolkit = MultiMailToolkit(api_key="MULTIMAIL_API_KEY")
tools = toolkit.get_tools()

# Create an agent with email capabilities
email_agent = Agent(
    role="Email Assistant",
    goal="Help the user manage their email inbox",
    backstory="You are a helpful email assistant that reads, triages, and drafts replies.",
    tools=tools,
    verbose=True,
)

# Define a task
task = Task(
    description="Check mailbox YOUR_MAILBOX_ID for new emails and summarize them.",
    expected_output="A summary of recent emails with sender, subject, and urgency.",
    agent=email_agent,
)

# Run the crew
crew = Crew(agents=[email_agent], tasks=[task], verbose=True)
result = crew.kickoff()
print(result)
```

## Available Tools

| Tool | Description |
|------|-------------|
| `check_inbox` | List recent emails in a mailbox |
| `read_email` | Read the full content of an email |
| `send_email` | Send an email (held for approval if gated) |
| `reply_email` | Reply to an existing email thread |
| `search_contacts` | Search contacts by name or email |
| `list_pending` | List emails awaiting human approval |
| `decide_email` | Approve or reject a pending email |
| `get_thread` | Get all emails in a conversation |
| `tag_email` | Add key-value tags to an email |

This toolkit complements MultiMail's 38 MCP tools with CrewAI-native wrappers for common email workflows.

## Compliance

MultiMail handles regulatory compliance at the infrastructure layer — no SDK-side code changes needed:

- **EU AI Act Article 50**: Every AI-sent email includes a cryptographically signed `ai_generated` disclosure in the `X-MultiMail-Identity` header
- **US State Laws**: Maine, New York, California, Illinois — AI disclosure built into email delivery
- **CAN-SPAM**: Unsubscribe headers and physical address footers on all outbound email
- **Formally Verified**: Lean 4 proofs of identity header tamper evidence

MultiMail handles EU AI Act Article 50 compliance at the infrastructure layer. Every AI-sent email includes signed `ai_generated` disclosure automatically.

See [multimail.dev/use-cases/eu-ai-act-email-compliance](https://multimail.dev/use-cases/eu-ai-act-email-compliance) for details.

## Oversight Modes

MultiMail supports graduated oversight so your agent doesn't send unsupervised email:

- **`gated_all`** — Agent drafts, human approves everything
- **`gated_send`** — Agent reads freely, human approves outbound *(default)*
- **`monitored`** — Agent sends, human can review after
- **`autonomous`** — Full agent control

When a mailbox uses gated oversight, `send_email` returns `pending_send_approval` and the email waits for human review. The agent can check status with `list_pending`.

## Using Individual Tools

```python
from multimail import MultiMail
from crewai_multimail import CheckInboxTool, SendEmailTool

client = MultiMail("MULTIMAIL_API_KEY")

inbox_tool = CheckInboxTool(client=client)
send_tool = SendEmailTool(client=client)

# Use directly
result = inbox_tool.run(mailbox_id="your_mailbox_id", limit=5)
print(result)
```

## Multi-Agent Crew Example

See [`examples/support_crew.py`](examples/support_crew.py) for a full example with a triage agent and a responder agent working together as a crew.

## Links

- [MultiMail](https://multimail.dev) — Homepage & docs
- [multimail](https://pypi.org/project/multimail/) — Base Python SDK
- [MCP Server](https://www.npmjs.com/package/@multimail/mcp-server) — For Claude, Cursor, and other MCP clients
