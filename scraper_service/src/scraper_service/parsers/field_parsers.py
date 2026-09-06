"""Methods used to extract individual fields, used by the unified_parser"""

from dataclasses import dataclass
import logging
import re
from typing import Literal, Callable

from scraper_service.models.listing import AcademicLevel
from scraper_service.models.subject import PURE_SCIENCES, Subject, AcademicBand, BandedSubject, G_BANDS, SUBJECTS_WITH_G_BANDS, H_BANDS, SUBJECTS_WITH_H_BANDS, SUBJECTS_WITH_PURITY

logger = logging.getLogger(__name__)

PTN_BAND_G1 = re.compile(r"\b(?:NT|G1)\b", re.IGNORECASE)
PTN_BAND_G2 = re.compile(r"\b(?:NA|G2)\b", re.IGNORECASE)
PTN_BAND_G3 = re.compile(r"\b(?:Express|G3)\b", re.IGNORECASE)
PTN_BAND_H1 = re.compile(r"\bH1\b", re.IGNORECASE)
PTN_BAND_H2 = re.compile(r"\bH2\b", re.IGNORECASE)
PTN_BAND_H3 = re.compile(r"\bH3\b", re.IGNORECASE)
PTN_BAND_IP = re.compile(r"\bIP\b", re.IGNORECASE)

PTN_PURITY_PURE = re.compile(r"\bpure\b", re.IGNORECASE)
PTN_PURITY_COMBINED = re.compile(r"\bcomb(?:ined)?\b", re.IGNORECASE)

