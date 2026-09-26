"use server";
import { pool } from "@/config/db";
import { Listing, ListingSchema } from "@/lib/schemas/listing";
import { z } from "zod";

export interface FilterParams {
  levels?: string[];
  bands?: string[];
  subjects?: string[];
  page?: number;
  limit?: number;
}

export async function getListings(filters: FilterParams): Promise<Listing[]> {
  const page = filters.page || 1;
  const limit = filters.limit || 20;
  const offset = (page - 1) * limit;

  // Base condition (AND across conditions)
  const conditions: string[] = [];
  const values: (string | number | string[])[] = [];

  // 1. levels filter (OR within array)
  if (filters.levels && filters.levels.length > 0) {
    values.push(filters.levels);
    conditions.push(`level = ANY($${values.length})`);
  }

  // 2. Bands filter (OR within array)
  if (filters.bands && filters.bands.length > 0) {
    values.push(filters.bands);
    conditions.push(`band = ANY($${values.length})`);
  }

  // 3. Subjects filter (OR within array)
  if (filters.subjects && filters.subjects.length > 0) {
    values.push(filters.subjects);
    conditions.push(`subject = ANY($${values.length})`);
  }

  // Add pagination limits
  values.push(limit, offset);
  const limitIndex = values.length - 1;
  const offsetIndex = values.length;
  const whereClause =
    conditions.length > 0 ? `WHERE ${conditions.join(" AND ")}` : "";

  const queryText = `
    SELECT 
      id,
      source_id AS "sourceId",
      agency_name AS "agencyName",
      location,
      rate_pt_min::float AS "ratePtMin",
      rate_pt_max::float AS "ratePtMax",
      rate_ft_min::float AS "rateFtMin",
      rate_ft_max::float AS "rateFtMax",
      rate_ex_moe_min::float AS "rateExMoeMin",
      rate_ex_moe_max::float AS "rateExMoeMax",
      rate_cur_moe_min::float AS "rateCurMoeMin",
      rate_cur_moe_max::float AS "rateCurMoeMax",
      rate_general_min::float AS "rateGeneralMin",
      rate_general_max::float AS "rateGeneralMax",
      schedule,
      description,
      source_url AS "sourceUrl",
      level AS "acadLevel",
      subject,
      band
    FROM listings
    ${whereClause}
    LIMIT $${limitIndex} OFFSET $${offsetIndex}
  `;

  const { rows } = await pool.query(queryText, values);
  return z.array(ListingSchema).parse(rows);
}
