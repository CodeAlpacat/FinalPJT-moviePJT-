<template>
  <!-- <v-app>
    <v-app-bar app color="blue darken-4" height="50px" dark shrink-on-scroll absolute scroll-target="#scrolling-techniques-2">
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
    <v-sheet id="scrolling-techniques-2" class="overflow-y-auto">
      <v-container style="height: 130px"> </v-container>
    </v-sheet>

    <transition
      mode="out-in"
      enter-active-class="animate__animated animate__fadeIn animate__faster"
      leave-active-class="animate__animated animate__fadeOut animate__faster"
    >
      <router-view />
    </transition>
  </v-app> -->
  <v-app>
    <v-app-bar
      fixed
      color="#fcb69f"
      dark
      shrink-on-scroll
      src="https://picsum.photos/1920/1080?random"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-app-bar-title
        >도라이썬

        <v-text-field label="Filled" filled></v-text-field>
        <v-btn>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-app-bar-title>
      <v-spacer></v-spacer>

      <v-btn>
        <router-link :to="{ name: 'profile', params: { username } }">
          {{ currentUser.username }}'s page
        </router-link>
      </v-btn>
      <v-btn>
        <router-link to="/home">HOME</router-link>
      </v-btn>
      <v-btn>
        <router-link to="/community">커뮤니티</router-link>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
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
    window.addEventListener( "activate", event => { event.waitUntil( async function () { // Feature-detect
     if ( self.registration.navigationPreload ) { // Enable navigation preloads! 
     console.log( "Enable navigation preloads!" ); 
     await self.registration.navigationPreload.enable(); } return; } ) } );
    window.addEventListener('fetch', event => {
          // Prevent the default, and handle the request ourselves.
          event.respondWith(async function() {
            // Try to get the response from a cache.
            const cachedResponse = await caches.match(event.request);
            // Return it if we found one.
            if (cachedResponse) return cachedResponse;
            // If we didn't find a match in the cache, use the network.
            return fetch(event.request);
          }());
        });


import { mapActions, mapGetters } from "vuex";
export default {
  name: "App",
  components: {},
  data: () => ({
    collapseOnScroll: true,
  }),
  computed: {
    ...mapGetters(["isLoggedIn", "currentUser"]),
    username() {
      return this.currentUser.username ? this.currentUser.username : "guest";
    },
  },
  methods: {
    ...mapActions(["fetchCurrentUser"]),
  },
  created() {
    this.fetchCurrentUser();
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
  font-family: "Jeju Gothic", sans-serif !important;
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
