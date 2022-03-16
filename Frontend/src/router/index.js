import Vue from "vue";
import VueRouter from "vue-router";

import Intro from "@/views/Intro.vue";
import Home from "@/views/Home.vue";

import User from "@/views/User.vue";
import Signup from "@/components/user/Signup.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Intro",
    component: Intro,
  },
  {
    path: "/home",
    name: "Home",
    component: Home,
  },

  {
    path: "/user",
    name: "User",
    component: User,
    children: [
      {
        path: "signup",
        name: "Signup",
        component: Signup,
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
