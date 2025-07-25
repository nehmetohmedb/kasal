import queue
from datetime import datetime
from typing import Optional
from src.utils.user_context import GroupContext

class JobOutputQueue:
    """Singleton holder for the job output queue."""
    _instance = None
    _queue = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JobOutputQueue, cls).__new__(cls)
            cls._instance._queue = queue.Queue()
        return cls._instance

    def get_queue(self) -> queue.Queue:
        """Get the singleton queue instance."""
        return self._queue

# Function to get the singleton queue instance easily
def get_job_output_queue() -> queue.Queue:
    return JobOutputQueue().get_queue()

def enqueue_log(execution_id: str, content: str, timestamp: Optional[datetime] = None, group_context: GroupContext = None) -> bool:
    """
    Enqueue a log message to be processed by the logs writer.
    
    Args:
        execution_id: ID of the execution (job_id)
        content: Content of the log message
        timestamp: Optional timestamp, defaults to current time
        group_context: Optional group context for logging isolation
        
    Returns:
        bool: True if enqueued successfully, False otherwise
    """
    try:
        # Get the queue
        job_queue = get_job_output_queue()
        
        # Prepare the log data
        log_data = {
            "job_id": execution_id,
            "content": content,
            "timestamp": timestamp or datetime.now()
        }
        
        # Add group context information if available
        if group_context:
            log_data["group_id"] = group_context.primary_group_id
            log_data["group_email"] = group_context.group_email
        
        # Add to queue
        job_queue.put_nowait(log_data)
        return True
    except queue.Full:
        # Queue is full
        return False
    except Exception:
        # Any other error
        return False 