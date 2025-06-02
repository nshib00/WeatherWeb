/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../weather/templates/**/*.html',  // шаблоны в приложении weather
    '../templates/**/*.html', // шаблоны в корне проекта 
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

