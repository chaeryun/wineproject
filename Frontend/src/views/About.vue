<template>
  <div class="about mt-13">
    <h1>와인 사전</h1>
    <div class="text-center">
      <button class="food-button" style="height: 50px; width:350px;" @click="word"><h2>FAQ Top10</h2></button>
      <button class="food-button" style="height: 50px; width:350px;" @click="sense"><h2>주요 생산국</h2></button>
    </div>

    <br />

    <router-view></router-view>
    <br />
  </div>
</template>

<script>
export default {
  name: "About",

  methods: {
    word() {
      this.$router.push({ name: "Wineword" });
    },
    sense() {
      this.$router.push({ name: "Winesense" });
    },
  },
};
</script>