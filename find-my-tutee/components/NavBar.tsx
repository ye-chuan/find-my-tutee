import { Button } from "@/components/ui/button";
interface NavBarProps {
  onNext: () => Promise<void>;
  onPrev: () => Promise<void>;
  children: React.ReactNode;
}

export function NavBar({ onNext, onPrev, children }: NavBarProps) {
  return (
    <div className="flex flex-wrap justify-center gap-2 md:flex-row">
      <Button variant="outline" onClick={onPrev}>
        Prev
      </Button>
      {children}
      <Button variant="outline" onClick={onNext}>
        Next
      </Button>
    </div>
  );
}
