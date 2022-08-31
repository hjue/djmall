import axios from "axios";
import router from "../router";
import store from "../store";
// 创建axios对象
const request = axios.create({
  baseURL: import.meta.env.VITE_BASE_API, // api的base_url
  timeout: 50000, // 请求超时设置
});
// request 拦截器
request.interceptors.request.use(
  (config) => {
    if (store.getters.token) {
      config.headers["authorization"] = "authorization "; // + getToken()
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
// response 拦截器
request.interceptors.response.use(
  (response) => {
    const result = response.data;
    if (result.code === 20000) {
      // 成功回调
      return Promise.resolve(result);
    } else {
      if (result.code === 10004) {
        // token 过期跳转到登录页
        // router.replace({ path: '/login' })
      }
      return Promise.reject(result).catch((e) => {});
    }
  },
  (error) => {
    return Promise.reject(error).catch((e) => {});
  }
);
export { request };
