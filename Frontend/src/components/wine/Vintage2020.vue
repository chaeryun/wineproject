<template>
  <!-- hero area start -->
  <!-- 인기1위 -->
  <section class="hero-area" id="home">
    <div class="container">
      <div class="hero-area-slider">
        <div class="row hero-area-slide">
          <div class="col-lg-6 col-md-5">
            <div class="hero-area-content">
              <img :src="this.vintagelist[0].image" height="700" contain />
            </div>
          </div>
          <div class="col-lg-6 col-md-7">
            <div class="hero-area-content pr-50">
              <h1 class="text-center">👑 Top 1</h1>
              <hr />
              <h3 class="text-center">{{ vintagelist[0].wine }}</h3>
              <hr />
              <p class="fs-5 fw-bold text-center">
                Wine Type /
                <span class="fs-6 fw-normal">{{ vintagelist[0].color }}</span>
              </p>
              <p class="fs-5 fw-bold text-center">
                Winery /
                <span class="fs-6 fw-normal">{{ vintagelist[0].winery }}</span>
              </p>
              <p class="fs-5 fw-bold text-center">
                Grapes /
                <span class="fs-6 fw-normal">{{ vintagelist[0].grapes }}</span>
              </p>
              <p class="fs-5 fw-bold text-center">
                Country /
                <span class="fs-6 fw-normal">{{ vintagelist[0].country }}</span>
              </p>
              <p class="fs-5 fw-bold text-center">
                Price /
                <span class="fs-6 fw-normal"
                  >￦ {{ vintagelist[0].price }}</span
                >
              </p>
              <button class="btn btn-warning" id="go-to-detail">
                Details..
              </button>
              <br />
            </div>
          </div>
        </div>
      </div>
      <!-- 인기 2위 -->
      <div class="hero-area-slider2">
        <div class="row hero-area-slide" id="second-vintage">
          <div class="col-lg-5 col-md-4">
            <div class="hero-area-content">
              <img :src="this.vintagelist[1].image" height="700" contain />
            </div>
          </div>
          <div class="col-lg-6 col-md-7">
            <div class="hero-area-content pr-50">
              <h1 class="text-center">👑 Top 2</h1>
              <hr />
              <h3 class="text-center">{{ vintagelist[1].wine }}</h3>
              <hr />
              <p class="fs-5 fw-bold text-center">
                Wine Type /
                <span class="fs-6 fw-normal">{{ vintagelist[1].color }}</span>
              </p>
              <p class="fs-5 fw-bold text-center">
                Winery /
                <span class="fs-6 fw-normal">{{ vintagelist[1].winery }}</span>
              </p>
              <p class="fs-5 fw-bold text-center">
                Grapes /
                <span class="fs-6 fw-normal">{{ vintagelist[1].grapes }}</span>
              </p>
              <p class="fs-5 fw-bold text-center">
                Country /
                <span class="fs-6 fw-normal">{{ vintagelist[1].country }}</span>
              </p>
              <p class="fs-5 fw-bold text-center">
                Price /
                <span class="fs-6 fw-normal"
                  >￦ {{ vintagelist[1].price }}</span
                >
              </p>
              <button class="btn btn-warning" id="go-to-detail">
                Details..
              </button>
              <br />
            </div>
          </div>
        </div>
      </div>
      <!-- 인기3위 -->
      <div class="row hero-area-slide" id="third-vintage">
        <div class="col-lg-5 col-md-4">
          <div class="hero-area-content">
            <img :src="this.vintagelist[2].image" height="700" contain />
          </div>
        </div>
        <div class="col-lg-6 col-md-7">
          <div class="hero-area-content pr-50">
            <h1 class="text-center">👑 Top 3</h1>
            <hr />
            <h3 class="text-center">{{ vintagelist[2].wine }}</h3>
            <hr />
            <p class="fs-5 fw-bold text-center">
              Wine Type /
              <span class="fs-6 fw-normal">{{ vintagelist[2].color }}</span>
            </p>
            <p class="fs-5 fw-bold text-center">
              Winery /
              <span class="fs-6 fw-normal">{{ vintagelist[2].winery }}</span>
            </p>
            <p class="fs-5 fw-bold text-center">
              Grapes /
              <span class="fs-6 fw-normal">{{ vintagelist[2].grapes }}</span>
            </p>
            <p class="fs-5 fw-bold text-center">
              Country /
              <span class="fs-6 fw-normal">{{ vintagelist[2].country }}</span>
            </p>
            <p class="fs-5 fw-bold text-center">
              Price /
              <span class="fs-6 fw-normal">￦ {{ vintagelist[2].price }}</span>
            </p>
            <button class="btn btn-warning" id="go-to-detail">Details..</button>
            <br />
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- hero area end -->
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "Vintage2020",

  data() {
    return {
      year: 2020,
      vintagelist: [],
    };
  },

  created() {
    // 2020년 vintage wine list 호출
    this.getVintage2020();
  },

  methods: {
    async getVintage2020() {
      await http({
        method: "get",
        url: "wine/recommand/vintage/" + this.year + "/",
      })
        .then((res) => {
          console.log(res);
          this.vintagelist = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
