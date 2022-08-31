export default [
  {
    url: "/addcart",
    method: "post",
    response: (query) => {
      if (query.body.count && query.body.idGoods && query.body.idSku) {
        return { code: 20000, msg: "成功", data: 1, success: true };
      }
    },
  },
];
