const API_BASE = "https://your-railway-app.up.railway.app/categories";

export async function fetchAuto() {
  const res = await fetch(`${API_BASE}/auto`);
  if (!res.ok) throw new Error("Failed to fetch auto");
  return res.json();
}

