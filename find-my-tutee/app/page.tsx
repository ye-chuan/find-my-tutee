import { Button } from "@/components/ui/button";
import { ListingCard } from "@/components/ListingCard";
import { Listing } from "@/lib/schemas/listing";
import { TagDrawer } from "@/components/TagDrawer";
import { getTags } from "./actions/getTags";

const test: Listing = {
  id: "job_987654321",
  sourceId: "EXT-2026-89A",
  agencyName: "Apex Tuition Agency",
  subject:
    "A2 Mathematics B2 Mathematics C2 Mathematics D2 Mathematics E2 Mathematics",
  acadLevel: "Sec 3",
  location: "Bishan MRT / Ang Mo Kio Area",
  ratePtMin: 45,
  ratePtMax: 45,

  schedule: "Once a week, 1.5 hours (Saturdays 10:00 AM)",
  description:
    "Looking for an engaging tutor familiar with the latest syllabus.Looking for an engaging tutor familiar with the latest syllabus.Looking for an engaging tutor familiar with the latest syllabus.Looking for an engaging tutor familiar with the latest syllabus.Looking for an engaging tutor familiar with the latest syllabus.",
  sourceUrl: "https://apextuition.example.com/listings/job_987654321",
};

const test1: Listing = {
  id: "job_987654321",
  sourceId: "EXT-2026-89A",
  agencyName: "Apex Tuition Agency",
  subject: "G2 Mathematics",
  acadLevel: "Sec 3",
  location: "Bishan MRT / Ang Mo Kio Area",
  ratePtMin: undefined,
  ratePtMax: undefined,
  rateFtMin: 145,
  rateFtMax: 245,
  rateExMoeMin: undefined,
  rateExMoeMax: undefined,
  rateCurMoeMin: 145,
  rateCurMoeMax: 245,

  schedule: "Once a week, 1.5 hours (Saturdays 10:00 AM)",
  description:
    "Looking for an engaging tutor familiar with the latest syllabus.",
  sourceUrl: "https://apextuition.example.com/listings/job_987654321",
};
const tagMap = new Map<string, string[]>();
tagMap.set("levels", await getTags("level", "alllevels"));
tagMap.set("bands", await getTags("band", "allbands"));
tagMap.set("subjects", await getTags("subject", "allsubjects"));
console.log(tagMap);

export default function Page() {
  return (
    <div className="flex min-h-svh p-6">
      <div className="flex flex-col items-center gap-4">
        <div>
          <TagDrawer tagMap={tagMap} />
        </div>
        <div className="font-mono text-xs text-muted-foreground">
          (Press <kbd>d</kbd> to toggle dark mode)
        </div>
        <div className="flex flex-wrap justify-center gap-2">
          <ListingCard details={test} />
          <ListingCard details={test1} />
          <ListingCard details={test} />
          <ListingCard details={test} />
        </div>
      </div>
    </div>
  );
}
