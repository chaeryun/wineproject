<template>
  <v-app id="inspire">
    <v-row>
      <v-carousel
        cycle
        height="700"
        hide-delimiter-background
        show-arrows-on-hover
      >
        <v-carousel-item v-for="wine in wines" :key="wine.name">
          <v-sheet height="100%">
            <v-row class="fill-height" align="center" justify="center">
              <img :src="wine.picture" alt="img" height="710" />
            </v-row>
          </v-sheet>
        </v-carousel-item>
      </v-carousel>
    </v-row>
    <br />
    <br />

    <v-row class="text-h7" justify="center">
      <h1 class="mt-10 mb-10">올해의 와인</h1>
    </v-row>
    <v-row justify="center">
      <v-col cols="3">
        <v-card
          class="mx-auto"
          max-width="380"
          style="
            border-radius: 100px;
            background-color: #232320;
            box-shadow: 0 0 10px grey;
          "
          hover
          outlined
        >
          <v-btn class="mt-7 ml-10" text icon large color="red lighten-2">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <a href="/detail" style="color: gainsboro">
            <v-img
              :src="require('@/assets/sample/sample1.png')"
              height="300"
              contain
            /><v-img />
            <hr style="border-width: 2px; border-color: pink" />
            <v-card-title class="justify-center" style="padding-top: 1px"
              ><div>Dom Pérignon</div>
              P2 Plénitude Brut Champagne 1995</v-card-title
            >
            <v-card-text class="text-center fs-5"
              >#France #Sparkling</v-card-text
            >
          </a>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card
          class="mx-auto"
          max-width="380"
          style="
            border-radius: 100px;
            background-color: #232320;
            box-shadow: 0 0 10px grey;
          "
          hover
          outlined
        >
          <v-btn class="mt-7 ml-10" text icon large color="red lighten-2">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <a href="/detail" style="color: gainsboro">
            <v-img
              :src="require('@/assets/sample/sample2.png')"
              height="300"
              contain
            /><v-img />
            <hr style="border-width: 2px; border-color: pink" />
            <v-card-title class="justify-center" style="padding-top: 1px"
              ><div>Dom Pérignon</div>
              P2 Plénitude Brut Champagne 1995</v-card-title
            >
            <v-card-text class="text-center fs-5"
              >#France #Sparkling</v-card-text
            >
          </a>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card
          class="mx-auto"
          max-width="380"
          style="
            border-radius: 100px;
            background-color: #232320;
            box-shadow: 0 0 10px grey;
          "
          hover
          outlined
        >
          <v-btn class="mt-7 ml-10" text icon large color="red lighten-2">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <a href="/detail" style="color: gainsboro">
            <v-img
              :src="require('@/assets/sample/sample3.png')"
              height="300"
              contain
            /><v-img />
            <hr style="border-width: 2px; border-color: pink" />
            <v-card-title class="justify-center" style="padding-top: 1px"
              ><div>Dom Pérignon</div>
              P2 Plénitude Brut Champagne 1995</v-card-title
            >
            <v-card-text class="text-center fs-5"
              >#France #Sparkling</v-card-text
            >
          </a>
        </v-card>
      </v-col>
    </v-row>

    <v-row class="pa-2 mt-15 text-h7" justify="center">
      <h1 class="mt-10 mb-10">이달의 와인</h1>
    </v-row>
    <v-row justify="center">
      <v-col cols="3">
        <v-card
          class="mx-auto"
          max-width="380"
          style="
            border-radius: 100px;
            background-color: #232320;
            box-shadow: 0 0 10px grey;
          "
          hover
          outlined
        >
          <v-btn class="mt-7 ml-10" text icon large color="red lighten-2">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <a href="/detail" style="color: gainsboro">
            <v-img
              :src="require('@/assets/sample/sample1.png')"
              height="300"
              contain
            /><v-img />
            <hr style="border-width: 2px; border-color: pink" />
            <v-card-title class="justify-center" style="padding-top: 1px"
              ><div>Dom Pérignon</div>
              P2 Plénitude Brut Champagne 1995</v-card-title
            >
            <v-card-text class="text-center fs-5"
              >#France #Sparkling</v-card-text
            >
          </a>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card
          class="mx-auto"
          max-width="380"
          style="
            border-radius: 100px;
            background-color: #232320;
            box-shadow: 0 0 10px grey;
          "
          hover
          outlined
        >
          <v-btn class="mt-7 ml-10" text icon large color="red lighten-2">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <a href="/detail" style="color: gainsboro">
            <v-img
              :src="require('@/assets/sample/sample2.png')"
              height="300"
              contain
            /><v-img />
            <hr style="border-width: 2px; border-color: pink" />
            <v-card-title class="justify-center" style="padding-top: 1px"
              ><div>Dom Pérignon</div>
              P2 Plénitude Brut Champagne 1995</v-card-title
            >
            <v-card-text class="text-center fs-5"
              >#France #Sparkling</v-card-text
            >
          </a>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card
          class="mx-auto"
          max-width="380"
          style="
            border-radius: 100px;
            background-color: #232320;
            box-shadow: 0 0 10px grey;
          "
          hover
          outlined
        >
          <v-btn class="mt-7 ml-10" text icon large color="red lighten-2">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <a href="/detail" style="color: gainsboro">
            <v-img
              :src="require('@/assets/sample/sample3.png')"
              height="300"
              contain
            /><v-img />
            <hr style="border-width: 2px; border-color: pink" />
            <v-card-title class="justify-center" style="padding-top: 1px"
              ><div>Dom Pérignon</div>
              P2 Plénitude Brut Champagne 1995</v-card-title
            >
            <v-card-text class="text-center fs-5"
              >#France #Sparkling</v-card-text
            >
          </a>
        </v-card>
      </v-col>
    </v-row>
    <br />
  </v-app>
</template>

<script>
export default {
  name: "Home",
  components: {},
  data() {
    return {
      wines: [
        { name: "wine2", picture: require("@/assets/reco2.jpg") },
        { name: "wine5", picture: require("@/assets/wine5.jpg") },
        { name: "wine7", picture: require("@/assets/reco7.png") },
      ],
    };
  },
};
</script>
<style></style>
