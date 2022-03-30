import { apiInstance } from "./index.js";

const api = apiInstance();

async function findById(username, success, fail) {
  api.defaults.headers["access-token"] = sessionStorage.getItem("access-token");
  await api.get(`/accounts/get_user/${username}`).then(success).catch(fail);
}

export { findById };
