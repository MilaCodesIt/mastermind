"""Evidence Processor - Core forensic analysis system"""

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import logging

logger = logging.getLogger(__name__)


class EvidenceProcessor:
    """Process forensic evidence for Case 1FDV-23-0001009"""
    
    EVIDENCE_TYPES = {
        'financial': ['pdf', 'xlsx', 'xls', 'csv'],
        'property': ['pdf'],
        'phone_records': ['pdf', 'txt', 'csv'],
        'communications': ['pdf', 'json', 'txt', 'docx'],
        'meeting_transcripts': ['txt', 'pdf', 'docx'],
        'legal_documents': ['pdf', 'docx', 'txt'],
        'forensic_reports': ['pdf']
    }
    
    def __init__(self, case_id: str = "1FDV-23-0001009"):
        self.case_id = case_id
        self.base_dir = Path(__file__).parent.parent.parent
        self.evidence_dir = self.base_dir / "case-files" / case_id / "evidence"
        self.chain_of_custody_file = self.evidence_dir / "chain-of-custody.json"
        self.chain_of_custody = self._load_chain_of_custody()
        
        # Ensure directories exist
        self.evidence_dir.mkdir(parents=True, exist_ok=True)
        for evidence_type in self.EVIDENCE_TYPES:
            (self.evidence_dir / evidence_type).mkdir(exist_ok=True)
    
    def process_evidence(self, file_path: Path, evidence_type: str, metadata: Optional[Dict] = None) -> Dict[str, Any]:
        """Process evidence file with chain-of-custody logging"""
        
        if not file_path.exists():
            raise FileNotFoundError(f"Evidence file not found: {file_path}")
        
        # Calculate integrity hash
        file_hash = self._calculate_hash(file_path)
        
        # Create evidence record
        evidence = {
            'evidence_id': file_hash[:16],
            'case_id': self.case_id,
            'type': evidence_type,
            'file_name': file_path.name,
            'file_path': str(file_path),
            'file_size': file_path.stat().st_size,
            'sha256_hash': file_hash,
            'timestamp': datetime.now().isoformat(),
            'processor': 'forensic-analyst-agent',
            'metadata': metadata or {}
        }
        
        # Log in chain of custody
        self._log_custody(evidence)
        
        logger.info(f"Processed evidence: {evidence['evidence_id']} - {file_path.name}")
        
        return evidence
    
    def process_financial_record(self, file_path: Path) -> Dict[str, Any]:
        """Process bank statements and child support worksheets"""
        metadata = {
            'category': 'financial',
            'subcategory': self._detect_financial_type(file_path)
        }
        return self.process_evidence(file_path, 'financial', metadata)
    
    def process_property_inspection(self, file_path: Path, address: Optional[str] = None) -> Dict[str, Any]:
        """Process property inspection reports"""
        metadata = {
            'category': 'property',
            'address': address or self._extract_address(file_path)
        }
        return self.process_evidence(file_path, 'property', metadata)
    
    def process_phone_records(self, file_path: Path, phone_number: Optional[str] = None) -> Dict[str, Any]:
        """Process phone records"""
        metadata = {
            'category': 'communications',
            'phone_number': phone_number or self._extract_phone_number(file_path.name)
        }
        return self.process_evidence(file_path, 'phone_records', metadata)
    
    def process_communications(self, file_path: Path, platform: Optional[str] = None) -> Dict[str, Any]:
        """Process communications (OFW messages, chat transcripts, emails)"""
        metadata = {
            'category': 'communications',
            'platform': platform or self._detect_platform(file_path)
        }
        return self.process_evidence(file_path, 'communications', metadata)
    
    def process_meeting_transcript(self, file_path: Path, meeting_date: Optional[str] = None) -> Dict[str, Any]:
        """Process meeting transcripts"""
        metadata = {
            'category': 'meeting_transcript',
            'meeting_date': meeting_date or self._extract_meeting_date(file_path.name)
        }
        return self.process_evidence(file_path, 'meeting_transcripts', metadata)
    
    def _calculate_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash for integrity verification"""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def _log_custody(self, evidence: Dict[str, Any]):
        """Log evidence in chain of custody"""
        custody_entry = {
            'timestamp': datetime.now().isoformat(),
            'action': 'evidence_processed',
            'evidence_id': evidence['evidence_id'],
            'file_hash': evidence['sha256_hash'],
            'processor': 'forensic-analyst-agent',
            'details': {
                'type': evidence['type'],
                'file_name': evidence['file_name'],
                'file_size': evidence['file_size']
            }
        }
        
        self.chain_of_custody.append(custody_entry)
        self._save_chain_of_custody()
    
    def _load_chain_of_custody(self) -> List[Dict[str, Any]]:
        """Load existing chain of custody"""
        if self.chain_of_custody_file.exists():
            with open(self.chain_of_custody_file, 'r') as f:
                return json.load(f)
        return []
    
    def _save_chain_of_custody(self):
        """Save chain of custody to disk"""
        self.chain_of_custody_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.chain_of_custody_file, 'w') as f:
            json.dump(self.chain_of_custody, f, indent=2)
    
    def _detect_financial_type(self, file_path: Path) -> str:
        """Detect type of financial document"""
        name_lower = file_path.name.lower()
        if 'bank' in name_lower or 'statement' in name_lower:
            return 'bank_statement'
        elif 'child support' in name_lower or 'csgw' in name_lower:
            return 'child_support_worksheet'
        elif 'tax' in name_lower:
            return 'tax_document'
        return 'unknown'
    
    def _extract_address(self, file_path: Path) -> str:
        """Extract address from property inspection filename"""
        import re
        match = re.search(r'(\d+[^_]*)', file_path.name)
        return match.group(1) if match else 'unknown'
    
    def _extract_phone_number(self, filename: str) -> str:
        """Extract phone number from filename"""
        import re
        match = re.search(r'(\d{10})', filename)
        return match.group(1) if match else 'unknown'
    
    def _detect_platform(self, file_path: Path) -> str:
        """Detect communication platform"""
        name_lower = file_path.name.lower()
        if 'ofw' in name_lower:
            return 'Our Family Wizard'
        elif 'chat' in name_lower:
            return 'chat_platform'
        elif 'email' in name_lower:
            return 'email'
        return 'unknown'
    
    def _extract_meeting_date(self, filename: str) -> str:
        """Extract meeting date from filename"""
        import re
        match = re.search(r'(september|october|november|december)\s+(\d+)', filename, re.IGNORECASE)
        if match:
            return f"{match.group(1)} {match.group(2)}"
        return 'unknown'
    
    def get_chain_of_custody(self) -> List[Dict[str, Any]]:
        """Get complete chain of custody log"""
        return self.chain_of_custody
    
    def verify_evidence_integrity(self, evidence_id: str, current_hash: str) -> bool:
        """Verify evidence has not been tampered with"""
        for entry in self.chain_of_custody:
            if entry.get('evidence_id') == evidence_id:
                return entry.get('file_hash') == current_hash
        return False


if __name__ == "__main__":
    # Example usage
    processor = EvidenceProcessor()
    print(f"Evidence processor initialized for case: {processor.case_id}")
    print(f"Evidence directory: {processor.evidence_dir}")
    print(f"Chain of custody entries: {len(processor.chain_of_custody)}")
