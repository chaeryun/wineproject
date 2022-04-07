<template>
  <div class="wine mt-13">
    <v-container>
      <h1 class="mb-13">
        <span
          style="
            text-align: center;
            border-radius: 15px 15px 15px 0;
            border: 3px solid #ffad5b;
            padding: 0.5em 0.6em;
            color: bullywood;
          "
          >와인 조회</span
        >
      </h1>
      <hr style="border-color:grey;" />

      <label for="productCategory" class="ml-15 mb-5"> | Wine Search </label>
      <div class="form-group px-15 mx-15">
        <v-select
          style="
            border-radius: 100px;
            height: 55px;
            width: 80px;
            margin-right: 10px;
            background-color: wheat;
            box-shadow: 0 0 10px grey;
          "
          v-model="country"
          :items="countrylist"
          item-text="name"
          item-value="value"
          label="국가"
          solo
          item-color="warning"
        >
        </v-select>
        <v-select
          style="
            border-radius: 100px;
            height: 55px;
            width: 80px;
            margin-right: 10px;
            background-color: wheat;
            box-shadow: 0 0 10px grey;
          "
          v-model="grape"
          :items="grapes"
          item-text="name"
          item-value="value"
          label="포도품종"
          solo
          item-color="warning"
        >
        </v-select>

        <v-select
          style="
            border-radius: 100px;
            height: 55px;
            width: 80px;
            margin-right: 10px;
            background-color: wheat;
            box-shadow: 0 0 10px grey;
          "
          v-model="price"
          :items="prices"
          item-text="name"
          item-value="value"
          label="가격"
          solo
          item-color="warning"
        >
        </v-select>

        <v-select
          style="
            border-radius: 100px;
            height: 55px;
            width: 80px;
            margin-right: 10px;
            background-color: wheat;
            box-shadow: 0 0 10px grey;
          "
          v-model="taste"
          :items="tastes"
          item-text="name"
          item-value="value"
          label="향"
          solo
          item-color="warning"
        >
        </v-select>
      </div>
      <label for="productCategory" class="ml-15 mt-5 mb-5">
        | Wine Style
      </label>
      <div class="form-group px-15 mx-15">
        <v-select
          style="
            border-radius: 100px;
            height: 55px;
            margin-right: 10px;
            background-color: wheat;
            box-shadow: 0 0 10px grey;
          "
          v-model="dryscore"
          :items="drylist"
          item-text="name"
          item-value="value"
          label="당도"
          solo
          item-color="warning"
        >
        </v-select>

        <v-select
          style="
            border-radius: 100px;
            height: 55px;
            margin-right: 10px;
            background-color: wheat;
            box-shadow: 0 0 10px grey;
          "
          v-model="softscore"
          :items="softlist"
          item-text="name"
          item-value="value"
          label="산도"
          solo
          item-color="warning"
        >
        </v-select>

        <v-select
          style="
            border-radius: 100px;
            height: 55px;
            margin-right: 10px;
            background-color: wheat;
            box-shadow: 0 0 10px grey;
          "
          v-model="lightscore"
          :items="lightlist"
          item-text="name"
          item-value="value"
          label="바디"
          solo
          item-color="warning"
        >
        </v-select>
        <v-select
          style="
            border-radius: 100px;
            height: 55px;
            margin-right: 10px;
            background-color: wheat;
            box-shadow: 0 0 10px grey;
          "
          v-model="smoothscore"
          :items="smoothlist"
          item-text="name"
          item-value="value"
          label="타닌"
          solo
          item-color="warning"
        >
        </v-select>
      </div>
      <div class="select-input mt-10 ml-14 pl-10">
        <input
          type="text"
          class="form-control"
          id="wineName"
          placeholder="와인 이름을 검색해주세요."
          v-model="keyword"
          @keyup.enter="searchresultshow(keyword)"
        />
        <v-btn
          id="searchWine"
          class="btn"
          style="width: 70px"
          @click="winesearch"
        >
          <img src="../assets/find.png" id="find-icon" class="pb-2" alt="" />
        </v-btn>
      </div>

      <hr style="border-color:grey;" />
      <!-- 와인타입 선택바 -->
      <!-- 텅빌때, 수정하세여!!-->
      <template v-if = " winelistIsEmpty" >
        <div class="justify-center mt-15" style="display:flex;">
      <img src="../assets/error.png" style="width:70px; height:70px;" alt="empty" />
      <h2 class="ml-5 mt-3 mb-15 pb-15">조회하신 와인이 없습니다. 다른 와인을 검색해주세요.</h2>
      </div >
      </template>

      <v-bottom-navigation
        v-else
        color="#CD5C5C"
        width="450px"
        style="
          border-radius: 30px;
          margin-left: 110px;
          background-color: #ffdead;
          text-align: center;
        "
      >
        <v-btn value="red" @click="typered">
          <span class="fs-6">Red</span>
        </v-btn>

        <v-btn value="white" @click="typewhite">
          <span class="fs-6">White</span>
        </v-btn>

        <v-btn value="rose" @click="typerose">
          <span class="fs-6">Rose</span>
        </v-btn>

        <v-btn value="sparkling" @click="typesparkling">
          <span class="fs-6">Sparkling</span>
        </v-btn>

        <v-btn value="port" @click="typeport">
          <span class="fs-6">Port</span>
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
              border-radius: 80px;
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
    countrylist: [
      { name: "국가", value: "all" },
      { name: "France", value: "France" },
      { name: "United States", value: "United States" },
      { name: "Italy", value: "Italy" },
      { name: "Spain", value: "Spain" },
      { name: "Australia", value: "Australia" },
      { name: "South Africa", value: "South Africa" },
      { name: "Austria", value: "Austria" },
      { name: "Germany", value: "Germany" },
      { name: "Argentina", value: "Argentina" },
      { name: "Greece", value: "Greece" },
      { name: "Chile", value: "Chile" },
      { name: "Greece", value: "Greece" },
      { name: "New Zealand", value: "New Zealand" },
      { name: "Brazil", value: "Brazil" },
      { name: "Georgia", value: "Georgia" },
      { name: "Romania", value: "Romania" },
      { name: "Switzerland", value: "Switzerland" },
      { name: "Canada", value: "Canada" },
      { name: "Slovenia", value: "Slovenia" },
      { name: "Israel", value: "Israel" },
    ],
    country: "all",

    grapes: [
      { name: "포도품종", value: "all" },
      { name: "Chardonnay", value: "Chardonnay" },
      { name: "Touriga Nacional", value: "Touriga Nacional" },
      { name: "Pinot Noir", value: "Pinot Noir" },
      { name: "Touriga Franca", value: "Touriga Franca" },
      { name: "Tinta Roriz", value: "Tinta Roriz" },
      { name: "Cabernet Sauvignon", value: "Cabernet Sauvignon" },
      { name: "Tinta Barroca", value: "Tinta Barroca" },
      { name: "Grenache", value: "Grenache" },
      { name: "Tinto Cao", value: "Tinto Cao" },
      { name: "Shiraz/Syrah", value: "Shiraz/Syrah" },
      { name: "Merlot", value: "Merlot" },
      { name: "Cinsault", value: "Cinsault" },
      { name: "Mourvedre", value: "Mourvedre" },
      { name: "Cabernet Franc", value: "Cabernet Franc" },
      { name: "Pinot Meunier", value: "Pinot Meunier" },
      { name: "Souzao", value: "Souzao" },
      { name: "Tinta Amarela", value: "Tinta Amarela" },
      { name: "Malbec", value: "Malbec" },
      { name: "Touriga Francesa", value: "Touriga Francesa" },
    ],
    grape: "all",

    prices: [
      { name: "가격", value: "0" },
      { name: "1만원이하", value: "10000" },
      { name: "1만원 ~ 3만원", value: "30000" },
      { name: "3만원 ~ 5만원", value: "50000" },
      { name: "5만원 ~ 7만원", value: "70000" },
      { name: "7만원 ~ 10만원", value: "100000" },
      { name: "10만원 ~ 20만원", value: "200000" },
      { name: "20만원 ~ 50만원", value: "500000" },
      { name: "50만원 ~ 100만원", value: "1000000" },
      { name: "100만원이상", value: "1000001" },
    ],
    price: 0,
    minprice: "",
    maxprice: "",

    tastes: [
      { name: "향", value: "all" },
      { name: "Citrus", value: "Citrus" },
      { name: "Oak", value: "Oak" },
      { name: "Strawberry", value: "Strawberry" },
      { name: "Leather", value: "Leather" },
      { name: "Brioche", value: "Brioche" },
      { name: "Blackberry", value: "Blackberry" },
      { name: "Apple", value: "Apple" },
      { name: "Honey", value: "Honey" },
      { name: "Minerals", value: "Minerals" },
      { name: "Chocolate", value: "Chocolate" },
      { name: "Peach", value: "Peach" },
      { name: "Raisin", value: "Raisin" },
      { name: "Plum", value: "Plum" },
      { name: "Caramel", value: "Caramel" },
      { name: "Vanilla", value: "Vanilla" },
      { name: "Butter", value: "Butter" },
      { name: "Tobacco", value: "Tobacco" },
      { name: "Cherry", value: "Cherry" },
      { name: "Earthy", value: "Earthy" },
    ],
    taste: "all",

    drylist: [
      { name: "당도", value: "0" },
      { name: "1", value: "1" },
      { name: "2", value: "2" },
      { name: "3", value: "3" },
      { name: "4", value: "4" },
      { name: "5", value: "5" },
    ],
    dryscore: 0,

    softlist: [
      { name: "산도", value: "0" },
      { name: "1", value: "1" },
      { name: "2", value: "2" },
      { name: "3", value: "3" },
      { name: "4", value: "4" },
      { name: "5", value: "5" },
    ],
    softscore: 0,

    lightlist: [
      { name: "바디", value: "0" },
      { name: "1", value: "1" },
      { name: "2", value: "2" },
      { name: "3", value: "3" },
      { name: "4", value: "4" },
      { name: "5", value: "5" },
    ],
    lightscore: 0,

    smoothlist: [
      { name: "타닌", value: "0" },
      { name: "1", value: "1" },
      { name: "2", value: "2" },
      { name: "3", value: "3" },
      { name: "4", value: "4" },
      { name: "5", value: "5" },
    ],
    smoothscore: 0,

    // winelist 저장
    winelist: [],
    redwinelist: [],
    whitewinelist: [],
    rosewinelist: [],
    sparklingwinelist: [],
    portwinelist: [],
    recentlist: [],

    // 임시 list
    templist: [],

    redoption: false,
    whiteoption: false,
    roseoption: false,
    sparklingoption: false,
    portoption: false,

    // 검색기능
    keyword: "",
    // 검색 와인 리스트
    keywordlist: [],

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
    winelistIsEmpty(){
      console.log(this.recentlist.length);
      return this.recentlist.length==0;
    }
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
          this.templist = res.data;

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
      this.redwinelist = [];
      this.whitewinelist = [];
      this.rosewinelist = [];
      this.sparklingwinelist = [];
      this.portwinelist = [];

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

      // console.log("red winelist :", this.redwinelist);
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
        this.recentlist = this.templist;
        this.redoption = false;
      }
    },
    typewhite() {
      if (!this.whiteoption) {
        this.recentlist = this.whitewinelist;
        this.whiteoption = true;
      } else {
        this.recentlist = this.templist;
        this.whiteoption = false;
      }
    },
    typerose() {
      if (!this.roseoption) {
        this.recentlist = this.rosewinelist;
        this.roseoption = true;
      } else {
        this.recentlist = this.templist;
        this.roseoption = false;
      }
    },
    typesparkling() {
      if (!this.sparklingoption) {
        this.recentlist = this.sparklingwinelist;
        this.sparklingoption = true;
      } else {
        this.recentlist = this.templist;
        this.sparklingoption = false;
      }
    },
    typeport() {
      if (!this.portoption) {
        this.recentlist = this.portwinelist;
        this.portoption = true;
      } else {
        this.recentlist = this.templist;
        this.portoption = false;
      }
    },

    winesearch() {
      if (this.price > 0 && this.price <= 10000) {
        this.minprice = 0;
        this.maxprice = 10000;
      } else if (this.price > 10000 && this.price <= 30000) {
        this.minprice = 10000;
        this.maxprice = 30000;
      } else if (this.price > 30000 && this.price <= 50000) {
        this.minprice = 30000;
        this.maxprice = 50000;
      } else if (this.price > 50000 && this.price <= 70000) {
        this.minprice = 50000;
        this.maxprice = 70000;
      } else if (this.price > 70000 && this.price <= 100000) {
        this.minprice = 70000;
        this.maxprice = 100000;
      } else if (this.price > 100000 && this.price <= 200000) {
        this.minprice = 100000;
        this.maxprice = 200000;
      } else if (this.price > 200000 && this.price <= 500000) {
        this.minprice = 200000;
        this.maxprice = 500000;
      } else if (this.price > 500000 && this.price <= 1000000) {
        this.minprice = 500000;
        this.maxprice = 1000000;
      } else if (this.price > 1000000) {
        this.minprice = 1000000;
        this.maxprice = 10000000;
      } else if (this.price == 0) {
        this.minprice = 0;
        this.maxprice = 100000000;
      }

      // console.log("국가 :", this.country);
      // console.log("포도품종 :", this.grape);
      // console.log("최소가격 :", this.minprice);
      // console.log("최대가격 :", this.maxprice);
      // console.log("향 :", this.taste);
      // console.log("당도 :", this.dryscore);
      // console.log("산도 :", this.softscore);
      // console.log("바디 :", this.lightscore);
      // console.log("타닌 :", this.smoothscore);
      // console.log("키워드 :", this.keyword);

      if (this.keyword == "") {
        this.search();
      } else {
        this.searchresultshow(this.keyword);
      }
    },

    async search() {
      await http({
        method: "get",
        url:
          "wine/recommand/categorize/" +
          this.country +
          "/" +
          this.grape +
          "/" +
          this.minprice +
          "/" +
          this.maxprice +
          "/" +
          this.taste +
          "/" +
          this.dryscore +
          "/" +
          this.softscore +
          "/" +
          this.lightscore +
          "/" +
          this.smoothscore +
          "/",
      })
        .then((res) => {
          console.log(res);
          this.recentlist = res.data;

          // 임시 list
          this.templist = res.data;

          // wine type별 winelist 추가
          this.typewine(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    searchresultshow(keyword) {
      if (keyword != "") {
        // console.log("keyword", keyword);
        // console.log("전체 : winelist", this.winelist);

        // 키워드 리스트 초기화
        this.keywordlist = [];

        for (let i = 0; i < this.winelist.length; i++) {
          if (
            this.winelist[i].wine.toLowerCase().includes(keyword.toLowerCase())
          ) {
            // console.log("키워드 일치");
            this.keywordlist.push(this.winelist[i]);
            // console.log("키워드 일치 와인리스트", this.keywordlist);
          }
        }

        this.recentlist = this.keywordlist;
      } else {
        alert("키워드를 입력해주세요!");
      }
    },
  },
};
</script>

<style>
.form-group {
  display: flex;
  text-align: center;
}

label {
  font-size: 19px;
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
  height: 45px;
  margin-right: 1em;
  margin-left: 20px;
  background-color: wheat;
}

#searchWine {
  border-radius: 2em;
  color: white;
  background-color: wheat;
  height: 48px;
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
