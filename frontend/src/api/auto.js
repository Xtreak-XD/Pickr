const API_BASE = import.meta.env.VITE_API_URL;

export async function fetchAuto() {
  const res = await fetch(`${API_BASE}/auto`);
  if (!res.ok) throw new Error("Failed to fetch auto");
  return res.json();
}

