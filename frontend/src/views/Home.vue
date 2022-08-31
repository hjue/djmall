<template>
  <div class="page">
    <van-swipe :autoplay="3000">
      <van-swipe-item v-for="(e, i) in data.bannerList" :key="i">
        <img
          style="width: 100%"
          :src="e.fields.pic"
          @click="onSwipeClick(e.pk)"
        />
      </van-swipe-item>
    </van-swipe>
    <!-- 主页推荐列表 -->
    <van-row>
      <van-col span="24" v-for="(e, i) in data.imageList" :key="i">
        <van-card
          :num="e.fields.stock"
          :price="e.fields.price"
          :desc="e.fields.descript"
          :title="e.fields.name"
          :thumb="e.fields.pic"
          :tag="e.fields.isHot ? '火' : ''"
          :origin-price="Math.floor(e.fields.price * 1.1)"
          @click="gotoDetail(e.pk)"
        >
          <template #tags>
            <van-tag plain type="danger" v-if="e.fields.isHot">热门</van-tag>
            <van-tag plain type="danger" v-if="e.fields.isNew">新品</van-tag>
          </template>
          <template #footer>
            <van-button size="mini">百亿补贴</van-button>
          </template>
        </van-card>
      </van-col>
    </van-row>
    <!-- 个性推荐列表 -->
    <div>
      <van-divider span="24">个性推荐</van-divider>
    </div>
    <van-list @load="onLoad" v-model="data.loading" :finished="data.finished">
      <van-row>
        <van-col span="24" v-for="(e, i) in data.autoList" :key="i">
          <van-card
            :tag="e.fields.isHot ? '火' : ''"
            :num="e.fields.stock"
            :price="e.fields.price"
            :origin-price="Math.floor(e.fields.price * 1.1)"
            :desc="e.fields.descript"
            :title="e.fields.name"
            :thumb="e.fields.pic"
            @click="gotoDetail(e.pk)"
          >
            <template #tags>
              <van-tag plain type="danger" v-if="e.fields.isHot">热门</van-tag>
              <van-tag plain type="danger" v-if="e.fields.isNew">新品</van-tag>
            </template>
            <template #footer>
              <van-button size="mini">百亿补贴</van-button>
            </template>
          </van-card>
        </van-col>
      </van-row>
    </van-list>
  </div>
</template>
<script>
import { reactive } from "vue";
import { request } from "../utils/request";
import { useRouter } from "vue-router";
import { Toast } from "vant";
export default {
  setup() {
    const data = reactive({
      bannerList: [],
      imageList: [],
      autoList: [],
      loading: false,
      finished: false,
      page: 1,
      limit: 5,
      key: "",
    });
    const router = useRouter();
    request("/home/ad/").then((res) => {
      data.bannerList = res.data;
    });
    const onSwipeClick = (id) => {
      gotoDetail(id)
    };
    // 主页推荐列表
    request("/home/hot/").then((res) => {
      data.imageList = res.data;
    });
    //
    const onLoad = () => {
      if (data.loading == false && data.finished == false) {
        // 将 loading 设置为 true，表示处于加载状态
        data.loading = true;
        // 异步更新数据
        request.post("/search/", {
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
    const gotoDetail = (id) => {
      router.push({
        name: "详情页",
        params: { id: id },
      });
    };
    return {
      data,
      onSwipeClick,
      onLoad,
      gotoDetail
    };
  },
};
</script>