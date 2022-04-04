<template>
  <div class="home">
    <h1 class="text-center mb-10 fw-bold">Detail</h1>
    <main class="mt-3">
      <div class="container">
        <div class="row">
          <div class="col-md-6 pt-15 text-center">
            <div>
              <div>
                <!-- <v-img
                  :src="this.winedetail.image"
                  padding-top="100px"
                  width="100px"
                  height="450"
                  alt="No image"
                  contain
                /><v-img /> -->
                <img id="wine-img" :src="this.winedetail.image" alt="..." />
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card shadow-sm" id="info-card">
              <div class="card-body">
                <h5 class="card-title mx-3 pt-1 pb-1">
                  {{ this.winedetail.wine }}
                </h5>
                <h5 class="pt-5 pb-3 border-top">
                  <div class="badge bg-secondary mx-3" id="my-badge">
                    WINE TYPE
                  </div>
                  {{ this.winedetail.color }}
                </h5>
                <div class="card-text border-top pt-3 pb-3">
                  <h5 class="pt-3 pb-3">
                    <div class="badge bg-secondary mx-3" id="my-badge">
                      WINERY
                    </div>
                    {{ this.winedetail.winery }}
                  </h5>
                  <h5 class="pt-3 pb-3">
                    <div class="badge bg-secondary mx-3" id="my-badge">
                      WINE
                    </div>
                    {{ this.winedetail.wine }}
                  </h5>
                  <h5 class="pt-3 pb-3">
                    <div class="badge bg-secondary mx-3" id="my-badge">
                      GRAPES
                    </div>
                    {{ this.winedetail.grapes }}
                  </h5>
                  <h5 class="pt-3 pb-3">
                    <div class="badge bg-secondary mx-3" id="my-badge">
                      ALCOHOL
                    </div>
                    {{ this.winedetail.alcohol }}
                  </h5>
                  <h5 class="card-title pt-5 border-top">
                    <div class="badge bg-danger mx-3" id="my-badge">PRICE</div>
                    {{ this.winedetail.price }}원
                  </h5>
                </div>
              </div>
              <div class="fs-4 fw-bold pb-10 align-right border-top pt-3 pl-10">
                | TASTE
              </div>

              <span class="pl-10">
                당도
                <v-chip-group>
                  <v-chip
                    v-for="chips in chiplist"
                    :key="chips"
                    :bind="sweet"
                    :color="sweet === chips ? 'red' : ' gray'"
                  >
                    {{ chips }}
                  </v-chip>
                </v-chip-group>
              </span>

              <span class="pl-10">
                산도
                <v-chip-group>
                  <v-chip
                    v-for="chips in chiplist"
                    :key="chips"
                    :bind="acidic"
                    :color="acidic === chips ? 'red' : ' gray'"
                  >
                    {{ chips }}
                  </v-chip>
                </v-chip-group>
              </span>

              <span class="pl-10">
                바디
                <v-chip-group>
                  <v-chip
                    v-for="chips in chiplist"
                    :key="chips"
                    :bind="bold"
                    :color="bold === chips ? 'red' : ' gray'"
                  >
                    {{ chips }}
                  </v-chip>
                </v-chip-group>
              </span>

              <span class="pl-10">
                타닌
                <v-chip-group>
                  <v-chip
                    v-for="chips in chiplist"
                    :key="chips"
                    :bind="tannic"
                    :color="tannic === chips ? 'red' : ' gray'"
                  >
                    {{ chips }}
                  </v-chip>
                </v-chip-group>
              </span>
            </div>
          </div>
        </div>
      </div>
    </main>
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

      // 당도, 산도, 바디, 타닌
      sweet: "",
      acidic: "",
      bold: "",
      tannic: "",
    };
  },

  created() {
    // wineID값 가져오기
    this.wineid = this.$route.query.wine_id;
    this.getWineDetail();
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
          this.winevalue(this.winedetail);
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

      console.log("당도 :", this.sweet);
      console.log("산도 :", this.acidic);
      console.log("바디 :", this.bold);
      console.log("타닌 :", this.tannic);
    },
  },
};
</script>

<style>
#info-card {
  border-style: dashed;
  border-radius: 30px;
  border-width: 5px thick;
  display: flex;
}

#wine-img {
  padding-top: 100px;
  width: 100px;
  height: 450px;
}

.badge {
  height: 40px;
  text-align: center;
  padding-top: 10px;
  display: block;
  width: 70px;
}

#my-badge {
  height: 40px;
  display: inline;
  padding-bottom: 11px;
  width: 70px;
  text-align: center;
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
</style>
