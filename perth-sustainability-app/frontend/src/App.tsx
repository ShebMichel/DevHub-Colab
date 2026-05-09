import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import HomePage from "./pages/HomePage";
import RegisterPage from "./pages/RegisterPage";
import DashboardPage from "./pages/DashboardPage";
import AddUsagePage from "./pages/AddUsagePage";
import { Leaf } from "lucide-react";

function App() {
  return (
    <BrowserRouter
      future={{ v7_startTransition: true, v7_relativeSplatPath: true }}
    >
      <div className="flex flex-col max-w-5xl min-h-screen p-5 mx-auto bg-green-50">
        <header className="my-5 mb-10">
          <Link to="/" className="flex items-center gap-2">
            <div className="p-3 text-white bg-green-600 rounded-full">
              <Leaf />
            </div>
            <p className="text-xl antialiased font-bold text-emerald-600">
              Sustainability Tracker
            </p>
          </Link>
        </header>
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route path="/household/:id" element={<DashboardPage />} />
            <Route path="/household/:id/add" element={<AddUsagePage />} />
          </Routes>
        </main>
        <footer className="my-5 text-center text-gray-600">
          <div>
            <p>
              © 2025 Sustainability Tracker - Track your environmental impact
            </p>
          </div>
        </footer>
      </div>
    </BrowserRouter>
  );
}

export default App;
