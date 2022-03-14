<template>
  <div>
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list class="pa-1">
        <v-list-tile avatar>
          <v-list-tile-avatar>
            <img src="" />
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>Wine website</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
      <v-list class="pt-0" dense>
        <v-divider></v-divider>
        <v-list-tile v-for="item in items" :key="item.title" :to="item.to">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar dark color="blue-gray" clipped-left fixed app>
      <v-toolbar-side-icon
        @click.stop="drawer = !drawer"
        class="hidden-md-and-up"
      ></v-toolbar-side-icon>
      <v-toolbar-title class="headline text-uppercase white--text">
        <span>My </span>
        <span class="font-weight-light" style="margin-right:200px">Wine</span>
      </v-toolbar-title>
      <v-autocomplete
        v-model="model"
        :items="items"
        :loading="isLoading"
        :search-input.sync="search"
        chips
        clearable
        hide-details
        hide-selected
        item-text="name"
        item-value="symbol"
        label="검색어를 입력해주세요..."
        solo
      >
        <template v-slot:no-data>
          <v-list-item>
            <v-list-item-title>
              Winery와 Wine명으로 검색해주세요
              <strong>!</strong>
            </v-list-item-title>
          </v-list-item>
        </template>
        <template v-slot:selection="{ attr, on, item, selected }">
          <v-chip
            v-bind="attr"
            :input-value="selected"
            color="blue-grey"
            class="white--text"
            v-on="on"
          >
            <span v-text="item.name"></span>
          </v-chip>
        </template>
        <template v-slot:item="{ item }">
          <v-list-item-avatar
            color="indigo"
            class="text-h5 font-weight-light white--text"
          >
            {{ item.name.charAt(0) }}
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title v-text="item.name"></v-list-item-title>
            <v-list-item-subtitle v-text="item.symbol"></v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-icon>mdi-bitcoin</v-icon>
          </v-list-item-action>
        </template>
      </v-autocomplete>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat to="/main">Home</v-btn>
        <v-btn flat to="/about">Wine</v-btn>
        <v-btn flat to="/recommend">Recommend</v-btn>
        <v-btn flat to="/vintage">Vintage</v-btn>
        <v-btn flat to="/lounge">Lounge</v-btn>
        <v-btn flat to="/login"><img src="../assets/login.png" style="height:30px;"></v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      drawer: null,
      items: [
        { title: "Home", icon: "dashboard", to: "/main" },
        { title: "About", icon: "question_answer", to: "/about" },
      ],
    };
  },
};
</script>
