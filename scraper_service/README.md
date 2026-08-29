# Scraper Service
Meant to be used with AWS Lambda.

## 4-Stage Pipeline
1. External Data Source
    - In JSON / HTML webscraped
2. Source Boundary Model
    - Applicable to only to JSON responses from external sources
    - A Pydantic model is used to validate the shape of external data at the boundary
    - Web scrapped data is converted from *External Data Source* over to the *RawListingDTO*
3. RawListingDTO
    - A *source adapter* function is used to convert the *Source Boundary Model* to this *RawListingDTO*
    - This is an intermediate object used solely to be passed to the *unified parser*
    - Consists mainly of raw unnormalised strings and values (e.g. "Primary 3 Math", "G2 e-math")
4. Unified Listing Model
    - The *unified parser* takes in a *RawListingDTO* and parses the raw strings into a highly structured *Unified Listing Model* that is then used interally throughout the system

So why this 4-step pipeline instead of the following 3 steps:
External Data Source -> Source Boundary Model -> Unified Listing Model

This is because every source requires a *Source Boundary Model*, and also an adapter to convert source model directly into the *Unified Listing Model*.

However this will result in a repeat of common parsing logic used for every site.
For instance,
- every site will need to have logic to treat "Secondary 4" and "Sec 4" the same and use the same regex expression

This also concentrate the complexity of handling multiple subjects / odd cases all in one place (the *unified parser*).
For instance,
- "Primary 5 Math and Science" would be broken into "Multiple Subjects" with tags "math" and "science", this logic should not need to be repeated for every external source

