import { Card, CardHeader, CardTitle, CardDescription, CardAction, CardContent, CardFooter } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { TagLine } from "@/components/TagLine"
import { BookText, GraduationCap, House } from "lucide-react"

interface ListingCardProps {
  subject: string;
  agency: string;
}

export function ListingCard({ subject, agency }: ListingCardProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="wrap-anywhere">{subject}</CardTitle>
        <CardDescription>{agency}</CardDescription>
        <CardAction>
          <div>PT $25 - $50</div>
          <div>FT $25 - $50</div>
          <div>MOE $25 - $50</div>
        </CardAction>
      </CardHeader>
      <CardContent className="flex flex-col gap-4">
        <div>
          <div className="flex items-center gap-2">
            <BookText className="w-4" />
            H2 Mathematics
          </div>
          <div className="flex items-center gap-2">
            <GraduationCap className="w-4" />
            JC 2
          </div>
          <div className="flex items-center gap-2">
            <House className="w-4" />
            322 Hougang Ave 8
          </div>
        </div>

        <div>
          Student struggles with trigonometry. Easily distracted.
        </div>
      </CardContent>
      <CardFooter>
        <TagLine />
      </CardFooter>
      <Button>Apply</Button>
    </Card>
  )
}
