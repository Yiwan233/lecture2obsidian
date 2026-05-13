from typing import TypedDict, Optional


class MathAgentState(TypedDict):
    query: str
    item_type: str
    document_name: str
    chapter: str
    current_doc_topics: list[str]
    global_vault_topics: list[str]
    retrieved_contexts: list[str]
    draft_note: str
    iteration: int
    feedback: Optional[str]
