import React, { useState } from 'react'
import { motion,AnimatePresence } from 'framer-motion'
import LogoAnimation from '../components/LogoAnimation'
import MailOutlineOutlinedIcon from '@mui/icons-material/MailOutlineOutlined';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import {Link} from 'react-router-dom'

const HomePage = () => {
    const [isLogin,setIsLogin]=useState(true)
    const colorsMain=['#352F44','#352F44','#B9B4C7','#5C5470','#352F44']
    const colorsWhite=['#ffffff','#ffffff','#BDBDBD','#ffffff','#ffffff']
    const [currentText, setCurrentText] = useState('Sign up and discover a great amount of new opportunities!');
    const [currentTitle,setCurrentTitle]=useState('New Here?')
    const [currentButton,setCurrentButton]=useState('Sign Up')

    const textVariants = {
        initial: { opacity: 0, y: -20 },
        animate: { opacity: 1, y: 0 },
        exit: { opacity: 0, y: 20 },
      };
    
      const textTransition = {
        duration: 0.5,
      };

      const handleToggle=(e)=>{
            e.preventDefault()
            setIsLogin(prev=>!prev)
            setCurrentText(isLogin?'Sign up and discover a great amount of new opportunities!':'To keep connected with us please login with you personal info')
            setCurrentTitle(isLogin?'New Here?':'Welcome back!')
            setCurrentButton(!isLogin?'Sign In':'Sign Up')
      }

      




    return (
    <div className={`relative font-br-hendrix h-screen w-full flex ${isLogin?'md:flex-row flex-col':'md:flex-row-reverse flex-col-reverse'}`}>
        <div className=' absolute z-10 left-2 top-4'>
            {
                isLogin?
                <LogoAnimation colors={colorsMain}/>:
                <LogoAnimation colors={colorsWhite}/>
            }
        </div>
        <motion.div layout className=' flex-1 flex flex-col items-center justify-between'>
            <div className=' h-[20%]'></div>
            <h1 className='font-black text-dark-purple text-6xl'>Login to Your Account </h1>
            <p className=' text-[#414141] opacity-50 text-xl'>Login to use our service</p>
            <div className=' w-[70%] h-[10%] bg-main-gray rounded-full flex items-center justify-between space-x-4 px-4'>
                <MailOutlineOutlinedIcon style={{color:'#352F44',fontSize:30}}/>
                <input placeholder='Email' type="email" className=' text-lg font-medium bg-transparent outline-none flex-1' />

            </div>
            <div className=' w-[70%] h-[10%] bg-main-gray rounded-full flex items-center justify-between space-x-4 px-4'>
                <LockOutlinedIcon style={{color:'#352F44',fontSize:30}}/>
                <input placeholder='Password' type="password" className=' text-lg font-medium bg-transparent outline-none flex-1' />
            </div>
            <div className='flex w-[70%] justify-start font-semibold text-lg text-dark-purple'>
                <Link className=' '>
                    Forgot your password?
                </Link>
            </div>
            <button className='w-[33%] mb-2 h-16 bg-dark-purple rounded-full text-white font-bold text-xl'>
                <p>Sign in</p>
            </button>


        </motion.div>
        <motion.div layout transition={{duration:1}} className={`relative md:w-[40%] md:h-auto h-[40%] bg-gradient-to-tr from-light-purple via-main-purple to-secondary-purple flex flex-col justify-center items-center`}>
            <div className=' flex flex-col items-center w-full space-y-6'>
                <AnimatePresence exitBeforeEnter={false} mode="wait">
                    {
                        <motion.div key={currentTitle} initial="initial" animate="animate" exit="exit" variants={textVariants} transition={textTransition}  className=' font-black text-white text-5xl'>
                            <h2>
                                {currentTitle}
                            </h2>
                            
                        </motion.div>
                    }
                </AnimatePresence>
                <AnimatePresence exitBeforeEnter={false} mode="wait">
                    {
                        <motion.div key={currentText} initial="initial" animate="animate" exit="exit" variants={textVariants} transition={textTransition}  className=' text-white text-2xl px-[10%] h-20 text-center'>
                            <p>
                                {currentText}
                            </p>
                            
                        </motion.div>
                    }
                </AnimatePresence>
                <button onClick={(e)=>handleToggle(e)} className=' w-1/2 outline outline-2 outline-white text-white py-3 font-bold text-xl rounded-full flex justify-center items-center active:outline-white active:text-white hover:outline-main-pink hover:text-main-pink duration-300' >
                    <AnimatePresence exitBeforeEnter={false} mode="wait">
                        {
                            <motion.div key={currentButton} initial="initial" animate="animate" exit="exit" variants={textVariants} transition={textTransition} >
                                <p>
                                    {currentButton}
                                </p>
                                
                            </motion.div>
                        }
                    </AnimatePresence>
                </button>
            </div>
        </motion.div>

    </div>
  )
}

export default HomePage