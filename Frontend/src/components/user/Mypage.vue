<template>
  <div class="wine mt-13">
    <v-container>
      <h1>My page</h1>
      <v-row class="text-h7" justify="center">
        <h2 class="ml-10 pb-5">| 내가 찜한 목록</h2>
      </v-row>
      <v-row justify="center" class="mb-5">
        <v-col cols="2">
          <v-card
            class="mx-auto"
            max-width="260"
            style="
              border-radius: 200px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-7 ml-15" text icon large color="red">
              <v-icon>mdi-circle</v-icon> RED
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample1.png')"
                height="200"
                contain
                style="margin-bottom: 50px"
              /><v-img />
            </a>
          </v-card>
        </v-col>

        <v-col cols="2">
          <v-card
            class="mx-auto"
            max-width="260"
            style="
              border-radius: 200px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-7 ml-15" text icon large color="green">
              <v-icon>mdi-circle</v-icon>WHITE
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample2.png')"
                height="200"
                contain
                style="margin-bottom: 50px"
              /><v-img />
            </a>
          </v-card>
        </v-col>

        <v-col cols="2">
          <v-card
            class="mx-auto"
            max-width="260"
            style="
              border-radius: 200px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-7 ml-15" text icon large color="red lighten-3">
              <v-icon>mdi-circle</v-icon>ROSE
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample3.png')"
                height="200"
                contain
                style="margin-bottom: 50px"
              /><v-img />
            </a>
          </v-card>
        </v-col>

        <v-col cols="2">
          <v-card
            class="mx-auto"
            max-width="260"
            style="
              border-radius: 200px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-7 ml-15" text icon large color="blue">
              <v-icon>mdi-circle</v-icon>PORT
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample1.png')"
                height="200"
                contain
                style="margin-bottom: 50px"
              /><v-img />
            </a>
          </v-card>
        </v-col>
        <v-col cols="2">
          <v-card
            class="mx-auto"
            max-width="260"
            style="
              border-radius: 200px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn class="mt-7 ml-16" text icon large color="purple lighten-2">
              <v-icon>mdi-circle</v-icon> SPARKLING
            </v-btn>
            <a href="/detail" style="color: gainsboro">
              <v-img
                :src="require('@/assets/sample/sample2.png')"
                height="200"
                contain
                style="margin-bottom: 50px"
              /><v-img />
            </a>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import http from "@/util/http-common";

export default {
  name: "mypage",
  components: {},

  data: () => ({}),

  computed: {
    // user 정보 가져오기
    userInfo() {
      return this.$store.state.userInfo;
    },
  },

  created() {
    this.getUserWine();
  },

  methods: {
    async getUserWine() {
      await http({
        methods: "get",
        url: "wine/latest_wine_list/" + this.userInfo.username + "/",
      })
        .then((res) => {
          console.log("winelist : ", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style></style>
