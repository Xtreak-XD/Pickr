const API_BASE = import.meta.env.VITE_API_URL;

export async function fetchClothes() {
  const res = await fetch(`${API_BASE}/clothes`);
  if (!res.ok) throw new Error("Failed to fetch clothes");
  return res.json();
}

