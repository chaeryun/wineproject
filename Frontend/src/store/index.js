import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

import memberStore from "@/store/modules/memberStore.js";

export default new Vuex.Store({
  state: {
    // 유저상태 저장(login, logout)
    userstate: {
      islogin: false,
    },

    // 유저정보 저장
    member: {
      id: null,
      password: null,
      nickname: null,
      email: null,
    },
  },
  mutations: {
    userstate(state, data) {
      state.userstate.islogin = data;
    },
  },
  actions: {},
  modules: { memberStore },
  plugins: [
    createPersistedState({
      storage: sessionStorage,
    }),
  ],
});
