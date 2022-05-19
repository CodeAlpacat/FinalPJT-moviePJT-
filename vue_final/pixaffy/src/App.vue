<template>
  <v-app>
      <v-app-bar app color="secondary" dark prominent shrink-on-scroll>
        <div class="d-flex">
          <v-app-bar-nav-icon> </v-app-bar-nav-icon>
          <v-toolbar-title>Title</v-toolbar-title>
        </div>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
        <v-menu left bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon v-bind="attrs" v-on="on">
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
            <v-btn icon v-bind="attrs" v-on="on">
              <router-link to="/">시작</router-link>
            </v-btn>
            <v-btn icon v-bind="attrs" v-on="on">
              <router-link to="/home">HOME</router-link>
            </v-btn>
            <v-btn icon v-bind="attrs" v-on="on">
              <router-link to="/movie">MOVIE</router-link>
            </v-btn>
          </template>
        </v-menu>
      </v-app-bar>
      <v-sheet>
        <v-container style="height: 130px"></v-container>
      </v-sheet>
    <router-view />
  </v-app>
</template>

<script>
export default {
  name: "App",
  components: {},
  data: () => ({
    collapseOnScroll: true,
  }),

};
</script>
<style lang="scss">
nav {
  padding: 30px;
  background-color: #2e343b;

  a {
    font-weight: bold;
    font-size: 24px;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#app-background {
  background-color: #2e343b;
}
.app__bar {
  position: sticky;
}
</style>
