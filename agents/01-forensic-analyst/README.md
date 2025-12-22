# Forensic Analyst Agent

## Overview

The Forensic Analyst Agent is responsible for processing, analyzing, and preserving evidence for Case 1FDV-23-0001009 with complete chain-of-custody documentation.

## Capabilities

### Evidence Processing

- **Financial Records**: Bank statements, child support worksheets, tax documents
- **Property Inspections**: Home inspection reports, residential evaluations
- **Phone Records**: Call logs, text messages, communications history
- **Communications**: OFW messages, chat transcripts, email threads
- **Meeting Transcripts**: VoiceAccess recordings, court proceedings
- **Legal Documents**: Motions, orders, proposed decrees
- **Forensic Reports**: Device analysis, malware detection

### Chain-of-Custody

- Cryptographic hash calculation (SHA-256)
- Timestamp logging for all evidence handling
- Integrity verification
- Tamper detection
- Audit trail generation

### Analysis Tools

- Financial analyzer (income variance, pattern detection)
- Property inspector (condition assessment, value analysis)
- Phone record parser (call patterns, message extraction)
- Communications analyzer (sentiment analysis, keyword extraction)
- Timeline builder (event reconstruction, correlation)

## Usage

```python
from agents.forensic_analyst import EvidenceProcessor

# Initialize processor
processor = EvidenceProcessor(case_id="1FDV-23-0001009")

# Process financial evidence
evidence = processor.process_financial_record(Path("2022-bank-statements.pdf"))

# Process property inspection
property_evidence = processor.process_property_inspection(
    Path("2086_Palolo_Ave_Report.pdf"),
    address="2086 Palolo Ave, Honolulu, HI"
)

# Process phone records
phone_evidence = processor.process_phone_records(
    Path("5003674385.pdf"),
    phone_number="5003674385"
)

# Process communications
comm_evidence = processor.process_communications(
    Path("OFW_Messages_Report.pdf"),
    platform="Our Family Wizard"
)

# Verify evidence integrity
is_valid = processor.verify_evidence_integrity(
    evidence_id="a1b2c3d4e5f6g7h8",
    current_hash="sha256_hash_value"
)
```

## Evidence Types Supported

### Financial (`.pdf`, `.xlsx`, `.csv`)
- Bank statements (2022-2024)
- Child support worksheets (CSGW)
- Income documentation
- Tax records

### Property (`.pdf`)
- Home inspection reports
- Residential evaluations
- Property appraisals

### Communications (`.pdf`, `.json`, `.txt`, `.docx`)
- OFW (Our Family Wizard) messages
- Chat transcripts
- Email threads
- Text message logs

### Phone Records (`.pdf`, `.txt`, `.csv`)
- Call logs
- Text message records
- Communications history

### Meeting Transcripts (`.txt`, `.pdf`, `.docx`)
- VoiceAccess transcriptions
- Court proceedings
- Mediation sessions

## Chain-of-Custody Format

```json
{
  "timestamp": "2025-12-22T02:49:00Z",
  "action": "evidence_processed",
  "evidence_id": "a1b2c3d4e5f6g7h8",
  "file_hash": "sha256_hash_value",
  "processor": "forensic-analyst-agent",
  "details": {
    "type": "financial",
    "file_name": "2022-bank-statements.pdf",
    "file_size": 19811796
  }
}
```

## Output Directory Structure

```
case-files/1FDV-23-0001009/evidence/
├── financial/
│   ├── 2022-YEAR-JANUARY-TO-DECEMBER.pdf
│   ├── 2023-YEAR-JANUARY-TO-DECEMBER.pdf
│   ├── 2024-YEAR-JANUARY-TO-JUNE.pdf
│   └── child-support-worksheets/
├── property/
│   ├── 2086_Palolo_Ave___Residential_Report.pdf
│   └── 100_Waimano_Home_Rd_HPD_Pearl_City___Home_Inspection_Report.pdf
├── phone_records/
│   ├── 5003674385.pdf
│   └── 9060678681.pdf
├── communications/
│   ├── OFW_Messages_Report_2024-12-30.pdf
│   ├── chat_total_optimal_3.txt
│   └── CHAT_commands.docx
├── meeting_transcripts/
│   ├── 8_40_am_voiceaccess_meeting_september_28_transcript.txt
│   └── 5_17_pm_voiceaccess_meeting_september_29_transcript.txt
└── chain-of-custody.json
```

## Integration

- **Agent 02 (Legal Automation)**: Provides evidence for motion exhibits
- **Agent 06 (Chain-of-Custody)**: Logs all evidence handling
- **Agent 08 (Documentation)**: Generates forensic reports
- **Agent 09 (Integration Orchestrator)**: Coordinates multi-agent workflows
