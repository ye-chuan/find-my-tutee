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
import { Listing } from "@/lib/schemas/listing";
import { MarqueeText } from "@/components/MarqueeText";

function RateDisplay({
  rateMin,
  rateMax,
  rateType,
}: {
  rateMin?: number;
  rateMax?: number;
  rateType: string;
}) {
  let text: string;
  if (rateMin === undefined || rateMax === undefined) {
    return null;
  }
  if (rateMin === rateMax) {
    text = rateMax.toString();
  } else {
    text = `${rateMin}-${rateMax}`;
  }
  return (
    <div>
      {rateType}
      {" $"}
      {text}
    </div>
  );
}

interface ListingCardProps {
  details: Listing;
}

export function ListingCard({ details }: ListingCardProps) {
  return (
    <Card className="w-110">
      <CardContent className="flex flex-col gap-4">
        <div className="flex flex-col">
          <div className="flex min-h-20 gap-x-8">
            <CardTitle className="overflow-hidden whitespace-nowrap">
              <MarqueeText text={details.subject} />
              <CardDescription>{details.agencyName}</CardDescription>
            </CardTitle>
            {/* <CardDescription>{details.agencyName}</CardDescription> */}

            <div className="ml-auto flex-none">
              <RateDisplay
                rateMin={details.ratePtMin}
                rateMax={details.ratePtMax}
                rateType="PT"
              />
              <RateDisplay
                rateMin={details.rateFtMin}
                rateMax={details.rateFtMax}
                rateType="FT"
              />
              <RateDisplay
                rateMin={details.rateExMoeMin}
                rateMax={details.rateExMoeMax}
                rateType="E-MOE"
              />
              <RateDisplay
                rateMin={details.rateCurMoeMin}
                rateMax={details.rateCurMoeMax}
                rateType="C-MOE"
              />
              <RateDisplay
                rateMin={details.rateGenMin}
                rateMax={details.rateGenMax}
                rateType=""
              />
            </div>
          </div>
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
        </div>
        <div className="grid h-18 [scrollbar-width:none] place-items-center overflow-auto">
          {details.description}
        </div>
      </CardContent>
      <CardFooter>
        <TagLine />
      </CardFooter>
      <URLButton url={details.sourceUrl}></URLButton>
    </Card>
  );
}
