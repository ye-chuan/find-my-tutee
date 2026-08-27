import { Button } from "@/components/ui/button";
import { ListingCard } from "@/components/ListingCard";
import { Listing } from "@/lib/schemas/listing";

const test: Listing = {
  id: "job_987654321",
  sourceId: "EXT-2026-89A",
  agencyName: "Apex Tuition Agency",
  subject: "G2 Mathematics",
  acadLevel: "Sec 3",
  location: "Bishan MRT / Ang Mo Kio Area",
  ratePtMin: 45,
  ratePtMax: 45,

  schedule: "Once a week, 1.5 hours (Saturdays 10:00 AM)",
  description:
    "Looking for an engaging tutor familiar with the latest syllabus.",
  sourceUrl: "https://apextuition.example.com/listings/job_987654321",
};

const test1: Listing = {
  id: "job_987654321",
  sourceId: "EXT-2026-89A",
  agencyName: "Apex Tuition Agency",
  subject: "G2 Mathematics",
  acadLevel: "Sec 3",
  location: "Bishan MRT / Ang Mo Kio Area",
  ratePtMin: 45,
  ratePtMax: 45,
  rateFtMin: 45,
  rateFtMax: 45,
  rateExMoeMin: 45,
  rateExMoeMax: 45,
  rateCurMoeMin: 45,
  rateCurMoeMax: 45,

  schedule: "Once a week, 1.5 hours (Saturdays 10:00 AM)",
  description:
    "Looking for an engaging tutor familiar with the latest syllabus.Looking for an engaging tutor familiar with the latest syllabus.Looking for an engaging tutor familiar with the latest syllabus.Looking for an engaging tutor familiar with the latest syllabus.Looking for an engaging tutor familiar with the latest syllabus.v",
  sourceUrl: "https://apextuition.example.com/listings/job_987654321",
};

export default function Page() {
  return (
    <div className="flex min-h-svh p-6">
      <div className="flex flex-col items-center gap-4">
        <div>
          <h1 className="font-medium">Project ready!</h1>
          <p>You may now add components and start building.</p>
          <p>We&apos;ve already added the button component for you.</p>
          <Button className="mt-2">Button</Button>
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
