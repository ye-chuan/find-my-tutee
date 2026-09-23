import { pool } from "@/config/db";

export async function getTags(db: string, col: string): Promise<string[]> {
  const queryText = `
    SELECT ${db}
    FROM ${col};
  `;

  try {
    const { rows } = await pool.query<Record<string, string>>(queryText);
    // Dynamically access key matching the db parameter name
    return rows.map((row) => row[db]);
  } catch (error) {
    console.error("Error fetching subjects:", error);
    throw error;
  }
}
