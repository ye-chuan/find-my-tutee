//"use client"
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardAction,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import { URLButton } from "@/components/URLButton";
import { TagLine } from "@/components/TagLine";
import { BookText, GraduationCap, House } from "lucide-react";
import { ListingDetails } from "@/components/ListingDetails";

interface ListingCardProps {
  details: ListingDetails;
}

export function ListingCard({ details }: ListingCardProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="wrap-anywhere">{details.subject}</CardTitle>
        <CardDescription>{details.agency}</CardDescription>
        <CardAction>
          <div>PT {details.pt}</div>
          <div>FT {details.ft}</div>
          <div>MOE {details.moe}</div>
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

        <div>{details.description}</div>
      </CardContent>
      <CardFooter>
        <TagLine />
      </CardFooter>
      <URLButton url={details.url}></URLButton>
    </Card>
  );
}
