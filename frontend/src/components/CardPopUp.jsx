import React from "react";
import { motion } from "framer-motion";

export const CardPopup = ({ product, onClose }) => {
  if (!product) return null;
  const linkName = document.createElement('a')
  linkName.href = product.img_link

  const tags = [product.subCategory, product.mainCategory]
  const productPrice = product.price.split(" ")[0]
  const productRating = product.ratings.split(" ")[0] // fix the rating name 

  return (
    <motion.div
      onClick={onClose}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 flex items-center justify-center z-50 bg-black/60"
    >
      <motion.div
        onClick={(e) => e.stopPropagation()} // stops closing when clicking inside
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.9, opacity: 0 }}
        transition={{ type: "spring", stiffness: 400, damping: 25 }}
        className="bg-white w-80 sm:w-96 rounded-xl shadow-lg p-6 relative"
      >
        {/* Close button */}
        <button
          onClick={onClose}
          className="absolute top-2 right-2 text-gray-600 hover:text-black"
        >
          ✕
        </button>

        <h2 className="text-xl font-bold mb-2">{product.title}</h2>
        <img
          src={product.img_link || "/No Image.png"}
          alt={product.name}
          className="w-32 h-32 object-cover rounded-lg mx-auto mb-4"
        />
        <p className="text-gray-700 mb-2">{product.description || "No description available."}</p>
        <p className="font-semibold mb-2">Price: {productPrice}</p>
        <p className="mb-2">⭐ {productRating || "N/A"}/5</p>

        {tags.filter(Boolean).length > 0 && (
          <div className="flex gap-2 flex-wrap mt-2">
            {tags.filter(Boolean).map((tag, i) => (
              <span
                key={i}
                className="bg-purple-200 text-purple-800 px-2 py-1 text-xs rounded-full"
              >
                {tag}
              </span>
            ))}
          </div>
        )}

      </motion.div>
    </motion.div>
  );
};
