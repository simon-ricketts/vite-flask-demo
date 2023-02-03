import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue2";
import path from "path";
import { visualizer } from "rollup-plugin-visualizer";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), visualizer()],
  build: {
    rollupOptions: {
      treeshake: false,
    },
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    host: "127.0.0.1",
    proxy: {
      "/api": "http://127.0.0.1:5212",
    },
  },
});
