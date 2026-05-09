import { Router, Request, Response } from "express";
import { Pool } from "pg";
import { parse } from "csv-parse/sync";
import { stringify } from "csv-stringify/sync";

const router = Router();

// POST add usage entry
router.post("/", async (req: Request, res: Response) => {
  const pool: Pool = req.app.locals.db;
  const { household_id, entry_type, value, recorded_at } = req.body;

  if (!household_id || !entry_type || value === undefined) {
    return res.status(400).json({ error: "Missing required fields" });
  }

  if (!["water", "energy"].includes(entry_type)) {
    return res
      .status(400)
      .json({ error: 'entry_type must be "water" or "energy"' });
  }

  try {
    const timestamp = recorded_at || new Date().toISOString();

    const result = await pool.query(
      `INSERT INTO usage_entries (household_id, entry_type, value, recorded_at)
       VALUES ($1, $2, $3, $4)
       RETURNING *`,
      [household_id, entry_type, parseFloat(value), timestamp]
    );

    res.status(201).json(result.rows[0]);
  } catch (error) {
    console.error("Error adding usage entry:", error);
    res.status(500).json({ error: "Failed to add usage entry" });
  }
});

// DELETE usage entry
router.delete("/:id", async (req: Request, res: Response) => {
  const pool: Pool = req.app.locals.db;
  const { id } = req.params;

  try {
    const result = await pool.query(
      "DELETE FROM usage_entries WHERE id = $1 RETURNING id",
      [id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({ error: "Entry not found" });
    }

    res.json({ message: "Entry deleted" });
  } catch (error) {
    console.error("Error deleting entry:", error);
    res.status(500).json({ error: "Failed to delete entry" });
  }
});

// GET export CSV for household
router.get("/export/:household_id", async (req: Request, res: Response) => {
  const pool: Pool = req.app.locals.db;
  const { household_id } = req.params;

  try {
    const result = await pool.query(
      `SELECT id, entry_type, value, recorded_at
       FROM usage_entries
       WHERE household_id = $1
       ORDER BY recorded_at`,
      [household_id]
    );

    const csv = stringify(result.rows, {
      header: true,
      columns: ["id", "entry_type", "value", "recorded_at"],
    });

    res.setHeader("Content-Type", "text/csv");
    res.setHeader(
      "Content-Disposition",
      `attachment; filename=usage_${household_id}.csv`
    );
    res.send(csv);
  } catch (error) {
    console.error("Error exporting CSV:", error);
    res.status(500).json({ error: "Failed to export CSV" });
  }
});

// POST import CSV for household
router.post("/import/:household_id", async (req: Request, res: Response) => {
  const pool: Pool = req.app.locals.db;
  const { household_id } = req.params;
  const { csv_data } = req.body;

  if (!csv_data) {
    return res.status(400).json({ error: "CSV data required" });
  }

  const client = await pool.connect();

  try {
    const records = parse(csv_data, {
      columns: true,
      skip_empty_lines: true,
    });

    await client.query("BEGIN");

    for (const row of records) {
      const timestamp = row.recorded_at || new Date().toISOString();
      await client.query(
        `INSERT INTO usage_entries (household_id, entry_type, value, recorded_at)
         VALUES ($1, $2, $3, $4)`,
        [household_id, row.entry_type, parseFloat(row.value), timestamp]
      );
    }

    await client.query("COMMIT");

    res.json({ message: "Import successful", count: records.length });
  } catch (error: any) {
    await client.query("ROLLBACK");
    console.error("Error importing CSV:", error);
    res.status(400).json({ error: `Import failed: ${error.message}` });
  } finally {
    client.release();
  }
});

export default router;
