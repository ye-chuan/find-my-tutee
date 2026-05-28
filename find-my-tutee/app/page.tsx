import { Button } from "@/components/ui/button"

import { ListingCard } from "@/components/ListingCard"

export default function Page() {
  return (
    <div className="flex min-h-svh p-6">
      <div className="flex flex-col gap-4">
        <div>
          <h1 className="font-medium">Project ready!</h1>
          <p>You may now add components and start building.</p>
          <p>We&apos;ve already added the button component for you.</p>
          <Button className="mt-2">Button</Button>
        </div>
        <div className="font-mono text-xs text-muted-foreground">
          (Press <kbd>d</kbd> to toggle dark mode)
        </div>

        <div className="grid gap-4 grid-cols-1 md:grid-cols-2 xl:grid-cols-3">
          <ListingCard subject="Hi Geography Amazing" agency="Elite Tutors" />
          <ListingCard subject="hi" agency="Elite Tutors" />
          <ListingCard subject="hi" agency="Elite Tutors" />
          <ListingCard subject="hi" agency="Elite Tutors" />
        </div>

      </div>
    </div>
  )
}
