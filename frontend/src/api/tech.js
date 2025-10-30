// api/tech.js
const API_BASE = "http://127.0.0.1:8000/";

export async function fetchTech() {
  const res = await fetch(`${API_BASE}/api/categories/tech`);
  if (!res.ok) throw new Error("Failed to fetch tech items");
  return res.json();
}
