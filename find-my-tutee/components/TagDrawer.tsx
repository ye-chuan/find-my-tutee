import { Button } from "@/components/ui/button";
import { TagCarousel } from "@/components/TagCarousel";

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

export function TagDrawer() {
  return (
    <Drawer showSwipeHandle>
      <DrawerTrigger render={<Button variant="destructive">FILTER</Button>} />
      <DrawerContent>
        <DrawerHeader>
          <DrawerTitle>Drawer</DrawerTitle>
          <DrawerDescription>Drawer with a swipe handle.</DrawerDescription>
        </DrawerHeader>
        <div className="mx-50">
          <TagCarousel />
        </div>
        <DrawerFooter>
          <DrawerClose render={<Button>Close</Button>} />
        </DrawerFooter>
      </DrawerContent>
    </Drawer>
  );
}
