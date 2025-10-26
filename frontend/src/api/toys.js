const API_BASE = import.meta.env.VITE_API_URL;

export async function fetchToys() {
  const res = await fetch(`${API_BASE}/toys`);
  if (!res.ok) throw new Error("Failed to fetch toys");
  return res.json();
}
