import "dotenv/config";
import { Pool } from "pg";

// Reuse the pool instance in development to prevent connection leaks during HMR
const globalForDb = globalThis as unknown as { pool: Pool };
export const pool =
  globalForDb.pool ||
  new Pool({
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    host: process.env.DB_HOST,
    port: Number(process.env.DB_PORT),
    database: process.env.DB_NAME,
  });

if (process.env.NODE_ENV !== "production") {
  globalForDb.pool = pool;
}

// Example query
// async function testConnection() {
//   try {
//     const res = await pool.query("SELECT NOW()");
//     const table = await pool.query("SELECT * FROM employees");
//     const query = await pool.query(
//       "SELECT pid, application_name, backend_start, query FROM pg_stat_activity WHERE state = 'active';",
//     );
//     console.log("Connected successfully! Server time:", res.rows[0].now);
//     //console.log(table.rows);
//     //console.log(query.rows);
//     // await pool.end();
//   } catch (err) {
//     if (err instanceof Error) {
//       console.error("Database connection error:", err.message);
//     }
//   }
// }

// testConnection();
