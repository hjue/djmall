<template>
  <div class="page">
    <!-- 空面板 -->
    <van-empty
      v-if="data.goodsList && data.goodsList.length == 0"
      description="空空如也"
    />
    <!-- 购物车列表 -->
    <template v-else v-for="(goods, i) in data.goodsList" :key="i">
      <!-- 可删除的商品栏 -->
      <van-swipe-cell @click="deleteGoods($event, goods.fields.id)">
        <van-row justify="space-between">
          <van-col span="3" style="display: flex; align-content: center">
            <!-- 复选框 -->
            <van-checkbox
              v-model="goods.fields.check"
              style="padding-left: 16px"
              @click="chechCheckbox"
            ></van-checkbox>
          </van-col>
          <van-col span="21">
            <!-- 商品卡片 -->
            <van-card
              :num="goods.fields.count"
              :price="goods.fields.id_sku.price"
              :desc="goods.fields.id_goods.descript"
              :title="goods.fields.id_goods.name"
              :thumb="goods.fields.id_goods.pic"
              :tag="goods.fields.id_goods.isHot ? '火' : ''"
              :origin-price="goods.fields.id_goods.price"
            >
              <!-- 动态添加的底部数据 -->
              <template #tags>
                <template v-for="(v, n) in JSON.parse(goods.fields.id_sku.attribute)" :key="n">
                  <van-tag plain type="danger">{{v}}/</van-tag>
                </template>
              </template>
            </van-card>
          </van-col>
        </van-row>
        <!-- 删除滑块 -->
        <template #right>
          <van-button square text="删除" type="danger" style="height: 100%;" />
        </template>
      </van-swipe-cell>
    </template>
    <!-- 底部提交订单模块 -->
    <van-submit-bar
      v-if="data.goodsList && data.goodsList.length != 0"
      :price="data.total"
      button-text="提交订单"
      style="bottom: 50px"
      @submit="addOrder"
    >
      <van-checkbox v-model="data.check" @click="checkAll">全选</van-checkbox>
    </van-submit-bar>

    <van-dialog
      title="订单创建成功"
      confirmButtonText="立即支付"
      :showCancelButton="true"
      cancelButtonText="稍后支付"
      v-model:show="data.show"
      @confirm="confirm"
    >
    </van-dialog>
  </div>
</template>
<script>
import { onMounted, reactive } from "vue";
import { useRouter } from 'vue-router';
import { request } from '../../utils/request';
import { Toast } from "vant";
export default {
  setup() {
    const data = reactive({
      check: true,
      total: 0,
      goodsList: [],
      show: false,
      user: {},
      order: {
        id:'',
        sn:''
      }
    });
    const router = useRouter();
    // 单选
    const chechCheckbox = () => {
      data.check = data.goodsList.every((goods) => {
        return goods.fields.check == true;
      });
      changeTotal();
    };
    // 全选
    const checkAll = () => {
      data.goodsList.forEach((goods) => {
        goods.fields.check = data.check;
      });
      changeTotal();
    };
    // 修改价格
    const changeTotal = () => {
      data.total = 0;
      data.goodsList.forEach((goods) => {
        if (goods.fields.check) {
          data.total += goods.fields.id_sku.price * 100 * goods.fields.count;
        }
      });
    };
    //删除购物车
    const deleteGoods = (position, id) => {
      if (position == "right") {
        data.goodsList = data.goodsList.filter((goods) => {
          if (id != goods.fields.id) {
            return goods;
          }
        });
        // localStorage.goodsList = JSON.stringify(data.goodsList);
        request
          .post("/cart/delete/", {
            id: id,
          })
          .then((res) => {
            if (res.data) {
              console.log(res.data);
            }
          });
      }
    };
    // 获取购物车
    const getCart = () => {
      request("/cart/get/?user=" + data.user.id)
        .then((res) => {
          if (res && res.data) {
            data.goodsList = res.data
            data.goodsList = data.goodsList.map((e) => {
              e.fields['check'] = true
              return e
            })
          }
          changeTotal();
        });
    }
    // 提交订单
    const addOrder = () => {
      // 添加订单
      // 异步更新数据
      let param = {
        total_count: 0,
        total_amount: data.total,
        postage: 0,
        user: data.user.id,
        item:[]
      }
      data.goodsList.forEach((goods)=>{
        if (goods.fields.check) {
          param.total_count += goods.fields.count
          let item = {}
          item['id'] = goods.fields.id
          item['goods'] = goods.fields.id_goods.id
          item['name'] = goods.fields.id_goods.name
          item['sku'] = goods.fields.id_sku.id
          item['price'] = goods.fields.id_sku.price
          item['count'] = goods.fields.count
          item['total_amount'] = goods.fields.id_sku.price * goods.fields.count
          item['pic'] = goods.fields.id_goods.pic
          param.item.push(item)
        }
      })
      request.post("/order/add/", param)
      .then((res) => {
        if (res.data) {
          data.order.id = res.data.id
          data.order.sn = res.data.sn
        }
        getCart();
      });
      data.show = true
    }
    // 提交订单
    const confirm = () => {
      request.post("/order/pay/", data.order)
      .then((res) => {
        if (res.data.status == 2) {
          Toast("支付成功，等待发货");
          console.log(res.data);
        }
        getCart();
      });
    }
    // 页面渲染加载购物车
    onMounted(() => {
      try {
        data.user = JSON.parse(localStorage.user);
        console.log(data.user);
      } catch {}
      if (!data.user || !data.user.id) {
        // 跳转到登录
        router.push({
          name: "个人中心",
        });
        Toast("请先登录");
        return
      }
      getCart();
    });
    return {
      data,
      chechCheckbox,
      checkAll,
      deleteGoods,
      getCart,
      addOrder,
      confirm
    };
  },
};
</script>
<style>
</style>