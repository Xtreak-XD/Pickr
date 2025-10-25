import React, { useState } from 'react';

export const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {
    console.log("Logging in with", username, password);
  };

  const handleSignUp = () => {
    console.log("Signing up with", username, password);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      {/* Title */}
      <h1 className="text-3xl font-bold text-black mb-6">Login</h1>

      {/* Login box */}
      <div className="flex flex-col items-center gap-4 w-64 sm:w-64 md:w-80 lg:w-96 p-6 bg-[#0F4C75] rounded-xl shadow-lg">
        {/* Username */}
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="w-full px-3 py-2 rounded-md outline-none bg-white"
        />

        {/* Password */}
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full px-3 py-2 rounded-md outline-none bg-white"
        />

        {/* Buttons */}
        <div className="flex gap-4 mt-4">
          <button
            onClick={handleLogin}
            className="bg-[#BBE1FA] hover:bg-amber-700 text-white font-semibold px-4 py-2 rounded-md"
          >
            Log In
          </button>
          <button onClick={handleSignUp}  className="bg-[#BBE1FA] hover:bg-cyan-900 text-white font-semibold px-4 py-2 rounded-md">
            Sign Up
          </button>
        </div>
      </div>
    </div>
  );
};
