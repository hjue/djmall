export default [
  {
    url: "/api/get",
    method: "get",
    response: ({ query }) => {
      return {
        code: 0,
        data: ["测试", query],
      };
    },
  },
  {
    url: "/api/post",
    method: "post",
    timeout: 2000,
    response: {
      code: 0,
      data: {
        name: "测试",
      },
    },
  },
];
