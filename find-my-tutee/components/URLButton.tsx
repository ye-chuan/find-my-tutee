"use client";
import { Button } from "@/components/ui/button";

interface URLButtonProps {
  url: string;
}

export function URLButton({ url }: URLButtonProps) {
  return <Button onClick={() => window.open(url, "_blank")}>Apply</Button>;
}
