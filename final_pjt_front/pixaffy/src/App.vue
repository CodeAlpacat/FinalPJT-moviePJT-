<template>
  <v-app>
    <v-app-bar app color="blue darken-4" height="50px" dark shrink-on-scroll>
      <div class="d-flex">
        <v-app-bar-nav-icon> </v-app-bar-nav-icon>
        <v-toolbar-title></v-toolbar-title>
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
          |
          <v-btn icon v-bind="attrs" v-on="on">
            <router-link to="/signup">Signup</router-link>
          </v-btn>
          |
          <v-btn icon v-bind="attrs" v-on="on">
            <router-link to="/login">LogIn</router-link>
          </v-btn>
          |
          <v-btn icon v-bind="attrs" v-on="on">
            <router-link to="/logout">Logout</router-link>
          </v-btn>
          <v-btn icon v-bind="attrs" v-on="on">
            <router-link :to="{ name: 'profile', params: { username } }">
              {{ currentUser.username }}'s page
            </router-link>
          </v-btn>
        </template>
      </v-menu>
      <template v-slot:extension>
        <v-autocomplete clearable dense rounded solo-inverted></v-autocomplete>
      </template>
    </v-app-bar>
    <v-sheet>
      <v-container style="height: 130px"> </v-container>
    </v-sheet>

    <transition
      mode="out-in"
      enter-active-class="animate__animated animate__fadeIn animate__faster"
      leave-active-class="animate__animated animate__fadeOut animate__faster"
    >
      <router-view />
    </transition>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  name: "App",
  components: {},
  data: () => ({
    collapseOnScroll: true,
  }),
  computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
};
</script>
<style lang="scss">
@import url(//fonts.googleapis.com/earlyaccess/jejogothic.css);
nav {
  padding: 10px;
}
.v-application span a {
  color: rgb(242, 237, 243);
  text-decoration: none;
  font-family: 'Jeju Gothic', sans-serif;
}
#app-background {
  background-color: #2e343b;
}
.app__bar {
  position: sticky;
}
#app-bar {
  max-height: 200px;
}
</style>
