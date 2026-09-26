import { Button } from "@/components/ui/button";
import { ArrowLeftIcon, ArrowRightIcon } from "lucide-react";
interface NavBarProps {
  onNext: () => Promise<void>;
  onPrev: () => Promise<void>;
  children: React.ReactNode;
}

export function NavBar({ onNext, onPrev, children }: NavBarProps) {
  return (
    <div className="flex flex-wrap justify-center gap-2 md:flex-row">
      <Button variant="outline" onClick={onPrev}>
        <ArrowLeftIcon />
      </Button>
      {children}
      <Button variant="outline" onClick={onNext}>
        <ArrowRightIcon />
      </Button>
    </div>
  );
}
