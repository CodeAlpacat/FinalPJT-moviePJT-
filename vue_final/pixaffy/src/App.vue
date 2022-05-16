<template>
  <v-app>
    <app-bar>
    </app-bar>
    <router-view />
  </v-app>
</template>

<script>
import AppBar from "./components/AppBar.vue";
export default {
  name: "App",
  components: {
    AppBar,
  },
  data: () => ({
    //
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
</style>
