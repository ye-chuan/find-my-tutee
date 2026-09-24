"use client";

import { Listing } from "@/lib/schemas/listing";
import { ListingCard } from "./ListingCard";
import { useState } from "react";
import { NavBar } from "./NavBar";
import { FilterParams, getListings } from "@/actions/getListings";

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

  async function handleNext() {
    const nextPage = page + 1;
    const nextListings = await getListings({
      page: nextPage,
      limit: limit,
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
    });
    setListings(prevListings);
  }

  // Finish up this function and pass it down to the TagDrawerClient theough NavBar to use function upon close
  async function handleFilter(filters: FilterParams) {
    const filteredListings = await getListings({
      page: 1,
      limit: limit,
      subjects: filters.subjects,
      bands: filters.bands,
      levels: filters.levels,
    });
    setListings(filteredListings);
  }

  return (
    <div className="flex flex-col">
      <div className="flex flex-wrap justify-center gap-2">
        {listings.map((listing) => (
          <ListingCard details={listing} key={listing.id} />
        ))}
      </div>
      <div className="p-6">
        <NavBar onNext={handleNext} onPrev={handlePrev} children={children} />
      </div>
    </div>
  );
}
