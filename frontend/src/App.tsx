import { Route, Routes, Link } from 'react-router-dom'
import Home from './pages/Home'
import About from './pages/About'

export default function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <nav className="p-4 bg-gray-900 text-white flex justify-between">
        <Link to="/">MadeByParm</Link>
        <div className="space-x-4">
          <Link to="/about">About</Link>
        </div>
      </nav>
      <main className="flex-grow">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </main>
      <footer className="p-4 text-center text-sm text-gray-500">\u00a9 2024 MadeByParm</footer>
    </div>
  )
}
