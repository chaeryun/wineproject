import axios from "axios";

export default {
  axios: axios.create({
    baseURL: "https://localhost:8080",
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTION",
      "Access-Control-Allow-Headers":
        "Origin,Accept,X-Requested-With,Content-Type,Access-Control-Request-Method,Access-Control-Request-Headers,Authorization",
      "Access-Control-Expose-Headers": "Content-Length,Content-Range",
    },
  }),
};
