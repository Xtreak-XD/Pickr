const API_BASE = "https://your-railway-app.up.railway.app/categories";

export async function fetchToys() {
  const res = await fetch(`${API_BASE}/toys`);
  if (!res.ok) throw new Error("Failed to fetch toys");
  return res.json();
}
