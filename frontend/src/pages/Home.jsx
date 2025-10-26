import { useRef, useState, useLayoutEffect } from 'react'
import { Card } from "../components/Card"
import { CardPopup } from "../components/CardPopUp";
import { AnimatePresence } from "framer-motion";
import Confetti from 'react-confetti'

const test = [
  {name: "Headphones", image: "/No Image.png", price: "20.99", description: "Noise-cancelling wireless headphones.", rating: 4.5, tags: ["Audio", "Electronics"]},
  {name: "Phone", image: "/No Image.png", price: "200.99", description: "Latest smartphone with great camera.", rating: 4.2, tags: ["Mobile", "Electronics"]},
  {name: "Shoes", image: "/No Image.png", price: "60.00", description: "Comfortable running shoes.", rating: 4.0, tags: ["Sports", "Footwear"]}
]
 
export const Home = () => {
  const [index, setIndex] = useState(0)
  const [message, setMessage] = useState("")
  const [bgColor, setBgColor] = useState("bg-black-700")
  const [selectedProduct, setSelectedProduct] = useState(null);
  const containerRef = useRef(null)
  const [dimensions, setDimensions] = useState({ width: 0, height: 0 })
  const [showConfetti, setShowConfetti] = useState(false)

  // track container size dynamically
  useLayoutEffect(() => {
    if (!containerRef.current) return
    const resizeObserver = new ResizeObserver(() => {
      if (containerRef.current) {
        const { offsetWidth, offsetHeight } = containerRef.current
        setDimensions({ width: offsetWidth, height: offsetHeight })
      }
    })
    resizeObserver.observe(containerRef.current)
    return () => resizeObserver.disconnect()
  }, [])

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

    // after 500ms show next product
    setTimeout(() => {
      setMessage("")
      setIndex((prev) => prev + 1)
    }, 500)
  }
  
  const product = test[index];

  if (!product) {
    return <p> NO MORE ITEMS</p>
  }

  return (
    <div 
      ref={containerRef} 
      className="relative flex flex-col items-center justify-center min-h-[calc(100vh-4rem)]"
    >
      {message && (
        <div
          id="message"
          className={`absolute top-10 text-white px-4 py-2 rounded-xl shadow-lg z-10 ${bgColor}`}
        >
          {message}
        </div>
      )}

      {showConfetti && (
        <Confetti
          width={dimensions.width}
          height={dimensions.height}
          numberOfPieces={600}
          gravity={0.8}
        />
      )}

      {/* Card */}
      <Card
        productName={product.name}
        productImage={product.image}
        productPrice={product.price}
        onSwipe={handleSwipe}
        onImageClick={() => setSelectedProduct(product)}
      />

      {/* Button directly under card */}
      <button
        onClick={() => handleSwipe("dislike")}
        className="mt-6 px-6 py-3 rounded-full bg-red-600 text-white font-semibold shadow-md hover:bg-red-700 transition"
      >
        Not Interested
      </button>

      <AnimatePresence>
        {selectedProduct && (
          <CardPopup
            product={selectedProduct}
            onClose={() => setSelectedProduct(null)}
          />
        )}
      </AnimatePresence>
    </div>
  )
}
