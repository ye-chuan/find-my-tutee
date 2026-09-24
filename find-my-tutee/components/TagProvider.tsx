"use client";
import { createContext } from "react";
import { tagMap } from "@/app/page";
import { ListingBoard } from "./ListingBoard";

export const TagContext = createContext<Map<string, string[]>>(tagMap);
export function TagProvider({ children }: { children: React.ReactNode }) {
  return <TagContext.Provider value={tagMap}>{children}</TagContext.Provider>;
}
