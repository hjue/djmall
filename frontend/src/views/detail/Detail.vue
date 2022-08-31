<template>
  <!-- 导航栏 -->
  <van-nav-bar
    left-text="返回"
    left-arrow
    :fixed="true"
    :title="$route.name"
    @click-left="$router.back()"
  />
  <!-- 轮播图 -->
  <van-swipe :autoplay="3000" style="margin-top:45px;">
    <van-swipe-item v-for="(image, i) in data.bannerList" :key="i">
      <img
        style="width: 100%"
        :src="image"
      />
    </van-swipe-item>
  </van-swipe>
  <!-- 商品卡片 -->
  <van-card
    :num="data.goods.stock"
    :price="data.goods.price"
    :desc="data.goods.descript"
    :title="data.goods.name"
    :tag="data.goods.isHot ? '火' : ''"
    :origin-price="Math.floor(data.goods.price * 1.1)"
  >
    <template #tags>
      <van-tag plain type="danger" v-if="data.goods.isHot">热门</van-tag>
      <van-tag plain type="danger" v-if="data.goods.isNew">新品</van-tag>
    </template>
  </van-card>
  <!-- 商品 -->
  <div class="detail" v-html="data.detail"></div>
  <!-- 商品操作栏 -->
  <van-action-bar>
    <van-action-bar-button type="warning" text="加入购物车" @click="openSku" />
    <van-action-bar-button type="danger" text="打开购物车" @click="openCart" />
  </van-action-bar>
  <!-- sku -->
  <van-action-sheet
    v-model:show="data.show"
    title="商品参数"
    cancel-text="确定"
    :closeable="false"
    @cancel="onSure"
  >
    <!-- 商品展示栏目 -->
    <van-card
      :num="data.goods.stock"
      :price="data.goods.price"
      :desc="data.goods.descript"
      :title="data.goods.name"
      :thumb="data.goods.pic"
      :origin-price="Math.floor(data.goods.price * 1.1)"
    >
      <!-- 动态添加的底部数据 -->
      <template #tags>
        <template v-for="(sku, i) in data.goods.sku" :key="i">
          <template v-for="(v, n) in JSON.parse(sku.fields.attribute)" :key="n">
            <van-tag plain type="danger" v-if="data.goods.skuid == sku.fields.id">{{v}}/</van-tag>
          </template>
        </template>
      </template>
    </van-card>
    <!-- 循环展示的参数信息 -->
    <template v-for="(sku, i) in data.goods.sku" :key="i">
      <van-field :label="'套餐'+(i+1)">
        <template #input>
          <van-radio-group v-model="data.goods.skuid" direction="horizontal">
            <van-radio :name="i+1">
              <template v-for="(v, n) in JSON.parse(sku.fields.attribute)" :key="n">
                {{v}}/
              </template>
            </van-radio>
          </van-radio-group>
        </template>
      </van-field>
    </template>
  </van-action-sheet>
</template>
<script>
import { onMounted, reactive } from "vue";
import { useRoute, useRouter } from "vue-router";
import { request } from "../../utils/request";
import { Toast } from "vant";
export default {
  setup() {
    const data = reactive({
      goods: {},
      detail: "",
      bannerList: [],
      sku: '',
      show: false,
    });
    const route = useRoute();
    const router = useRouter();
    request.post("/detail/",{id: route.params.id})
    .then((res) => {
      data.goods = res.data[0].fields;
      data.detail = res.data[0].fields.detail;
      data.bannerList = res.data[0].fields.gallery;
    });
    // 打开购物车
    const openCart = () => {
      router.push({
        name: "购物车",
      });
    }
    // 打开sku列表
    const openSku = () => {
      data.show = true;
    };
    let goodsList = [];
    // 添加到购物车
    const onSure = () => {
      let user = {}
      try {
        user = JSON.parse(localStorage.user);
      } catch {}
      if (!user || !user.id) {
        // 跳转到登录
        router.push({
          name: "个人中心",
        });
        Toast("请先登录");
        return
      }
      // 添加购物车
      let goods = {
        user: user.id,
        goods: data.goods.id,
        sku: data.goods.skuid,
        count: 1
      }
      request.post("/cart/add/",goods)
      .then((res) => {
        if (res.data == 2) {
          Toast("添加购物车成功");
        }
      })
      .catch((e)=>{
        Toast(e);
      });
    };
    onMounted(() => {});
    return {
      data,
      openCart,
      openSku,
      onSure,
    };
  },
};
</script>
<style>
.detail img {
  width: 100%;
}
</style>