"use client";
import { useState } from "react";
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";

type TagState = Record<string, boolean>;
interface TagGroupProps {
  tags: string[];
}

export function TagGroup({ tags }: TagGroupProps) {
  const [selectedTags, setSelectedTags] = useState<TagState>({});

  const handleTag = (tag: string): void => {
    setSelectedTags((prev) => ({
      ...prev,
      [tag]: !prev[tag],
    }));
  };

  return (
    <div className="group-data-[swipe-axis=x]/drawer-popup:size-full group-data-[swipe-axis=y]/drawer-popup:h-80 group-data-[swipe-axis=y]/drawer-popup:w-full">
      <ToggleGroup variant="outline" multiple>
        <div className="flex flex-wrap gap-2">
          {tags.map((tag) => (
            <ToggleGroupItem
              key={tag}
              value={tag}
              onClick={() => handleTag(tag)}
            >
              {tag}
            </ToggleGroupItem>
          ))}
        </div>
      </ToggleGroup>
    </div>
  );
}
