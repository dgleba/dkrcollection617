import { defineConfig } from 'vite'
import { createVuePlugin as vue } from "vite-plugin-vue2";
import Components from 'unplugin-vue-components/vite'

const path = require("path");

// https://vitejs.dev/config/
export default defineConfig({
  
  // David Gleba show error in app, since it flashes in inpect console for only a brief moment and cannot read it.
  // server: {
    // // ...
    // clientLogLevel: 'warning',
    // overlay: {
      // warning: true,
      // error: true
    // }
  // },
  
  
  plugins: [
    vue(),
    Components({
      resolvers: [
        {
          type: 'component',
          resolve: (name) => {
            const blackList = ['VChart', 'VHeadCard']
            if (name.match(/^V[A-Z]/) && !blackList.includes(name))
              return { name, from: 'vuetify/lib' }
          },
        },
      ],
      dts: false,
      types: [],
    }),
  ],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})