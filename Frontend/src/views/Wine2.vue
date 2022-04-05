<template>
  <div class="wine mt-13">
    <v-container>
      <h1>와인 조회</h1>
      <hr />
      <form
        v-on:submit.prevent="registerProduct()"
        enctype="multipart/form-data"
      >
        <label for="productCategory"> | Wine Search </label>
        <div class="form-group">
          <select
            class="form-control secondary"
            id="productCategory"
            ref="productCategory"
          >
            <option value="1">국가</option>
            <option value="2">France</option>
            <option value="3">United States</option>
            <option value="4">Italy</option>
            <option value="5">Spain</option>
            <option value="6">Australia</option>
            <option value="7">South Africa</option>
            <option value="8">Austria</option>
            <option value="9">Germany</option>
            <option value="10">Argentina</option>
            <option value="11">Greece</option>
            <option value="12">Chile</option>
            <option value="13">New Zealand</option>
            <option value="14">Brazil</option>
            <option value="15">Georgia</option>
            <option value="16">Romania</option>
            <option value="17">Switzerland</option>
            <option value="18">Canada</option>
            <option value="19">Slovenia</option>
            <option value="20">Israel</option>
          </select>
          <select
            class="form-control secondary"
            id="productCategory"
            ref="productCategory"
          >
            <option value="1">포도품종</option>
            <option value="2">Chardonnay</option>
            <option value="3">Touriga Nacional</option>
            <option value="4">Pinot Noir</option>
            <option value="5">Touriga Franca</option>
            <option value="6">Tinta Roriz</option>
            <option value="7">Cabernet Sauvignon</option>
            <option value="8">Tinta Barroca</option>
            <option value="9">Grenache</option>
            <option value="10">Tinto Cao</option>
            <option value="11">Shiraz/Syrah</option>
            <option value="12">Merlot</option>
            <option value="13">Cinsault</option>
            <option value="14">Mourvedre</option>
            <option value="15">Cabernet Franc</option>
            <option value="16">Pinot Meunier</option>
            <option value="17">Souzao</option>
            <option value="18">Tinta Amarela</option>
            <option value="19">Malbec</option>
            <option value="20">Touriga Francesa</option>
          </select>
          <select
            class="form-control secondary"
            id="productCategory"
            ref="productCategory"
          >
            <option value="1">가격</option>
            <option value="2">1만원 이하</option>
            <option value="3">1만원 ~ 3만원</option>
            <option value="4">3만원 ~ 5만원</option>
            <option value="5">5만원 ~ 7만원</option>
            <option value="6">7만원 ~ 10만원</option>
            <option value="7">10만원 ~ 20만원</option>
            <option value="8">20만원 ~ 50만원</option>
            <option value="9">50만원 ~ 100만원</option>
            <option value="10">100만원 이상</option>
          </select>
          <select
            class="form-control secondary"
            id="productCategory"
            ref="productCategory"
          >
            <option value="1">향</option>
            <option value="2">Citrus</option>
            <option value="3">Oak</option>
            <option value="4">Strawberry</option>
            <option value="5">Leather</option>
            <option value="6">Brioche</option>
            <option value="7">Blackberry</option>
            <option value="8">Apple</option>
            <option value="9">Honey</option>
            <option value="10">Minerals</option>
            <option value="11">Chocolate</option>
            <option value="12">Peach</option>
            <option value="13">Raisin</option>
            <option value="14">Plum</option>
            <option value="15">Caramel</option>
            <option value="16">Vanilla</option>
            <option value="17">Butter</option>
            <option value="18">Tobacco</option>
            <option value="19">Cherry</option>
            <option value="19">Earthy</option>
          </select>
        </div>
        <label for="productCategory"> | Wine Style </label>
        <div class="form-group">
          <select
            class="form-control secondary"
            id="productCategory"
            ref="productCategory"
          >
            <option value="1">당도</option>
            <option value="2">1</option>
            <option value="3">2</option>
            <option value="4">3</option>
            <option value="5">4</option>
            <option value="6">5</option>
          </select>
          <select
            class="form-control secondary"
            id="productCategory"
            ref="productCategory"
          >
            <option value="1">산도</option>
            <option value="2">1</option>
            <option value="3">2</option>
            <option value="4">3</option>
            <option value="5">4</option>
            <option value="6">5</option>
          </select>
          <select
            class="form-control secondary"
            id="productCategory"
            ref="productCategory"
          >
            <option value="1">바디</option>
            <option value="2">1</option>
            <option value="3">2</option>
            <option value="4">3</option>
            <option value="5">4</option>
            <option value="6">5</option>
          </select>
          <select
            class="form-control secondary"
            id="productCategory"
            ref="productCategory"
          >
            <option value="1">타닌</option>
            <option value="2">1</option>
            <option value="3">2</option>
            <option value="4">3</option>
            <option value="5">4</option>
            <option value="6">5</option>
          </select>
        </div>
        <div class="select-input">
          <input
            type="text"
            class="form-control"
            id="wineName"
            placeholder="와인 이름을 검색해주세요."
            ref="wineName"
          />
          <button type="submit" id="searchWine" class="btn btn-warning" style="width:72px;">
            <img src="../assets/find.png" id="find-icon" class="pb-2" alt="" />
          </button>
        </div>
      </form>
      <hr />
      <!-- 와인타입 선택바 -->
      <v-bottom-navigation color="warning" width="450px" style="border-radius: 20px; margin-left: 10px; background-color: cornsilk;">
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

      <v-row>
        <div
          class="col-xl-3 col-lg-4 col-md-6"
          :key="i"
          v-for="(wine, i) in calData"
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
            <div
              class="d-flex justify-content-between align-items-center"
            ></div>
          </v-card>
        </div>
      </v-row>
      <v-row>
        <v-pagination
          v-model="currentPage"
          :length="numOfPages"
          :total-visible="10"
        ></v-pagination>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import http from "@/util/http-common";

