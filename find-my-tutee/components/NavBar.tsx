import { Button } from "@/components/ui/button";
interface NavBarProps {
  onNext: () => Promise<void>;
  onPrev: () => Promise<void>;
}

export function NavBar({ onNext, onPrev }: NavBarProps) {
  return (
    <div>
      <Button variant="outline" onClick={onPrev}>
        Prev
      </Button>
      <Button variant="outline" onClick={onNext}>
        Next
      </Button>
    </div>
  );
}
