"""Agent Messaging System"""

from typing import Dict, List, Callable
import asyncio
import logging

logger = logging.getLogger(__name__)

class AgentMessaging:
    """Real-time messaging between agents"""
    
    def __init__(self):
        self.subscribers = {}
        self.message_queue = asyncio.Queue()
    
    def subscribe(self, agent_name: str, callback: Callable):
        """Subscribe agent to message bus"""
        if agent_name not in self.subscribers:
            self.subscribers[agent_name] = []
        self.subscribers[agent_name].append(callback)
        logger.info(f"Agent {agent_name} subscribed to message bus")
    
    async def publish(self, message: Dict):
        """Publish message to subscribed agents"""
        await self.message_queue.put(message)
        
        target = message.get('to')
        if target and target in self.subscribers:
            for callback in self.subscribers[target]:
                callback(message)
        
        logger.info(f"Message published: {message.get('from')} -> {message.get('to')}")
    
    async def process_queue(self):
        """Process message queue"""
        while True:
            message = await self.message_queue.get()
            # Process message
            logger.debug(f"Processing message: {message}")
            self.message_queue.task_done()
