"""Evidence Integrity Verification"""

import hashlib
from pathlib import Path
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)

class IntegrityVerifier:
    """Verify evidence integrity with cryptographic hashing"""
    
    def __init__(self):
        self.verification_log = []
    
    def verify_file(self, file_path: Path, expected_hash: str) -> Dict:
        """Verify file integrity"""
        
        current_hash = self._calculate_hash(file_path)
        is_valid = current_hash == expected_hash
        
        result = {
            'file': str(file_path),
            'expected_hash': expected_hash,
            'current_hash': current_hash,
            'is_valid': is_valid,
            'timestamp': str(datetime.now())
        }
        
        self.verification_log.append(result)
        
        logger.info(f"Integrity check: {file_path.name} - {'VALID' if is_valid else 'INVALID'}")
        
        return result
    
    def _calculate_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash"""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()

from datetime import datetime
