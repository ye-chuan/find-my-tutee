import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel";
import { TagGroup } from "./TagGroup";
import { getTags } from "@/app/actions/getTags";

const subjects = await getTags("subject", "allsubjects");
console.log(subjects);
export function TagCarousel() {
  return (
    <Carousel>
      <CarouselContent>
        <CarouselItem>
          <TagGroup tags={subjects} />
        </CarouselItem>
        <CarouselItem>
          <TagGroup tags={subjects} />
        </CarouselItem>
        <CarouselItem>
          <TagGroup tags={subjects} />
        </CarouselItem>
      </CarouselContent>
      <CarouselPrevious />
      <CarouselNext />
    </Carousel>
  );
}
