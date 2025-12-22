"""Evidence Logging with Chain-of-Custody"""

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class EvidenceLogger:
    """Log evidence handling with cryptographic verification"""
    
    def __init__(self, case_id: str = "1FDV-23-0001009"):
        self.case_id = case_id
        self.log_file = Path(f"case-files/{case_id}/evidence/chain-of-custody.json")
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        self.custody_log = self._load_log()
    
    def log_action(
        self,
        evidence_id: str,
        action: str,
        actor: str,
        details: Dict = None
    ) -> Dict:
        """Log evidence handling action"""
        
        entry = {
            'timestamp': datetime.now().isoformat(),
            'evidence_id': evidence_id,
            'action': action,
            'actor': actor,
            'details': details or {},
            'log_hash': None
        }
        
        # Calculate hash of entry
        entry_str = json.dumps(entry, sort_keys=True)
        entry['log_hash'] = hashlib.sha256(entry_str.encode()).hexdigest()[:16]
        
        self.custody_log.append(entry)
        self._save_log()
        
        logger.info(f"Custody log: {action} on {evidence_id} by {actor}")
        
        return entry
    
    def _load_log(self) -> List[Dict]:
        """Load existing custody log"""
        if self.log_file.exists():
            with open(self.log_file, 'r') as f:
                return json.load(f)
        return []
    
    def _save_log(self):
        """Save custody log"""
        with open(self.log_file, 'w') as f:
            json.dump(self.custody_log, f, indent=2)
