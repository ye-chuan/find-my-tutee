import { Button } from "@/components/ui/button";
import { ListingDetails } from "@/components/ListingDetails";
import { ListingCard } from "@/components/ListingCard";

const test = new ListingDetails(
  "Math",
  "EliteTutors",
  "$25-$50",
  "$25-$50",
  "$25-$50",
  "https://www.elitetutor.sg/k17782-jc1-h2-economics-bishan-street-13-45-130-hour/",
);

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
          <ListingCard details={test} />
          <ListingCard details={test} />
          <ListingCard details={test} />
        </div>
      </div>
    </div>
  );
}
