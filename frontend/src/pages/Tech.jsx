import { useEffect, useState } from "react";
import { Card } from "../components/Card";
import { CardPopup } from "../components/CardPopUp";
import { AnimatePresence } from "framer-motion";
import { fetchTech } from "../api/tech";
import { CategoryTabs } from "../components/CategoryTabs";

export const Tech = () => {
  const [items, setItems] = useState([]);
  const [index, setIndex] = useState(0);
  const [selectedProduct, setSelectedProduct] = useState(null);

  useEffect(() => {
      fetchTech()
        .then(data => setItems(data))
        .catch(err => console.error(err));
    }, []);

  const product = items[index];

  if (!product) return <p>No more Tech items</p>;

  return (
    <div className="flex flex-col items-center justify-center min-h-[calc(100vh-4rem)]">
      {/* Category buttons at the top */}
      <div className="absolute top-2 left-0 right-0 flex justify-center">
        <CategoryTabs />
      </div>

      <Card
        productName={product.title}
        productImage={product.img_link}
        productPrice={product.price}
        onSwipe={() => setIndex((prev) => prev + 1)}
        onImageClick={() => setSelectedProduct(product)}
      />

      <AnimatePresence>
        {selectedProduct && (
          <CardPopup
            product={product}
            onClose={() => setSelectedProduct(null)}
          />
        )}
      </AnimatePresence>
    </div>
  );
};