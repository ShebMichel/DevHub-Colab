import { Router, Request, Response } from "express";
import { Pool } from "pg";
import { computeGreenScore, generateTips } from "../services/greenScore";

const router = Router();

// GET all households
router.get("/", async (req: Request, res: Response) => {
  const pool: Pool = req.app.locals.db;
  try {
    const result = await pool.query(
      "SELECT * FROM households ORDER BY created_at DESC"
    );
    res.json({ households: result.rows });
  } catch (error) {
    console.error("Error fetching households:", error);
    res.status(500).json({ error: "Failed to fetch households" });
  }
});

// GET single household with dashboard data
router.get("/:id", async (req: Request, res: Response) => {
  const pool: Pool = req.app.locals.db;
  const { id } = req.params;

  try {
    const householdResult = await pool.query(
      "SELECT * FROM households WHERE id = $1",
      [id]
    );

    if (householdResult.rows.length === 0) {
      return res.status(404).json({ error: "Household not found" });
    }

    const household = householdResult.rows[0];

    const entriesResult = await pool.query(
      `SELECT * FROM usage_entries 
       WHERE household_id = $1 
       ORDER BY recorded_at DESC 
       LIMIT 50`,
      [id]
    );

    const summaryResult = await pool.query(
      `SELECT entry_type, SUM(value) as total
       FROM usage_entries
       WHERE household_id = $1
       GROUP BY entry_type`,
      [id]
    );

    const summary = summaryResult.rows.reduce((acc: any, row: any) => {
      acc[row.entry_type] = parseFloat(row.total);
      return acc;
    }, {});

    const greenScore = await computeGreenScore(pool, parseInt(id));
    const tips = generateTips(greenScore, household.postcode);

    res.json({
      household,
      entries: entriesResult.rows,
      summary,
      greenScore,
      tips,
    });
  } catch (error) {
    console.error("Error fetching household:", error);
    res.status(500).json({ error: "Failed to fetch household data" });
  }
});

// POST create household
router.post("/", async (req: Request, res: Response) => {
  const pool: Pool = req.app.locals.db;
  const { name, members, postcode } = req.body;

  if (!name || !postcode || !members) {
    return res
      .status(400)
      .json({ error: "Name, number of occupants, and postcode are required" });
  }

  try {
    const result = await pool.query(
      "INSERT INTO households (name, members, postcode) VALUES ($1, $2, $3) RETURNING *",
      [name, members, postcode]
    );

    res.status(201).json(result.rows[0]);
  } catch (error) {
    console.error("Error creating household:", error);
    res.status(500).json({ error: "Failed to create household" });
  }
});

// DELETE household
router.delete("/:id", async (req: Request, res: Response) => {
  const pool: Pool = req.app.locals.db;
  const { id } = req.params;

  try {
    const result = await pool.query(
      "DELETE FROM households WHERE id = $1 RETURNING id",
      [id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({ error: "Household not found" });
    }

    res.json({ message: "Household deleted" });
  } catch (error) {
    console.error("Error deleting household:", error);
    res.status(500).json({ error: "Failed to delete household" });
  }
});

export default router;
