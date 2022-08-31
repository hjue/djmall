export default [
  {
    url: "/userinfo",
    method: "get",
    response: (query) => {
      if (
        query.headers.authorization ==
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjE3MDU0MjksInVzZXJJZCI6MSwidXVpZCI6ImU2Yzc2YWEyLTZlOGYtNDQ5Mi1iZTNhLTkzMTZmOWFhNmY5OCIsInVzZXJuYW1lIjoiMTUwMTExMTIyMjIifQ.Orx4Ngmjxcnivl6eg5lHLAzk0zFEMIXkkmiQqUvjY_c"
      ) {
        return {
          code: 20000,
          msg: "成功",
          success: true,
          data: {
            user: {
              mobile: "15011112222",
              avatar: "449c2a9d-a7f9-4dd7-b0b2-a176ff8bf25a.jpeg",
              nickName: "艾尼路",
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
