<template>
  <div class="food mt-13">
    <h1 style="margin-bottom: 20px">음식과 어울리는 와인 추천</h1>
    <div class="text-center">
    <hr style="border-color: grey"/>
      <button class="food-button" @click="clickfood($event)" value="shellfish">
        <img src="../assets/food/shellfish.png" class="food-img" /> Shellfish
      </button>
      <button class="food-button" @click="clickfood($event)" value="pork">
        <img src="../assets/food/pork.png" class="food-img" /> Pork
      </button>
      <button class="food-button" @click="clickfood($event)" value="beef">
        <img src="../assets/food/beef.png" class="food-img" /> Beef
      </button>
      <button
        class="food-button"
        @click="clickfood($event)"
        value="mild and soft cheese"
      >
        <img src="../assets/food/mildandsoftcheese.png" class="food-img" /> Soft
        Cheese
      </button>
      <button class="food-button" @click="clickfood($event)" value="poultry">
        <img src="../assets/food/poultry.png" class="food-img" /> Poultry
      </button>
      <button class="food-button" @click="clickfood($event)" value="richfish">
        <img src="../assets/food/richfish.png" class="food-img" /> Rich fish
      </button>
      <button class="food-button" @click="clickfood($event)" value="lamb">
        <img src="../assets/food/lamb.png" class="food-img" /> Lamb
      </button>
      <button class="food-button" @click="clickfood($event)" value="pasta">
        <img src="../assets/food/pasta.png" class="food-img" /> Pasta
      </button>
      <button
        class="food-button"
        @click="clickfood($event)"
        value="mature and hard cheese"
      >
        <img src="../assets/food/matureandhardcheese.png" class="food-img" />
        Hard Cheese
      </button>
      <button class="food-button" @click="clickfood($event)" value="salmon">
        <img src="../assets/food/salmon.png" class="food-img" /> Salmon
      </button>
      <button class="food-button" @click="clickfood($event)" value="cured meat">
        <img src="../assets/food/curedmeat.png" class="food-img" /> Cured Meat
      </button>
      <button class="food-button" @click="clickfood($event)" value="tuna">
        <img src="../assets/food/tuna.png" class="food-img" /> Tuna
      </button>
      <button class="food-button" @click="clickfood($event)" value="vegetarian">
        <img src="../assets/food/vegetarian.png" class="food-img" /> Vegetarian
      </button>
      <button class="food-button" @click="clickfood($event)" value="aperitif">
        <img src="../assets/food/aperitif.png" class="food-img" /> Aperitif
      </button>
      <button class="food-button" @click="clickfood($event)" value="veal">
        <img src="../assets/food/veal.png" class="food-img" /> Veal
      </button>
      <button class="food-button" @click="clickfood($event)" value="appetizers">
        <img src="../assets/food/appetizersandsnaks.png" class="food-img" />
        Appetizers
      </button>
      <button class="food-button" @click="clickfood($event)" value="bluecheese">
        <img src="../assets/food/bluecheese.png" class="food-img" /> Blue Cheese
      </button>
      <button class="food-button" @click="clickfood($event)" value="spicyfood">
        <img src="../assets/food/spicyfood.png" class="food-img" /> Spicy Food
      </button>
      <button
        class="food-button"
        @click="clickfood($event)"
        value="sweetdessert"
      >
        <img src="../assets/food/sweetdesserts.png" class="food-img" /> Sweet
        Dessert
      </button>
      <button class="food-button" @click="clickfood($event)" value="deer">
        <img src="../assets/food/deer.png" class="food-img" /> Deer
      </button>
      <button class="food-button" @click="clickfood($event)" value="leanfish">
        <img src="../assets/food/leanfish.png" class="food-img" /> Lean Fish
      </button>
    </div>
    <hr style="border-color: grey"/>
    <!-- 와인타입 선택바 -->
    <div style="position: relative; left: 2%; padding-top: 30px">
      <v-bottom-navigation
        color="#CD5C5C"
        width="450px"
        style="
          border-radius: 20px;
          margin-left: 10px;
          background-color: #FFDEAD;
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
    </div>

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
          <div class="d-flex justify-content-between align-items-center"></div>
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
    <br />
  </div>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "Wine",
  data: () => ({
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

    // winelist 저장
    winelist: [],

    // pagenation
    currentPage: 1,
    perPage: 20,

    // food 저장
    food: "",
    foodlist: [],

    // 최종 보여줄 리스트
    recentlist: [],
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
          this.foodlist = res.data;
          this.recentlist = res.data;

          this.typewine(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    winedetail(wine) {
      this.$router.push({ path: "/detail", qeury: { wine: wine } });
    },

    // food button 클릭시 추천와인리스트 가져오기
    clickfood(e) {
      console.log("food btn", e.target.value);
      this.food = e.target.value;
      this.recommandfood();
    },

    async recommandfood() {
      await http({
        methods: "get",
        url: "wine/recommand/onlyfood/" + this.food + "/",
      })
        .then((res) => {
          console.log(res);
          this.foodlist = res.data;
          this.recentlist = res.data;
          this.typewine(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    typewine(wine) {
      console.log("wine", wine[0]);
      // 배열초기화
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
    },

    typered() {
      if (!this.redoption) {
        this.recentlist = this.redwinelist;
        this.redoption = true;
      } else {
        this.recentlist = this.foodlist;
        this.redoption = false;
      }
    },
    typewhite() {
      if (!this.whiteoption) {
        this.recentlist = this.whitewinelist;
        this.whiteoption = true;
      } else {
        this.recentlist = this.foodlist;
        this.whiteoption = false;
      }
    },
    typerose() {
      if (!this.roseoption) {
        this.recentlist = this.rosewinelist;
        this.roseoption = true;
      } else {
        this.recentlist = this.foodlist;
        this.roseoption = false;
      }
    },
    typesparkling() {
      if (!this.sparklingoption) {
        this.recentlist = this.sparklingwinelist;
        this.sparklingoption = true;
      } else {
        this.recentlist = this.foodlist;
        this.sparklingoption = false;
      }
    },
    typeport() {
      if (!this.portoption) {
        this.recentlist = this.portwinelist;
        this.portoption = true;
      } else {
        this.portoption = false;
        this.recentlist = this.foodlist;
      }
    },

    winedetail(wine_id) {
      this.$router.push({ path: "/detail", query: { wine_id: wine_id } });
    },
  },
};
</script>

<style>
.food-button {
  background-color: rgb(78, 78, 78);
  box-shadow: 0 0 10px #3b3b34;
  color: cornsilk;
  font-size: 22px;
  width: 12em;
  height: 70px;
  border-radius: 40px;
  margin: 10px;
  opacity: 0.8;
}

.food-img {
  width: 70px;
  height: 68px;
}
</style>
