/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#1F3A5F",
        accent: "#2E7D6B",
        bg: "#F8F9FB",
        text: "#1A1A1A",
        danger: "#C44536",
      },
    },
  },
  plugins: [],
};
