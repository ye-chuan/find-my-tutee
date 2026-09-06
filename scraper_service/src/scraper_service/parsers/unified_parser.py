from dataclasses import dataclass
import re
import logging

from typing import Callable

from scraper_service.models import subject
from scraper_service.models.listing import Listing
from scraper_service.parsers.field_parsers import extract_acad_levels, extract_bandedsubjects

logger = logging.getLogger(__name__)

@dataclass
class RawListingDTO():
    """DTO to be passed into the unified parser which will then parse this DTO into an actual Listing object

    Attributes:
        agency_name (str): Unique name of the tuition agency
        source_url (list[str]): List of components that makes up the source url of the listing
            (e.g. ["https://example.com/", "/listing/394"]) The trailing and leading `/` can be omitted (e.g. ["example.com", "listing/3"] or ["example.com", "listing/4"]) all work
        subject (str): Raw string containing subject and band (e.g. "G2 Elementary Mathematics", "Sec 3 G2 E-Math")
        acad_level (str): Raw string containing academic level (e.g. "Sec 3 E-Math", "Primary 2", "J2 Econs 2x a week")
        rate_string (str | None): Raw string containing the various rates (e.g. "Fees: $3000/month Graduate/ Full Time tutors", "Part-Time  ($25-35/h)<br>Full-Time  ($40-45/h)")

        location (str): **Exact string** containing address
        source_id (str): Exact External ID of the listing from the source (if any)
        schedule (str): Exact string of lesson frequency (e.g. "2x/wk 2h", "Monday, Tuesday or Saturday")
        description (str): Exact string of listing description
    """
    agency_name: str
    source_url: list[str]

    subject: str
    acad_level: str

    rate_string: str | None = None

    location: str = ""
    source_id: str = ""
    schedule: str = ""
    description: str = ""

def unifiedParser(rawListing: RawListingDTO) -> Listing | None:
    """Unified parser capable of parsing raw string (in the Singapore context) from various agencies into the Listing object

    Returns:
        Listing - If Listing can be created
        None - If Listing cannot be created (e.g. due to malformed/missing inputs)
    """
    
    # Exact strings
    agency_name = rawListing.agency_name.strip()
    location = rawListing.location.strip()
    source_id = rawListing.source_id.strip()
    schedule = rawListing.schedule.strip()
    description = rawListing.description.strip()
    source_url = rawListing.source_url.strip()

    # Academic Level
    acad_levels = extract_acad_levels(rawListing.acad_level)
    if len(acad_levels) > 1:
        logging.info("Rejected listing due to having multiple academic levels")
        return None
    acad_level = acad_levels.pop()

    # Subject
    bandedsubjects = extract_bandedsubjects(rawListing.subject)

    # id
    internal_id = f"{agency_name}-{source_id}"
    if not source_id:
        # TODO: After having all other info
        internal_id = f"{agency_name}"

    return Listing(
        id=internal_id,
        source_id=source_id,
        agency_name=agency_name,
        subject=bandedsubjects,
        acad_level=acad_level,
        location=location,
    )

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.debug("Logging test in __main__")
