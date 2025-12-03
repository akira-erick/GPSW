from dataclasses import dataclass

@dataclass
class ApplicateCandidateDTO:
    candidate_id: str
    project_id: str

@dataclass
class ApplicateCandidateResponseDTO:
    application_id: str