# Base patterns for Subjects
# Order matters, higher priority matches should be on top (e.g. "English Literature" before "Literature")
SUBJECT_REGEX: dict[Subject, re.Pattern[str]] = {
    ## Mathematics (Specific variations MUST come before general Math)
    Subject.FURTHER_MATHEMATICS: re.compile(r"\b(?:further|f)[\s\.-]*math(?:ematic)?s?\b", re.IGNORECASE),
    Subject.A_MATH: re.compile(r"\b(?:add(?:itional)?|a)[\s\.-]*math(?:ematic)?s?\b", re.IGNORECASE),
    Subject.E_MATH: re.compile(r"\b(?:elem(?:entary)?|e)[\s\.-]*math(?:ematic)?s?\b", re.IGNORECASE),
    Subject.MATHEMATICS: re.compile(r"\bmath(?:ematic)?s?\b", re.IGNORECASE),

    ## Sciences
    Subject.CHEMISTRY: re.compile(r"\bchem(?:istry)?\b", re.IGNORECASE),
    Subject.PHYSICS: re.compile(r"\bphys?(?:ics?)?\b", re.IGNORECASE),
    Subject.BIOLOGY: re.compile(r"\bbio(?:logy)?\b", re.IGNORECASE),
    Subject.SCIENCE: re.compile(r"\bsciences?\b", re.IGNORECASE),

    ## Literatures (Must come before base languages)
    # Matches: English Literature, Eng Lit, EL Lit, or just "Literature" / "Lit"
    Subject.ENGLISH_LITERATURE: re.compile(r"\b(?:(?:eng(?:lish)?|el)[\s-]*)?lit(?:erature)?\b", re.IGNORECASE),
    # Matches: Chinese Literature, CLit, CL Lit, Mandarin Lit
    Subject.CHINESE_LITERATURE: re.compile(r"\b(?:chinese|mandarin|cl)[\s-]*lit(?:erature)?\b", re.IGNORECASE),
    # Matches: Malay Literature, MLit, ML Lit
    Subject.MALAY_LITERATURE: re.compile(r"\b(?:malay|ml)[\s-]*lit(?:erature)?\b", re.IGNORECASE),
    # Matches: Tamil Literature, TLit, TL Lit
    Subject.TAMIL_LITERATURE: re.compile(r"\b(?:tamil|tl)[\s-]*lit(?:erature)?\b", re.IGNORECASE),

    ## Higher Mother Tongues (Must come before base languages)
    # Matches: Higher Chinese, Higher Mandarin, HCL, Higher CL
    Subject.HIGHER_CHINESE: re.compile(r"\b(?:higher[\s-]*(?:chinese|mandarin|cl)|hcl)\b", re.IGNORECASE),
    # Matches: Higher Malay, HML, Higher ML
    Subject.HIGHER_MALAY: re.compile(r"\b(?:higher[\s-]*(?:malay|ml)|hml)\b", re.IGNORECASE),
    # Matches: Higher Tamil, HTL, Higher TL
    Subject.HIGHER_TAMIL: re.compile(r"\b(?:higher[\s-]*(?:tamil|tl)|htl)\b", re.IGNORECASE),

    ## Base Languages (Lower Precedence)
    # Matches: General Paper, GP
    Subject.GENERAL_PAPER: re.compile(r"\b(?:general\s*paper|gp)\b", re.IGNORECASE),
    # Matches: English, Eng, EL
    Subject.ENGLISH: re.compile(r"\b(?:eng(?:lish)?|el|lang(?:uage)?[\s-]*arts?)\b", re.IGNORECASE),
    # Matches: Chinese, Mandarin, CL
    Subject.CHINESE: re.compile(r"\b(?:chinese|mandarin|cl)\b", re.IGNORECASE),
    # Matches: Malay, Bahasa Melayu, ML
    Subject.MALAY: re.compile(r"\b(?:malay|bahasa\s*melayu|ml)\b", re.IGNORECASE),
    # Matches: Tamil, TL
    Subject.TAMIL: re.compile(r"\b(?:tamil|tl)\b", re.IGNORECASE),

    ## Humanities
    Subject.HISTORY: re.compile(r"\bhist(?:ory)?\b", re.IGNORECASE),
    Subject.GEOGRAPHY: re.compile(r"\bgeog(?:raphy)?\b", re.IGNORECASE),
    Subject.SOCIAL_STUDIES: re.compile(r"\b(?:social\s*studies|ss)\b", re.IGNORECASE),
    Subject.ECONOMICS: re.compile(r"\becon(?:omic)?s?\b", re.IGNORECASE),

    ## Business & Tech
    # Matches: Principles of Accounts, POA, Accounts, Accounting
    Subject.PRINCIPLES_OF_ACCOUNTS: re.compile(r"\b(?:poa|principles\s*of\s*accounts?|account(?:ing|s)?)\b", re.IGNORECASE),
    # Matches: Computing, Computer Science, Computer Studies, Comp Sci
    Subject.COMPUTING: re.compile(r"\b(?:computing|comp(?:uter)?\s*(?:sci(?:ence)?|studies))\b", re.IGNORECASE),
    ## Enrichment & Arts
    # Matches: Art, Arts, Visual Arts
    Subject.ART: re.compile(r"\b(?:visual\s*)?arts?\b", re.IGNORECASE),
    # Matches: Piano
    Subject.PIANO: re.compile(r"\bpiano\b", re.IGNORECASE),
    # Matches: Violin
    Subject.VIOLIN: re.compile(r"\bviolin\b", re.IGNORECASE),
    # Matches: Guitar (also catches acoustic/electric guitar if phrased as "acoustic guitar")
    Subject.GUITAR: re.compile(r"\bguitar\b", re.IGNORECASE),
    # Matches: Drum, Drums, Drumming
    Subject.DRUMS: re.compile(r"\bdrums?(?:ming)?\b", re.IGNORECASE),
}

