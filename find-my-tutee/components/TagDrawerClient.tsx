"use client";
import { Button } from "@/components/ui/button";
import { TagCarousel } from "@/components/TagCarousel";
import { TagState } from "./TagDrawer";
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer";
import { useState } from "react";

// Lifting The State
export function TagDrawerClient({
  initialStateMap,
}: {
  initialStateMap: Record<string, TagState>;
}) {
  const [catToTags, setCatToTags] =
    useState<Record<string, TagState>>(initialStateMap);
  const handleTag = (category: string, tag: string): void => {
    setCatToTags((prev) => ({
      ...prev,
      [category]: {
        ...prev[category],
        [tag]: !prev[category]?.[tag],
      },
    }));
  };
  return (
    <Drawer showSwipeHandle>
      <DrawerTrigger render={<Button variant="destructive">FILTER</Button>} />
      <DrawerContent>
        <DrawerHeader>
          <DrawerTitle>Drawer</DrawerTitle>
          <DrawerDescription>Drawer with a swipe handle.</DrawerDescription>
        </DrawerHeader>
        <div className="mx-50">
          <TagCarousel catToTags={catToTags} onTagToggle={handleTag} />
        </div>
        <DrawerFooter>
          <DrawerClose render={<Button>Close</Button>} />
        </DrawerFooter>
      </DrawerContent>
    </Drawer>
  );
}
