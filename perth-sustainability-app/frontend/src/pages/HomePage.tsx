import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { householdApi, Household } from "../api/client";
import { Leaf, Zap, Droplet } from "lucide-react";
import { getScoreColor } from "../utils/helpers";

function HomePage() {
  const [householdsWithData, setHouseholdsWithData] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadHouseholds();
  }, []);

  const loadHouseholds = async () => {
    try {
      const response = await householdApi.getAll();
      const households = response.data.households;

      const householdsData = await Promise.all(
        households.map(async (household: Household) => {
          try {
            const data = await householdApi.getById(household.id);
            return { ...household, ...data.data };
          } catch {
            return household;
          }
        })
      );
      setHouseholdsWithData(householdsData);
    } catch (error) {
      console.error("Failed to load households:", error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div>
        <div>Loading...</div>
      </div>
    );
  }

  return (
    <div className="">
      <div className="flex flex-col items-center">
        <p className="text-center">
          Monitor your household's water and energy usage, get personalized
          tips, and track your environmental impact with our Green Score system.
        </p>
        <Link
          to="/register"
          className="inline-block px-3 py-2 mt-8 font-semibold text-white transition-all duration-200 bg-green-600 rounded-md hover:bg-green-500 active:scale-95"
        >
          Register Household
        </Link>
      </div>

      <div className="mt-8">
        <h2 className="font-semibold">Registered Households:</h2>

        {householdsWithData.length === 0 ? (
          <p>No households registered yet. Be the first to start tracking!</p>
        ) : (
          <div className="grid gap-4 mt-4 md:grid-cols-2 lg:grid-cols-3">
            {householdsWithData.map((household) => (
              <Link
                key={household.id}
                to={`/household/${household.id}`}
                className="block p-4 mt-4 transition duration-300 ease-in-out bg-white border border-gray-400 rounded-xl hover:shadow-lg"
              >
                <div className="flex items-center justify-between mb-8">
                  <div className="flex flex-col">
                    <strong>{household.name}</strong>
                    <span className="text-gray-600">
                      {household.members} member{household.members !== 1 && "s"}
                    </span>
                  </div>
                  <div
                    className={`flex gap-1 px-3 py-2 ${getScoreColor(
                      household.greenScore
                    )} rounded-xl`}
                  >
                    <Leaf />
                    <p className="font-semibold">{household.greenScore}</p>
                  </div>
                </div>
                <div className="text-gray-600">
                  <div className="flex justify-between">
                    <div className="flex items-center gap-1 mb-2">
                      <Droplet className="w-5 h-5 text-blue-600" />
                      <span>Water usage: </span>
                    </div>
                    <p>
                      {household.summary.water
                        ? `${household.summary.water} L/day`
                        : "No data"}
                    </p>
                  </div>
                  <div className="flex justify-between">
                    <div className="flex items-center gap-1">
                      <Zap className="w-5 h-5 text-yellow-500" />
                      <span>Energy usage:</span>
                    </div>
                    <p>
                      {household.summary.energy
                        ? `${household.summary.energy} kWh/day`
                        : "No data"}
                    </p>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default HomePage;
