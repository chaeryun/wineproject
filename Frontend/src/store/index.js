import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import jwt_decode from "jwt-decode";
import { findById } from "@/api/member.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // 유저상태 저장(login, logout)
    userstate: {
      islogin: false,
    },

    // 유저정보 저장
    userInfo: {
      username: null,
      nickname: null,
      email: null,
    },

    userlist: [],
  },
  mutations: {
    userstate(state, data) {
      state.userstate.islogin = data;
    },

    user(state, data) {
      state.userInfo = data;
    },

    SET_USER_INFO: (state, userInfo) => {
      state.userstate.isLogin = true;
      state.userInfo = userInfo;
    },

    userlist(state, data) {
      state.userlist = data;
    },
  },
  actions: {
    getUserInfo({ commit }, token) {
      let decode_token = jwt_decode(token);
      console.log("token : ", decode_token);
      findById(
        decode_token.username,
        (response) => {
          if (response.data.message === "success") {
            commit("SET_USER_INFO", response.data.userInfo);
          } else {
            console.log("유저 정보 없음!!");
          }
        },
        (error) => {
          console.log("여기서", error);
        }
      );
    },
  },

  modules: {},
  plugins: [
    createPersistedState({
      storage: sessionStorage,
    }),
  ],
});
