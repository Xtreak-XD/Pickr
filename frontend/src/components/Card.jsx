import React from "react";
import { motion } from "framer-motion";

export const Card = ({ productName, productImage, productPrice, onSwipe, onImageClick }) => {
  const handleSwipe = (offsetY) => {
    if (offsetY < -100) {
      onSwipe("like");
    } else if (offsetY > 100) {
      onSwipe("dislike");
    }
  }

  return (
    <motion.div
      drag="y"
      dragConstraints={{ top: 0, bottom: 0 }} // only up/down
      dragElastic={0.4} // how stretchy it feels
      onDragEnd={(event, info) => {
        handleSwipe(info.offset.y);
      }}
      onClick={onImageClick}
      whileTap={{ scale: 0.90, rotate: 3 }} // small press effect
      className="relative w-60 sm:w-76 md:w-92   lg:w-[28rem] aspect-square rounded-xl overflow-hidden shadow-2xl"
    >
      {/* Image */}
      <div className="w-full h-full overflow-hidden">
        <motion.img
          src={productImage || "/No Image.png"}
          alt={productName || "No Name"}
          className="w-full h-full object-cover pointer-events-none"//transition-transform duration-300 hover:scale-105
          onError={(e) => (e.currentTarget.src = "/No Image.png")}
        />
      </div>

      {/* Price */}
      <div className="absolute top-5 left-2 bg-white/70 px-2 py-1 rounded text-xs sm:text-sm md:text-base font-semibold z-10">
        {productPrice || "$19.99"}
      </div>

      {/* Name */}
      <div className="absolute top-5 right-2 bg-white/70 px-2 py-1 rounded text-xs sm:text-sm md:text-base font-semibold z-10">
        {productName || "Cool Product"}
      </div>
    </motion.div>
  );
};
