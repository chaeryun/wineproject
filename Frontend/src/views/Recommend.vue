<template>
  <div class="wine mt-13">
    <v-container>
      <h1>Recommend</h1>
      <v-row class="text-h7" justify="center">
        <h2 class="ml-10 pb-5">| 최근 찜한 목록</h2>
      </v-row>
      <v-row justify="center" class="mb-5">
        <v-col cols="2" v-for="wine in userwishlist" :key="wine.wine_id">
          <v-card
            class="mx-auto"
            max-width="260"
            style="
              border-radius: 200px;
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
              height="200"
              contain
              style="margin-bottom: 50px"
              @click="winedetail(wine.wine_id)"
            /><v-img />
            <hr
              style="border-width: 2px; border-color: pink; margin-bottom: -5px"
            />
            <v-card-text
              class="text-center fs-5"
              style="margin-top: -12px; color: gainsboro"
              >{{ wine.wine }}<br />
              <br />
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <v-row
        class="pa-5-mt-1 text-h7 pt-10 pb-5 mt-10"
        justify="center"
        height="200"
      >
        <h2 class="ml-10">| OO님과 유사한 취향의 와인</h2>
      </v-row>
      <v-row justify="center" class="mb-5">
        <v-col cols="3">
          <v-card
            class="mx-auto"
            max-width="380"
            style="
              border-radius: 100px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-5 ml-10" text icon large color="red lighten-2">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample1.png')"
                height="300"
                contain
              /><v-img />
              <hr style="border-width: 2px; border-color: pink" />
              <v-card-title class="justify-center" style="padding-top: 1px"
                ><div>Dom Pérignon</div>
                P2 Plénitude Brut Champagne 1995</v-card-title
              >
              <v-card-text class="text-center fs-5"
                >#France #Sparkling</v-card-text
              >
            </a>
          </v-card>
        </v-col>

        <v-col cols="3">
          <v-card
            class="mx-auto"
            max-width="380"
            style="
              border-radius: 100px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-5 ml-10" text icon large color="red lighten-2">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample2.png')"
                height="300"
                contain
              /><v-img />
              <hr style="border-width: 2px; border-color: pink" />
              <v-card-title class="justify-center" style="padding-top: 1px"
                ><div>Dom Pérignon</div>
                P2 Plénitude Brut Champagne 1995</v-card-title
              >
              <v-card-text class="text-center fs-5"
                >#France #Sparkling</v-card-text
              >
            </a>
          </v-card>
        </v-col>

        <v-col cols="3">
          <v-card
            class="mx-auto"
            max-width="380"
            style="
              border-radius: 100px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-5 ml-10" text icon large color="red lighten-2">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample3.png')"
                height="300"
                contain
              /><v-img />
              <hr style="border-width: 2px; border-color: pink" />
              <v-card-title class="justify-center" style="padding-top: 1px"
                ><div>Dom Pérignon</div>
                P2 Plénitude Brut Champagne 1995</v-card-title
              >
              <v-card-text class="text-center fs-5"
                >#France #Sparkling</v-card-text
              >
            </a>
          </v-card>
        </v-col>

        <v-col cols="3">
          <v-card
            class="mx-auto"
            max-width="380"
            style="
              border-radius: 100px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-5 ml-10" text icon large color="red lighten-2">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample3.png')"
                height="300"
                contain
              /><v-img />
              <hr style="border-width: 2px; border-color: pink" />
              <v-card-title class="justify-center" style="padding-top: 1px"
                ><div>Dom Pérignon</div>
                P2 Plénitude Brut Champagne 1995</v-card-title
              >
              <v-card-text class="text-center fs-5"
                >#France #Sparkling</v-card-text
              >
            </a>
          </v-card>
        </v-col>
      </v-row>
      <v-row justify="center" class="mb-5">
        <v-col cols="3">
          <v-card
            class="mx-auto"
            max-width="380"
            style="
              border-radius: 100px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-5 ml-10" text icon large color="red lighten-2">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample1.png')"
                height="300"
                contain
              /><v-img />
              <hr style="border-width: 2px; border-color: pink" />
              <v-card-title class="justify-center" style="padding-top: 1px"
                ><div>Dom Pérignon</div>
                P2 Plénitude Brut Champagne 1995</v-card-title
              >
              <v-card-text class="text-center fs-5"
                >#France #Sparkling</v-card-text
              >
            </a>
          </v-card>
        </v-col>

        <v-col cols="3">
          <v-card
            class="mx-auto"
            max-width="380"
            style="
              border-radius: 100px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-5 ml-10" text icon large color="red lighten-2">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample2.png')"
                height="300"
                contain
              /><v-img />
              <hr style="border-width: 2px; border-color: pink" />
              <v-card-title class="justify-center" style="padding-top: 1px"
                ><div>Dom Pérignon</div>
                P2 Plénitude Brut Champagne 1995</v-card-title
              >
              <v-card-text class="text-center fs-5"
                >#France #Sparkling</v-card-text
              >
            </a>
          </v-card>
        </v-col>

        <v-col cols="3">
          <v-card
            class="mx-auto"
            max-width="380"
            style="
              border-radius: 100px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-5 ml-10" text icon large color="red lighten-2">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample3.png')"
                height="300"
                contain
              /><v-img />
              <hr style="border-width: 2px; border-color: pink" />
              <v-card-title class="justify-center" style="padding-top: 1px"
                ><div>Dom Pérignon</div>
                P2 Plénitude Brut Champagne 1995</v-card-title
              >
              <v-card-text class="text-center fs-5"
                >#France #Sparkling</v-card-text
              >
            </a>
          </v-card>
        </v-col>

        <v-col cols="3">
          <v-card
            class="mx-auto"
            max-width="380"
            style="
              border-radius: 100px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-5 ml-10" text icon large color="red lighten-2">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample3.png')"
                height="300"
                contain
              /><v-img />
              <hr style="border-width: 2px; border-color: pink" />
              <v-card-title class="justify-center" style="padding-top: 1px"
                ><div>Dom Pérignon</div>
                P2 Plénitude Brut Champagne 1995</v-card-title
              >
              <v-card-text class="text-center fs-5"
                >#France #Sparkling</v-card-text
              >
            </a>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import http from "@/util/http-common";

export default {
  name: "Recommend",
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
  },

  created() {
    // user 와인 가져오기
    this.getUserWine();

    // Recommand와인 가져오기
    // this.recommandWine();
  },
  methods: {
    async getUserWine() {
      await http({
        methods: "get",
        url: "wine/latest_wine_list/" + this.userInfo.username + "/",
      })
        .then((res) => {
          // console.log("winelist : ", res.data);
          this.wishlist = res.data;

          // wine_id check
          for (let i = 0; i < this.wishlist.length; i++) {
            // console.log("winenumber", this.wishlist[i].wine);
            this.getwishlist(this.wishlist[i].wine);
          }
          // wine_id로 winelist 받아오기
        })
        .catch((err) => {
          console.log(err);
        });
    },

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

    // async recommandWine() {
    //   await http({
    //     methods: "get",
    //     url: "wine/recommnad/latest_wishlist/" + this.userInfo.username + "/",
    //   })
    //     .then((res) => {
    //       console.log(res);
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    // },
  },
};
</script>

<style></style>
