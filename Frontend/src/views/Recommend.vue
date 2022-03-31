<template>
  <div class="recommend">
    <Navbar />
    <h1 class="text-center mb-10">Recommend</h1>
    <v-row class="text-h7" justify="center">
      <h2 class="ml-10 pb-5"> | 최근 찜한 목록</h2>
    </v-row>
    <v-row justify="center">
      <v-col cols="3">
        <v-card class="mx-2 ml-10" max-width="300" tile hover outlined id="wish-card">
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="200"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-2" max-width="300" tile hover outlined id="wish-card">
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="200"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-2" max-width="300" hover outlined>
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample2.png')"
            height="200"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-2" max-width="300" hover outlined>
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="200"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <v-row class="pa-5-mt-1 text-h7 pt-10 pb-5 border-top mt-10" justify="center" height="200">
      <h2 class="ml-10">| OO님과 유사한 취향의 와인</h2>
    </v-row>
    <v-row justify="center">
      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample2.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>
<script>
import Navbar from "@/components/layout/Navbar";

export default {
  name: "Recommend",
  components: {
    Navbar,
  },
};
</script>

<style>
</style>