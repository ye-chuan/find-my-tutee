# Model for response of `https://smiletutor-carlos.appspot.com/public/v2/tuition_assignments/0`

from typing import Annotated
from pydantic import BaseModel, Field, HttpUrl

from scraper_service.models.listing import Listing

import sys
print(sys.path)

class SmileTutorRawListing(BaseModel):
    job_id: Annotated[str, Field(description="External system's display ID (e.g. J1808BS)")]
    address: Annotated[str, Field(description="Raw address string")]
    assignment_details: Annotated[str, Field(description="Full text description of the assignment")]
    tutor_gender: Annotated[str, Field(description="Preferred gender of the tutor")]
    level: Annotated[str, Field(description="Broad category like 'Primary'")]
    tutor_category: Annotated[str, Field(description="Comma-separated internal categories")]
    tutor_category_label: Annotated[str, Field(description="Comma-separated display labels for tutor categories")]
    looking_for: Annotated[str, Field(description="HTML formatted string containing rates and roles")]
    level_subjects: Annotated[str, Field(description="Subject and level (e.g. 'P3 Chinese')")]
    apply: Annotated[str, Field(description="Frequency and duration (e.g. '2x/wk 2h')")]
    urgent: Annotated[bool, Field(description="Whether the job is marked urgent")]
    job_url: Annotated[str, Field(description="Relative path to the job listing page")]

class SmileTutorAPIResponse(BaseModel):
    data: Annotated[list[SmileTutorRawListing], Field(description="List of raw listings returned by the API")]

def urlCombine(base: str, path: str) -> str:
    """Simply make sure there is only 1 slash in between `base` and `path`"""
    return base.rstrip("/") + "/" + path.lstrip("/")

def smiletutorToListing(rawListing: SmileTutorRawListing) -> Listing | None:
    agency_name = "smiletutor"
    agency_url_root = "https://smiletutor.sg"
    listing = Listing(
        id=f"{agency_name}-{rawListing.job_id}",
        source_id=rawListing.job_id,
        agency_name=agency_name,
        subject=rawListing.level_subjects,
        acad_level=rawListing.level,
        location=rawListing.address,
        schedule=rawListing.apply,
        description=rawListing.assignment_details,
        source_url=HttpUrl(urlCombine(agency_url_root, rawListing.job_url))
    )
    return listing

