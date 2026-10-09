"use client";

import { Listing } from "@/lib/schemas/listing";
import { ListingCard } from "./ListingCard";
import { useState } from "react";
import { NavBar } from "./NavBar";
import { FilterParams, getListings } from "@/actions/getListings";
import { FilterProvider } from "./FilterContext";
import type { TagState } from "./TagDrawer";
import { SearchBar } from "./SearchBar";

interface ListingBoardClientProps {
  initialListings: Listing[];
  limit: number;
  children: React.ReactNode;
}
export function ListingBoardClient({
  initialListings,
  limit,
  children,
}: ListingBoardClientProps) {
  const [page, setPage] = useState(1);
  const [listings, setListings] = useState(initialListings);
  const [currentFilters, setCurrentFilters] = useState<FilterParams>({});
  const [currentSearch, setCurrentSearch] = useState("");

  async function handleNext() {
    const nextPage = page + 1;
    const nextListings = await getListings({
      page: nextPage,
      limit: limit,
      subjects: currentFilters.subjects,
      bands: currentFilters.bands,
      levels: currentFilters.levels,
      search: currentSearch,
    });
    if (nextListings.length > 0) {
      setPage(nextPage);
      setListings(nextListings);
    }
  }

  async function handlePrev() {
    const prevPage = Math.max(1, page - 1);
    setPage(prevPage);
    const prevListings = await getListings({
      page: prevPage,
      limit: limit,
      subjects: currentFilters.subjects,
      bands: currentFilters.bands,
      levels: currentFilters.levels,
      search: currentSearch,
    });
    setListings(prevListings);
  }

  // Finish up this function and pass it down to the TagDrawerClient theough NavBar to use function upon close
  async function handleFilter(catToTags: Record<string, TagState>) {
    const filters = tagStateToFilterParams(catToTags);
    const filteredListings = await getListings({
      page: 1,
      limit: limit,
      subjects: filters.subjects,
      bands: filters.bands,
      levels: filters.levels,
      search: currentSearch,
    });
    setListings(filteredListings);
    setPage(1);
  }

  function tagStateToFilterParams(
    catToTags: Record<string, TagState>,
  ): FilterParams {
    const result: FilterParams = {};
    for (const [category, tags] of Object.entries(catToTags)) {
      const selected = Object.keys(tags).filter((tag) => tags[tag]);
      if (selected.length === 0) continue;
      const key = `${category}` as keyof FilterParams;
      (result[key] as string[]) = selected;
    }
    setCurrentFilters(result);
    return result;
  }

  async function onSearchBarEnter() {
    const currentListings = await getListings({
      page: 1,
      limit: limit,
      subjects: currentFilters.subjects,
      bands: currentFilters.bands,
      levels: currentFilters.levels,
      search: currentSearch,
    });
    setListings(currentListings);
  }

  return (
    <div className="flex flex-col">
      <div className="flex justify-center p-6">
        <SearchBar
          value={currentSearch}
          onValueChange={setCurrentSearch}
          onEnter={onSearchBarEnter}
          listingLength={listings.length}
        />
      </div>
      <div className="flex flex-wrap justify-center gap-2">
        {listings.map((listing) => (
          <ListingCard details={listing} key={listing.id} />
        ))}
      </div>
      <div className="p-6">
        <FilterProvider onFilterApply={handleFilter}>
          <NavBar onNext={handleNext} onPrev={handlePrev} children={children} />
        </FilterProvider>
      </div>
    </div>
  );
}
