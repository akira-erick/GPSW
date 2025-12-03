from dataclasses import dataclass

@dataclass
class CreateCandidateDTO:
    name: str
    email: str
    resume: str

@dataclass
class CandidateDTO:
    id: str
    name: str
    email: str
    resume: str

@dataclass
class CreateCandidateResponseDTO:
    id: str