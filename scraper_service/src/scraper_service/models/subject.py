from dataclasses import dataclass
from enum import StrEnum

class AcademicBand(StrEnum):
    G1 = "G1"  # NT
    G2 = "G2"  # NA
    G3 = "G3"  # Express
    IP = "IP"
    H1 = "H1"
    H2 = "H2"
    H3 = "H3"
    GENERAL = "General" # For everything else

G_BANDS = {
    AcademicBand.G1,
    AcademicBand.G2,
    AcademicBand.G3,
}

H_BANDS = {
    AcademicBand.H1,
    AcademicBand.H2,
    AcademicBand.H3,
}

class Subject(StrEnum):
    # Mathematics
    MATHEMATICS = "Math"
    E_MATH = "E-Math"
    A_MATH = "A-Math"
    FURTHER_MATHEMATICS = "Further Math"

    # Sciences
    SCIENCE = "Science" # Covers Primary and Lower Secondary Science
    PURE_PHYSICS = "Pure Physics"
    PURE_CHEMISTRY = "Pure Chemistry"
    PURE_BIOLOGY = "Pure Biology"
    COMBINED_CHEMISTRY = "Combined Chemistry"
    COMBINED_BIOLOGY = "Combined Biology"
    COMBINED_PHYSICS = "Combined Physics"
    PHYSICS = "Physics"
    CHEMISTRY = "Chemistry"
    BIOLOGY = "Biology"

    # Languages
    ENGLISH = "English"
    CHINESE = "Chinese"
    HIGHER_CHINESE = "Higher Chinese"
    MALAY = "Malay"
    HIGHER_MALAY = "Higher Malay"
    TAMIL = "Tamil"
    HIGHER_TAMIL = "Higher Tamil"
    GENERAL_PAPER = "General Paper"

    # Literature
    ENGLISH_LITERATURE = "English Literature"
    CHINESE_LITERATURE = "Chinese Literature"
    MALAY_LITERATURE = "Malay Literature"
    TAMIL_LITERATURE = "Tamil Literature"
    COMBINED_LITERATURE = "Combined Literature"
    COMBINED_ENGLISH_LITERATURE = "Combined English Lit."
    COMBINED_CHINESE_LITERATURE = "Combined Chinese Lit."
    COMBINED_MALAY_LITERATURE = "Combined Malay Lit."
    COMBINED_TAMIL_LITERATURE = "Combined Tamil Lit."

    # Humanities & Arts
    HISTORY = "History"
    GEOGRAPHY = "Geography"
    SOCIAL_STUDIES = "Social Studies"
    ECONOMICS = "Economics"
    COMBINED_HISTORY = "Combined History"
    COMBINED_GEOGRAPHY = "Combined Geography"

    # Business, Tech & Enrichment
    PRINCIPLES_OF_ACCOUNTS = "Principles of Accounts"
    COMPUTING = "Computing"
    ART = "Art"
    PIANO = "Piano"
    VIOLIN = "Violin"
    GUITAR = "Guitar"
    DRUMS = "Drums"

    # Others
    OTHERS = "Others"

@dataclass
class SubjectPurityVariants:
    combined: Subject | None = None
    pure: Subject | None = None

PURE_SCIENCES = {
    Subject.PURE_PHYSICS,
    Subject.PURE_BIOLOGY,
    Subject.PURE_CHEMISTRY,
}

SUBJECTS_WITH_PURITY: dict[Subject, SubjectPurityVariants] = {
    Subject.PHYSICS: SubjectPurityVariants(Subject.COMBINED_PHYSICS, Subject.PURE_PHYSICS),
    Subject.BIOLOGY: SubjectPurityVariants(Subject.COMBINED_BIOLOGY, Subject.PURE_BIOLOGY),
    Subject.CHEMISTRY: SubjectPurityVariants(Subject.COMBINED_CHEMISTRY, Subject.PURE_CHEMISTRY),
    Subject.SCIENCE: SubjectPurityVariants(),   # Just to keep the purity flag since "Combined Science (Phys / Bio)" is valid

    Subject.HISTORY: SubjectPurityVariants(Subject.COMBINED_HISTORY),
    Subject.GEOGRAPHY: SubjectPurityVariants(Subject.COMBINED_GEOGRAPHY),
    Subject.ENGLISH_LITERATURE: SubjectPurityVariants(Subject.COMBINED_ENGLISH_LITERATURE),
    Subject.CHINESE_LITERATURE: SubjectPurityVariants(Subject.COMBINED_CHINESE_LITERATURE),
    Subject.TAMIL_LITERATURE: SubjectPurityVariants(Subject.COMBINED_TAMIL_LITERATURE),
    Subject.MALAY_LITERATURE: SubjectPurityVariants(Subject.COMBINED_MALAY_LITERATURE),
}

