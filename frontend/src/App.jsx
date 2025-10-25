import { useEffect, useState } from 'react'
import { Card } from "./components/Card"
import { NavBar } from './components/Navbar'
import { Routes, Route } from 'react-router-dom';
import { Home } from './pages/Home';
import { Profile } from './pages/Profile';
import { Settings } from './pages/Settings';
import { Login } from './pages/Login';

function App() {
  return (
    <div className="flex items-center justify-center min-h-screen bg-zinc-800">
      {/* App container */}
      <div className="flex flex-col items-center justify-between min-h-screen w-64 sm:w-80 md:w-96 lg:w-[28rem] bg-white shadow-lg rounded-2xl">
        <div className="flex-1 flex items-center justify-center">
          <Routes>
            <Route path={"/login"} component={Login}></Route>
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
