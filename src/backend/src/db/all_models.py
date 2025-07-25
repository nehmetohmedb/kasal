"""
Collection of all database models for easy import.
"""

# Import base for direct access
from src.db.base import Base

# Import all models to register them with SQLAlchemy
from src.models.agent import Agent
from src.models.task import Task
from src.models.execution_history import ExecutionHistory, TaskStatus, ErrorTrace
from src.models.tool import Tool
from src.models.log import LLMLog
from src.models.model_config import ModelConfig
from src.models.databricks_config import DatabricksConfig
from src.models.initialization_status import InitializationStatus
from src.models.template import PromptTemplate
from src.models.execution_trace import ExecutionTrace
from src.models.crew import Crew, Plan
from src.models.flow import Flow
from src.models.flow_execution import FlowExecution, FlowNodeExecution
from src.models.schedule import Schedule
from src.models.api_key import ApiKey
from src.models.schema import Schema
from src.models.execution_logs import ExecutionLog
from src.models.engine_config import EngineConfig
from src.models.mcp_server import MCPServer
from src.models.mcp_settings import MCPSettings
# Multi-group models (formerly multi-tenant)
from src.models.group import Group, GroupUser
from src.models.chat_history import ChatHistory

# User and RBAC models
from src.models.user import User, UserProfile, RefreshToken, ExternalIdentity, Role, Privilege, RolePrivilege, UserRole, IdentityProvider

# Billing models
from src.models.billing import LLMUsageBilling, BillingPeriod, BillingAlert

# Documentation models
from src.models.documentation_embedding import DocumentationEmbedding

# Add additional models here as your application grows
# from src.models.order import Order

# This ensures all models are registered with SQLAlchemy metadata
__all__ = [
    "Base",
    "Agent",
    "Task",
    "ExecutionHistory", 
    "TaskStatus", 
    "ErrorTrace",
    "Tool",
    "LLMLog",
    "ModelConfig",
    "DatabricksConfig",
    "InitializationStatus",
    "PromptTemplate",
    "ExecutionTrace",
    "Crew", 
    "Plan",
    "Flow",
    "FlowExecution", 
    "FlowNodeExecution",
    "Schedule",
    "ApiKey",
    "Schema",
    "ExecutionLog",
    "EngineConfig",
    "MCPServer",
    "MCPSettings",
    # Multi-group models
    "Group",
    "GroupUser",
    "ChatHistory",
    # User and RBAC models
    "User",
    "UserProfile", 
    "RefreshToken",
    "ExternalIdentity",
    "Role",
    "Privilege",
    "RolePrivilege",
    "UserRole",
    "IdentityProvider",
    # Billing models
    "LLMUsageBilling",
    "BillingPeriod", 
    "BillingAlert",
    # Documentation models
    "DocumentationEmbedding"
] 