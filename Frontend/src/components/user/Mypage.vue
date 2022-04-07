<template>
  <div class="wine mt-13">
    <v-container>
      <h1 class="mb-10">
        <span
          style="
            text-align: center;
            border-radius: 15px 15px 15px 0;
            border: 3px solid #ffad5b;
            padding: 0.5em 0.6em;
            color: bullywood;
          "
          >My page</span
        >
      </h1>
      <v-row class="text-h7" justify="center">
        <h2 class="ml-10 pb-5">| {{ userInfo.nickname }}님이 찜한 목록</h2>
      </v-row>

      <!-- 텅빌때, 수정하세여!!-->
      <template v-if = " winelistIsEmpty" >
        <div class="justify-center mt-15" style="display:flex;">
      <img src="../../assets/no_wine.png" style="width:70px; height:65px;" alt="empty" />
      <h2 class="ml-5 mt-4 mb-15 pb-15">찜한 와인이 없습니다. 마음에 드는 와인을 찜해주세요.</h2>
      </div >
      </template>

      <v-row v-else justify="center" class="mb-5">
        <v-col cols="2" v-for="wine in userwishlist" :key="wine.wine_id">
          <v-card
            class="mt-10"
            style="
              height: 450px;
              margin: auto;
              border-radius: 90px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn
              class="mt-7 ml-15"
              text
              icon
              large
              :color="
                wine.color == 'white'
                  ? 'green lighten-3'
                  : wine.color == 'red'
                  ? 'red'
                  : wine.color == 'rose'
                  ? 'red lighten-3'
                  : wine.color == 'port'
                  ? 'blue lighten-3'
                  : 'purple lighten-2'
              "
            >
              <v-icon>mdi-circle</v-icon> {{ wine.color }}
            </v-btn>

            <v-img
              :src="wine.image"
              height="250"
              contain
              @click="winedetail(wine.wine_id)"
            /><v-img />
            <hr
              style="border-width: 2px; border-color: pink; margin-bottom: 5px"
            />
            <v-card-text class="text-center fs-5" style="color: gainsboro"
              >{{ wine.wine }}<br />
              <br />
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import http from "@/util/http-common";

export default {
  name: "mypage",
  components: {},

  data: () => ({
    // username 호출시 반환된 데이터 저장
    wishlist: [],

    // wineid로 호출한 wine 데이터 저장
    userwishlist: [],
  }),

  computed: {
    // user 정보 가져오기
    userInfo() {
      return this.$store.state.userInfo;
    },
    winelistIsEmpty(){
      console.log(this.wishlist.length);
      return this.wishlist.length==0;
    }
  },

  created() {
    this.getUserWine();
  },

  methods: {
    async getUserWine() {
      await http({
        methods: "get",
        url: "wine/latest_wine_totallist/" + this.userInfo.username + "/",
      })
        .then((res) => {
          // console.log("winelist : ", res.data);
          this.wishlist = res.data;

          // wine_id check
          for (let i = 0; i < this.wishlist.length; i++) {
            // console.log("winenumber", this.wishlist[i].wine);
            this.getwishlist(this.wishlist[i].wine);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // wine_id로 winelist 받아오기
    async getwishlist(wine_id) {
      await http({
        methods: "get",
        url: "wine/get_wine_data/" + wine_id + "/",
      })
        .then((res) => {
          // console.log(res);
          // wine data list에 추가
          this.userwishlist.push(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // 와인상세페이지로 이동
    winedetail(wine_id) {
      this.$router.push({ path: "/detail", query: { wine_id: wine_id } });
    },
  },
};
</script>

<style></style>