# Subjects offered at the Junior College (A-Level) level with H1, H2, or H3 bands
SUBJECTS_WITH_H_BANDS = {
    # Mathematics
    Subject.MATHEMATICS,          # H1/H2 Math
    Subject.FURTHER_MATHEMATICS,  # H2 Further Math

    # Sciences (JCs use general names rather than "Pure" or "Combined")
    Subject.PHYSICS,              # H1/H2/H3 Physics
    Subject.CHEMISTRY,            # H1/H2/H3 Chemistry
    Subject.BIOLOGY,              # H1/H2/H3 Biology

    # Languages
    Subject.GENERAL_PAPER,        # H1 General Paper
    Subject.CHINESE,              # H1 Chinese
    Subject.MALAY,                # H1 Malay
    Subject.TAMIL,                # H1 Tamil
    Subject.ENGLISH_LITERATURE,   # H1/H2/H3 Literature in English
    Subject.CHINESE_LITERATURE,   # H2 Chinese Language and Literature
    Subject.MALAY_LITERATURE,     # H2 Malay Language and Literature
    Subject.TAMIL_LITERATURE,     # H2 Tamil Language and Literature

    # Humanities & Arts
    Subject.HISTORY,              # H1/H2/H3 History
    Subject.GEOGRAPHY,            # H1/H2/H3 Geography
    Subject.ECONOMICS,            # H1/H2/H3 Economics
    Subject.ART,                  # H2/H3 Art

    # Business & Tech
    Subject.PRINCIPLES_OF_ACCOUNTS, # H2 Principles of Accounting
    Subject.COMPUTING,              # H2 Computing
}

# Subjects offered at the Secondary level under Full SBB with G1, G2, or G3 bands
SUBJECTS_WITH_G_BANDS = {
    # Mathematics
    Subject.MATHEMATICS,          # G1/G2/G3 Mathematics
    Subject.E_MATH,               # Equivalent to G3 Mathematics
    Subject.A_MATH,               # G2/G3 Additional Mathematics

    # Sciences
    Subject.SCIENCE,              # G1/G2 Science
    Subject.PURE_PHYSICS,         # G3 Physics
    Subject.PURE_CHEMISTRY,       # G3 Chemistry
    Subject.PURE_BIOLOGY,         # G3 Biology
    Subject.COMBINED_PHYSICS,     # G2/G3 Combined Science
    Subject.COMBINED_CHEMISTRY,   # G2/G3 Combined Science
    Subject.COMBINED_BIOLOGY,     # G2/G3 Combined Science

    # Languages
    Subject.ENGLISH,              # G1/G2/G3 English
    Subject.CHINESE,              # G1/G2/G3 Chinese
    Subject.HIGHER_CHINESE,       # G3 Higher Chinese
    Subject.MALAY,                # G1/G2/G3 Malay
    Subject.HIGHER_MALAY,         # G3 Higher Malay
    Subject.TAMIL,                # G1/G2/G3 Tamil
    Subject.HIGHER_TAMIL,         # G3 Higher Tamil
    Subject.ENGLISH_LITERATURE,   # G1/G2/G3 Literature in English
    Subject.CHINESE_LITERATURE,   # G2/G3 Literature in Chinese
    Subject.MALAY_LITERATURE,     # G2/G3 Literature in Malay
    Subject.TAMIL_LITERATURE,     # G2/G3 Literature in Tamil

    # Humanities & Arts
    Subject.HISTORY,              # G2/G3 History
    Subject.GEOGRAPHY,            # G2/G3 Geography
    Subject.SOCIAL_STUDIES,       # G1/G2/G3 (Part of Humanities)
    Subject.COMBINED_HISTORY,     # G2/G3 Humanities (Social Studies, History)
    Subject.COMBINED_GEOGRAPHY,   # G2/G3 Humanities (Social Studies, Geography)
    Subject.COMBINED_LITERATURE,  # G2/G3 Humanities (Social Studies, Literature)
    Subject.COMBINED_ENGLISH_LITERATURE,
    Subject.COMBINED_CHINESE_LITERATURE,
    Subject.COMBINED_MALAY_LITERATURE,
    Subject.COMBINED_TAMIL_LITERATURE,
    Subject.ART,                  # G1/G2/G3 Art

    # Business & Tech
    Subject.PRINCIPLES_OF_ACCOUNTS, # G2/G3 POA
    Subject.COMPUTING,              # G3 Computing
}

@dataclass(frozen=True)
class BandedSubject:
    """Subject with the Band (if any)"""
    band: AcademicBand
    subject: Subject
