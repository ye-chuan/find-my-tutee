import { Search } from "lucide-react";

import {
  InputGroup,
  InputGroupAddon,
  InputGroupInput,
} from "@/components/ui/input-group";

interface SearchBarProps {
  value: string;
  onValueChange: (value: string) => void;
  onEnter: () => void;
  listingLength: number;
}

export function SearchBar({
  value,
  onValueChange,
  onEnter,
  listingLength,
}: SearchBarProps) {
  function handleSearch(e: React.KeyboardEvent<HTMLInputElement>) {
    if (e.key === "Enter") {
      onEnter();
    }
  }

  return (
    <InputGroup className="max-w-xs">
      <InputGroupInput
        value={value}
        onChange={(e) => onValueChange(e.target.value)}
        placeholder="Search..."
        onKeyDown={handleSearch}
      />
      <InputGroupAddon>
        <Search />
      </InputGroupAddon>
      <InputGroupAddon align="inline-end">
        {listingLength} results
      </InputGroupAddon>
    </InputGroup>
  );
}
