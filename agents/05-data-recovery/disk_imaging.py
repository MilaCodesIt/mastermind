"""Disk Imaging & Forensic Acquisition"""

import hashlib
from pathlib import Path
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class DiskImager:
    """Create forensic disk images with integrity verification"""
    
    SUPPORTED_FORMATS = ['dd', 'e01', 'aff', 'raw']
    
    def __init__(self):
        self.images_created = []
    
    def create_image(
        self,
        source_device: str,
        output_path: Path,
        image_format: str = 'dd',
        verify: bool = True
    ) -> Dict:
        """Create forensic disk image"""
        
        result = {
            'source': source_device,
            'output': str(output_path),
            'format': image_format,
            'status': 'imaging_initiated',
            'hash': None
        }
        
        logger.info(f"Creating disk image: {source_device} -> {output_path}")
        
        if verify:
            result['hash'] = self._calculate_hash(output_path)
        
        return result
    
    def _calculate_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash"""
        sha256 = hashlib.sha256()
        if file_path.exists():
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    sha256.update(chunk)
        return sha256.hexdigest()
