import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel";
import { TagGroup } from "./TagGroup";
import type { TagState } from "@/components/TagDrawer";

interface TagCarouselProps {
  catToTags: Record<string, TagState>;
  onTagToggle: (category: string, tag: string) => void;
}
export function TagCarousel({ catToTags, onTagToggle }: TagCarouselProps) {
  return (
    <Carousel>
      <CarouselContent>
        {Object.entries(catToTags).map(([category, tags]) => (
          <CarouselItem key={category}>
            <TagGroup
              tags={tags}
              category={category}
              onTagToggle={onTagToggle}
            />
          </CarouselItem>
        ))}
      </CarouselContent>
      <CarouselPrevious />
      <CarouselNext />
    </Carousel>
  );
}
