import { Badge } from "@/components/ui/badge";
import { BookText, Globe } from "lucide-react";

export function TagLine() {
  return (
    <div className="flex gap-2">
      <Badge>
        <BookText data-icon="inline-start" />
        PT
      </Badge>
      <Badge>
        <Globe data-icon="inline-start" />
        EliteTutors
      </Badge>
    </div>
  );
}