export default {
  name: "Wine",
  data: () => ({
    // winelist 저장
    winelist: [],
    redwinelist: [],
    whitewinelist: [],
    rosewinelist: [],
    sparklingwinelist: [],
    portwinelist: [],
    recentlist: [],

    redoption: false,
    whiteoption: false,
    roseoption: false,
    sparklingoption: false,
    portoption: false,

    // pagenation
    currentPage: 1,
    perPage: 20,
  }),

  created() {
    // wine page 클릭시 함수호출
    this.getWineList();
  },

  computed: {
    startOffset() {
      return (this.currentPage - 1) * this.perPage;
    },
    endOffset() {
      return this.startOffset + this.perPage;
    },
    numOfPages() {
      return Math.ceil(this.recentlist.length / this.perPage);
    },
    calData() {
      return this.recentlist.slice(this.startOffset, this.endOffset);
    },

    // user 정보 가져오기
    userinfo() {
      return this.$store.state.userInfo;
    },
  },

  methods: {
    // 전체 와인 불러와서 winelist에 넣기
    async getWineList() {
      await http({
        method: "get",
        url: "wine/get_wine_list/",
      })
        .then((res) => {
          //   console.log("wine list :", res);
          this.winelist = res.data;
          this.recentlist = this.winelist;
          // console.log("winelist", this.winelist);

          // wine type별 winelist 추가
          this.typewine(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    typewine(wine) {
      console.log("wine", wine[0]);
      for (let i = 0; i < wine.length; i++) {
        if (wine[i].color == "red") {
          this.redwinelist.push(wine[i]);
        } else if (wine[i].color == "white") {
          this.whitewinelist.push(wine[i]);
        } else if (wine[i].color == "rose") {
          this.rosewinelist.push(wine[i]);
        } else if (wine[i].color == "sparkling") {
          this.sparklingwinelist.push(wine[i]);
        } else if (wine[i].color == "port") {
          this.portwinelist.push(wine[i]);
        }
      }

      console.log("red winelist :", this.redwinelist);
    },

    // 와인 상세페이지 이동
    winedetail(wine_id) {
      this.$router.push({ path: "/detail", query: { wine_id: wine_id } });
    },

    typered() {
      if (!this.redoption) {
        this.recentlist = this.redwinelist;
        this.redoption = true;
      } else {
        this.recentlist = this.winelist;
        this.redoption = false;
      }
    },
    typewhite() {
      if (!this.whiteoption) {
        this.recentlist = this.whitewinelist;
        this.whiteoption = true;
      } else {
        this.recentlist = this.winelist;
        this.whiteoption = false;
      }
    },
    typerose() {
      if (!this.roseoption) {
        this.recentlist = this.rosewinelist;
        this.roseoption = true;
      } else {
        this.recentlist = this.winelist;
        this.roseoption = false;
      }
    },
    typesparkling() {
      if (!this.sparklingoption) {
        this.recentlist = this.sparklingwinelist;
        this.sparklingoption = true;
      } else {
        this.recentlist = this.winelist;
        this.sparklingoption = false;
      }
    },
    typeport() {
      if (!this.portoption) {
        this.recentlist = this.portwinelist;
        this.portoption = true;
      } else {
        this.recentlist = this.winelist;
        this.portoption = false;
      }
    },
  },
};
</script>

<style>
.form-group {
  display: flex;
}

label {
  margin-left: 1em;
  font-weight: bold;
}

select {
  margin: 1em;
}

h1 {
  text-align: center;
}

#productCategory {
  color: white;
  border-radius: 2em;
  text-align: center;
  height: 50px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
    rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
}

option {
  border-radius: 2em;
}

.select-input {
  display: flex;
  margin: 1em;
}

button {
  color: white;
  width: 90px;
  height: 50px;
}

#wineName {
  width: 900px;
  border-radius: 2em;
  height: 50px;
  margin-right: 1em;
}

#searchWine {
  border-radius: 2em;
  color: white;
}

hr {
  border-style: dashed;
  border-color: orange;
  margin: 30px;
  border-width: 2px;
}

#wine-card {
  display: flex;
}

v-card {
  padding: 2em;
}
</style>
