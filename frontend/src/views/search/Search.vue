<template>
  <div class="page">
    <form>
      <van-search
        show-action
        placeholder="搜索"
        :autofocus="true"
        v-model="data.key"
        @search="onSearch"
      />
    </form>
    <!-- 个性推荐列表 -->
    <van-empty v-if="data.autoList.length == 0" description="空空如也" />
    <van-list
      v-else
      @load="onLoad"
      v-model="data.loading"
      :finished="data.finished"
    >
      <van-row>
        <van-col span="24" v-for="(e, i) in data.autoList" :key="i">
          <van-card
            :tag="e.fields.isHot ? 'Hot' : ''"
            :num="e.fields.stock"
            :price="e.fields.price"
            :origin-price="Math.floor(e.fields.price * 1.1)"
            :desc="e.fields.descript"
            :title="e.fields.name"
            :thumb="e.fields.pic"
          >
            <template #tags>
              <van-tag plain type="danger" v-if="e.fields.isHot">热门</van-tag>
              <van-tag plain type="danger" v-if="e.fields.isNew">新品</van-tag>
            </template>
            <template #footer>
              <van-button size="mini"
                ><van-icon name="cart-o" color="#1989fa"
              /></van-button>
              <van-button size="mini">立即下单</van-button>
            </template>
          </van-card>
        </van-col>
      </van-row>
    </van-list>
  </div>
</template>
<script>
import { reactive } from 'vue';
import { Toast } from 'vant';
import { request } from '../../utils/request';
export default {
  setup() {
    const data = reactive({
      autoList: [],
      loading: false,
      finished: false,
      page: 1,
      limit: 5,
      key: "",
    });
    const onSearch = () => {
      data.autoList = [];
      data.page = 1;
      data.finished = false;
      onLoad();
    };
    const onLoad = () => {
      if (!data.loading) {
        // 将 loading 设置为 true，表示处于加载状态
        data.loading = true;
        // 异步更新数据
        request
          .post("/search/", {
            page: data.page++,
            limit: data.limit,
            key: data.key,
          })
          .then((res) => {
            if (res.data) {
              data.autoList = data.autoList.concat(res.data);
            }
            if (Math.ceil(res.total / data.limit) <= data.page) {
              data.finished = true;
              Toast("没有更多数据了");
            }
            // 加载状态结束
            data.loading = false;
          });
      }
    };
    return {
      data,
      onSearch,
      onLoad,
    };
  },
};
</script>