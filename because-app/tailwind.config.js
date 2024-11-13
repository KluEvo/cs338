const { text } = require("stream/consumers");

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,html}",
    "./public/index.html",
    "./src/**/Components/*.js",
  ],
  theme: {
    extend: {
      colors: {
        background: "bg-sky-900",
        text: "#ffffff",
      },
    },
  },
  plugins: [],
};
