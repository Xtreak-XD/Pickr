import React, { useEffect, useState } from 'react'

export const Profile = ({ userProp }) => {
  const [user, setUser] = useState(userProp ?? {
    name: 'Miguel Avila',
    email: '',
    bio: 'This is the bio...',
    avatar: '/No Image.png',
  })
  const [wishlist, setWishlist] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    async function loadWishlist() {
      setLoading(true)
      setError(null)
      try {
        const res = await fetch('/api/wishlist')
        if (!res.ok) {
          setWishlist([])
        } else {
          const data = await res.json()
          setWishlist(Array.isArray(data) ? data : [])
        }
      } catch (err) {
        setWishlist([])
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }

    loadWishlist()
  }, [])

  return (
    <div className="relative w-full">
      {/* Red banner at top */}
      <div className="w-full h-36 bg-[#9ed5f9]" />

      {/* Profile picture overlapping banner */}
      <div className="absolute top-20 left-1/2 transform -translate-x-1/2 w-32 h-32 rounded-full border-4 border-white overflow-hidden shadow-lg bg-gray-200">
        <img
          src={user.avatar}
          alt="Profile"
          className="w-full h-full object-cover"
        />
      </div>

      {/* Info section below */}
      <div className="mt-18 px-6 text-center">
        <h2 className="text-xl font-bold text-gray-900">{user.name}</h2>
        <p className="text-sm text-gray-500">{user.email || 'no-email@example.com'}</p>
        <p className="mt-2 text-gray-700">{user.bio}</p>
      </div>

      <hr className="my-6 border-gray-200" />

      {/* Wishlist section */}
      <div className="px-6 mb-8">
        <h3 className="text-lg font-semibold mb-3">Wishlist</h3>

        {loading && <div className="text-sm text-gray-500">Loading wishlist...</div>}
        {error && <div className="text-sm">Failed to load wishlist: {error}</div>}
        {!loading && wishlist.length === 0 && (
          <div className="text-sm text-gray-500">No liked items yet.</div>
        )}

        <div className="mt-3 grid grid-cols-2 gap-3">
          {wishlist.map(item => (
            <div
              key={item.id}
              className="flex flex-col items-start gap-2 bg-white rounded-lg shadow-sm p-3"
            >
              <div className="w-full h-28 bg-gray-100 rounded-md overflow-hidden">
                <img
                  src={item.image || '/No Image.png'}
                  alt={item.title}
                  className="w-full h-full object-cover"
                />
              </div>
              <div className="text-sm font-medium">{item.title}</div>
              {item.price && <div className="text-xs text-gray-500">${item.price}</div>}
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default Profile
