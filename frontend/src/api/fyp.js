const API_BASE = "https://knighthacks.netlify.app/api/categories/fyp"; 

export async function fetchFYP() {
  const res = await fetch(`${API_BASE}/fyp`);
  if (!res.ok) throw new Error("Failed to fetch fyp");
  return res.json();
}
