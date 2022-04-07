<template>
  <v-app id="inspire">
    <!-- <v-row>
      <v-carousel
        cycle
        height="700"
        hide-delimiter-background
        show-arrows-on-hover
      >
        <v-carousel-item v-for="wine in wines" :key="wine.name">
          <v-sheet height="100%">
            <v-row class="fill-height" align="center" justify="center">
              <img :src="wine.picture" alt="img" height="710" />
            </v-row>
          </v-sheet>
        </v-carousel-item>
      </v-carousel>
    </v-row> -->

    <video autoplay loop muted>
      <source src="../assets/video/wine.mp4" type="video/mp4" />
    </video>
    <br />
    <br />

    <v-row class="text-h7 text-center" justify="center">
      <!-- <h1 class="mt-10 mb-10">요즘 인기 많은 와인</h1> -->
      <!--       
<h1><span style="border-bottom: 12px solid #dcf1fb; padding: 0 0 0 0.2em;" class="mb-10 mt-10">인기 와인</span></h1> -->
      <h1 class="mb-10 mt-15">
        <span
          style="
            text-align: center;
            border-radius: 15px 15px 15px 0;
            border: 3px solid #ffad5b;
            padding: 0.5em 0.6em;
            color: #ff8000;
          "
          >인기 폭발 와인</span
        >
      </h1>

      <!-- 와인타입 선택바 -->
      <div style="position: relative; left: 9%; padding-top: 30px">
        <v-bottom-navigation
          color="#CD5C5C"
          width="450px"
          style="
            border-radius: 30px;
            margin-left: 10px;
            background-color: #ffdead;
            text-align: center;
          "
        >
          <v-btn value="red" @click="redReview">
            <span class="fs-6">Red</span>
          </v-btn>

          <v-btn value="white" @click="whiteReview">
            <span class="fs-6">White</span>
          </v-btn>

          <v-btn value="rose" @click="roseReview">
            <span class="fs-6">Rose</span>
          </v-btn>

          <v-btn value="sparkling" @click="sparklingReview">
            <span class="fs-6">Sparkling</span>
          </v-btn>

          <v-btn value="port" @click="portReview">
            <span class="fs-6">Port</span>
          </v-btn>
        </v-bottom-navigation>
      </div>
    </v-row>

    <v-row style="justify-content: center">
      <div class="col-2" :key="i" v-for="(wine, i) in reviewlist">
        <v-card
          class="mx-auto mt-10"
          max-width="380"
          style="
            border-radius: 100px;
            height: 360px;
            color: gainsboro;
            background-color: #232320;
            box-shadow: 0 0 10px grey;
          "
          hover
          outlined
        >
          <v-btn
            class="mt-6 pl-10 ml-8"
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
            height="270"
            alt="No image"
            contain
            @click="winedetail(wine.wine_id)"
          /><v-img />
          <br />
          <hr
            style="border-width: 2px; border-color: pink; margin-bottom: -5px"
          />
          <v-card-title class="justify-center"
            >[{{ wine.winery }}]</v-card-title
          >
          <v-card-text
            class="text-center fs-5"
            style="margin-top: -12px; color: gainsboro"
            >{{ wine.wine }}<br />
            <br />
          </v-card-text>
          <div class="d-flex justify-content-between align-items-center"></div>
        </v-card>
      </div>
    </v-row><br /><br />

    <v-row class="pt-15 mt-15 text-h7" style="justify-content: center">
      <!-- <h1 class="mt-10 mb-10">만족도 높은 와인</h1> -->
      <h1 class="mb-10 mt-15">
        <span
          style="
            text-align: center;
            border-radius: 15px 15px 15px 0;
            border: 3px solid #ffad5b;
            padding: 0.5em 0.6em;
            color: #ff8000;
          "
          >만족도 높은 와인</span
        >
      </h1>
    </v-row>
    <!-- 와인타입 선택바 -->
    <div style="position: relative; left: 9%; padding-top: 30px">
      <v-bottom-navigation
        color="#CD5C5C"
        width="450px"
        style="
          border-radius: 30px;
          margin-left: 10px;
          background-color: #ffdead;
          text-align: center;
        "
      >
        <v-btn value="red" @click="redScore">
          <span class="fs-6">Red</span>
        </v-btn>

        <v-btn value="white" @click="whiteScore">
          <span class="fs-6">White</span>
        </v-btn>

        <v-btn value="rose" @click="roseScore">
          <span class="fs-6">Rose</span>
        </v-btn>

        <v-btn value="sparkling" @click="sparklingScore">
          <span class="fs-6">Sparkling</span>
        </v-btn>

        <v-btn value="port" @click="portScore">
          <span class="fs-6">Port</span>
        </v-btn>
      </v-bottom-navigation>
    </div>

    <v-row style="justify-content: center">
      <div class="col-2" :key="i" v-for="(wine, i) in scorelist">
        <v-card
          class="mx-auto mt-10"
          max-width="380"
          style="
            border-radius: 100px;
            height: 360px;
            color: gainsboro;
            background-color: #232320;
            box-shadow: 0 0 10px grey;
          "
          hover
          outlined
        >
          <v-btn
            class="mt-5 ml-10 pl-8"
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
            height="280"
            alt="No image"
            contain
            @click="winedetail(wine.wine_id)"
          /><v-img />
          <br />
          <hr
            style="border-width: 2px; border-color: pink; margin-bottom: -5px"
          />
          <v-card-title class="justify-center"
            >[{{ wine.winery }}]</v-card-title
          >
          <v-card-text
            class="text-center fs-5"
            style="margin-top: -12px; color: gainsboro"
            >{{ wine.wine }}<br />
            <br />
          </v-card-text>
          <div class="d-flex justify-content-between align-items-center"></div>
        </v-card>
      </div>
    </v-row>
    <div class="mt-15 mb-15 pt-15 pb-15"></div>
  </v-app>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "Home",
  components: {},
  data() {
    return {
      wines: [
        { name: "wine7", picture: require("@/assets/reco7.png") },
        { name: "wine2", picture: require("@/assets/reco2.jpg") },
      ],

      // type default value="red"
      scorecolor: "red",
      reviewcolor: "red",

      // Score 기반 리스트
      scorelist: [],
      reviewlist: [],
    };
  },

  created() {
    // Score 기반 추천
    this.recoScore();

    // reviews 기반 추천
    this.recoReview();
  },

  methods: {
    // Score 기반 와인 데이터 가져오기
    async recoScore() {
      await http({
        method: "get",
        url: "wine/recommand/color_score/" + this.scorecolor + "/",
      })
        .then((res) => {
          // console.log("recoScore", res.data);
          this.scorelist = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // Review 기반 와인 데이터 가져오기
    async recoReview() {
      await http({
        method: "get",
        url: "wine/recommand/reviews/" + this.reviewcolor + "/",
      })
        .then((res) => {
          // console.log("recoReview", res.data);
          this.reviewlist = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    redScore() {
      this.scorecolor = "red";
      // type별 와인 데이터 불러오기
      this.scoretype();
    },

    whiteScore() {
      this.scorecolor = "white";
      // type별 와인 데이터 불러오기
      this.scoretype();
    },

    roseScore() {
      this.scorecolor = "rose";
      // type별 와인 데이터 불러오기
      this.scoretype();
    },

    sparklingScore() {
      this.scorecolor = "sparkling";
      // type별 와인 데이터 불러오기
      this.scoretype();
    },

    portScore() {
      this.scorecolor = "port";
      // type별 와인 데이터 불러오기
      this.scoretype();
    },

    async scoretype() {
      await http({
        method: "get",
        url: "wine/recommand/color_score/" + this.scorecolor + "/",
      })
        .then((res) => {
          console.log("scoretype", res.data);
          this.scorelist = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    redReview() {
      this.reviewcolor = "red";
      this.reviewtype();
    },

    whiteReview() {
      this.reviewcolor = "white";
      this.reviewtype();
    },

    roseReview() {
      this.reviewcolor = "rose";
      this.reviewtype();
    },

    sparklingReview() {
      this.reviewcolor = "sparkling";
      this.reviewtype();
    },

    portReview() {
      this.reviewcolor = "port";
      this.reviewtype();
    },

    async reviewtype() {
      await http({
        method: "get",
        url: "wine/recommand/reviews/" + this.reviewcolor + "/",
      })
        .then((res) => {
          console.log("reviewtype", res.data);
          this.reviewlist = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // 와인 상세페이지 이동
    winedetail(wine_id) {
      this.$router.push({ path: "/detail", query: { wine_id: wine_id } });
    },
  },
};
</script>
<style>
video {
  /* min-width: 100%;
  width: auto; height: auto;
  object-fit: cover;  */
  width: 100%;
  height: 780px;
  object-fit: fill;
}
</style>
