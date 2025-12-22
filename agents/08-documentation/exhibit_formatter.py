"""Court Exhibit Formatter"""

from pathlib import Path
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class ExhibitFormatter:
    """Format evidence as court exhibits"""
    
    EXHIBIT_TEMPLATE = """EXHIBIT {exhibit_number}

Case: {case_id}
Description: {description}
Date: {date}

Evidence Details:
{details}

Chain of Custody:
{custody}
"""
    
    def __init__(self, case_id: str = "1FDV-23-0001009"):
        self.case_id = case_id
        self.exhibit_counter = 0
    
    def format_exhibit(self, evidence: Dict) -> str:
        """Format evidence as court exhibit"""
        
        self.exhibit_counter += 1
        exhibit_num = chr(64 + self.exhibit_counter)  # A, B, C, ...
        
        exhibit = self.EXHIBIT_TEMPLATE.format(
            exhibit_number=exhibit_num,
            case_id=self.case_id,
            description=evidence.get('description', ''),
            date=evidence.get('date', ''),
            details=evidence.get('details', ''),
            custody=evidence.get('custody', '')
        )
        
        logger.info(f"Exhibit {exhibit_num} formatted")
        
        return exhibit
