// api/tech.js
const API_BASE = "https://backend-production-6987.up.railway.app";

export async function fetchTech() {
  const res = await fetch(`${API_BASE}/api/categories/tech`);
  if (!res.ok) throw new Error("Failed to fetch tech items");
  return res.json();
}
