from typing import Annotated, Self

from pydantic import BaseModel, HttpUrl, Field, model_validator
from enum import StrEnum

from scraper_service.models.subject import BandedSubject

class AcademicLevel(StrEnum):
    # Pre-School
    NURSERY = "Nursery"
    KINDERGARTEN = "Kindergarten"
    K1 = "K1"
    K2 = "K2"

    # Primary
    PSLE = "Primary" # When not specified
    P1 = "Pri 1"
    P2 = "Pri 2"
    P3 = "Pri 3"
    P4 = "Pri 4"
    P5 = "Pri 5"
    P6 = "Pri 6"

    # Secondary
    SEC = "Secondary"
    SEC_1 = "Sec 1"
    SEC_2 = "Sec 2"
    SEC_3 = "Sec 3"
    SEC_4 = "Sec 4"
    SEC_5 = "Sec 5"

    # Junior College
    ALEVEL = "A-Levels"
    JC_1 = "JC 1"
    JC_2 = "JC 2"

    # Integrated Programme (IP)
    IP = "IP"
    IP_1 = "IP Y1"
    IP_2 = "IP Y2"
    IP_3 = "IP Y3"
    IP_4 = "IP Y4"
    IP_5 = "IP Y5"
    IP_6 = "IP Y6"

    # International / IB / IGCSE
    GRADE_1 = "Grade 1"
    GRADE_2 = "Grade 2"
    GRADE_3 = "Grade 3"
    GRADE_4 = "Grade 4"
    GRADE_5 = "Grade 5"
    GRADE_6 = "Grade 6"
    GRADE_7 = "Grade 7"
    GRADE_8 = "Grade 8"
    GRADE_9 = "Grade 9"
    GRADE_10 = "Grade 10"
    GRADE_11 = "Grade 11"
    GRADE_12 = "Grade 12"
    IB_DP_1 = "IB Diploma Y1"
    IB_DP_2 = "IB Diploma Y2"

    # Tertiary
    POLYTECHNIC = "Polytechnic"
    UNIVERSITY = "University"

    GENERAL = "General" # For everything else

class Listing(BaseModel):
    id: Annotated[str, Field(description="Internal ID")]
    source_id: Annotated[str | None, Field(description="External ID (if any)")] = None
    agency_name: Annotated[str, Field(description="Tuition Agency Name")]

    subject: Annotated[list[BandedSubject], Field(description="Each subject refers to a specific syllabus, with the band (if any), but without the level. e.g. G2 Mathematics")]
    acad_level: Annotated[AcademicLevel, Field(description="e.g. P3, Sec 3, J2")]
    location: Annotated[str | None, Field(description="Human Readable Address / Rough Area")] = None

    rate_pt_min: Annotated[int | None, Field(description="Min Part-Time Pay")] = None
    rate_pt_max: Annotated[int | None, Field(description="Max Part-Time Pay")] = None
    rate_ft_min: Annotated[int | None, Field(description="Min Full-Time Pay")] = None
    rate_ft_max: Annotated[int | None, Field(description="Max Full-Time Pay")] = None
    rate_ex_moe_min: Annotated[int | None, Field(description="Min Ex-MOE Pay")] = None
    rate_ex_moe_max: Annotated[int | None, Field(description="Max Ex-MOE Pay")] = None
    rate_cur_moe_min: Annotated[int | None, Field(description="Min Current MOE Pay")] = None
    rate_cur_moe_max: Annotated[int | None, Field(description="Max Current MOE Pay")] = None
    rate_general_min: Annotated[int | None, Field(description="Min General Pay (Did not specify type)")] = None
    rate_general_max: Annotated[int | None, Field(description="Max General Pay (Did not specify type)")] = None

    schedule: Annotated[str, Field(description="e.g. Once a week")] = ""

    description: Annotated[str, Field(description="Additional information")] = ""
    source_url: Annotated[HttpUrl, Field(description="URL to redirect to agency site")]

    @model_validator(mode="after")
    def check_rate_pairs(self) -> Self:
        """Checks that rates are all or nothing (contains either both min-max or none)"""
        pairs = (
            (self.rate_pt_min, self.rate_pt_max, "Part-Time"),
            (self.rate_ft_min, self.rate_ft_max, "Full-Time"),
            (self.rate_ex_moe_min, self.rate_ex_moe_max, "Ex-MOE"),
            (self.rate_cur_moe_max, self.rate_cur_moe_max, "Current MOE"),
            (self.rate_general_min, self.rate_general_max, "General"),
        )
        for min_rate, max_rate, rate_type in pairs:
            if (min_rate is None) != (max_rate is None):
                raise ValueError(f"Data integrity error: {rate_type} rate are incomplete (only min / max exist)")
        return self

