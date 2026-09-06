import { pool } from "@/config/db";

export async function getTags(db: string, col: string): Promise<string[]> {
  const queryText = `
    SELECT ${db}
    FROM ${col};
  `;

  try {
    const { rows } = await pool.query<{ subject: string }>(queryText);
    // Maps the result rows array to return a flat array of strings
    return rows.map((row) => row.subject);
  } catch (error) {
    console.error("Error fetching subjects:", error);
    throw error;
  }
}
