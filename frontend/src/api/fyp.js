// api/fyp.js
const API_BASE = import.meta.env.VITE_API_URL;

export async function fetchFYP() {
  console.log("API_BASE =", API_BASE); // should print your Railway URL

  const res = await fetch(`${API_BASE}/api/categories/fyp`);
  console.log("Fetching from:", res.url, "Status:", res.status);

  if (!res.ok) {
    const text = await res.text();
    console.error("Backend returned:", text);
    throw new Error(`Failed to fetch fyp: ${res.status}`);
  }

  return res.json();
}
