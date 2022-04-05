<template>
  <div class="wine mt-13">
    <v-container>
      <!-- <h1>추천 받기</h1> -->
      <v-row class="text-h7" justify="center">
        <h2 class="ml-10 mt-10 pb-5">| OO님이 최근 찜한 와인</h2>
        <h5 class="ml-12 pb-5">oo님이 찜한 와인 목록을 기반으로 유사한 취향의 와인을 추천해드립니다.</h5>
      </v-row>
      <v-row justify="center" class="mb-5">
        <v-col cols="2" v-for="wine in userwishlist" :key="wine.wine_id">
          <v-card
            class="mx-auto"
            style="
              height: 450px;
              margin: auto;
              border-radius: 50px;
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
            <v-card-text
              class="text-center fs-5"
              style="color: gainsboro"
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

      <!-- 와인타입 선택바 -->
      <v-bottom-navigation color="warning" width="450px" style="border-radius: 20px; margin-left: 15px; background-color: cornsilk;">
        <v-btn value="red" @click="typered">
          <span class="fs-6">Red</span>
          <img src="../assets/red.png" style="width:30px; height:30px;" />
        </v-btn>

        <v-btn value="white" @click="typewhite">
          <span class="fs-6">White</span>
          <img src="../assets/white.png" style="width:30px; height:30px;" />
        </v-btn>

        <v-btn value="rose" @click="typerose">
          <span class="fs-6">Rose</span>
          <img src="../assets/rose.png" style="width:30px; height:30px;" />
        </v-btn>

        <v-btn value="sparkling" @click="typesparkling">
          <span class="fs-6">Sparkling</span>
          <img src="../assets/sparkling.png" style="width:30px; height:30px;" />
        </v-btn>

        <v-btn value="port" @click="typeport">
          <span class="fs-6">Port</span>
          <img src="../assets/port.png" style="width:30px; height:30px;" />
        </v-btn>
      </v-bottom-navigation>


      <v-row justify="center" class="mb-5 mt-5">
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
