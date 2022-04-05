<template>
  <v-app id="inspire">
    <v-row>
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
    </v-row>
    <br />
    <br />

    <v-row class="text-h7" justify="center">
      <h1 class="mt-10 mb-10">요즘 인기 많은 와인</h1>
    </v-row>
    <!-- 와인타입 선택바 -->
    <div style="position: relative; left: 15%; margin-bottom: 30px">
      <v-bottom-navigation
        color="warning"
        width="450px"
        style="
          border-radius: 20px;
          margin-left: 10px;
          background-color: cornsilk;
          text-align: center;
        "
      >
        <v-btn value="red" @click="redReview">
          <span class="fs-6">Red</span>
          <img src="../assets/red.png" style="width: 30px; height: 30px" />
        </v-btn>

        <v-btn value="white" @click="whiteReview">
          <span class="fs-6">White</span>
          <img src="../assets/white.png" style="width: 30px; height: 30px" />
        </v-btn>

        <v-btn value="rose" @click="roseReview">
          <span class="fs-6">Rose</span>
          <img src="../assets/rose.png" style="width: 30px; height: 30px" />
        </v-btn>

        <v-btn value="sparkling" @click="sparklingReview">
          <span class="fs-6">Sparkling</span>
          <img
            src="../assets/sparkling.png"
            style="width: 30px; height: 30px"
          />
        </v-btn>

        <v-btn value="port" @click="portReview">
          <span class="fs-6">Port</span>
          <img src="../assets/port.png" style="width: 30px; height: 30px" />
        </v-btn>
      </v-bottom-navigation>
    </div>

    <v-row>
      <div
        class="col-xl-3 col-lg-4 col-md-6"
        :key="i"
        v-for="(wine, i) in reviewlist"
      >
        <v-card
          class="mx-auto mt-10"
          max-width="380"
          style="
            border-radius: 100px;
            height: 530px;
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
            height="300"
            alt="No image"
            contain
            @click="winedetail(wine.wine_id)"
          /><v-img />
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

    <v-row class="pa-2 mt-15 text-h7" justify="center">
      <h1 class="mt-10 mb-10">만족도 높은 와인</h1>
    </v-row>
    <!-- 와인타입 선택바 -->
    <div style="position: relative; left: 15%; margin-bottom: 30px">
      <v-bottom-navigation
        color="warning"
        width="450px"
        style="
          border-radius: 20px;
          margin-left: 10px;
          background-color: cornsilk;
        "
      >
        <v-btn value="red" @click="redScore">
          <span class="fs-6">Red</span>
          <img src="../assets/red.png" style="width: 30px; height: 30px" />
        </v-btn>

        <v-btn value="white" @click="whiteScore">
          <span class="fs-6">White</span>
          <img src="../assets/white.png" style="width: 30px; height: 30px" />
        </v-btn>

        <v-btn value="rose" @click="roseScore">
          <span class="fs-6">Rose</span>
          <img src="../assets/rose.png" style="width: 30px; height: 30px" />
        </v-btn>

        <v-btn value="sparkling" @click="sparklingScore">
          <span class="fs-6">Sparkling</span>
          <img
            src="../assets/sparkling.png"
            style="width: 30px; height: 30px"
          />
        </v-btn>

        <v-btn value="port" @click="portScore">
          <span class="fs-6">Port</span>
          <img src="../assets/port.png" style="width: 30px; height: 30px" />
        </v-btn>
      </v-bottom-navigation>
    </div>

    <v-row>
      <div
        class="col-xl-3 col-lg-4 col-md-6"
        :key="i"
        v-for="(wine, i) in scorelist"
      >
        <v-card
          class="mx-auto mt-10"
          max-width="380"
          style="
            border-radius: 100px;
            height: 530px;
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
            height="300"
            alt="No image"
            contain
            @click="winedetail(wine.wine_id)"
          /><v-img />
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
    <br />
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
        { name: "wine2", picture: require("@/assets/reco2.jpg") },
        { name: "wine5", picture: require("@/assets/wine5.jpg") },
        { name: "wine7", picture: require("@/assets/reco7.png") },
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
          console.log("recoScore", res.data);
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
          console.log("recoReview", res.data);
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
  },
};
</script>
<style></style>
