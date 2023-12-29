import { useState } from 'react'
import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';


function App() {
  

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index element={<HomePage/>}>

          </Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
