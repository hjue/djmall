<template>
  <div class="page">
    因为在setup内部没有this访问权限，不能直接使用this访问this.$router 或者
    this.$route。所有使用useRouter, useRoute来获取
  </div>
</template>
<script>
import { getCurrentInstance } from "vue";
import { useStore } from "vuex";
export default {
  setup() {
    // 获取路由对象 router 的方法1
    const vue = getCurrentInstance();
    const store1 = vue.ctx.$store;
    console.log(store1);
    // 获取路由对象 router 的方法2
    const store2 = useStore();
    console.log(store2);

    // router对应的属性使用大全
    // ------------------------------------------------------
    // fullPath: "/user"  完整路由路径
    // hash: "" 锚点部分
    // href: "/user"  跳转来的时候的路径
    // matched: [{…}]   路由匹配日规则数组
    // meta: {0: "istabbar"}  路由附加的元数据
    // name: "个人中心" 路由的名称
    // params: {}   路由跳转时带过来的附加参数，如果是对象需要转换成JSON格式
    // path: "/user"  编码 URL 的 pathname 部分，与路由地址有关
    // query: {}   地址附带的参数
    // redirectedFrom: undefined  重定向跳转过来之前的地址，如果没有重定向，则为 undefined。
    return {};
  },
  mounted() {
    // 获取路由对象 router 的方法3
    console.log(this.$store);
  },
};
</script>