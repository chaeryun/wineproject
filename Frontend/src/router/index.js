import Vue from "vue";
import VueRouter from "vue-router";

import Intro from "@/views/Intro.vue";
import Home from "@/views/Home.vue";
import Detail from "@/views/Detail.vue";
import Wine2 from "@/views/Wine2.vue";
import Vintage from "@/views/Vintage.vue";
import Recommend from "@/views/Recommend.vue";
import About from "@/views/About.vue";

import User from "@/views/User.vue";
import Signup from "@/components/user/Signup.vue";
import Userlogin from "@/components/user/login.vue";
import Mypage from "@/components/user/Mypage.vue";

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
    path: "/detail",
    name: "Detail",
    component: Detail,
  },
  {
    path: "/wine",
    name: "Wine2",
    component: Wine2,
  },
  {
    path: "/recommend",
    name: "Recommend",
    component: Recommend,
  },
  {
    path: "/vintage",
    name: "Vintage",
    component: Vintage,
  },
  {
    path: "/about",
    name: "About",
    component: About,
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
      {
        path: "login",
        name: "login",
        component: Userlogin,
      },
      {
        path: "mypage",
        name: "Mypage",
        component: Mypage,
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
