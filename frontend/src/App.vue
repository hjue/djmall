<template>
  <div id="app">
    <van-nav-bar v-if="$route.meta[0] == 'istabbar'" :title="$route.name"/>
    <router-view></router-view>
    <van-tabbar v-if="$route.meta[0] == 'istabbar'" v-model="active" @change="onChange" route id="tabbar">
      <van-tabbar-item replace to="/" icon="home-o">{{$route.title}}</van-tabbar-item>
      <van-tabbar-item replace to="/search" icon="search">{{$route.title}}</van-tabbar-item>
      <van-tabbar-item replace to="/cart" icon="cart-o">{{$route.title}}</van-tabbar-item>
      <van-tabbar-item replace to="/user" icon="setting-o">{{$route.title}}</van-tabbar-item>
    </van-tabbar>
  </div>
</template>
<script>
import { ref } from 'vue';
export default {
  setup() {
    const active = ref(0);
    const onChange = (index) => {
      active.value = index;
    };
    return {
      active,
      onChange,
    };
  },
};
</script>
<style>
#app{
  padding-bottom: 30px;
}
</style>