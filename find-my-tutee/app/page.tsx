import { ListingCard } from "@/components/ListingCard";
import { Listing } from "@/lib/schemas/listing";
import { TagDrawer } from "@/components/TagDrawer";
import { getTags } from "../actions/getTags";
import { ListingBoard } from "@/components/ListingBoard";

const tagMap = new Map<string, string[]>();
tagMap.set("levels", await getTags("level", "alllevels"));
tagMap.set("bands", await getTags("band", "allbands"));
tagMap.set("subjects", await getTags("subject", "allsubjects"));
//console.log(tagMap);

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
        <ListingBoard />
      </div>
    </div>
  );
}
