import React from 'react';
import { AnimatePresence, color, motion } from 'framer-motion';

const LogoAnimation = ({colors}) => {
  
  
  
  return (
    <motion.svg
      
      id="Layer_1"
      data-name="Layer 1"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 483.42 1017.1"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
      exit={{opacity:0}}
      className=' h-12 w-12 md:h-20 md:w-20'
    >
      <motion.polygon
        className="cls-1"
        points="482.9 0 482.9 296 297.44 388.12 0.52 240.64 0.52 535.59 0 535.85 0 239.84 482.9 0"
        initial={{ opacity: 0, scale: 0, fill: colors[0] }}
        animate={{ opacity: 1, scale: 1, fill: colors[0] }}
        transition={{ delay: 0.2, duration: 0.125 }}
      />
      <motion.polygon
        className="cls-1"
        points="297.44 388.12 0.52 535.59 0.52 240.64 297.44 388.12"
        initial={{ opacity: 0, scale: 0, fill: colors[1] }}
        animate={{ opacity: 1, scale: 1, fill: colors[1] }}
        transition={{ delay: 0.4, duration: 0.125 }}
      />
      <motion.polygon
        className="cls-2"
        points="483.42 480.49 483.42 481.25 186.21 628.87 186.2 628.87 0.52 536.65 0.52 535.59 297.44 388.12 483.42 480.49"
        initial={{ opacity: 0, scale: 0, fill: colors[2] }}
        animate={{ opacity: 1, scale: 1, fill: colors[2] }}
        transition={{ delay: 0.375, duration: 0.125 }}
      />
      <motion.polygon
        className="cls-3"
        points="483.42 481.25 483.42 776.49 186.21 628.87 483.42 481.25"
        initial={{ opacity: 0, scale: 0, fill: colors[3] }}
        animate={{ opacity: 1, scale: 1, fill: colors[3] }}
        transition={{ delay: 0.5, duration: 0.125 }}
      />
      <motion.polygon
        className="cls-1"
        points="483.42 776.49 483.42 777.26 0.52 1017.1 0.52 721.1 186.2 628.87 186.21 628.87 483.42 776.49"
        initial={{ opacity: 0, scale: 0, fill: colors[4] }}
        animate={{ opacity: 1, scale: 1, fill: colors[4]}}
        transition={{ delay: 0.675, duration: 0.125}}
      />
    </motion.svg>
  );
};

export default LogoAnimation;
