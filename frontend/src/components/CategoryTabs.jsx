// src/components/CategoryTabs.jsx
import { Link } from "react-router-dom";

export const CategoryTabs = () => {
  const categories = [
    { name: "FYP", path: "/" },
    { name: "Tech", path: "/tech" },
    { name: "Toys", path: "/toys" },
    { name: "Clothes", path: "/clothes" },
    { name: "Auto", path: "/auto" },
  ];

  return (
    <div className="flex gap-6 text-white font-semibold">
      {categories.map((cat) => (
        <Link
          key={cat.name}
          to={cat.path}
          className="bg-transparent hover:underline hover:text-yellow-300"
        >
          {cat.name}
        </Link>
      ))}
    </div>
  );
};
