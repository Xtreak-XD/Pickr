// Card.jsx
import React from 'react';

export const Card = () => {
  return (
    <div className="relative w-64 sm:w-80 md:w-96 lg:w-[28rem] aspect-square rounded-xl overflow-hidden shadow-2xl">
      {/* Image */}
      <img src="/No Image.png" alt="No Image" className="w-full h-full object-cover" />

      {/* Price - top left */}
      <div className="absolute top-5 left-2 bg-white/70 px-2 py-1 rounded text-xs sm:text-sm md:text-base font-semibold z-10">
        $19.99
      </div>

      {/* Name - top right */}
      <div className="absolute top-5 right-2 bg-white/70 px-2 py-1 rounded text-xs sm:text-sm md:text-base font-semibold z-10">
        Cool Product
      </div>
    </div>
  );
};
