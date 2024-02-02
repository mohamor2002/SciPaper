import { useEffect, useState } from 'react'
import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import SearchPage from './pages/SearchPage'
import ResultsPage from './pages/ResultsPage'
import { useSelector } from 'react-redux';
import ArticlePage from './pages/ArticlePage'
import ProfilePage from './pages/ProfilePage';
import FavouritesPage from './pages/FavouritesPage';
import AdminHomePage from './pages/AdminHomePage'
import NotFoundPage from './pages/NotFoundPage';


function App() {
  
  const user =useSelector(state=>state.data.user.user)
  return (
    <>
    
      <BrowserRouter>
        <Routes>
          <Route index element={user?<SearchPage/>:<HomePage/>}></Route>
          <Route path='/search' element={<ResultsPage/>}></Route>
          <Route path='article/:id' element={<ArticlePage/>}></Route>
          <Route path='profile' element={<ProfilePage/>}></Route>
          <Route path='favourites' element={<FavouritesPage/>}></Route>
          <Route path='*' element={<NotFoundPage/>}></Route>
          <Route path='admin'>
            <Route index element={user?<SearchPage/>:<AdminHomePage/>}></Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
