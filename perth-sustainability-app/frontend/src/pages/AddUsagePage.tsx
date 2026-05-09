import { useState } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import { usageApi } from "../api/client";
import { ArrowLeft, Droplet, Zap } from "lucide-react";

function AddUsagePage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    entry_type: "water" as "water" | "energy",
    value: "",
    recorded_at: "",
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      await usageApi.create({
        household_id: Number(id),
        entry_type: formData.entry_type,
        value: parseFloat(formData.value),
        recorded_at: formData.recorded_at || undefined,
      });
      navigate(`/household/${id}`);
    } catch (err: any) {
      setError(err.response?.data?.error || "Failed to add entry");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="px-4 md:px-0">
      <div className="mb-4 md:mb-6">
        <Link
          to={`/household/${id}`}
          className="flex items-center gap-2 text-base font-semibold text-gray-600 md:text-lg hover:text-gray-800"
        >
          <ArrowLeft className="w-5 h-5 md:w-6 md:h-6" />
          Back to Household
        </Link>
      </div>

      <div>
        <h1 className="text-xl font-bold md:text-2xl">Add Usage Entry</h1>
        <p className="mb-4 text-sm text-gray-600 md:mb-6 md:text-base">
          Enter the details of your water or energy usage below.
        </p>
        <form
          onSubmit={handleSubmit}
          className="w-full p-4 bg-white border rounded-lg shadow-md md:p-6 md:max-w-2xl lg:max-w-4xl"
        >
          {error && <div>{error}</div>}

          <div className="mb-4">
            <label htmlFor="entry_type" className="text-gray-800">
              Entry Type
            </label>
            <div className="grid grid-cols-1 gap-3 mt-2 md:grid-cols-2">
              <button
                onClick={(e) =>
                  setFormData({ ...formData, entry_type: "water" })
                }
                className={
                  formData.entry_type === "water"
                    ? "flex items-center justify-center w-full gap-3 p-2 border border-blue-400 rounded-lg bg-blue-50 shadow-md"
                    : "flex items-center justify-center w-full gap-3 p-2 border border-gray-300 rounded-lg bg-white"
                }
              >
                <Droplet className="text-blue-500" />
                <div>
                  <p
                    className={
                      "font-semibold " +
                      (formData.entry_type === "water"
                        ? "text-blue-600"
                        : "text-gray-800")
                    }
                  >
                    Water
                  </p>
                  <p className="text-gray-600">Litres</p>
                </div>
              </button>
              <button
                onClick={(e) =>
                  setFormData({ ...formData, entry_type: "energy" })
                }
                className={
                  formData.entry_type === "energy"
                    ? "flex items-center justify-center w-full gap-3 p-2 border border-yellow-400 rounded-lg bg-yellow-50 shadow-md"
                    : "flex items-center justify-center w-full gap-3 p-2 border border-gray-300 rounded-lg bg-white"
                }
              >
                <Zap
                  className={
                    formData.entry_type === "energy" ? "text-yellow-600" : ""
                  }
                />
                <div>
                  <p
                    className={
                      "font-semibold " +
                      (formData.entry_type === "energy"
                        ? "text-yellow-600"
                        : "text-gray-800")
                    }
                  >
                    Energy
                  </p>
                  <p className="text-gray-600">kWh</p>
                </div>
              </button>
            </div>
          </div>

          <div className="mb-4">
            <label htmlFor="value" className="block mb-1 text-gray-800">
              Value <span className="text-red-500">*</span>
            </label>
            <div className="relative">
              <input
                className="w-full px-3 py-2 pr-16 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:outline-none focus:border-transparent"
                type="number"
                id="value"
                step="0.01"
                required
                value={formData.value}
                onChange={(e) =>
                  setFormData({ ...formData, value: e.target.value || "" })
                }
                placeholder={
                  formData.entry_type === "water" ? "e.g., 150" : "e.g., 12.5"
                }
              />
              <span className="absolute font-medium text-gray-600 -translate-y-1/2 right-3 top-1/2">
                {formData.entry_type === "water" ? "L" : "kWh"}
              </span>
            </div>
          </div>

          <div>
            <label className="block mb-1 text-gray-800" htmlFor="recorded_at">
              Date & Time <span className="text-gray-600">(Optional)</span>
            </label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:outline-none focus:border-transparent"
              type="datetime-local"
              id="recorded_at"
              value={formData.recorded_at}
              onChange={(e) =>
                setFormData({ ...formData, recorded_at: e.target.value })
              }
            />
            <p className="mt-1 text-sm text-gray-600">
              Leave blank to use current date and time
            </p>
          </div>

          <div className="flex flex-col-reverse gap-3 pt-4 mt-6 border-t sm:flex-row sm:justify-end sm:gap-4">
            <button
              type="button"
              onClick={() => navigate(`/household/${id}`)}
              className="w-full px-4 py-2 font-semibold text-gray-700 transition-colors border border-gray-300 rounded-lg sm:w-auto hover:bg-gray-50"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="w-full px-4 py-2 font-semibold text-white transition-colors bg-blue-500 rounded-lg sm:w-auto hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed"
            >
              {loading ? "Adding..." : "Add Entry"}
            </button>
          </div>
        </form>
      </div>
      <div className="grid max-w-full grid-cols-1 gap-4 mt-6 mb-8 md:grid-cols-2 lg:gap-6 md:max-w-2xl lg:max-w-4xl">
        <div className="flex flex-col p-4 border border-blue-200 rounded-xl bg-blue-50 md:p-5">
          <div className="flex items-start gap-3 md:gap-4">
            <Droplet className="w-6 h-6 mt-1 text-blue-500 md:w-8 md:h-8" />
            <div>
              <h3 className="text-base font-semibold text-blue-900 md:text-lg">
                Water Usage
              </h3>
              <p className="text-xs text-blue-600 md:text-sm">
                Track consumption in litres. Average household uses 150-250L per
                person daily.
              </p>
            </div>
          </div>
        </div>
        <div className="flex flex-col p-4 border border-yellow-200 rounded-xl bg-yellow-50 md:p-5">
          <div className="flex items-start gap-3 md:gap-4">
            <Zap className="w-6 h-6 mt-1 text-yellow-600 md:w-8 md:h-8" />
            <div>
              <h3 className="text-base font-semibold text-yellow-900 md:text-lg">
                Energy Usage
              </h3>
              <p className="text-xs text-yellow-700 md:text-sm">
                Track consumption in kWh. Average household uses 8-10 kWh daily.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AddUsagePage;
