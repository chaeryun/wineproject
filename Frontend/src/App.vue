<template>
  <v-app>
    <navbar v-if="$route.name !== 'Intro'" />

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Navbar from "./components/layout/Navbar.vue";
export default {
  name: "App",
  components: { Navbar },

  data: () => ({
    //
  }),
};
</script>
