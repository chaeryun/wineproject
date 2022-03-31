<template>
  <v-app id="inspire">
    <v-row>
      <v-carousel
        cycle
        height="610"
        hide-delimiter-background
        show-arrows-on-hover
      >
        <v-carousel-item v-for="wine in wines" :key="wine.name">
          <v-sheet height="100%">
            <v-row class="fill-height" align="center" justify="center">
              <img :src="wine.picture" alt="img" height="550" />
            </v-row>
          </v-sheet>
        </v-carousel-item>
      </v-carousel>
    </v-row>
    <br />
    <br />

    <v-row class="text-h7" justify="center">
      <h1>올해의 와인</h1>
    </v-row>
    <v-row justify="center">
      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" tile>
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-img
            :src="require('@/assets/sample/sample2.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row class="pa-5-mt-1 text-h7" justify="center" height="200">
      <h1>이달의 와인</h1>
    </v-row>
    <v-row justify="center">
      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-img
            :src="require('@/assets/sample/sample2.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-app>
</template>
<script>
export default {
  name: "Home",
  components: {},
  data() {
    return {
      wines: [
        { name: "wine1", picture: require("@/assets/wine1.jpg") },
        { name: "wine3", picture: require("@/assets/wine4.jpg") },
      ],
    };
  },
};
</script>
<style scoped></style>
