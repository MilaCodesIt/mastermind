"""Motion Generator for Hawaii Family Court"""

from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
import json

class MotionGenerator:
    """Generate legal motions with proper citations"""
    
    MOTION_TEMPLATES = {
        'audio_access': 'Motion for Access to Court Audio Recordings',
        'sanctions': 'Motion for Sanctions - Decree Delay',
        'vacate': 'Motion to Vacate Decree - Due Process Violations',
        'correct_records': 'Motion to Correct Court Records',
        'proposed_decree': 'Proposed Divorce Decree'
    }
    
    def __init__(self, case_id: str = "1FDV-23-0001009"):
        self.case_id = case_id
        self.templates_dir = Path(__file__).parent / "templates" / "hawaii-family-court"
        self.templates_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_motion(
        self,
        motion_type: str,
        facts: List[str],
        legal_basis: List[Dict[str, str]],
        relief_sought: List[str],
        **kwargs
    ) -> str:
        """Generate motion with Hawaii Family Court formatting"""
        
        template = self._get_template(motion_type)
        
        motion_content = f"""IN THE FAMILY COURT OF THE FIRST CIRCUIT
STATE OF HAWAI'I

In re the Marriage of:

[PETITIONER NAME],
    Petitioner,

and

[RESPONDENT NAME],
    Respondent.

)
)
)
)
)
)
)
)

CIVIL NO. {self.case_id}

{self.MOTION_TEMPLATES.get(motion_type, 'MOTION')}

COMES NOW [PARTY NAME], appearing pro se, and respectfully moves this Court as follows:

## INTRODUCTION

{kwargs.get('introduction', '')}

## STATEMENT OF FACTS

"""
        
        for i, fact in enumerate(facts, 1):
            motion_content += f"{i}. {fact}\n\n"
        
        motion_content += "\n## LEGAL BASIS\n\n"
        
        for basis in legal_basis:
            citation = basis.get('citation', '')
            explanation = basis.get('explanation', '')
            motion_content += f"{citation}: {explanation}\n\n"
        
        motion_content += "\n## RELIEF SOUGHT\n\nWHEREFORE, Movant respectfully requests that this Court:\n\n"
        
        for i, relief in enumerate(relief_sought, 1):
            motion_content += f"{i}. {relief}\n\n"
        
        motion_content += """DATED: {date}

Respectfully submitted,

_________________________
[PARTY NAME]
Pro Se
""".format(date=datetime.now().strftime("%B %d, %Y"))
        
        return motion_content
    
    def _get_template(self, motion_type: str) -> str:
        """Load motion template"""
        template_file = self.templates_dir / f"{motion_type}.md"
        if template_file.exists():
            return template_file.read_text()
        return ""
