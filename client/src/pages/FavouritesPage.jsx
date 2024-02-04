import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom';
import Navbar from '../components/Navbar';
import { AnimatePresence, motion } from 'framer-motion';
import TuneRoundedIcon from '@mui/icons-material/TuneRounded';
import SearchIcon from '@mui/icons-material/Search';
import TagRoundedIcon from '@mui/icons-material/TagRounded';
import PersonRoundedIcon from '@mui/icons-material/PersonRounded';
import BusinessRoundedIcon from '@mui/icons-material/BusinessRounded';
import CalendarMonthRoundedIcon from '@mui/icons-material/CalendarMonthRounded';
import { Link } from 'react-router-dom';
import KeyboardArrowUpRoundedIcon from '@mui/icons-material/KeyboardArrowUpRounded';
import AddIcon from '@mui/icons-material/Add';
import { useSelector } from 'react-redux';
// import articles from '../constants/articles';
import getArticles from '../api/getArticles';






const FavouritesPage = () => {
  const user =useSelector(state=>state.data.user.user)
  const [loading, setLoading] = useState(true);
  const [articles,setArticles]=useState(null)
  /*const populateDocuments = async(user)=>{
    const favourites = user.favourites
    console.log(favourites);
    articles = await getArticles({'id': favourites,}); 
  }
  populateDocuments(user);*/
  useEffect(()=>{
    const getArticlesEffect=async()=>{
      const a = await getArticles({'id':user.favourites});
      setArticles(a)
      setLoading(false);
      console.log(a)
    }
     getArticlesEffect()
  },
  [])
  // console.log(articles);

  const SkeletonCard=()=>{
    return(
      <motion.div initial={{borderRadius:40}} animate={{borderRadius:0}} transition={{duration:1}} className=' items-end md:pl-8 pl-4 pr-2 py-3 font-br-hendrix space-y-2 animate-pulse flex flex-col w-full bg-gradient-to-r from-main-gray to-white'>
        <div className='h-12 w-full rounded-xl bg-gray-200 pb-4 animate-pulse'></div>
        <div className='h-4 w-[60%] rounded-xl bg-gray-200 animate-pulse'></div>
        <div className='h-4 w-[60%] rounded-xl bg-gray-200 animate-pulse'></div>
        <div className='h-4 w-[60%] rounded-xl bg-gray-200 animate-pulse'></div>
        <div className='h-4 w-[60%] rounded-xl bg-gray-200 animate-pulse'></div>
      </motion.div>
    )
  }

  const ArticleCard=({id,title,keywords,authors,institutions,date})=>{
    return(
      <motion.div dragSnapToOrigin dragConstraints={{ left: 0, right: 300 }} drag initial={{borderRadius:40}} animate={{borderRadius:0}} transition={{duration:1}} className=' items-end md:pl-8 pl-4 pr-2 py-3 font-br-hendrix flex flex-col w-full bg-gradient-to-r from-main-gray to-white'>
        <h2 className=' mb-4 font-medium text-left text-lg md:text-2xl hover:underline'>
          <Link to={`/article/${id}`}>
            {title}
          </Link>
        </h2>
        <div className='flex flex-row-reverse md:text-base text-sm items-end space-x-2'>
          <TagRoundedIcon/>
          <div className='overflow-hidden opacity-70 whitespace-nowrap'>
            {
              keywords?.map((k,index)=>(
                `${k}${index==keywords.length-1?'':', '}` 
              ))
            }
          </div>
        </div>
        <div className='flex flex-row-reverse md:text-base text-sm items-end space-x-2'>
          <PersonRoundedIcon/>
          <div className='overflow-hidden opacity-70 whitespace-nowrap'> 
            {
              authors.map((k,index)=>(
                `${k}${index==authors.length-1?'':', '}` 
              ))
            }
          </div>
        </div>
        <div className='flex flex-row-reverse md:text-base text-sm items-end space-x-2'>
          <BusinessRoundedIcon/>
          <div className='overflow-hidden opacity-70 whitespace-nowrap'>
            {
              institutions.map((k,index)=>(
                `${k}${index==institutions.length-1?'':', '}` 
              ))
            }
          </div>
        </div>
        <div className='flex flex-row-reverse md:text-base text-sm items-end space-x-2'>
          <CalendarMonthRoundedIcon/>
          <div className='overflow-hidden opacity-70 whitespace-nowrap'>
            {date}
          </div>
        </div>
      </motion.div>
    )
  }






  return (
    <div className=' font-br-hendrix w-full relative h-screen'>
      <Navbar />
      <div className='md:grid md:grid-cols-4 flex flex-col w-full h-screen'>
      <motion.div initial={{y:-200}} animate={{y:0}} exit={{y:-200}} className="flex flex-col items-center justify-center px-6 pt-20 pb-4 md:pt-28 space-y-4 col-span-1 bg-[#EDF5F3] w-full h-full">
        <h2 className=' font-semibold text-xl md:text-2xl'>Favourites</h2>
        </motion.div>
        <motion.div initial={{y:200}} animate={{y:0}} exit={{y:200}} className='col-span-3 px-2 md:pl-8 pt-8 md:pt-24 w-full h-screen flex flex-col'>  
          <div>
          </div>
          <div className='list flex flex-col space-y-6 px-2 pb-2 mt-2 flex-1 overflow-y-scroll'>
            {!loading?
              articles.map((article)=>(
                <ArticleCard key={article.id} id={article.id} keywords={article.keywords} title={article.title} authors={article.authors} institutions={article.institutions} date={article.date}/>
              )):
              [1,2,3,4,5].map(()=>(
                <SkeletonCard/>
              ))
            }
          </div>
        </motion.div>
      </div>
    </div>
  )
}
export default FavouritesPage