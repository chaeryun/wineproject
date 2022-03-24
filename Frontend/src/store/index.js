import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

import memberStore from "@/store/modules/memberStore.js";

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: { memberStore },
  plugins: [
    createPersistedState({
      storage: sessionStorage,
    }),
  ],
});
