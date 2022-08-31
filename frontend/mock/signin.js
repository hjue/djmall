export default [
  {
    url: "/signin",
    method: "post",
    response: (query) => {
      if (
        query.body.username == "15011112222" &&
        query.body.password == "admin"
      ) {
        return {
          code: 20000,
          msg: "成功",
          success: true,
          data: {
            user: {
              mobile: "15011112222",
              avatar: "fdc78c42-e0ee-41c5-b813-4fb86be4b6ad.jpg",
              nickname: "艾尼路",
              introduce: "一个喜欢购物的穷光蛋",
              lastLoginTime: "2021-04-23 01:43:49",
              gender: "male",
              wechatNickName: null,
              wechatHeadImgUrl: null,
              refreshWechatInfo: true,
            },
            token:
              "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjE3MDU0MjksInVzZXJJZCI6MSwidXVpZCI6ImU2Yzc2YWEyLTZlOGYtNDQ5Mi1iZTNhLTkzMTZmOWFhNmY5OCIsInVzZXJuYW1lIjoiMTUwMTExMTIyMjIifQ.Orx4Ngmjxcnivl6eg5lHLAzk0zFEMIXkkmiQqUvjY_c",
          },
        };
      }
    },
  },
];
