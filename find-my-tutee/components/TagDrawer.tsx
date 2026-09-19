import { TagDrawerClient } from "./TagDrawerClient";

export type TagState = Record<string, boolean>;

export function TagDrawer({ tagMap }: { tagMap: Map<string, string[]> }) {
  const initialStateMap: Record<string, TagState> = {};
  for (const [category, tags] of tagMap) {
    const initialTags: TagState = {};
    tags.forEach((tag) => (initialTags[tag] = false));
    initialStateMap[category] = initialTags;
  }

  return <TagDrawerClient initialStateMap={initialStateMap} />;
}
