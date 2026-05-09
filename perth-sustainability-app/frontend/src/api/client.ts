import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL || "/api";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export interface Household {
  id: number;
  name: string;
  members: number;
  postcode: string;
  created_at: string;
}

export interface UsageEntry {
  id: number;
  household_id: number;
  entry_type: "water" | "energy";
  value: number;
  recorded_at: string;
}

export interface DashboardData {
  household: Household;
  entries: UsageEntry[];
  summary: { water?: number; energy?: number };
  greenScore: number;
  tips: string[];
}

export const householdApi = {
  getAll: () => api.get<{ households: Household[] }>("/households"),
  getById: (id: number) => api.get<DashboardData>(`/households/${id}`),
  create: (data: { name: string; members: number; postcode: string }) =>
    api.post<Household>("/households", data),
  delete: (id: number) => api.delete(`/households/${id}`),
};

export const usageApi = {
  create: (data: {
    household_id: number;
    entry_type: "water" | "energy";
    value: number;
    recorded_at?: string;
  }) => api.post<UsageEntry>("/usage", data),
  delete: (id: number) => api.delete(`/usage/${id}`),
  exportCsv: (householdId: number) =>
    api.get(`/usage/export/${householdId}`, { responseType: "blob" }),
  importCsv: (householdId: number, csvData: string) =>
    api.post(`/usage/import/${householdId}`, { csv_data: csvData }),
};

export default api;
