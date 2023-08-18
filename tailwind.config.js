/** @type {import('tailwindcss').Config} */
export default {
   content: ['./src/**/*.{html,js,svelte,ts}'],
   theme: {
      extend: {
         colors: {
            primary: {
               500: "#002366",
               600: "#263b4c"
            },
            secondary: {
               500: "#808080"
            },
            dark: "rgb(24, 25, 25)",
         }
      },
   },
   plugins: [],
}

