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
                <h5 class="card-title pb-1 fs-3">
                  {{ this.winedetail.wine }}
                  {{ this.winedetail.location }}
                </h5>
                <h5 class="pt-5 pb-3 border-top">
                  <span class="badge outlined" id="my-badge"> Wine Type</span>
                  {{ this.winedetail.color }}
                </h5>
                <div class="card-text border-top pt-3 pb-3">
                  <h5 class="pt-3 pb-3">
                    <span class="badge" id="my-badge"> Winery </span>
                    {{ this.winedetail.winery }}
                  </h5>
                  <h5 class="pt-3 pb-3">
                    <span class="badge" id="my-badge"> Wine name</span>
                    {{ this.winedetail.wine }}
                  </h5>
                  <h5 class="pt-3 pb-3">
                    <span class="badge" id="my-badge"> Country</span>
                    {{ this.winedetail.country }}
                  </h5>
                  <h5 class="pt-3 pb-3">
                    <span class="badge" id="my-badge"> Grpaes </span>
                    {{ this.winedetail.grapes }}
                  </h5>
                  <h5 class="pt-3 pb-3">
                    <span class="badge" id="my-badge"> Alcohol </span>
                    {{ this.winedetail.alcohol }}%
                  </h5>
                  <h5 class="card-title pt-5 border-top">
                    <span class="badge" id="my-badge"> Price </span>
                    {{ this.winedetail.price }}원
                  </h5>
                </div>
              </div>
              <div class="fs-4 fw-bold pb-7 pl-3 pt-10">BOUQUET</div>
              <span class="pl-3" :key="taste" v-for="taste in tastes">
                <span class="col-4 fs-5 fw-bold" id="my-badge">{{
                  taste
                }}</span>
              </span>
              <br />
            </div>
            <div class="col-4">
              <div class="fs-4 fw-bold pb-5 ml-10 align-right pt-6">TASTE</div>
              <span class="pl-3 fs-5 ml-10">
                당도
                <v-chip-group class="chip-group-box">
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

              <span class="pl-3 fs-5 ml-10">
                산도
                <v-chip-group class="chip-group-box">
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

              <span class="pl-3 fs-5 ml-10">
                바디
                <v-chip-group class="chip-group-box">
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

              <span class="pl-3 fs-5 ml-10">
                타닌
                <v-chip-group class="chip-group-box">
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

              <span class="pl-3 fs-5 ml-10">
                탄산
                <v-chip-group class="chip-group-box">
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
                <div class="fs-4 fw-bold pb-5 ml-10 align-right pt-10">
                  FOOD
                </div>
                <span :key="food" v-for="food in temp">
                  <span
                    class="fs-4 ml-10 mb-5 text-center"
                    style="color: white; display: inline-block"
                    ><img
                      :src="require(`../assets/food/${food}.png`)"
                      style="width: 60px; height: 55px; margin-right: 10px"
                      alt="no image"
                    />{{ food }}</span
                  >
                </span>
              </div>
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
    };
  },

  created() {
    // wineID값 가져오기
    this.wineid = this.$route.query.wine_id;
    this.getWineDetail();
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
          console.log(this.winedetail);

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

          console.log("slicefood", this.foods);
          console.log("temp: ", this.temp);

          // taste 배열로 변환
          console.log("taste", this.winedetail.taste);

          this.slicetaste = this.winedetail.taste.replace(reg, "");
          this.tastes = this.slicetaste.split(",");
          console.log("taste : ", this.tastes);
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
  },
};
</script>

<style>
#wine-img {
  width: 170px;
  height: 700px;
  margin-top: 10px;
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
