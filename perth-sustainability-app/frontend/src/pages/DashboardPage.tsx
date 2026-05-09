import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { householdApi, usageApi, DashboardData } from "../api/client";
import {
  LineChart,
  Line,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import { ArrowLeft, Award, Download, Plus, Trash } from "lucide-react";
import { getScoreColor } from "../utils/helpers";

function DashboardPage() {
  const { id } = useParams<{ id: string }>();
  const [data, setData] = useState<DashboardData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadDashboard();
  }, [id]);

  const loadDashboard = async () => {
    try {
      const response = await householdApi.getById(Number(id));
      setData(response.data);
    } catch (error) {
      console.error("Failed to load dashboard:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleExport = async () => {
    try {
      const response = await usageApi.exportCsv(Number(id));
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", `usage_${id}.csv`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error("Export failed:", error);
    }
  };

  const handleDelete = async (entryId: number) => {
    try {
      await usageApi.delete(entryId);
      loadDashboard();
    } catch (error) {
      console.error("Delete failed:", error);
    }
  };

  if (loading) {
    return (
      <div>
        <div>Loading...</div>
      </div>
    );
  }

  if (!data) {
    return <div>Household not found</div>;
  }

  console.log(
    data.entries
      .filter((entry) => entry.entry_type === "water")
      .map((entry) => ({
        value: entry.value,
        date: entry.recorded_at,
      }))
  );

  const chartDataWater = data.entries
    .filter((entry) => entry.entry_type === "water")
    .map((entry) => ({
      value: entry.value,
      date: entry.recorded_at,
    }));

  const chartDataEnergy = data.entries
    .filter((entry) => entry.entry_type === "energy")
    .map((entry) => ({
      value: entry.value,
      date: entry.recorded_at,
    }));

  const chartData = [
    { name: "Water", Water: data.summary.water || 0, Energy: 0 },
    { name: "Energy", Water: 0, Energy: data.summary.energy || 0 },
  ];

  return (
    <div>
      <div>
        <div className="mb-4 md:mb-6">
          <Link
            to={`/`}
            className="flex items-center gap-2 text-base font-semibold text-gray-600 cursor-pointer md:text-lg hover:text-gray-800"
          >
            <ArrowLeft className="w-5 h-5 md:w-6 md:h-6" />
            Back to Home page
          </Link>
        </div>

        <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <strong className="text-xl">{data.household.name}</strong>
            <p className="text-gray-600">
              {data.household.members} member
              {data.household.members !== 1 && "s"}
            </p>
          </div>
          <div className="flex flex-col items-center gap-2 px-5 py-5 bg-white border border-gray-200 rounded-xl md:px-10">
            <div className="flex gap-3">
              <Award className="text-green-600" />
              <div className="text-gray-600">Green Score</div>
            </div>

            <div
              className={
                "text-4xl p-2 rounded-xl " + getScoreColor(data.greenScore)
              }
            >
              {data.greenScore}
            </div>
          </div>
        </div>
        <div className="grid grid-cols-1 gap-4 my-6 md:grid-cols-2">
          <div className="flex flex-col p-5 bg-blue-100 border-2 border-blue-200 rounded-lg">
            <div>
              <div>
                <h3 className="text-lg">💧 Total Water Usage</h3>
                <p className="mt-5 ml-1 text-4xl text-blue-500">
                  {data.summary.water?.toFixed(1) || 0} L
                </p>
              </div>
            </div>
            <p className="mt-2 ml-1 text-gray-600">This month</p>
          </div>
          <div className="flex flex-col p-5 bg-yellow-100 border-2 border-yellow-200 rounded-lg">
            <h3 className="text-lg">⚡ Total Energy</h3>
            <p className="mt-5 ml-1 text-4xl text-yellow-500">
              {data.summary.energy?.toFixed(1) || 0} kWh
            </p>
            <p className="mt-2 ml-1 text-gray-600">This month</p>
          </div>
        </div>
        <div className="grid grid-cols-1 gap-5 my-6 md:grid-cols-2">
          <div className="">
            <h3 className="mb-4 text-lg font-semibold">
              💧 Weekly Water Usage
            </h3>
            <ResponsiveContainer
              width="100%"
              height={400}
              className="pt-8 pr-8 bg-white border border-gray-300 rounded-lg"
            >
              <LineChart data={chartDataWater}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="week" />
                <YAxis domain={[500, "auto"]} />
                <Tooltip />
                <Legend />
                <Line
                  type="step"
                  dataKey="value"
                  name="Water (L)"
                  stroke="#3b82f6"
                  activeDot={{ r: 8 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
          <div className="">
            <h3 className="mb-4 text-lg font-semibold">
              ⚡ Weekly Energy Usage
            </h3>
            <ResponsiveContainer
              width="100%"
              height={400}
              className="pt-8 pr-8 bg-white border border-gray-300 rounded-lg"
            >
              <LineChart data={chartDataEnergy}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="week" />
                <YAxis domain={[400, "auto"]} />
                <Tooltip />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="value"
                  name="Energy (kWh)"
                  stroke="#facc15"
                  activeDot={{ r: 8 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      <div className="p-5 my-6 bg-green-100 border border-green-300 rounded-lg">
        <h2 className="text-lg font-semibold">💡 Personalized Tips</h2>
        <p className="mt-1 text-gray-600">
          Recommendations based on your usage patterns
        </p>
        <ul className="mt-4 space-y-3">
          {data.tips.map((tip, index) => (
            <li key={index} className="flex items-center gap-3">
              <span className="px-2 py-0.5 text-white bg-green-500 rounded-full">
                ✓
              </span>
              <span>{tip}</span>
            </li>
          ))}
        </ul>
      </div>

      <div className="p-5 bg-white border rounded-xl">
        <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <h2 className="text-lg font-semibold ">Recent Entries</h2>
            <p className="text-gray-600">Your latest usage record</p>
          </div>
          <div className="flex flex-col gap-3 sm:flex-row">
            <button
              onClick={handleExport}
              className="flex justify-center gap-2 p-2 border rounded-lg hover:bg-gray-50"
            >
              <Download />
              Export CSV
            </button>
            <Link
              to={`/household/${id}/add`}
              className="flex items-center justify-center gap-1 p-2 text-white bg-green-500 rounded-lg hover:bg-green-600"
            >
              <Plus />
              <div>Add Entry</div>
            </Link>
          </div>
        </div>

        {data.entries.length === 0 ? (
          <p className="mt-4 text-gray-600">No entries yet. Start tracking!</p>
        ) : (
          <div className="mt-6 overflow-x-auto">
            <table className="w-full border-collapse">
              <thead>
                <tr className="border-b border-gray-300">
                  <th className="px-4 py-3 text-sm font-semibold text-left text-gray-700">
                    Type
                  </th>
                  <th className="px-4 py-3 text-sm font-semibold text-left text-gray-700">
                    Value
                  </th>
                  <th className="px-4 py-3 text-sm font-semibold text-left text-gray-700">
                    Date
                  </th>
                  <th />
                </tr>
              </thead>
              <tbody>
                {data.entries.map((entry) => (
                  <tr
                    key={entry.id}
                    className="transition-colors border-b border-gray-200 hover:bg-gray-50"
                  >
                    <td className="px-4 py-3">
                      <span className="flex items-center gap-2 font-medium">
                        {entry.entry_type === "water"
                          ? "💧 Water"
                          : "⚡ Energy"}
                      </span>
                    </td>
                    <td className="px-4 py-3">
                      {entry.value} {entry.entry_type === "water" ? "L" : "kWh"}
                    </td>
                    <td className="px-4 py-3 text-sm text-gray-600">
                      {new Date(entry.recorded_at).toLocaleDateString()}{" "}
                    </td>
                    <td className="px-4 py-3 text-right">
                      <Trash
                        className="w-5 h-5 text-gray-700 cursor-pointer hover:text-red-800"
                        onClick={handleDelete.bind(null, entry.id)}
                      />
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
      <div className="flex items-center gap-2 mt-4 cursor-pointer md:mt-6">
        <ArrowLeft className="w-5 h-5 text-gray-600 md:w-6 md:h-6" />
        <Link
          to={`/`}
          className="text-base font-semibold text-gray-600 md:text-lg hover:text-gray-800"
        >
          Back to Home page
        </Link>
      </div>
    </div>
  );
}

export default DashboardPage;
