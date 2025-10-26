const API_BASE = "https://your-railway-app.up.railway.app/categories";

export async function fetchTechItems() {
  const res = await fetch(`${API_BASE}/tech`);
  if (!res.ok) throw new Error("Failed to fetch tech items");
  return res.json();
}
