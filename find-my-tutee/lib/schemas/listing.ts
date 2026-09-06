import { z } from "zod";

export const ListingSchema = z.object({
  // Identifiers
  id: z.string().describe("Internal ID"),
  sourceId: z.string().optional().describe("External ID (if any)"),
  agencyName: z.string().describe("Tuition Agency Name"),

  // Core Details
  subject: z
    .string()
    .describe(
      "Each subject refers to a specific syllabus, typically without the level. e.g. G2 Mathematics",
    ),
  acadLevel: z.string().describe("e.g. P3, Sec 3, J2"),
  location: z
    .string()
    .optional()
    .describe("Human Readable Address / Rough Area"),

  // Rates (Numeric Ranges)
  ratePtMin: z.number().int().optional().describe("Min Part-Time Pay"),
  ratePtMax: z.number().int().optional().describe("Max Part-Time Pay"),
  rateFtMin: z.number().int().optional().describe("Min Full-Time Pay"),
  rateFtMax: z.number().int().optional().describe("Max Full-Time Pay"),
  rateExMoeMin: z.number().int().optional().describe("Min Ex-MOE Pay"),
  rateExMoeMax: z.number().int().optional().describe("Max Ex-MOE Pay"),
  rateCurMoeMin: z.number().int().optional().describe("Min Cur-MOE Pay"),
  rateCurMoeMax: z.number().int().optional().describe("Max Cur-MOE Pay"),
  rateGenMin: z.number().int().optional().describe("Min Gen Pay"),
  rateGenMax: z.number().int().optional().describe("Max Gen Pay"),

  // Schedule, Description, & Link
  schedule: z.string().default("").describe("e.g. Once a week"),
  description: z.string().default("").describe("Additional information"),
  sourceUrl: z.string().url().describe("URL to redirect to agency site"),
});

export type Listing = z.infer<typeof ListingSchema>;
