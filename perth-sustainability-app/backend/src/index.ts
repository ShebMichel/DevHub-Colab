import express, { Request, Response } from "express";
import cors from "cors";
import dotenv from "dotenv";
import { initDatabase, createTables } from "./database";
import householdRoutes from "./routes/households";
import usageRoutes from "./routes/usage";
import { errorHandler } from "./middleware/errorHandler";

// Load environment variables
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Wait for database to be ready
async function waitForDatabase(maxRetries = 30, delay = 2000): Promise<void> {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const pool = initDatabase();
      await pool.query("SELECT 1");
      console.log("✓ Database connection established");
      return;
    } catch (error) {
      console.log(`Waiting for database... (attempt ${i + 1}/${maxRetries})`);
      await new Promise((resolve) => setTimeout(resolve, delay));
    }
  }
  throw new Error("Could not connect to database after maximum retries");
}

// Initialize database and start server
async function startServer() {
  try {
    // Wait for PostgreSQL to be ready
    await waitForDatabase();

    // Get database pool
    const pool = initDatabase();

    // Create tables if they don't exist
    await createTables();
    console.log("✓ Database tables ready");

    // Make pool available to routes
    app.locals.db = pool;

    // Routes
    app.use("/api/households", householdRoutes);
    app.use("/api/usage", usageRoutes);

    // Health check
    app.get("/health", async (req: Request, res: Response) => {
      try {
        await pool.query("SELECT 1");
        res.json({ status: "ok", timestamp: new Date().toISOString() });
      } catch (error) {
        res
          .status(503)
          .json({ status: "error", message: "Database unavailable" });
      }
    });

    // Error handling
    app.use(errorHandler);

    app.listen(PORT, () => {
      console.log(`✓ Backend server running on port ${PORT}`);
      console.log(`✓ Health check: http://localhost:${PORT}/health`);
      console.log(`✓ Environment: ${process.env.NODE_ENV}`);
    });
  } catch (error) {
    console.error("✗ Failed to start server:", error);
    process.exit(1);
  }
}

startServer();

export default app;
