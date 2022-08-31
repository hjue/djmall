export default [
  {
    url: "/logout",
    method: "get",
    response: (query) => {
      return { code: 20000, msg: "成功", data: null, success: true };
    },
  },
];