ACADLEVEL_RESOLVER: dict[re.Pattern[str], Callable[[re.Match[str]], AcademicLevel]] = {
    # Primary: e.g., Primary 5, Pri 3, P1
    re.compile(r"\b(?:pri(?:mary)?\s*([1-6])?|p([1-6]))\b", re.IGNORECASE): lambda m: AcademicLevel.__members__.get(f"P{m.group(1) or m.group(2)}", AcademicLevel.PSLE),

    # Secondary: e.g., Secondary 4, Sec 2, S1
    re.compile(r"\b(?:sec(?:ondary)?\s*([1-5])?|s([1-5]))\b", re.IGNORECASE): lambda m: AcademicLevel.__members__.get(f"SEC_{m.group(1) or m.group(2)}", AcademicLevel.SEC),
    re.compile(r"\b(?:o\s*-?\s*levels?)\b", re.IGNORECASE): lambda m: AcademicLevel.SEC,

    # Junior College: e.g., Junior College 1, JC 2, JC2
    re.compile(r"\b(?:junior\s*college|jc)\s*([12])?\b", re.IGNORECASE): lambda m: AcademicLevel.__members__.get(f"JC_{m.group(1)}", AcademicLevel.ALEVEL),
    re.compile(r"\ba\s*-?\s*levels?\b", re.IGNORECASE): lambda m: AcademicLevel.ALEVEL,

    # Kindergarten: e.g., Kindergarten 2, K1
    re.compile(r"\b(?:(?:kindergarten)\s*([12])?|k([12]))\b", re.IGNORECASE): lambda m: AcademicLevel.__members__.get(f"K{m.group(1) or m.group(2)}", AcademicLevel.KINDERGARTEN),

    # Nursery: e.g., Nursery, N1, N2
    re.compile(r"\b(?:nursery|n1|n2)\b", re.IGNORECASE): lambda m: AcademicLevel.NURSERY,

    # IP: e.g., IP Year 1, IP 2, IP Y3
    re.compile(r"\bip\s*(?:year\s*|y)?([1-6])\b", re.IGNORECASE): lambda m: AcademicLevel[f"IP_{m.group(1)}"],

    # International Grades: e.g., Grade 10, Gr 8
    re.compile(r"\b(?:grade|gr)\s*([1-9]|1[0-2])\b", re.IGNORECASE): lambda m: AcademicLevel[f"GRADE_{m.group(1)}"],

    # IB Diploma: e.g., IB Diploma Year 1, IB DP 2, IB Y1
    re.compile(r"\bib\s*(?:diploma\s*)?(?:year\s*|y|dp)\s*([12])\b", re.IGNORECASE): lambda m: AcademicLevel[f"IB_DP_{m.group(1)}"],

    # Tertiary
    re.compile(r"\b(?:polytechnic|poly)\b", re.IGNORECASE): lambda m: AcademicLevel.POLYTECHNIC,
    re.compile(r"\b(?:university|uni|undergrad|degree)\b", re.IGNORECASE): lambda m: AcademicLevel.UNIVERSITY,
}


LEXICON = re.compile(
    rf"(?P<BAND>{PTN_BAND_H1.pattern}|{PTN_BAND_H2.pattern}|{PTN_BAND_H3.pattern}|" +
        rf"{PTN_BAND_G1.pattern}|{PTN_BAND_G2.pattern}|{PTN_BAND_G3.pattern}|" +
        rf"{PTN_BAND_IP.pattern})|" +
    rf"(?P<PURITY>{PTN_PURITY_PURE.pattern}|{PTN_PURITY_COMBINED.pattern})|" +
    rf"(?P<SUBJECT>{"|".join(compiled.pattern for compiled in SUBJECT_REGEX.values())})",
    re.IGNORECASE
)

