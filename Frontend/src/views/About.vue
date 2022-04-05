<template>
  <div class="about mt-13">
    <h1>와인 사전</h1>
    <div class="text-center">
      <button class="food-button" style="height: 50px; width:350px;" @click="word">자주 물어보는 질문 Top10</button>
      <button class="food-button" style="height: 50px; width:350px;" @click="sense">주요 생산국</button>
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