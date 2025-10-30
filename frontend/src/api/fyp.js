// const API_BASE = "https://roary.up.railway.app"; 
const API_BASE = "http://127.0.0.1:8000";
// in .env: VITE_API_URL=https://roary.up.railway.app

export async function fetchFYP() {
  console.log("API_BASE =", API_BASE);

  const res = await fetch(`${API_BASE}/api/categories/fyp`); // ✅ correct
  console.log("Fetching from:", res.url, "Status:", res.status);

  if (!res.ok) {
    const text = await res.text();
    console.error("Backend returned:", text);
    throw new Error(`Failed to fetch fyp: ${res.status}`);
  }

  return res.json();
}
