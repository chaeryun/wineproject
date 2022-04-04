<template>
  <div class="about mt-13">
    <h1>About Wine</h1>
    <div class="text-center">
      <button class="food-button" @click="word">기본 용어</button>
      <button class="food-button" @click="sense">와인 상식</button>
    </div>

    <br />

    <router-view></router-view>
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
