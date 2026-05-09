import dotenv from "dotenv";
import { initDatabase, createTables, closeDatabase } from "./database";

dotenv.config();

async function migrate() {
  try {
    console.log("Starting database migration...");

    initDatabase();
    console.log("✓ Database connection established");

    await createTables();
    console.log("✓ Tables created successfully");

    await closeDatabase();
    console.log("✓ Migration completed successfully");

    process.exit(0);
  } catch (error) {
    console.error("✗ Migration failed:", error);
    process.exit(1);
  }
}

migrate();
