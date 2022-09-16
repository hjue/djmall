import { createApp } from "vue";
import App from "./App.vue";
import router from "./router"; // 添加路由router引入
import store from "./store"; // 添加全局存储vuex引入
import vant from "vant"; //添加vant引入
import "vant/lib/index.css"; //添加vant样式
import elementPlus from "element-plus"; //添加felementPlus引入
import "element-plus/lib/theme-chalk/index.css"; //添加elementPlus样式
import "@fortawesome/fontawesome-free/css/all.css"; //添加fontawesome样式
import "@fortawesome/fontawesome-free/js/all"; //添加fontawesome脚本
// 创建VUE对象
const vue = createApp(App);
vue.config.globalProperties.url = 'http://127.0.0.1:8001/'
vue
  .use(router) // 使用.use(router)添加路由router
  .use(store) // 使用.use(store)添加全局存储vuex
  .use(vant) // .use(vant)添加vant
  .use(elementPlus) // .use(elementPlus)添加elementPlus
  .mount("#app");