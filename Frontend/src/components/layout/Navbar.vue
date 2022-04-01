<template>
  <div>
    <v-app-bar dark color="blue-gray" clipped-left fixed app>
      <v-app-bar-nav-icon
        @click.stop="drawer = !drawer"
        class="hidden-md-and-up"
      ></v-app-bar-nav-icon>
      <v-app-bar-title class="headline text-uppercase white--text">
        <a style="text-decoration: none;" href="/home"><h1 class="font-weight-light mt-3" style="margin-right: 200px; color:white;">와인어때?</h1></a>
      </v-app-bar-title>
      <v-autocomplete
        v-model="model"
        :items="items"
        :loading="isLoading"
        :search-input.sync="search"
        chips
        clearable
        hide-details
        hide-selected
        item-text="name"
        item-value="symbol"
        label="Search"
        solo
      >
        <template v-slot:no-data>
          <v-list-item>
            <v-list-item-title>
              Winery와 Wine명으로 검색해주세요
              <strong>!</strong>
            </v-list-item-title>
          </v-list-item>
        </template>
        <template v-slot:selection="{ attr, on, item, selected }">
          <v-chip
            v-bind="attr"
            :input-value="selected"
            color="blue-grey"
            class="white--text"
            v-on="on"
          >
            <span v-text="item.name"></span>
          </v-chip>
        </template>
        <template v-slot:item="{ item }">
          <v-list-item-avatar
            color="indigo"
            class="text-h5 font-weight-light white--text"
          >
            {{ item.name.charAt(0) }}
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title v-text="item.name"></v-list-item-title>
            <v-list-item-subtitle v-text="item.symbol"></v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-icon>mdi-bitcoin</v-icon>
          </v-list-item-action>
        </template>
      </v-autocomplete>
      <!-- <v-spacer></v-spacer> -->

      <!-- <v-app-bar class="hidden-sm-and-down">
        <v-btn text to="/main">Home</v-btn>
        <v-btn text to="/about">Wine</v-btn>
        <v-btn text to="/recommend">Recommend</v-btn>
        <v-btn text to="/vintage">Vintage</v-btn>
        <v-btn text to="/lounge">Lounge</v-btn>
        <v-btn text to="/login"
          ><img src="@/assets/login.png" style="height: 30px"
        /></v-btn>
        <v-btn text to="/login">login</v-btn>
        <v-btn text to="/signup">SignUp</v-btn>
      </v-app-bar> -->

      <v-tabs dark slider-size:1 right v-if="userstate.islogin == false">
        <v-tab v-for="link in beforelogin" :key="link.name" :to="link.route">
          {{ link.title }}
        </v-tab>
      </v-tabs>

      <v-tabs dark slider-size:1 right v-if="userstate.islogin == true">
        <v-tab
          v-for="link in afterlogin"
          :key="link.name"
          :to="link.route"
          @click="logout(link.name)"
        >
          {{ link.title }}
        </v-tab>
      </v-tabs>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      drawer: null,
      items: [
        { title: "Home", icon: "dashboard", to: "/home" },
        { title: "About", icon: "question_answer", to: "/about" },
      ],
      beforelogin: [
        { title: "Home", name: "Home", route: `/home` },
        { title: "Wine", name: "Wine", route: `/wine` },
        { title: "Recommend", name: "Recommend", route: `/recommend` },
        { title: "Vintage", name: "Vintage", route: `/vintage` },
        { title: "Detail", name: "Detail", route: `/detail` },
        { title: "Login", name: "Login", route: `/user/login` },
        { title: "Signup", name: "Singup", route: `/user/signup` },
      ],

      afterlogin: [
        { title: "Home", name: "Home", route: `/home` },
        { title: "Wine", name: "Wine", route: `/wine` },
        { title: "Recommend", name: "Recommend", route: `/recommend` },
        { title: "Vintage", name: "Vintage", route: `/vintage` },
        { title: "Detail", name: "Detail", route: `/detail` },
        { title: "Mypage", name: "Mypage", route: `/user/mypage` },
        { title: "Logout", name: "Logout" },
      ],

      isLoading: false,
      model: null,
      search: null,
      tab: null,

      user: true,
    };
  },

  computed: {
    userstate() {
      return this.$store.state.userstate;
    },
  },
  methods: {
    signup() {
      this.$router.push({ name: "Signup" });
    },

    logout(name) {
      // 임시로그아웃(API 연동시 user정보 초기화 및 세션스토리지 토큰 초기화 해줘야함)
      if (name === "Logout") {
        this.$store.commit("userstate", false);
        sessionStorage.clear();
        location.reload();
        // this.$router.push({ name: "Home" });
        alert("로그아웃");
      }
    },
  },
};

</script>