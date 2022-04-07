<template>
  <div class="vintage">
    <!-- <Navbar /> -->
    <!-- <h1 class="fw-bold mb-5">Vintage</h1> -->
    <h1 class="text-center pt-13">
      날씨 기반 빅데이터로 추천하는<br />
      2019 / 2020 / 2021해의 Good Vintage Wine Top3
    </h1>
    <div class="form-group justify-center mt-3 mb-3">
      <button class="food-button" style="height: 50px" @click="year2019">
        2019
      </button>
      <button class="food-button" style="height: 50px" @click="year2020">
        2020
      </button>
      <button class="food-button" style="height: 50px" @click="year2021">
        2021
      </button>
    </div>

    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: "Vintage",

  data() {
    return {};
  },

  methods: {
    year2019() {
      this.$router.push({ name: "Vintage2019" });
    },

    year2020() {
      this.$router.push({ name: "Vintage2020" });
    },

    year2021() {
      this.$router.push({ name: "Vintage2021" });
    },
  },
};
</script>

<style>
#productCategory2 {
  align-content: center;
  color: white;
  border-radius: 2em;
  text-align: center;
  height: 50px;
  width: 300px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
    rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
}

#go-to-detail {
  height: 40px;
  margin: auto;
  display: block;
  width: 100px;
}
.select-wine {
  margin-top: 14px;
}

#find-icon {
  width: 45px;
  height: 45px;
}

#second-vintage {
  float: left;
  max-width: 550px;
}

#third-vintage {
  float: right;
  max-width: 550px;
}

/* hero-area */

.hero-area {
  position: relative;
  color: white;
  background-image: url("../assets/hero-area.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  overflow: hidden;
}

.vintage {
  color: white;
  background-image: url("../assets/hero-area.png");
}

.hero-area-slide {
  background: #1b1d29a6;
  margin: 70px 15px 50px !important;
  padding-top: 52px;
  box-shadow: 0 0 20px #000000;
  max-width: 650px;
}

.hero-area-content > img {
  position: relative;
  margin-top: -90px;
}
.hero-area-slider {
  margin: auto;
  text-align: center;
  display: flex;
  justify-content: center;
}
.hero-area-slider2 {
  text-align: center;
}

.hero-area-content h3 {
  margin-top: 35px;
}
</style>
