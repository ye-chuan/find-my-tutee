"use client";
import { useState } from "react";

export function MarqueeText({ text }: { text: string }) {
  const [isHovered, setIsHovered] = useState(false);
  return (
    <div
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      className={`${isHovered ? "animate-marquee" : " "}`}
    >
      {text}
    </div>
  );
}
