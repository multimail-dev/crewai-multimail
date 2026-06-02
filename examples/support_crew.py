"""Example: Customer support crew that reads and responds to emails using MultiMail."""

from crewai import Agent, Task, Crew
from crewai_multimail import MultiMailToolkit

MAILBOX_ID = "YOUR_MAILBOX_ID"

# Create MultiMail tools
toolkit = MultiMailToolkit(api_key="MULTIMAIL_API_KEY")
tools = toolkit.get_tools()

# Define agents
triage_agent = Agent(
    role="Email Triage Specialist",
    goal="Check the inbox, read new emails, and categorize them by urgency and topic",
    backstory=(
        "You are a meticulous email triage specialist at Acme Corp. "
        "You read every incoming email, assess its urgency, and tag it "
        "with the appropriate category so the response team can prioritize."
    ),
    tools=tools,
    verbose=True,
)

responder_agent = Agent(
    role="Customer Support Responder",
    goal="Draft helpful, professional replies to customer emails",
    backstory=(
        "You are a friendly and knowledgeable support agent at Acme Corp. "
        "You write clear, concise replies that solve the customer's problem. "
        "The mailbox uses gated_send mode, so a human will review your "
        "replies before they are actually sent."
    ),
    tools=tools,
    verbose=True,
)

# Define tasks
triage_task = Task(
    description=(
        f"Check mailbox {MAILBOX_ID} for new inbound emails. "
        "Read each one and tag it with a category "
        "(support, billing, feature-request, or bug) and a priority (high, medium, low). "
        "Return a summary of what you found."
    ),
    expected_output="A list of new emails with their categories and priorities",
    agent=triage_agent,
)

respond_task = Task(
    description=(
        f"Using the triage summary, reply to each email in mailbox {MAILBOX_ID} "
        "that needs a response. Be concise and helpful. "
        "If you're unsure about something, say so rather than guessing."
    ),
    expected_output="Confirmation that replies have been drafted for all emails needing a response",
    agent=responder_agent,
    context=[triage_task],
)

# Assemble and run the crew
crew = Crew(
    agents=[triage_agent, responder_agent],
    tasks=[triage_task, respond_task],
    verbose=True,
)

result = crew.kickoff()
print(result)
