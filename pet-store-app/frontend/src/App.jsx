import React from 'react'

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <header className="text-3xl font-bold text-center text-teal-600 mb-8">
        🐾 Pet Store Dashboard
      </header>

      <main className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card title="Pets" count={12} />
        <Card title="Appointments" count={5} />
        <Card title="Inventory Items" count={34} />
      </main>
    </div>
  )
}

function Card({ title, count }) {
  return (
    <div className="bg-white shadow-md rounded-2xl p-6 text-center">
      <h2 className="text-lg font-semibold">{title}</h2>
      <p className="text-2xl font-bold text-teal-500">{count}</p>
    </div>
  )
}

export default App
