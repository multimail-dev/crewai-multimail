"""CrewAI tools for MultiMail — email capabilities for CrewAI agents."""

from crewai_multimail.tools import (
    MultiMailToolkit,
    CheckInboxTool,
    ReadEmailTool,
    SendEmailTool,
    ReplyEmailTool,
    SearchContactsTool,
    ListPendingTool,
    DecideEmailTool,
    GetThreadTool,
    TagEmailTool,
)

__version__ = "0.1.0"
__all__ = [
    "MultiMailToolkit",
    "CheckInboxTool",
    "ReadEmailTool",
    "SendEmailTool",
    "ReplyEmailTool",
    "SearchContactsTool",
    "ListPendingTool",
    "DecideEmailTool",
    "GetThreadTool",
    "TagEmailTool",
]
