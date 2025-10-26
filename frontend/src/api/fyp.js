const API_BASE = "https://your-railway-app.up.railway.app/categories";

export async function fetchFYP() {
  const res = await fetch(`${API_BASE}/fyp`);
  if (!res.ok) throw new Error("Failed to fetch fyp");
  return res.json();
}
