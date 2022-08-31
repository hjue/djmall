<template>
  <div class="page">
    <!-- 导航栏 -->
    <van-nav-bar
      left-text="返回"
      left-arrow
      :fixed="true"
      :title="$route.name"
      @click-left="$router.back()"
    />
    <van-list @load="onLoad" v-model="data.loading" :finished="data.finished" style="margin-top:45px;">
      <van-row>
        <van-col span="24" v-for="(e, i) in data.autoList" :key="i">
          <van-card
            :num="e.fields.total_count"
            :price="e.fields.total_amount/100"
            :title="'订单号'+e.fields.sn"
            :thumb="e.fields.pic"
          >
            <template #tags>
              <van-tag plain type="danger">{{e.fields.order_status}}</van-tag>
              <van-tag plain type="default">商品数量：{{e.fields.item.length}}</van-tag>
              <van-tag plain type="default">{{e.fields.create_time}}</van-tag>
            </template>
            <template #footer>
              <van-list>
                <van-row>
                  <van-col span="24" v-for="(ee, ii) in e.fields.item" :key="ii">
                    <van-card
                      :price="ee.fields.price"
                      :origin-price="ee.fields.total_amount"
                      :desc="'x'+ee.fields.count"
                      :title="ee.fields.name"
                      :thumb="ee.fields.pic"
                      @click="gotoDetail(ee.fields.id_goods)"
                    >
                    </van-card>
                  </van-col>
                </van-row>
              </van-list>
              <van-button size="mini" v-if="e.fields.order_status == '待支付'">支付</van-button>
            </template>
          </van-card>
        </van-col>
      </van-row>
    </van-list>
  </div>
</template>
<script>
import { reactive } from "vue";
import { request } from "../../utils/request";
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
    const onLoad = () => {
      if (data.loading == false && data.finished == false) {
        // 将 loading 设置为 true，表示处于加载状态
        data.loading = true;
        // 异步更新数据
        request.post("/order/list/", {
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
      onLoad,
      gotoDetail
    };
  },
};
</script>