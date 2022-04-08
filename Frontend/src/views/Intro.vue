<template>
  <v-app id="intro">
    <v-img
      :max-height="'calc(100vh - ' + $vuetify.application.top + 'px)'"
      src="https://cdn.imweb.me/upload/S2017101359e025984d346/671b7600c2bf9.jpg"
    >
      <v-theme-provider dark>
        <v-container fill-height>
          <v-row align="center" class="white--text mx-auto" justify="center" id="alert-card">
            <div
              class="text-center"
            >
              <div class="white--text text-center" cols="12" tag="h1">
                <span
                  :class="[
                    $vuetify.breakpoint.smAndDown ? 'display-2' : 'display-3',
                  ]"
                  class="font-weight-black fw-bold"
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
                  <h1 style="color: white;">만 19세 이상인가요?</h1>
                </span>

                <v-btn text>
                  <span
                    :class="[
                      $vuetify.breakpoint.smAndDown ? 'display-1' : 'display-2',
                    ]"
                    class="font-weight-black mr-5"
                    @click="gomain"
                  >
                    Yes 
                  </span>
                </v-btn>

                <span
                  :class="[
                    $vuetify.breakpoint.smAndDown ? 'display-0' : 'display-1',
                  ]"
                  class="font-weight-black"
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
              </div>
            </div>
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
      this.$router.push("/home");
    },
  },
};
</script>

<style>
#alert-card{
   height: 380px;
   max-width: 600px;
   background-color: #050000;
   background-color: rgba(3, 0, 0, 0.397);
   border-radius: 30px;
}
</style>
