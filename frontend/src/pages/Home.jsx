import { React, useState } from 'react'
import { Card } from "../components/Card"

const test = [
  {name: "Headphones", image: "/No Image.png", price: "20.99"},
  {name: "Phone", image: "/No Image.png", price: "200.99"},
  {name: "Shoes", image: "/No Image.png", price: "60.00"}
]
 
export const Home = () => {
  const [index, setIndex] = useState(0)
  const [message, setMessage] = useState("")
  const [bgColor, setBgColor] = useState("bg-black-700")

  const handleSwipe = (dir) => {
    if (dir === "like") {
      setMessage("Liked")
      setBgColor("bg-green-700")
    } else {
      setMessage("Disliked")
      setBgColor("bg-red-700")
    }

    // after 500ms show next product
    setTimeout(() => {
      setMessage("");
      setIndex((prev) => prev + 1);
    }, 500);
  }
  
  const product = test[index];

  if (!product) {
    return <p> NO MORE ITEMS</p>
  }

  return (
    <div className="grow flex items-center justify-center relative">
      {message && (
        <div id = "message" className={`absolute top-10 text-white px-4 py-2 rounded-xl shadow-lg z-10 ${bgColor}`}>
          {message}
        </div>
      )}

      <Card
        productName={product.name}
        productImage={product.image}
        productPrice={product.price}
        onSwipe={handleSwipe}
      />
    </div>
  )
}
