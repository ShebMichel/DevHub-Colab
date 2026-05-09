import { Pool } from "pg";
import { subDays } from "date-fns";

const BIN_SCHEDULES: Record<string, { general: string; recycling: string }> = {
  "6000": { general: "Monday", recycling: "Wednesday" },
  "6001": { general: "Tuesday", recycling: "Thursday" },
  "6002": { general: "Wednesday", recycling: "Friday" },
  "6003": { general: "Thursday", recycling: "Monday" },
  default: { general: "Friday", recycling: "Tuesday" },
};

export function getBinSchedule(postcode: string) {
  const prefix = postcode.replace(/\s/g, "").substring(0, 4);
  return BIN_SCHEDULES[prefix] || BIN_SCHEDULES["default"];
}

export async function computeGreenScore(
  pool: Pool,
  householdId: number
): Promise<number> {
  const thirtyDaysAgo = subDays(new Date(), 30);

  const result = await pool.query(
    `SELECT entry_type, value, recorded_at
     FROM usage_entries
     WHERE household_id = $1 AND recorded_at >= $2
     ORDER BY recorded_at`,
    [householdId, thirtyDaysAgo]
  );

  const entries = result.rows;

  if (entries.length === 0) {
    return 50;
  }

  const waterBaseline = 200.0;
  const energyBaseline = 20.0;

  // Group by date and calculate averages
  const dailyData: Record<string, { water: number[]; energy: number[] }> = {};

  entries.forEach((entry: any) => {
    const date = entry.recorded_at.toISOString().split("T")[0];
    if (!dailyData[date]) {
      dailyData[date] = { water: [], energy: [] };
    }
    if (entry.entry_type === "water") {
      dailyData[date].water.push(parseFloat(entry.value));
    } else if (entry.entry_type === "energy") {
      dailyData[date].energy.push(parseFloat(entry.value));
    }
  });

  const waterDailyTotals: number[] = [];
  const energyDailyTotals: number[] = [];

  Object.values(dailyData).forEach((day) => {
    if (day.water.length > 0) {
      waterDailyTotals.push(day.water.reduce((a, b) => a + b, 0));
    }
    if (day.energy.length > 0) {
      energyDailyTotals.push(day.energy.reduce((a, b) => a + b, 0));
    }
  });

  let waterScore = 50;
  let energyScore = 50;

  if (waterDailyTotals.length > 0) {
    const avgWater =
      waterDailyTotals.reduce((a, b) => a + b, 0) / waterDailyTotals.length;
    waterScore = Math.max(
      0,
      Math.min(100, (1 - avgWater / waterBaseline) * 100 + 50)
    );
  }

  if (energyDailyTotals.length > 0) {
    const avgEnergy =
      energyDailyTotals.reduce((a, b) => a + b, 0) / energyDailyTotals.length;
    energyScore = Math.max(
      0,
      Math.min(100, (1 - avgEnergy / energyBaseline) * 100 + 50)
    );
  }

  return Math.round(0.5 * energyScore + 0.5 * waterScore);
}

export function generateTips(greenScore: number, postcode: string): string[] {
  const tips: string[] = [];

  if (greenScore < 30) {
    tips.push(
      "Your score is low — consider an energy audit and reduce standby power (unplug chargers and unused devices)."
    );
    tips.push(
      "Install low-flow shower heads and check for leaks to reduce water usage."
    );
  } else if (greenScore < 60) {
    tips.push(
      "Good start — replace old incandescent bulbs with LED and run full loads in washing/dishwasher."
    );
    tips.push(
      "Track shower times and set a family challenge to save water each week."
    );
  } else {
    tips.push(
      "Great job! Keep monitoring and consider solar panels or a rainwater tank for further gains."
    );
    tips.push(
      "Share your habits with neighbours and start a community swap or tool library."
    );
  }

  const schedule = getBinSchedule(postcode);
  tips.push(
    `General waste day: ${schedule.general}. Recycling day: ${schedule.recycling}.`
  );

  return tips;
}
