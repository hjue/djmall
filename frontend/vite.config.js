import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { viteMockServe } from "vite-plugin-mock";
// vite配置项
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    viteMockServe({
      supportTs: false,
      mockPath: "mock", //mock的路径
    }),
  ],
  server: {
    host: "0.0.0.0",
    hmr: {      
      port: 443
    }
  }
});
