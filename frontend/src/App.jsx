import { useEffect, useState } from 'react'
import { NavBar } from './components/Navbar'
import { Routes, Route } from 'react-router-dom'
import { Home } from './pages/Home'
import { Profile } from './pages/Profile'
import { Settings } from './pages/Settings'
import { Login } from './pages/Login'

function App() {
  return (
    <div className="flex items-center justify-center min-h-screen shadow-[5px_0px_10px_rgba(100,24,0,0.3)] bg-zinc-800">
      {/* App container */}
      <div className="flex flex-col min-h-screen w-64 sm:w-80 md:w-96 lg:w-[28rem] bg-[#F0A500] shadow-lg rounded-2xl overflow-hidden">
        <div className="flex-1">
          <Routes>
            <Route path={"/login"} element={<Login/>}></Route>
            <Route path={"/"} element={<Home/>} />
            <Route path={"/settings"} element={<Settings/>} />
            <Route path={"/profile"} element={<Profile/>} />
          </Routes>
        </div>


        {/* Bottom navbar */}
        <div className="w-full">
          <NavBar />
        </div>
      </div>
    </div>
  )
}

export default App
