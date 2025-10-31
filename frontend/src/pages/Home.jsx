import { useRef, useState, useLayoutEffect, useEffect } from 'react'
import { Card } from "../components/Card"
import { CardPopup } from "../components/CardPopUp";
import { AnimatePresence } from "framer-motion";
import { fetchFYP } from "../api/fyp";
import { CategoryTabs } from "../components/CategoryTabs"; // import tabs
import { ConfettiEffect } from '../components/Confetti';

export const Home = () => {
  const [items, setItems] = useState([])  
  const [index, setIndex] = useState(0)
  const [message, setMessage] = useState("")
  const [bgColor, setBgColor] = useState("bg-black-700")
  const [selectedProduct, setSelectedProduct] = useState(null);
  const containerRef = useRef(null);
  const [showConfetti, setShowConfetti] = useState(false);
  const [dimension, setDimension] = useState({ width: 0, height: 0 });

  // fetch from Django backend
  useEffect(() => {
    fetchFYP()
      .then(data => setItems(data))
      .catch(err => console.error(err));
  }, []);

  // track container size dynamically
  useLayoutEffect(() => {
    if (!containerRef.current) return
    const resizeObserver = new ResizeObserver(() => {
      if (containerRef.current) {
        const { offsetWidth, offsetHeight } = containerRef.current
        setDimension({ width: offsetWidth, height: offsetHeight })
      }
    })
    resizeObserver.observe(containerRef.current)
    return () => resizeObserver.disconnect()
  }, [containerRef.current])

  const handleSwipe = (dir) => {
    if (dir === "like") {
      setMessage("Liked")
      setBgColor("bg-green-700")
      setShowConfetti(true)
      setTimeout(() => setShowConfetti(false), 2000)
    } else {
      setMessage("Disliked")
      setBgColor("bg-red-700")
      setShowConfetti(false)
    }

    setTimeout(() => {
      setMessage("")
      setIndex((prev) => prev + 1)
    }, 500)
  }

  const product = items[index]

  if (!product) {
    return <p>NO MORE ITEMS</p>; // Todo Make the loading animation here when changing products or no items left
  }

  return (
    <div 
      ref={containerRef} 
      className="relative flex flex-col items-center justify-center min-h-[calc(100vh-4rem)]"
    >
      {/* category buttons at the top */}
      <div className="absolute top-2 left-0 right-0 flex justify-center">
        <CategoryTabs />
      </div>

      {showConfetti && <ConfettiEffect width={dimension.width} height={dimension.height} />}
      {message && (
        <div
          id="message"
          className={`absolute top-14 text-white px-4 py-2 rounded-xl shadow-lg z-10 ${bgColor}`}
        >
          {message}
        </div>
      )}

      <Card
        productName={product.title}
        productImage={product.img_link}
        productPrice={product.price}
        onSwipe={handleSwipe}
        onImageClick={() => setSelectedProduct(product)}
      />

      <button
        onClick={() => handleSwipe("dislike")}
        className="mt-6 px-6 py-3 rounded-full bg-red-600 text-white font-semibold shadow-md hover:bg-red-700 transition"
      >
        Not Interested
      </button>

      <AnimatePresence>
        {selectedProduct && (
          <CardPopup
            product={product}
            onClose={() => setSelectedProduct(null)}
          />
        )}
      </AnimatePresence>
    </div>
  )
}
