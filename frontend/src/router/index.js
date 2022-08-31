import { createRouter, createWebHistory } from "vue-router";
// 路由规则
const routes = [
  {
    path: "/",
    name: "主页",
    meta: ["istabbar"],
    component: () => import("../views/Home.vue"),
  },
  {
    path: "/search",
    name: "搜索",
    meta: ["istabbar"],
    component: () => import("../views/search/Search.vue"),
  },
  {
    path: "/cart",
    name: "购物车",
    meta: ["istabbar"],
    component: () => import("../views/cart/Cart.vue"),
  },
  {
    path: "/user",
    name: "个人中心",
    meta: ["istabbar"],
    component: () => import("../views/user/User.vue"),
  },
  {
    path: "/test",
    name: "测试",
    component: () => import("../views/Test.vue"),
  },
  {
    path: "/detail",
    name: "详情页",
    component: () => import("../views/detail/Detail.vue"),
  },
  {
    path: "/order",
    name: "订单",
    component: () => import("../views/user/Order.vue"),
  },
];
//根据路由规则创建路由
const router = createRouter({
  history: createWebHistory(""),
  routes,
});
export default router;