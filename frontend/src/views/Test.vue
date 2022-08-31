<template>
  <div class="page">
    <van-nav-bar title="标题" left-text="返回" right-text="我的" left-arrow />
    <van-pull-refresh
      v-model="data.refreshing"
      @refresh="onRefresh"
      :finished="data.finished"
    >
      <van-list @load="onLoad" v-model="data.loading" :finished="data.finished">
        <van-row>
          <van-col span="24" v-for="(e, i) in data.imageList" :key="i">
            <van-card
              :tag="e.isHot ? 'Hot' : ''"
              :num="e.stock"
              :price="e.price"
              :origin-price="e.price * 1.1"
              :desc="e.descript"
              :title="e.name"
              :thumb="'/upload/' + e.pic"
            >
              <template #tags>
                <van-tag plain type="danger">热销</van-tag>
                <van-tag plain type="danger">广告</van-tag>
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
    </van-pull-refresh>
  </div>
</template>
<script>
import { reactive } from "vue";
import { request } from "/src/utils/request";
import { Notify } from "vant";
export default {
  setup() {
    // 在最后一个测试中赋值
    const data = reactive({
      refreshing: false,
      loading: false,
      finished: false,
      imageList: [],
      page: 1,
      limit: 5,
      key: "",
    });
    const onLoad = () => {
      console.log(data.loading);
      if (!data.loading) {
        // 将 loading 设置为 true，表示处于加载状态
        data.loading = true;
        // 异步更新数据
        setTimeout(() => {
          request
            .post("/search", {
              page: data.page,
              limit: data.limit,
              key: data.key,
            })
            .then((res) => {
              data.imageList = data.imageList.concat(res.data.records);
              console.log("添加数据", data.imageList);
              // 数据全部加载完成
              console.log(data.imageList.length);
              console.log(res.data.total);
              if (data.imageList.length - res.data.total >= 0) {
                data.finished = true;
                Notify("没有更多数据了");
              }
              // 加载状态结束
              data.loading = false;
            })
            .catch(function (error) {})
            .finally(() => {});
        }, 3000);
      }
    };
    const onRefresh = () => {
      if (data.refreshing) {
        data.imageList = [];
        data.refreshing = false;
        // 清空列表数据
        data.finished = false;
        data.loading = false;
        // 重新加载数据
        onLoad();
      }
    };
    ///////////////////////////////////////////////////
    1;
    //////////////////////////////////////////////////
    // 测试搜索页
    request
      .post("/search", {
        page: 2,
        limit: 10,
        key: "",
      })
      .then((res) => {
        data.imageList = data.imageList.concat(res.data.records);
        console.log("request测试搜索页", res);
      })
      .catch(function (error) {})
      .finally(() => {});
    // 测试搜索页
    fetch("/search", {
      method: "POST",
      mode: "cors",
      body: JSON.stringify({
        page: 2,
        limit: 10,
        key: "",
      }),
    }).then((res) =>
      res.json().then((data) => {
        console.log("fetch测试搜索页", data);
      })
    );
    ///////////////////////////////////////////////////
    2;
    //////////////////////////////////////////////////
    // 测试登录
    request
      .post("/signin", {
        username: "15011112222",
        password: "admin",
      })
      .then((res) => {
        console.log("request测试登录", res);
      })
      .catch(function (error) {})
      .finally(() => {});
    // 测试登录
    fetch("/signin", {
      method: "POST",
      mode: "cors",
      body: JSON.stringify({
        username: "15011112222",
        password: "admin",
      }),
    }).then((res) =>
      res.json().then((data) => {
        console.log("fetch测试登录", data);
      })
    );
    ///////////////////////////////////////////////////
    3;
    //////////////////////////////////////////////////
    // 测试获取用户信息
    request
      .get("/userinfo", {
        headers: {
          authorization:
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjE3MDU0MjksInVzZXJJZCI6MSwidXVpZCI6ImU2Yzc2YWEyLTZlOGYtNDQ5Mi1iZTNhLTkzMTZmOWFhNmY5OCIsInVzZXJuYW1lIjoiMTUwMTExMTIyMjIifQ.Orx4Ngmjxcnivl6eg5lHLAzk0zFEMIXkkmiQqUvjY_c",
        },
      })
      .then((res) => {
        console.log("request测试获取用户信息", res);
      })
      .catch(function (error) {})
      .finally(() => {});
    // 测试获取用户信息
    fetch("/userinfo", {
      method: "GET",
      mode: "cors",
      headers: {
        authorization:
          "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjE3MDU0MjksInVzZXJJZCI6MSwidXVpZCI6ImU2Yzc2YWEyLTZlOGYtNDQ5Mi1iZTNhLTkzMTZmOWFhNmY5OCIsInVzZXJuYW1lIjoiMTUwMTExMTIyMjIifQ.Orx4Ngmjxcnivl6eg5lHLAzk0zFEMIXkkmiQqUvjY_c",
      },
    }).then((res) =>
      res.json().then((data) => {
        console.log("fetch测试获取用户信息", data);
      })
    );
    ///////////////////////////////////////////////////
    4;
    //////////////////////////////////////////////////
    //测试添加购物车
    request
      .post(
        "/addcart",
        {
          count: 1,
          idGoods: 1,
          idSku: 1,
        },
        {
          headers: {
            authorization:
              "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjE3MDU0MjksInVzZXJJZCI6MSwidXVpZCI6ImU2Yzc2YWEyLTZlOGYtNDQ5Mi1iZTNhLTkzMTZmOWFhNmY5OCIsInVzZXJuYW1lIjoiMTUwMTExMTIyMjIifQ.Orx4Ngmjxcnivl6eg5lHLAzk0zFEMIXkkmiQqUvjY_c",
          },
        }
      )
      .then((res) => {
        console.log("request测试添加购物车", res);
      })
      .catch(function (error) {})
      .finally(() => {});
    //测试添加购物车
    fetch("/addcart", {
      method: "POST",
      mode: "cors",
      headers: {
        authorization:
          "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjE3MDU0MjksInVzZXJJZCI6MSwidXVpZCI6ImU2Yzc2YWEyLTZlOGYtNDQ5Mi1iZTNhLTkzMTZmOWFhNmY5OCIsInVzZXJuYW1lIjoiMTUwMTExMTIyMjIifQ.Orx4Ngmjxcnivl6eg5lHLAzk0zFEMIXkkmiQqUvjY_c",
      },
      body: JSON.stringify({
        count: 1,
        idGoods: 1,
        idSku: 1,
      }),
    }).then((res) =>
      res.json().then((data) => {
        console.log("fetch测试添加购物车", data);
      })
    );
    ///////////////////////////////////////////////////
    5;
    //////////////////////////////////////////////////
    // 测试详细信息
    request("/detail?id=10")
      .then((res) => {
        console.log("request测试详细信息", res);
      })
      .catch(function (error) {})
      .finally(() => {});
    // 测试详细信息
    fetch("/detail?id=10", {
      method: "GET",
      mode: "cors",
    }).then((res) =>
      res.json().then((data) => {
        console.log("fetch测试详细信息", data);
      })
    );
    ///////////////////////////////////////////////////
    6;
    //////////////////////////////////////////////////
    // 测试退出
    request("/logout").then((res) => {
      console.log("request测试退出", res);
    });
    // 测试退出
    fetch("/logout", {
      method: "GET",
      mode: "cors",
    }).then((res) =>
      res.json().then((data) => {
        console.log("fetch测试退出", data);
      })
    );
    ///////////////////////////////////////////////////
    7;
    //////////////////////////////////////////////////
    // 测试广告
    request("/home/ad").then((res) => {
      console.log("request测试广告", res);
    });
    // 测试广告
    fetch("/home/ad", {
      method: "GET",
      mode: "cors",
    }).then((res) =>
      res.json().then((data) => {
        console.log("fetch测试广告", data);
      })
    );
    ///////////////////////////////////////////////////
    8;
    //////////////////////////////////////////////////
    // 测试热推
    request("/home/hot").then((res) => {
      console.log("request测试热推", res);
    });
    // 测试热推
    fetch("/home/hot", {
      method: "GET",
      mode: "cors",
    }).then((res) =>
      res.json().then((data) => {
        console.log("fetch测试热推", data);
      })
    );
    ///////////////////////////////////////////////////
    9;
    //////////////////////////////////////////////////
    // 测试新品
    request("/home/new").then((res) => {
      console.log("request测试新品", res);
    });
    // 测试新品
    fetch("/home/new", {
      method: "GET",
      mode: "cors",
    }).then((res) =>
      res.json().then((data) => {
        console.log("fetch测试新品", data);
      })
    );
    ///////////////////////////////////////////////////
    10;
    //////////////////////////////////////////////////
    // 测试热搜
    request("/search/hot").then((res) => {
      console.log("request测试热搜", res);
    });
    // 测试热搜
    fetch("/search/hot", {
      method: "GET",
      mode: "cors",
    }).then((res) =>
      res.json().then((data) => {
        console.log("fetch测试热搜", data);
      })
    );
    return {
      data,
      onLoad,
      onRefresh,
    };
  },
};
</script>