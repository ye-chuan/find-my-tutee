"use client";
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";

type TagState = Record<string, boolean>;
interface TagGroupProps {
  category: string;
  tags: TagState;
  onTagToggle: (category: string, tag: string) => void;
}

export function TagGroup({ category, tags, onTagToggle }: TagGroupProps) {
  const tagsPressed: string[] = Object.keys(tags).filter((tag) => tags[tag]);
  return (
    <div className="group-data-[swipe-axis=x]/drawer-popup:size-full group-data-[swipe-axis=y]/drawer-popup:h-80 group-data-[swipe-axis=y]/drawer-popup:w-full">
      <ToggleGroup variant="outline" multiple value={tagsPressed}>
        <div className="flex flex-wrap gap-2">
          {Object.keys(tags).map((tag) => (
            <ToggleGroupItem
              key={tag}
              value={tag}
              onClick={() => onTagToggle(category, tag)}
            >
              {tag}
            </ToggleGroupItem>
          ))}
        </div>
      </ToggleGroup>
    </div>
  );
}
