import axios from "axios";

export default axios.create({
  baseURL: location.origin+"/api",
  headers: {
    "Content-type": "application/json",
  },
});
