import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { householdApi } from "../api/client";
import { ArrowLeft } from "lucide-react";

function RegisterPage() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: "",
    members: 1,
    postcode: "",
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const response = await householdApi.create(formData);
      navigate(`/household/${response.data.id}`);
    } catch (err: any) {
      setError(err.response?.data?.error || "Failed to register household");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <div>
        <div className="mb-4 md:mb-6">
          <Link
            to={`/`}
            className="flex items-center gap-2 text-base font-semibold text-gray-600 md:text-lg hover:text-gray-800"
          >
            <ArrowLeft className="w-5 h-5 md:w-6 md:h-6" />
            Back to Home page
          </Link>
        </div>
        <h1 className="mb-6 text-2xl font-bold">Register Your Household</h1>
        <form
          onSubmit={handleSubmit}
          className="w-full max-w-md p-6 bg-white border border-gray-200 rounded-lg shadow-sm md:max-w-4xl"
        >
          {error && (
            <div className="p-3 mb-4 text-sm text-red-700 bg-red-100 border border-red-200 rounded-lg">
              {error}
            </div>
          )}

          <div className="mb-4">
            <label
              htmlFor="name"
              className="block mb-2 text-sm font-semibold text-gray-700"
            >
              Household Name
            </label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
              type="text"
              id="name"
              required
              value={formData.name}
              onChange={(e) =>
                setFormData({ ...formData, name: e.target.value })
              }
              placeholder="e.g., Smith Family"
            />
          </div>

          <div className="mb-4">
            <label
              htmlFor="members"
              className="block mb-2 text-sm font-semibold text-gray-700"
            >
              Number of Occupants
            </label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
              type="number"
              id="members"
              required
              value={formData.members}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  members: parseInt(e.target.value) || 0,
                })
              }
              placeholder="e.g., 4"
              min="1"
            />
          </div>

          <div className="mb-6">
            <label
              htmlFor="postcode"
              className="block mb-2 text-sm font-semibold text-gray-700"
            >
              Postcode
            </label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
              type="text"
              id="postcode"
              required
              value={formData.postcode}
              onChange={(e) =>
                setFormData({ ...formData, postcode: e.target.value })
              }
              placeholder="e.g., 6000"
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full px-4 py-3 font-semibold text-white transition-colors bg-green-500 rounded-lg hover:bg-green-600 disabled:bg-gray-400 disabled:cursor-not-allowed"
          >
            {loading ? "Registering..." : "Register Household"}
          </button>
        </form>
      </div>
    </div>
  );
}

export default RegisterPage;
