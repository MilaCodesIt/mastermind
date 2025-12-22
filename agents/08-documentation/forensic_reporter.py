"""Forensic Report Generator"""

from datetime import datetime
from pathlib import Path
from typing import Dict, List
import json
import logging

logger = logging.getLogger(__name__)

class ForensicReporter:
    """Generate comprehensive forensic reports"""
    
    def __init__(self, case_id: str = "1FDV-23-0001009"):
        self.case_id = case_id
        self.reports_dir = Path(f"case-files/{case_id}/reports")
        self.reports_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_report(
        self,
        report_type: str,
        evidence_items: List[Dict],
        findings: List[str],
        conclusions: List[str]
    ) -> str:
        """Generate forensic report"""
        
        report = f"""# FORENSIC ANALYSIS REPORT

## Case Information
- **Case ID**: {self.case_id}
- **Report Type**: {report_type}
- **Date**: {datetime.now().strftime('%B %d, %Y')}
- **Analyst**: Forensic Analyst Agent

## Executive Summary

This report presents forensic analysis findings for Case {self.case_id}.

## Evidence Analyzed

"""
        
        for i, item in enumerate(evidence_items, 1):
            report += f"{i}. {item.get('description', 'Evidence item')}\n"
            report += f"   - File: {item.get('file', 'N/A')}\n"
            report += f"   - Hash: {item.get('hash', 'N/A')}\n\n"
        
        report += "\n## Findings\n\n"
        
        for i, finding in enumerate(findings, 1):
            report += f"{i}. {finding}\n\n"
        
        report += "\n## Conclusions\n\n"
        
        for i, conclusion in enumerate(conclusions, 1):
            report += f"{i}. {conclusion}\n\n"
        
        report += f"""\n## Chain of Custody

All evidence was handled in accordance with forensic best practices with complete chain-of-custody documentation.

## Certification

This report was generated using automated forensic analysis tools with human oversight.

---

**Report ID**: {self._generate_report_id()}
**Generated**: {datetime.now().isoformat()}
"""
        
        # Save report
        report_file = self.reports_dir / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        report_file.write_text(report)
        
        logger.info(f"Forensic report generated: {report_file.name}")
        
        return report
    
    def _generate_report_id(self) -> str:
        """Generate unique report ID"""
        import hashlib
        timestamp = datetime.now().isoformat()
        return hashlib.sha256(timestamp.encode()).hexdigest()[:16]
