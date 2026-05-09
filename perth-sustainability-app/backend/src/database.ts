import { Pool, QueryResult } from "pg";

let pool: Pool;

export function initDatabase() {
  pool = new Pool({
    host: process.env.DB_HOST || "localhost",
    port: parseInt(process.env.DB_PORT || "5432"),
    database: process.env.DB_NAME || "sustainability",
    user: process.env.DB_USER || "postgres",
    password: process.env.DB_PASSWORD || "postgres",
    max: 20,
    idleTimeoutMillis: 30000,
    connectionTimeoutMillis: 2000,
  });

  pool.on("error", (err) => {
    console.error("Unexpected database error:", err);
  });

  return pool;
}

export async function createTables() {
  const client = await pool.connect();
  try {
    await client.query(`
      CREATE TABLE IF NOT EXISTS households (
        id SERIAL PRIMARY KEY,
        name VARCHAR(120) NOT NULL,
        members INTEGER NOT NULL,
        postcode VARCHAR(10) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );

      CREATE TABLE IF NOT EXISTS usage_entries (
        id SERIAL PRIMARY KEY,
        household_id INTEGER NOT NULL,
        entry_type VARCHAR(20) NOT NULL CHECK(entry_type IN ('water', 'energy')),
        value DECIMAL(10, 2) NOT NULL,
        recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (household_id) REFERENCES households (id) ON DELETE CASCADE
      );

      CREATE INDEX IF NOT EXISTS idx_usage_household 
        ON usage_entries(household_id);
      CREATE INDEX IF NOT EXISTS idx_usage_date 
        ON usage_entries(recorded_at);
    `);
    console.log("Database tables created successfully");
  } catch (error) {
    console.error("Error creating tables:", error);
    throw error;
  } finally {
    client.release();
  }
}

export function getPool(): Pool {
  if (!pool) {
    throw new Error("Database not initialized. Call initDatabase() first.");
  }
  return pool;
}

export async function closeDatabase() {
  if (pool) {
    await pool.end();
  }
}

export interface Household {
  id: number;
  name: string;
  postcode: string;
  members: number;
  created_at: string;
}

export interface UsageEntry {
  id: number;
  household_id: number;
  entry_type: "water" | "energy";
  value: number;
  recorded_at: string;
}
