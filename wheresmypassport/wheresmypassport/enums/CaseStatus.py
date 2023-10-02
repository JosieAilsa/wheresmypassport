from enum import Enum

from sqlalchemy import Column


class CaseStatus(Enum):
    INITIAL_REQUEST = "initial request"
    DOCUMENTS_SENT = "documents sent"
    REVIEWING = "reviewing"
    APPROVED = "approved"
    POSTED = "posted"
    COMPLETE = "complete"


current_status = Column(Enum(CaseStatus), nullable=False)
