"""Resource Allocator - Dynamic Agent Scaling"""

from typing import Dict, List
import psutil
import logging

logger = logging.getLogger(__name__)

class ResourceAllocator:
    """Allocate system resources to agents"""
    
    def __init__(self):
        self.agent_resources = {}
        self.total_cpu = psutil.cpu_count()
        self.total_memory = psutil.virtual_memory().total
    
    def allocate(self, agent_name: str, cpu_cores: int, memory_gb: float) -> Dict:
        """Allocate resources to agent"""
        
        allocation = {
            'agent': agent_name,
            'cpu_cores': cpu_cores,
            'memory_gb': memory_gb,
            'status': 'allocated'
        }
        
        self.agent_resources[agent_name] = allocation
        
        logger.info(f"Resources allocated to {agent_name}: {cpu_cores} cores, {memory_gb}GB RAM")
        
        return allocation
    
    def get_system_status(self) -> Dict:
        """Get current system resource usage"""
        return {
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent
        }
