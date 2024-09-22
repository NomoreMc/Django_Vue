import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
        "/Account/api": 'http://localhost:8000',
        "/api": 'http://localhost:8000',
        "/upload": 'http://localhost:8000',
        "/Post/api": 'http://localhost:8000',
    },
  },
})
