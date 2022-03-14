<template>
  <v-app id="intro">
    <v-img
      :min-height="'calc(100vh - ' + $vuetify.application.top + 'px)'"
      src="https://cdn.imweb.me/upload/S2017101359e025984d346/671b7600c2bf9.jpg"
    >
      <v-theme-provider dark>
        <v-container fill-height>
          <v-row align="center" class="white--text mx-auto" justify="center">
            <v-alert
              border="top"
              color="#F15F5F"
              shaped
              type="info"
              elevation="15"
              class="text-center"
            >
              <v-col class="white--text text-center" cols="12" tag="h1">
                <span
                  :class="[
                    $vuetify.breakpoint.smAndDown ? 'display-2' : 'display-3',
                  ]"
                  class="font-weight-black"
                >
                  잠깐만요!
                </span>

                <br />
                <br />

                <span
                  :class="[
                    $vuetify.breakpoint.smAndDown ? 'display-1' : 'display-2',
                  ]"
                  class="font-weight-light"
                >
                  만 19세 이상인가요?
                </span>

                <br />
                <br />
                <v-btn text>
                  <span
                    :class="[
                      $vuetify.breakpoint.smAndDown ? 'display-1' : 'display-2',
                    ]"
                    class="font-weight-black"
                    @click="gomain"
                  >
                    Yes
                  </span>
                </v-btn>

                <span
                  :class="[
                    $vuetify.breakpoint.smAndDown ? 'display-0' : 'display-1',
                  ]"
                  class="font-weight-light"
                >
                  or
                </span>

                <v-btn text>
                  <span
                    :class="[
                      $vuetify.breakpoint.smAndDown ? 'display-1' : 'display-2',
                    ]"
                    class="font-weight-black"
                  >
                    No
                  </span>
                </v-btn>
              </v-col>
            </v-alert>
          </v-row>
        </v-container>
      </v-theme-provider></v-img
    >
  </v-app>
</template>

<script>
export default {
  name: "Intro",
  components: {},

  methods: {
    gomain() {
      console.log("click");
      this.$router.push("/main");
    },
  },
};
</script>

<style></style>
