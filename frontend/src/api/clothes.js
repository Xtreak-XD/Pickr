const API_BASE = "https://your-railway-app.up.railway.app/categories";

export async function fetchClothes() {
  const res = await fetch(`${API_BASE}/clothes`);
  if (!res.ok) throw new Error("Failed to fetch clothes");
  return res.json();
}

