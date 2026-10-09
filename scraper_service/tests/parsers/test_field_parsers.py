import unittest

from scraper_service.models.listing import AcademicLevel
from scraper_service.models.subject import Subject, AcademicBand, BandedSubject
import scraper_service.parsers.field_parsers as field_parsers

class TestExtractSpecificSciences(unittest.TestCase):
    def test_combined_sciences(self):
        cases = [
            # --- Generic Combined Sciences (No band specified) ---
            ("Combined Science (Chem / Phy)", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_CHEMISTRY), 
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_PHYSICS)
            }),
            ("Combined Physics and Combined Bio", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_PHYSICS), 
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_BIOLOGY)
            }),
            ("Combined Science(Chem/Phy)", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_CHEMISTRY), 
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_PHYSICS)
            }),
            ("Combined Science (Chem/Bio)", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_CHEMISTRY), 
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_BIOLOGY)
            }),
            ("Combined Chemistry", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_CHEMISTRY)
            }),
            ("Combined Chemistry/Physics", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_CHEMISTRY), 
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_PHYSICS)
            }),
            ("Combined Science (Physics/Chem)", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_PHYSICS), 
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_CHEMISTRY)
            }),
            ("Combined Science (Chemistry/Biology)", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_CHEMISTRY), 
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_BIOLOGY)
            }),
            ("Combined Science (Chemistry Only)", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_CHEMISTRY)
            }),
            ("Combined Science (Physics Only)", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_PHYSICS)
            }),

            # --- Banded Combined Sciences ---
            ("Secondary 4 G3 Combined Chemistry", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.COMBINED_CHEMISTRY)
            }),
            ("Secondary 4 NA Combined Science (Chem/Bio)", {
                BandedSubject(band=AcademicBand.G2, subject=Subject.COMBINED_CHEMISTRY), 
                BandedSubject(band=AcademicBand.G2, subject=Subject.COMBINED_BIOLOGY)
            }),

            # --- Pure Sciences (Implicitly G3) ---
            ("Secondary 3 Express Pure Chemistry & Pure Physics", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_CHEMISTRY), 
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_PHYSICS)
            }),
            ("O level Pure Physics", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_PHYSICS)
            }),
            ("Sec 3 Express Pure Chemistry", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_CHEMISTRY)
            }),
            ("Sec 4 Express Pure Biology", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_BIOLOGY)
            }),
            ("Pure Physics & Combined Bio / Chem", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_PHYSICS), 
                BandedSubject(band=AcademicBand.G3, subject=Subject.COMBINED_BIOLOGY), 
                BandedSubject(band=AcademicBand.G3, subject=Subject.COMBINED_CHEMISTRY)
            }),
            ("Pure Chemistry & Pure Physics", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_CHEMISTRY), 
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_PHYSICS)
            }),
            ("Pure Chemistry and Pure Biology", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_CHEMISTRY), 
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_BIOLOGY)
            }),

            # --- Others & JC/Tertiary ---
            ("Physics", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.PHYSICS)
            }),
            ("Bio", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.BIOLOGY)
            }),
            ("University Chem", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.CHEMISTRY)
            }),
            ("Junior College 1 H2 Biology", {
                BandedSubject(band=AcademicBand.H2, subject=Subject.BIOLOGY)
            }),
            ("JC2 H2 Chemistry", {
                BandedSubject(band=AcademicBand.H2, subject=Subject.CHEMISTRY)
            }),
            ("JC1 H2 Physics", {
                BandedSubject(band=AcademicBand.H2, subject=Subject.PHYSICS)
            }),
            
            # --- International / Fallbacks ---
            ("IGCSE Grade 9 Biology", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.BIOLOGY)
            }),
            ("IB Grade 12 (Diploma) SL Physics", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.PHYSICS)
            }),

            # --- Generic Science ---
            ("Pri and/OR Sec Science", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.SCIENCE)
            }),
        ]

        for raw_string, expected in cases:
            with self.subTest(case=raw_string):
                actual = field_parsers.extract_bandedsubjects(raw_string)
                self.assertEqual(actual, expected)

    def test_all_subject_combi(self):
        cases = [
            ("Secondary 3 G2 English, Math and Combined Science(Chem/Phy)", {
                BandedSubject(band=AcademicBand.G2, subject=Subject.ENGLISH), 
                BandedSubject(band=AcademicBand.G2, subject=Subject.MATHEMATICS), 
                BandedSubject(band=AcademicBand.G2, subject=Subject.COMBINED_CHEMISTRY), 
                BandedSubject(band=AcademicBand.G2, subject=Subject.COMBINED_PHYSICS)
            }),

            # JC Combination (Testing H-Bands and JC specific subjects)
            ("Looking for JC2 H2 Econs, H2 Math, and H1 GP tutor", {
                BandedSubject(band=AcademicBand.H2, subject=Subject.ECONOMICS),
                BandedSubject(band=AcademicBand.H2, subject=Subject.MATHEMATICS),
                BandedSubject(band=AcademicBand.H1, subject=Subject.GENERAL_PAPER)
            }),

            # MOE Acronyms
            ("P5 EL, CL, and Math", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.ENGLISH),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.CHINESE),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.MATHEMATICS)
            }),

            # Math Variations (A-Math/E-Math vs General Math)
            ("O-level AMath and E-Math", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.A_MATH),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.E_MATH)
            }),

            # Pure Science State Persistence
            ("Pure Bio and Chem", {
                # Assuming PURE_SCIENCES implicitly forces G3 based on your code logic
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_BIOLOGY),
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_CHEMISTRY)
            }),

            # Higher Mother Tongue & Literature ("Higher Chinese" to be detected and not "Chinese")
            ("Sec 2 Higher Chinese and English Lit", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.HIGHER_CHINESE),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.ENGLISH_LITERATURE)
            }),

            # Enrichment, Tech & Business
            ("Need help with Sec 4 POA, Computing, and Grade 8 Piano", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.PRINCIPLES_OF_ACCOUNTS),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMPUTING),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.PIANO)
            }),

            # IP Banding
            ## Language Arts is English
            ("IP Year 3 Math and Language Arts", {
                BandedSubject(band=AcademicBand.IP, subject=Subject.MATHEMATICS),
                BandedSubject(band=AcademicBand.IP, subject=Subject.ENGLISH)
            }),

            # Band State Clearing (Testing if an incompatible subject clears the preceding band)
            # e.g. "H2" shouldn't bleed into "Piano"
            ("H2 Physics and Grade 5 Piano", {
                BandedSubject(band=AcademicBand.H2, subject=Subject.PHYSICS),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.PIANO)
            }),

            # Heavy Mixed Purity and Bands 
            ("G3 E-Math, G2 English, and Combined Science (Bio/Phy)", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.E_MATH),
                BandedSubject(band=AcademicBand.G2, subject=Subject.ENGLISH),
                BandedSubject(band=AcademicBand.G2, subject=Subject.COMBINED_BIOLOGY),
                BandedSubject(band=AcademicBand.G2, subject=Subject.COMBINED_PHYSICS)
            }),
            # The "Language Arts" vs "Art" collision
            ("IP Year 2 Language Arts and Visual Arts", {
                BandedSubject(band=AcademicBand.IP, subject=Subject.ENGLISH), # Extracted from "Language Arts"
                BandedSubject(band=AcademicBand.IP, subject=Subject.ART)      # Extracted from "Visual Arts"
            }),

            # Math Variants
            ("O-Level Add Math, E-Math, and Further Maths", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.A_MATH),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.E_MATH),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.FURTHER_MATHEMATICS)
            }),

            # Literature vs Base Languages (Testing lexer ordering for Lit subjects)
            ("Sec 4 English Lit, Higher Chinese, and CL Lit", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.ENGLISH_LITERATURE),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.HIGHER_CHINESE),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.CHINESE_LITERATURE)
            }),

            # Complex Purity Overrides
            ("G3 Pure Physics, Chemistry, and Combined Bio", {
                # "Pure" applies to Physics and Chemistry. "Combined" overrides it for Bio.
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_PHYSICS),
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_CHEMISTRY),
                BandedSubject(band=AcademicBand.G3, subject=Subject.COMBINED_BIOLOGY)
            }),

            # Business, Tech & Music
            ("Sec 4 POA, Comp Sci, and Grade 8 Drumming", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.PRINCIPLES_OF_ACCOUNTS), # From POA
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMPUTING),              # From Comp Sci
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.DRUMS)                   # From Drumming
            }),

            # Extreme Shorthand & Mixed Bands 
            ("JC1 H2 Econs, H1 GP. Also Sec 3 G2 AMath.", {
                BandedSubject(band=AcademicBand.H2, subject=Subject.ECONOMICS),
                BandedSubject(band=AcademicBand.H1, subject=Subject.GENERAL_PAPER),
                BandedSubject(band=AcademicBand.G2, subject=Subject.A_MATH)
            }),

            # Extraneous Text with Multiple Languages
            ("Looking for a patient tutor for P5 Eng, Malay Language, and Higher Tamil.", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.ENGLISH),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.MALAY),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.HIGHER_TAMIL)
            }),

            # Smiletutor Examples
            (" P3 Chinese", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.CHINESE)
            }),

            (" Sec 1 Express Geography", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.GEOGRAPHY)
            }),

            (" Sec 3 Express Pure Chemistry", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_CHEMISTRY)
            }),

            (" P4 English", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.ENGLISH)
            }),

            (" JC1 H2 Math", {
                BandedSubject(band=AcademicBand.H2, subject=Subject.MATHEMATICS)
            }),

            (" Sec 3 NA G2 Combined Humanities (Geography Only)", {
                BandedSubject(band=AcademicBand.G2, subject=Subject.COMBINED_GEOGRAPHY)
            }),

            (" Sec 3 Combined Science (Chemistry Only)", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.COMBINED_CHEMISTRY)
            }),

            (" Sec 4 Express English", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.ENGLISH)
            }),

            (" Sec 4 NA Combined Science (Physics/Chem)", {
                BandedSubject(band=AcademicBand.G2, subject=Subject.COMBINED_PHYSICS),
                BandedSubject(band=AcademicBand.G2, subject=Subject.COMBINED_CHEMISTRY)
            }),

            (" K2 English & Math", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.ENGLISH),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.MATHEMATICS)
            }),

            (" JC2 H2 Physics", {
                BandedSubject(band=AcademicBand.H2, subject=Subject.PHYSICS)
            }),

            (" Sec 3 Express G3 Pure Physics", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.PURE_PHYSICS)
            }),

            (" Sec 2 Express History", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.HISTORY)
            }),

            (" Sec 4 Express Combined Humanities (Geography/SS)", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.COMBINED_GEOGRAPHY),
                BandedSubject(band=AcademicBand.G3, subject=Subject.SOCIAL_STUDIES)
            }),

            (" Sec 5 NA Combined Science (Chemistry Only)", {
                BandedSubject(band=AcademicBand.G2, subject=Subject.COMBINED_CHEMISTRY)
            }),

            (" Sec 3 NT G1 Science (NT)", {
                BandedSubject(band=AcademicBand.G1, subject=Subject.SCIENCE)
            }),

            (" JC2 H2 Biology", {
                BandedSubject(band=AcademicBand.H2, subject=Subject.BIOLOGY)
            }),

            (" IP Year 1 English Literature/Language Arts", {
                BandedSubject(band=AcademicBand.IP, subject=Subject.ENGLISH_LITERATURE)
            }),

            (" P4 English & Math & Science", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.ENGLISH),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.MATHEMATICS),
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.SCIENCE)
            }),

            (" Sec 3 Express Additional Math & Elementary Math", {
                BandedSubject(band=AcademicBand.G3, subject=Subject.A_MATH),
                BandedSubject(band=AcademicBand.G3, subject=Subject.E_MATH)
            }),

            (" JC2 H2 Economics", {
                BandedSubject(band=AcademicBand.H2, subject=Subject.ECONOMICS)
            }),

            (" Sec 2 NA G2 Math", {
                BandedSubject(band=AcademicBand.G2, subject=Subject.MATHEMATICS)
            }),

            ("IB/Grade 12 (Diploma) SL Mathematics", {
                BandedSubject(band=AcademicBand.GENERAL, subject=Subject.MATHEMATICS)
            })
        ]

        for raw_string, expected in cases:
            with self.subTest(case=raw_string):
                actual = field_parsers.extract_bandedsubjects(raw_string)
                self.assertEqual(actual, expected)

