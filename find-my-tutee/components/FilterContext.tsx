// components/FilterContext.tsx
"use client";
import { createContext, useContext } from "react";
import type { TagState } from "./TagDrawer";

type FilterContextValue = {
  onFilterApply: (catToTags: Record<string, TagState>) => void;
};

const FilterContext = createContext<FilterContextValue | null>(null);

export function FilterProvider({
  children,
  onFilterApply,
}: {
  children: React.ReactNode;
  onFilterApply: (catToTags: Record<string, TagState>) => void;
}) {
  return (
    <FilterContext.Provider value={{ onFilterApply }}>
      {children}
    </FilterContext.Provider>
  );
}

export function useFilterContext() {
  const ctx = useContext(FilterContext);
  if (!ctx) {
    throw new Error("useFilterContext must be used within a FilterProvider");
  }
  return ctx;
}
