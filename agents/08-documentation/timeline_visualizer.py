"""Timeline Visualization for Evidence"""

from datetime import datetime
from typing import List, Dict
import json
import logging

logger = logging.getLogger(__name__)

class TimelineVisualizer:
    """Create visual timelines from evidence"""
    
    def __init__(self):
        self.events = []
    
    def add_event(self, date: str, description: str, evidence_id: str = None):
        """Add event to timeline"""
        event = {
            'date': date,
            'description': description,
            'evidence_id': evidence_id
        }
        self.events.append(event)
        logger.info(f"Timeline event added: {date} - {description}")
    
    def generate_timeline(self) -> str:
        """Generate timeline visualization"""
        
        # Sort events by date
        sorted_events = sorted(self.events, key=lambda x: x['date'])
        
        timeline = "# Evidence Timeline\n\n"
        
        for event in sorted_events:
            timeline += f"## {event['date']}\n"
            timeline += f"{event['description']}\n"
            if event.get('evidence_id'):
                timeline += f"*Evidence ID: {event['evidence_id']}*\n"
            timeline += "\n"
        
        return timeline
