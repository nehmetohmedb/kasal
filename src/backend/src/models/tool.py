from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, JSON, DateTime

from src.db.base import Base


class Tool(Base):
    """
    SQLAlchemy model for tools.
    Enhanced with group isolation for multi-group deployments.
    """
    
    __tablename__ = "tools"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    config = Column(JSON, default=dict)
    enabled = Column(Boolean, default=True)
    
    # Multi-group fields
    group_id = Column(String(100), index=True, nullable=True)  # Group isolation
    created_by_email = Column(String(255), nullable=True)  # Creator email for audit
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, **kwargs):
        super(Tool, self).__init__(**kwargs)
        if self.config is None:
            self.config = {}
        if self.enabled is None:
            self.enabled = True
        if self.created_at is None:
            self.created_at = datetime.utcnow()
        if self.updated_at is None:
            self.updated_at = datetime.utcnow() 