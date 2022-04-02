<template>
  <div class="recommend">
    <Navbar />
    <h1>Recommend</h1>
    <v-row class="text-h7" justify="center">
      <h2 class="ml-10 pb-5"> | 최근 찜한 목록</h2>
    </v-row>
    <v-row justify="center" class="mb-5">
      <v-col cols="2">
          <v-card class="mx-auto" max-width="260"  style="border-radius: 200px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="200"
            contain
            style="margin-bottom: 50px;"
          /><v-img />
          </a>
        </v-card>
      </v-col>

       <v-col cols="2">
          <v-card class="mx-auto" max-width="260"  style="border-radius: 200px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample2.png')"
            height="200"
            contain
            style="margin-bottom: 50px;"
          /><v-img />
          </a>
        </v-card>
      </v-col>

      <v-col cols="2">
          <v-card class="mx-auto" max-width="260"  style="border-radius: 200px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="200"
            contain
            style="margin-bottom: 50px;"
          /><v-img />
          </a>
        </v-card>
      </v-col>

      <v-col cols="2">
          <v-card class="mx-auto" max-width="260"  style="border-radius: 200px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="200"
            contain
            style="margin-bottom: 50px;"
          /><v-img />
          </a>
        </v-card>
      </v-col>
    <v-col cols="2">
          <v-card class="mx-auto" max-width="260"  style="border-radius: 200px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample2.png')"
            height="200"
            contain
            style="margin-bottom: 50px;"
          /><v-img />
          </a>
        </v-card>
      </v-col>

    </v-row>

    <v-row class="pa-5-mt-1 text-h7 pt-10 pb-5 border-top mt-10" justify="center" height="200">
      <h2 class="ml-10">| OO님과 유사한 취향의 와인</h2>
    </v-row>
     <v-row justify="center" class="mb-5">
      <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
        </v-card>
      </v-col>

       <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample2.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
        </v-card>
      </v-col>

      <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
        </v-card>
      </v-col>

      <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
        </v-card>
      </v-col>
    </v-row>
     <v-row justify="center" class="mb-5">
      <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
        </v-card>
      </v-col>

       <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample2.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
        </v-card>
      </v-col>

      <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
        </v-card>
      </v-col>

      <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; background-color: #FFEAEA;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: black">
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
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