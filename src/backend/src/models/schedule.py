from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, JSON, Boolean, DateTime, Index

from src.db.base import Base


class Schedule(Base):
    """
    Schedule model for recurring job execution based on cron expressions.
    """
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cron_expression = Column(String, nullable=False)  # Cron expression for schedule timing
    agents_yaml = Column(JSON, nullable=False)  # Store agents configuration
    tasks_yaml = Column(JSON, nullable=False)  # Store tasks configuration
    inputs = Column(JSON, default=dict)  # Additional inputs for the job
    is_active = Column(Boolean, default=True)  # Whether the schedule is active
    planning = Column(Boolean, default=False)  # Whether planning is enabled
    model = Column(String, default="gpt-4o-mini")  # Model to use for planning
    last_run_at = Column(DateTime, nullable=True)  # Last time the schedule was executed
    next_run_at = Column(DateTime, nullable=True)  # Next scheduled run time
    created_at = Column(DateTime, default=datetime.utcnow)  # Use timezone-naive UTC time
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Use timezone-naive UTC time
    
    # Group isolation fields
    group_id = Column(String(100), nullable=True)  # Group isolation
    created_by_email = Column(String(255), nullable=True)

    __table_args__ = (
        Index('ix_schedule_group_id', 'group_id'),
        Index('ix_schedule_created_by_email', 'created_by_email'),
    )
    
    def __init__(self, **kwargs):
        super(Schedule, self).__init__(**kwargs)
        if self.inputs is None:
            self.inputs = {}
        if self.is_active is None:
            self.is_active = True
        if self.planning is None:
            self.planning = False
        if self.model is None:
            self.model = "gpt-4o-mini"
        if self.created_at is None:
            self.created_at = datetime.utcnow()
        if self.updated_at is None:
            self.updated_at = datetime.utcnow() 