class TestAcademicLevel(unittest.TestCase):
    def test_academic_level(self):
        cases = [
            # --- Standard Primary & Secondary ---
            ("Primary 6 English and Math (Same tutor)", {AcademicLevel.P6}),
            ("Secondary 1 G1 Maths @ Yishun", {AcademicLevel.SEC_1}),
            ("P3 Chinese @ Segar Gardens 468 Segar Road", {AcademicLevel.P3}),
            ("Sec 5 NA Combined Science (Chemistry Only)", {AcademicLevel.SEC_5}),
            ("O-levels Geography @ Sengkang", {AcademicLevel.SEC}),
            ("O Level Combined Chemistry/Physics @ Little India", {AcademicLevel.SEC}),
            ("O-level Pure Physics @ Redhill", {AcademicLevel.SEC}),
            ("Secondary 4 O level Chinese @ Bukit Batok", {AcademicLevel.SEC_4}),
            
            # --- Junior College ---
            ("Junior College 1 H2 Chemistry @ Pioneer", {AcademicLevel.JC_1}),
            ("Cambridge A Level Chemistry @ Marine Parade", {AcademicLevel.ALEVEL}),
            ("JC2 H2 Math @ ONLINE LESSON", {AcademicLevel.JC_2}),
            ("JC1 A-levels H2 Chem", {AcademicLevel.JC_1}),
            
            # --- Pre-School ---
            ("Kindergarten 2 Math @ Bedok Reservoir", {AcademicLevel.K2}),
            ("Nursery Math @ 22 Lorong Puntong", {AcademicLevel.NURSERY}),
            
            # --- Tertiary ---
            ("Polytechnic Diploma in Customer Experience Management in Business", {AcademicLevel.POLYTECHNIC}),
            ("University Economic & Business Statistics", {AcademicLevel.UNIVERSITY}),
            
            # --- International / IB / IP ---
            ("Grade 5 Electronic Drums @ Canberra", {AcademicLevel.GRADE_5}),
            ("IB Diploma Year 1 HL Math @ Buona Vista", {AcademicLevel.IB_DP_1}),
            ("IP Year 1 English Literature/Language Arts @ Jalan Jelita", {AcademicLevel.IP_1}),
            ("IB Grade 12 (Diploma) HL Psychology @ 27 Leonie Hill", {AcademicLevel.GRADE_12}),
            
            # --- Multiple Levels in a Single Listing ---
            ("Primary and Secondary English and Science (Same Tutor)", {AcademicLevel.PSLE, AcademicLevel.SEC}),
            ("P4 Chinese & P2 Chinese (2 sibling) @ Mosella 5A Muswell Hill", {AcademicLevel.P2, AcademicLevel.P4}),
            ("Pri and/OR Sec Science @ Tuition Centre", {AcademicLevel.PSLE, AcademicLevel.SEC}),
            
            # --- Fallback / General (Enrichment, Adult, Beginner) ---
            ("Conversational Business Chinese @ Online", {AcademicLevel.GENERAL}),
            ("Beginner Drum @ Pasir Ris", {AcademicLevel.GENERAL}),

            # --- Known Failure Cases
            #("Primary 1 & 2 English & Math (Same Tutor)", {AcademicLevel.P1, AcademicLevel.P2}),
            #("Grade 9-10 IGCSE/IB Science @ Novena", {AcademicLevel.GRADE_9, AcademicLevel.GRADE_10}),
        ]

        for raw_string, expected in cases:
            with self.subTest(raw_string=raw_string):
                actual = field_parsers.extract_acad_levels(raw_string)
                self.assertEqual(actual, expected)



if __name__ == "__main__":
    _ = unittest.main()
