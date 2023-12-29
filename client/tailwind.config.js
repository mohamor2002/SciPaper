/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
        fontFamily: {
          'br-hendrix': ['Br Hendrix', 'sans-serif'],
        },
        fontWeight: {
          'light': 300,
          'medium': 500,
          'semi-bold': 600,
        },
        colors:{
          'main-purple':'#545A70',
          'secondary-purple':'#5C5470',
          'light-purple':'#6A5470',
          'dark-purple':'#352F44',
          'main-pink':'#F1BBBB',
          'main-gray':'#EDF5F3'
        }
      }
  },
  plugins: [],
}

