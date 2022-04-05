<template>
  <div>
    <!-- <h1 class="text-center mt-13 fw-bold">Detail</h1> -->
    <main>
      <div class="container">
        <div>
          <div class="row my-border text-start">
            <div class="col-3 text-center">
              <img id="wine-img" :src="this.winedetail.image" alt="..." />
              <div>
                <br />
                <v-btn
                  right
                  class="fs-3"
                  text
                  icon
                  large
                  color="red lighten-3"
                  @click="wishlist"
                >
                  <v-icon>mdi-heart</v-icon> Wish List
                </v-btn>
              </div>
            </div>
            <div class="col-5 shadow-sm">
              <div class="fs-4 fw-bold pb-6 pt-8 pl-3">INFORAMTION</div>
              <div class="card-body">
                <h4 class="fw-bold card-title pb-1 fs-3">
                  {{ this.winedetail.wine }}
                  {{ this.winedetail.location }}
                </h4>
                <h4 class="pt-5 pb-3 border-top">
                  <span class="badge outlined" id="my-badge"> Wine Type</span>
                  {{ this.winedetail.color }}
                </h4>
                <div class="card-text border-top pt-3 pb-3">
                  <h4 class="pt-3 pb-3">
                    <span class="badge" id="my-badge"> Winery </span>
                    {{ this.winedetail.winery }}
                  </h4>
                  <h4 class="pt-3 pb-3">
                    <span class="badge" id="my-badge"> Wine name</span>
                    {{ this.winedetail.wine }}
                  </h4>
                  <h4 class="pt-3 pb-3">
                    <span class="badge" id="my-badge"> Country</span>
                    {{ this.winedetail.country }}
                  </h4>
                  <h4 class="pt-3 pb-3">
                    <span class="badge" id="my-badge"> Grpaes </span>
                    {{ this.winedetail.grapes }}
                  </h4>
                  <h4 class="pt-3 pb-3">
                    <span class="badge" id="my-badge"> Alcohol </span>
                    {{ this.winedetail.alcohol }}%
                  </h4>
                  <h4 class="card-title pt-5 border-top">
                    <span class="badge" id="my-badge"> Price </span>
                    {{ this.winedetail.price }}원
                  </h4>
                </div>
              </div>
              <br />
            </div>
            <div class="col-4">
              <div class="fs-4 fw-bold pb-6 pl-10 pt-8">BOUQUET</div>
              <span class="pl-3" :key="taste" v-for="taste in tastes">
                <span style="display:inline-flex; margin-left:40px;">
                  <h3 >{{taste}}</h3>
                  </span>
              </span>
              <div class="mt-4 fs-4 fw-bold pb-10 ml-10 align-right pt-5">TASTE</div>
        
              <span class="row pl-3 fs-5 ml-10">
                <h3 class="col-2">당도</h3>
                <v-chip-group class="col-8 chip-group-box">
                  <v-chip
                    v-for="chips in chiplist"
                    :key="chips"
                    :bind="sweet"
                    :color="
                      sweet === chips ? 'pink lighten-2' : 'pink lighten-5'
                    "
                    disabled
                  >
                    {{ chips }}
                  </v-chip>
                </v-chip-group>
              </span>

              <span class="row pl-3 fs-5 ml-10">
                <h3 class="col-2">산도</h3>
                <v-chip-group class="col-8 chip-group-box">
                  <v-chip
                    v-for="chips in chiplist"
                    :key="chips"
                    :bind="acidic"
                    :color="
                      acidic === chips ? 'pink lighten-2' : 'pink lighten-5'
                    "
                    disabled
                  >
                    {{ chips }}
                  </v-chip>
                </v-chip-group>
              </span>

              <span class="row pl-3 fs-5 ml-10">
                <h3 class="col-2">바디</h3>
                <v-chip-group class="col-8 chip-group-box">
                  <v-chip
                    v-for="chips in chiplist"
                    :key="chips"
                    :bind="bold"
                    :color="
                      bold === chips ? 'pink lighten-2' : 'pink lighten-5'
                    "
                    disabled
                  >
                    {{ chips }}
                  </v-chip>
                </v-chip-group>
              </span>

              <span class="row pl-3 fs-5 ml-10">
                <h3 class="col-2">타닌</h3>
                <v-chip-group class="col-8 chip-group-box">
                  <v-chip
                    v-for="chips in chiplist"
                    :key="chips"
                    :bind="tannic"
                    :color="
                      tannic === chips ? 'pink lighten-2' : 'pink lighten-5'
                    "
                    disabled
                  >
                    {{ chips }}
                  </v-chip>
                </v-chip-group>
              </span>

              <span class="row pl-3 fs-5 ml-10">
                <h3 class="col-2">탄산</h3>
                <v-chip-group class="col-8 chip-group-box">
                  <v-chip
                    v-for="chips in chiplist"
                    :key="chips"
                    :bind="gentle"
                    :color="
                      gentle === chips ? 'pink lighten-2' : 'pink lighten-5'
                    "
                    disabled
                  >
                    {{ chips }}
                  </v-chip>
                </v-chip-group>
              </span>

              <div>
                <div class="fs-4 mt-10 fw-bold pb-2 ml-10 align-right pt-2">
                  FOOD
                </div>
                <span :key="food" v-for="food in temp">
                  <span
                    class="fs-4 ml-10 mb-2 text-center"
                    style="color: white; display: inline-block"
                    ><img
                      :src="require(`../assets/food/${food}.png`)"
                      style="width: 60px; height: 55px; margin-right: 10px"
                      alt="no image"
                    /><h3> {{ food }} </h3></span
                  >
                </span>
              </div>
            </div>

            <!-- similar wine -->
            <div class="row">
              <div class="col-3"></div>
        <div class="col-8 ml-3 fs-4 fw-bold pb-5 align-right pt-10">
                SIMILAR WINE
                </div>

          <v-row justify="center" class="mb-5">
        <v-col cols="2" v-for="wine in recommandlist" :key="wine.wine_id">
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
            <v-card-text class="text-center fs-5" style="color: gainsboro"
              >{{ wine.wine }}<br />
              <br />
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
          </div>

          </div>
        </div>
      </div>
    </main>
    <br />

  </div>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "Winedetail",
  

  data() {
    return {
      wineid: 0,
      winedetail: [],

      chiplist: [1, 2, 3, 4, 5],

      // 유저 추천와인 list
      recommandlist: [],

      // 당도, 산도, 바디, 타닌, 탄산
      sweet: "",
      acidic: "",
      bold: "",
      tannic: "",
      gentle: "",

      slicefood: "",
      foods: [],
      temp: [],

      slicetaste: "",
      tastes: "",

      // 유사추천와인 담을 list
      similarlist: [],
    };
  },

  created() {
    // wineID값 가져오기
    this.wineid = this.$route.query.wine_id;
    this.getWineDetail();
    // user 와인 가져오기
    this.getUserWine();
    // Recommand와인 가져오기
    this.recommandWine();
  },

  computed: {
    // user 정보 가져오기
    userInfo() {
      return this.$store.state.userInfo;
    },
  },

  methods: {
    async getWineDetail() {
      await http({
        method: "get",
        url: "wine/get_wine_data/" + this.wineid,
        // params: {
        //   wine: this.wineid,
        // },
      })
        .then((res) => {
          this.winedetail = res.data;
          console.log("와인상세정보 :", this.winedetail);

          // wine 값 설정
          this.winevalue(this.winedetail);

          // food 배열로 변환
          var reg = /[`~!@#$%^&*()_|+\-=?;:'".<>\{\}\[\]\\\/ ]/gim;

          this.slicefood = this.winedetail.food.split(",");
          for (let i = 0; i < this.slicefood.length; i++) {
            this.foods[i] = this.slicefood[i].trim();
            this.temp[i] = this.foods[i].replace(reg, "");
          }

          for (let i = 0; i < this.temp.length; i++) {
            if (this.temp[i] == "") {
              this.temp[i] = "ice";
            }
          }

          // console.log("slicefood", this.foods);
          // console.log("temp: ", this.temp);

          // taste 배열로 변환
          // console.log("taste", this.winedetail.taste);

          this.slicetaste = this.winedetail.taste.replace(reg, "");
          this.tastes = this.slicetaste.split(",");
          // console.log("taste : ", this.tastes);

          // 유사와인 리스트 받기
          this.similarwine();
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

    // Wine 당도, 산도, 바디, 타닌 값 설정
    winevalue(wine) {
      // 당도값 설정
      if (wine.dry >= 0 && wine.dry < 2) {
        this.sweet = 1;
      } else if (wine.dry >= 2 && wine.dry < 4) {
        this.sweet = 2;
      } else if (wine.dry >= 4 && wine.dry < 6) {
        this.sweet = 3;
      } else if (wine.dry >= 6 && wine.dry < 8) {
        this.sweet = 4;
      } else if (wine.dry >= 8 && wine.dry < 10) {
        this.sweet = 5;
      }

      // 산도값 설정
      if (wine.soft >= 0 && wine.soft < 2) {
        this.acidic = 1;
      } else if (wine.soft >= 2 && wine.soft < 4) {
        this.acidic = 2;
      } else if (wine.soft >= 4 && wine.soft < 6) {
        this.acidic = 3;
      } else if (wine.soft >= 6 && wine.soft < 8) {
        this.acidic = 4;
      } else if (wine.soft >= 8 && wine.soft < 10) {
        this.acidic = 5;
      }

      // 바디값 설정
      if (wine.light >= 0 && wine.light < 2) {
        this.bold = 1;
      } else if (wine.light >= 2 && wine.light < 4) {
        this.bold = 2;
      } else if (wine.light >= 4 && wine.light < 6) {
        this.bold = 3;
      } else if (wine.light >= 6 && wine.light < 8) {
        this.bold = 4;
      } else if (wine.light >= 8 && wine.light < 10) {
        this.bold = 5;
      }

      // 타닌값 설정
      if (wine.smooth >= 0 && wine.smooth < 2) {
        this.tannic = 1;
      } else if (wine.smooth >= 2 && wine.smooth < 4) {
        this.tannic = 2;
      } else if (wine.smooth >= 4 && wine.smooth < 6) {
        this.tannic = 3;
      } else if (wine.smooth >= 6 && wine.smooth < 8) {
        this.tannic = 4;
      } else if (wine.smooth >= 8 && wine.smooth < 10) {
        this.tannic = 5;
      }

      // 탄산값 설정
      if (wine.gentle >= 0 && wine.gentle < 2) {
        this.gentle = 1;
      } else if (wine.gentle >= 2 && wine.gentle < 4) {
        this.gentle = 2;
      } else if (wine.gentle >= 4 && wine.gentle < 6) {
        this.gentle = 3;
      } else if (wine.gentle >= 6 && wine.gentle < 8) {
        this.gentle = 4;
      } else if (wine.gentle >= 8 && wine.gentle < 10) {
        this.gentle = 5;
      }
    },

    // wishlist 담기
    async wishlist() {
      await http({
        method: "post",
        url:
          "wine/add_wine_wishlist/" +
          this.winedetail.wine_id +
          "/" +
          this.userInfo.username +
          "/",
      })
        .then((res) => {
          alert("추가완료!");
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // 유사한 와인 가져오기
    async similarwine() {
      await http({
        method: "get",
        url: "wine/recommand/similar_wine/" + this.wineid + "/",
      })
        .then((res) => {
          // console.log(res);
          this.similarlist = res.data;
          console.log("유사와인추천 리스트 : ", this.similarlist);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
#wine-img {
  width: 170px;
  height: 700px;
  margin-top: 80px;
}

.badge {
  height: 40px;
  text-align: center;
  padding-top: 10px;
  display: block;
  width: 70px;
}

#my-badge {
  border-radius: 10px;
  display: inline;
  padding-bottom: 11px;
  text-align: center;
  background-color: darksalmon;
  margin-right: 11px;
}
.chip-group-box {
  margin-left: 40px;
}

#taste-badge {
  display: inline-flex;
  text-align: center;
  border-radius: 40px;
  width: 30px;
  height: 35px;
  margin-bottom: 2em;
  margin-left: 1em;
  padding-left: 1em;
}
#my-detail-card {
  border-radius: 30px;
  border-style: dashed;
  border-width: 5px thick;
  border-color: burlywood;
  margin-top: 10px;
  color: gainsboro;
}

.my-border {
  background-color: rgb(56, 54, 54);
  width: 100%;
  margin-top: 50px;
  display: flex;
  border-radius: 20px;
  opacity: 0.9;
  box-shadow: 0 0 15px grey;
  padding-top: 20px;
  padding-bottom: 20px;
}
</style>
