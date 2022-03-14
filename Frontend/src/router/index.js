import Vue from "vue";
import VueRouter from "vue-router";

import Intro from "../views/Intro.vue";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Intro",
    component: Intro,
  },
  {
    path: "/main",
    name: "Home",
    component: Home,
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