def extract_bandedsubjects(raw: str) -> set[BandedSubject]:
    """Extracts a set of Subject from raw string

    Known Limitations:
        - Banding (e.g. H2) and Purity (e.g. Combined) needs to come before the subject itself
            - e.g. The following will fail: Math (H2), Chemistry - Combined
        - Doesn't care about Academic Level (Sec 3 Math and J1 Math) will both just give Math
    """
    # Works by breaking the raw strings into a bunch of lexicons / tokens, and then settings states (band / purity) based on the tokens seen
    # e.g. "G2 Math and some Pure Chemistry, Phys, Combined Geography with G1 Computing" will be broken into:
    #       G2, Math, Pure, Chemistry, Phys, Combined, Geography, G1, Computing
    #       ^          ^                        ^                 ^
    #   sets band  sets purity              new purity         new band
    extracted: set[BandedSubject] = set()
    cur_purity: Literal["", "PURE", "COMBINED"] = ""
    cur_band = AcademicBand.GENERAL
    for m in LEXICON.finditer(raw):
        token = m.group()
        token_type = m.lastgroup
        logging.debug(f"Processing token: {token}")
        if token_type == "PURITY":
            if PTN_PURITY_PURE.fullmatch(token):
                cur_purity = "PURE"
            elif PTN_PURITY_COMBINED.fullmatch(token):
                cur_purity = "COMBINED"
            else:
                logging.warning(f"Extracted nonsensical Purity token: {token}")
            continue

        if token_type == "BAND":
            if PTN_BAND_IP.fullmatch(token):
                cur_band = AcademicBand.IP
            elif PTN_BAND_H1.fullmatch(token):
                cur_band = AcademicBand.H1
            elif PTN_BAND_H2.fullmatch(token):
                cur_band = AcademicBand.H2
            elif PTN_BAND_H3.fullmatch(token):
                cur_band = AcademicBand.H3
            elif PTN_BAND_G1.fullmatch(token):
                cur_band = AcademicBand.G1
            elif PTN_BAND_G2.fullmatch(token):
                cur_band = AcademicBand.G2
            elif PTN_BAND_G3.fullmatch(token):
                cur_band = AcademicBand.G3
            else:
                logging.warning(f"Extracted nonsensical Band token: {token}")
            continue

        # Only subject tokens should be left
        if token_type != "SUBJECT":
            logging.error(f"Unhandled token type: {token_type}")
            continue

        cur_subject = Subject.OTHERS
        for sub, pattern in SUBJECT_REGEX.items():
            if pattern.fullmatch(token):
                cur_subject = sub
                logging.debug(f"Token matched subject: {cur_subject}")
                break   # First match takes priority (e.g. "e-math" breaks before "math")
        else:
            logging.warning(f"Extracted nonsensical Subject token: {token}")

        if cur_subject in SUBJECTS_WITH_PURITY:
            purity_variants = SUBJECTS_WITH_PURITY[cur_subject]
            cur_subject = (purity_variants.combined if cur_purity == "COMBINED" and purity_variants.combined else
                           purity_variants.pure if cur_purity == "PURE" and purity_variants.pure else
                           cur_subject)
            logging.debug(f"Subject after purity: {cur_subject}")
        else:
            # Reset current purity if purity doesn't make sense for the current subject
            cur_purity = ""

        # Clear current band if the current subject doesn't belong in that band
        if ((cur_band in G_BANDS and cur_subject not in SUBJECTS_WITH_G_BANDS) or
            (cur_band in H_BANDS and cur_subject not in SUBJECTS_WITH_H_BANDS) or
            (cur_band == AcademicBand.IP and cur_subject not in SUBJECTS_WITH_H_BANDS | SUBJECTS_WITH_G_BANDS)):
            logging.debug(f"Band cleared as <{cur_subject}> doesn't have a band of <{cur_band}>")
            cur_band = AcademicBand.GENERAL

        # Implicit bands (e.g. Pure Sciences are only offered in the G3 level)
        if cur_subject in PURE_SCIENCES:
            cur_band = AcademicBand.G3

        # Discard redundancies for subjects with purity; e.g. Combined Science (Phy / Bio) shouldn't have "Science" as a subject
        if cur_subject in {Subject.COMBINED_PHYSICS, Subject.COMBINED_CHEMISTRY, Subject.COMBINED_BIOLOGY, Subject.PURE_PHYSICS, Subject.PURE_CHEMISTRY, Subject.PURE_BIOLOGY}:
            extracted.discard(BandedSubject(band = cur_band, subject = Subject.SCIENCE))
            logging.debug(f"Discarded <SCIENCE> since it preceeds the current <{cur_subject}>")

        extracted.add(BandedSubject(band = cur_band, subject=cur_subject))

    return extracted


def extract_acad_levels(raw: str) -> set[AcademicLevel]:
    """Extracts the Academic Levels from the string, uses AcademicLevel 'General' as fallback"""
    acad_levels: set[AcademicLevel] = set()
    
    for pattern, resolver in ACADLEVEL_RESOLVER.items():
        for match in pattern.finditer(raw):
            try:
                acad_levels.add(resolver(match))
            except KeyError:
                logger.warning("Illegal AcademicLevel Found by Regex")

    if len(acad_levels) == 0:
        acad_levels.add(AcademicLevel.GENERAL)

    # Remove redundancies (e.g. JC1 is a subset of ALEVELS)
    if {AcademicLevel.SEC_1, AcademicLevel.SEC_2, AcademicLevel.SEC_3, AcademicLevel.SEC_4, AcademicLevel.SEC_5} & acad_levels:
        acad_levels.discard(AcademicLevel.SEC)
    if {AcademicLevel.P1, AcademicLevel.P2, AcademicLevel.P3, AcademicLevel.P4, AcademicLevel.P5, AcademicLevel.P6} & acad_levels:
        acad_levels.discard(AcademicLevel.PSLE)
    if {AcademicLevel.JC_1, AcademicLevel.JC_2} & acad_levels:
        acad_levels.discard(AcademicLevel.ALEVEL)

    return acad_levels


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info("HI")
    print(extract_bandedsubjects("Combined Science (Chem / Phy)"))
