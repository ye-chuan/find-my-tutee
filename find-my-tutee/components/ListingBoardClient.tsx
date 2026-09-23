"use client";

import { Listing } from "@/lib/schemas/listing";
import { ListingCard } from "./ListingCard";
import { useState } from "react";
import { NavBar } from "./NavBar";
import { getListings } from "@/actions/getListings";
interface ListingBoardClientProps {
  initialListings: Listing[];
  limit: number;
}
export function ListingBoardClient({
  initialListings,
  limit,
}: ListingBoardClientProps) {
  const [page, setPage] = useState(1);
  const [listings, setListings] = useState(initialListings);

  async function handleNext() {
    const nextPage = page + 1;
    setPage(nextPage);
    const nextListings = await getListings({
      page: nextPage,
      limit: limit,
    });
    setListings(nextListings);
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
  return (
    <div>
      <div className="flex flex-wrap justify-center gap-2">
        {listings.map((listing) => (
          <ListingCard details={listing} key={listing.id} />
        ))}
      </div>
      <NavBar onNext={handleNext} onPrev={handlePrev} />
    </div>
  );
}
