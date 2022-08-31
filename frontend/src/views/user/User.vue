<template>
  <div class="page">
    <div style="padding: 20px 10px">
      <!-- 骨架屏，没有登录的时候显示骨架 -->
      <van-skeleton
        title
        avatar
        :row="2"
        :loading="data.user.username ? false : true"
        avatar-size="100"
      >
        <!-- 行显示 -->
        <van-row gutter="20">
          <van-col span="6">
            <div style="width:100px;height:100px;border-radius:50%;overflow:hidden;position:relative">
              <img :src="data.user.avatar" style="height:100px;position:absolute;left:-100px;right:-100px;margin:auto"/>
            </div>
          </van-col>
          <van-col span="18"
            ><div>
              <h4>{{ data.user.username }}</h4>
              <p>{{ data.user.introduce }}</p>
            </div></van-col
          >
        </van-row>
      </van-skeleton>
    </div>
    <!-- 基础设置 -->
    <van-cell-group title="基础设置">
      <van-cell title="订单" icon="balance-o" size="large" is-link @click="openOrder"/>
      <van-cell title="喜欢" icon="like-o" size="large" is-link />
    </van-cell-group>
    <!-- 系统设置 -->
    <van-cell-group title="系统设置">
      <van-cell title="安全中心" icon="setting-o" size="large" is-link />
      <van-cell title="商家中心" icon="shop-o" size="large" is-link />
    </van-cell-group>
    <!-- 账号设置 -->
    <van-cell-group title="账号设置" v-if="data.user.username ? true : false">
      <van-cell title="退出系统" icon="contact" size="large" @click="logout" />
    </van-cell-group>
    <!-- 登录按钮 -->
    <div style="padding: 0px 20px;margin:40px auto 5px" v-if="data.user.username ? false : true">
      <van-button type="primary" size="large" @click="signin">登录</van-button>
    </div>
    <!-- 注册按钮 -->
    <div style="padding: 0px 20px" v-if="data.user.username ? false : true">
      <van-button type="success" size="large" @click="signup">注册</van-button>
    </div>
    <!-- 登录对话框 -->
    <van-dialog
      title="登录"
      confirmButtonText="登录"
      v-model:show="data.signinshow"
      :closeOnClickOverlay="true"
      @confirm="confirm"
    >
      <van-form>
        <!-- 用户名 -->
        <van-field
          v-model="data.username"
          name="用户名"
          label="用户名"
          placeholder="用户名"
          :rules="[{ required: true, message: '请填写用户名' }]"
        />
        <!-- 密码 -->
        <van-field
          v-model="data.password"
          type="password"
          name="密码"
          label="密码"
          placeholder="密码"
          :rules="[{ required: true, message: '请填写密码' }]"
        />
      </van-form>
    </van-dialog>
    <!-- 注册对话框 -->
    <van-dialog
      title="注册"
      confirmButtonText="注册"
      v-model:show="data.signupshow"
      :closeOnClickOverlay="true"
      @confirm="upconfirm"
    >
      <van-form>
        <!-- 用户名 -->
        <van-field
          v-model="data.upusername"
          name="用户名"
          label="用户名"
          placeholder="用户名"
          :rules="[{ required: true, message: '请填写用户名' }]"
        />
        <!-- 密码 -->
        <van-field
          v-model="data.uppassword"
          type="password"
          name="密码"
          label="密码"
          placeholder="密码"
          :rules="[{ required: true, message: '请填写密码' }]"
        />
      </van-form>
    </van-dialog>
  </div>
</template>
<script>
import { onMounted, reactive } from "vue";
import { request } from "../../utils/request";
import { useRouter } from 'vue-router';
export default {
  setup() {
    const data = reactive({
      user: {},
      signinshow: false,
      signupshow: false,
      username: "admin",
      password: "admin",
      upusername: "",
      uppassword: "",
    });
    const router = useRouter();
    const signin = () => {
      data.signinshow = true;
    };
    const signup = () => {
      data.signupshow = true;
    };
    const confirm = () => {
      // post登录请求,提交用户名和密码
      request
        .post("/signin/", {
          username: data.username,
          password: data.password,
        })
        .then((res) => {
          data.user = res.data[0].fields;
          // 存储到本地存储
          localStorage.user = JSON.stringify(data.user);
        });
    };
    const upconfirm = () => {
      // post登录请求,提交用户名和密码
      request
        .post("/signup/", {
          username: data.upusername,
          password: data.uppassword,
        })
        .then((res) => {
          data.user = res.data[0].fields;
          // 存储到本地存储
          localStorage.user = JSON.stringify(data.user);
        });
    };
    // 退出登录
    const logout = () => {
      data.user = {};
      localStorage.removeItem("user");
    };
    // 打开订单页
    const openOrder = () => {
      router.push({
        name: "订单",
      });
    }
    onMounted(() => {
      // localStorage.removeItem("user");
      try {
        data.user = JSON.parse(localStorage.user);
      } catch {}
    });
    return {
      data,
      signin,
      signup,
      confirm,
      upconfirm,
      logout,
      openOrder,
    };
  },
};
</script>