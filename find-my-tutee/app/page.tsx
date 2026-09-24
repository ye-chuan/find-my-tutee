import { TagDrawer } from "@/components/TagDrawer";
import { getTags } from "../actions/getTags";
import { ListingBoard } from "@/components/ListingBoard";

export const tagMap = new Map<string, string[]>();
tagMap.set("levels", await getTags("level", "alllevels"));
tagMap.set("bands", await getTags("band", "allbands"));
tagMap.set("subjects", await getTags("subject", "allsubjects"));
//console.log(tagMap);

export default function Page() {
  return (
    <div className="flex min-h-svh justify-center p-6">
      <div className="flex flex-col items-center gap-4">
        <div className="font-mono text-xs text-muted-foreground">
          (Press <kbd>d</kbd> to toggle dark mode)
        </div>
        <ListingBoard children={<TagDrawer tagMap={tagMap} />} />
      </div>
    </div>
  );
}
