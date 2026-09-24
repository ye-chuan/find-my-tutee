import { getListings } from "@/actions/getListings";
import { ListingBoardClient } from "./ListingBoardClient";

export async function ListingBoard({
  children,
}: {
  children: React.ReactNode;
}) {
  const limit = 9;
  const initialListings = await getListings({ page: 1, limit: limit });
  return (
    <ListingBoardClient
      initialListings={initialListings}
      limit={limit}
      children={children}
    />
  );
}
