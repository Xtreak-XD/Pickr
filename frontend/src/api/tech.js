// api/tech.js
const API_BASE = import.meta.env.VITE_API_URL;

export async function fetchTech() {
  const res = await fetch(`${API_BASE}/api/categories/tech`);
  if (!res.ok) throw new Error("Failed to fetch tech items");
  return res.json();
}
