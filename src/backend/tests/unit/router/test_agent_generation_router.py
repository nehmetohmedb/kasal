"""
Unit tests for agent generation API router.

Tests the functionality of the agent generation API endpoints.
"""
import json
from unittest.mock import AsyncMock, MagicMock, patch
from src.dependencies.admin_auth import (
    require_authenticated_user, get_authenticated_user, get_admin_user
)

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.api.agent_generation_router import router, AgentPrompt
from src.services.agent_generation_service import AgentGenerationService


@pytest.fixture
def app():
    """Create a FastAPI app for testing."""
    app = FastAPI()
    app.include_router(router)
    return app



@pytest.fixture
def mock_current_user():
    """Create a mock authenticated user."""
    from src.models.enums import UserRole, UserStatus
    from datetime import datetime
    
    class MockUser:
        def __init__(self):
            self.id = "current-user-123"
            self.username = "testuser"
            self.email = "test@example.com"
            self.role = UserRole.REGULAR
            self.status = UserStatus.ACTIVE
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
    
    return MockUser()


@pytest.fixture
def client(app):
    """Create a test client for the app."""
    # Override authentication dependencies for testing
    app.dependency_overrides[require_authenticated_user] = lambda: mock_current_user
    app.dependency_overrides[get_authenticated_user] = lambda: mock_current_user
    app.dependency_overrides[get_admin_user] = lambda: mock_current_user


    return TestClient(app)


@pytest.fixture
def mock_agent_generation_service():
    """Create a mock agent generation service."""
    service_mock = MagicMock(spec=AgentGenerationService)
    # Configure the async methods
    service_mock.generate_agent = AsyncMock()
    return service_mock


@pytest.mark.asyncio
async def test_generate_agent_success(client, mock_agent_generation_service):
    """Test successful agent generation."""
    # Configure the mock service to return a valid agent config
    mock_agent_config = {
        "name": "Research Agent",
        "role": "Research Assistant",
        "goal": "Find relevant information from the web",
        "backstory": "I am Kasal specialized in research",
        "tools": ["web_search", "document_analyzer"],
        "advanced_config": {
            "llm": "gpt-4o-mini",
            "max_iter": 25
        }
    }
    mock_agent_generation_service.generate_agent.return_value = mock_agent_config
    
    # Configure the create mock to return our service mock
    with patch.object(
        AgentGenerationService, 
        "create", 
        return_value=mock_agent_generation_service
    ):
        # Make the request
        response = client.post(
            "/agent-generation/generate",
            json={
                "prompt": "Create a research agent that can search the web",
                "model": "gpt-4o-mini",
                "tools": ["web_search", "document_analyzer"]
            }
        )
        
        # Assert response
        assert response.status_code == 200
        
        # Validate response content
        result = response.json()
        assert result == mock_agent_config
        
        # Verify service method was called with correct parameters
        # Note: The actual call includes group_context parameter
        call_args = mock_agent_generation_service.generate_agent.call_args
        assert call_args is not None
        assert call_args.kwargs['prompt_text'] == "Create a research agent that can search the web"
        assert call_args.kwargs['model'] == "gpt-4o-mini"
        assert call_args.kwargs['tools'] == ["web_search", "document_analyzer"]


@pytest.mark.asyncio
async def test_generate_agent_with_default_model(client, mock_agent_generation_service):
    """Test agent generation with default model parameter."""
    mock_agent_config = {
        "name": "Simple Agent",
        "role": "Assistant",
        "goal": "Help the user",
        "backstory": "I'm a helpful assistant",
        "tools": [],
        "advanced_config": {
            "llm": "databricks-llama-4-maverick"
        }
    }
    mock_agent_generation_service.generate_agent.return_value = mock_agent_config
    
    with patch.object(
        AgentGenerationService, 
        "create", 
        return_value=mock_agent_generation_service
    ):
        # Make a request with only prompt, use default model
        response = client.post(
            "/agent-generation/generate",
            json={
                "prompt": "Create a simple agent"
            }
        )
        
        # Assert response
        assert response.status_code == 200
        
        # Validate service call - should use default model
        # Note: The actual call includes group_context parameter
        assert mock_agent_generation_service.generate_agent.called
        call_args = mock_agent_generation_service.generate_agent.call_args
        assert call_args[1]['prompt_text'] == "Create a simple agent"
        assert call_args[1]['model'] == "databricks-llama-4-maverick"  # Default model
        assert call_args[1]['tools'] == []
        assert 'group_context' in call_args[1]


@pytest.mark.asyncio
async def test_generate_agent_validation_error(client, mock_agent_generation_service):
    """Test agent generation with validation error."""
    # Configure mock to raise ValueError
    mock_agent_generation_service.generate_agent.side_effect = ValueError("Invalid prompt")
    
    with patch.object(
        AgentGenerationService, 
        "create", 
        return_value=mock_agent_generation_service
    ):
        # Make the request
        response = client.post(
            "/agent-generation/generate",
            json={
                "prompt": "Invalid prompt",
                "model": "gpt-4o-mini"
            }
        )
        
        # Assert response code and detail
        assert response.status_code == 400
        assert response.json()["detail"] == "Invalid prompt"


@pytest.mark.asyncio
async def test_generate_agent_general_error(client, mock_agent_generation_service):
    """Test agent generation with general error."""
    # Configure mock to raise general exception
    mock_agent_generation_service.generate_agent.side_effect = Exception("Service unavailable")
    
    with patch.object(
        AgentGenerationService, 
        "create", 
        return_value=mock_agent_generation_service
    ):
        # Make the request
        response = client.post(
            "/agent-generation/generate",
            json={
                "prompt": "Generate agent",
                "model": "gpt-4o-mini"
            }
        )
        
        # Assert response code and detail
        assert response.status_code == 500
        assert response.json()["detail"] == "Failed to generate agent configuration" 