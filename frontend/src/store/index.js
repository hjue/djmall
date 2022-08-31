import { createStore } from "vuex";
//创建存储对象
export default createStore({
  state() {
    return {
      count: 0,
    };
  },
  // 在其他视图中通过 $store.commit('setState', 10) 使用
  mutations: {
    setState(state, count) {
      state.count = count;
    },
  },
  // 相当于组件的计算属性 通过 $store.getters.doubleCount 获取计算后的值
  getters: {
    doubleCount(state) {
      return state.count * 2;
    },
  },
  // 异步任务 不会改变state 通过 $store.dispath('doubleCount') 使用
  actions: {
    doubleCount(context) {
      context.commit("doubleCount");
    },
  },
  // store的下级store 方便大型项目复杂数据管理
  modules: {},
});
