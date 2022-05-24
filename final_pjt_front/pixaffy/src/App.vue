<template>
  <v-app style="margin-top: 113px; background-color: #1F293C;">
    <v-app-bar
      fixed
      color="#252527"
      dark
      elevate-on-scroll
      src="https://picsum.photos/1920/1080?random"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right,"
        ></v-img>
      </template>
      <template v-slot:extension>
        <v-tabs align-with-title>
          <v-tab>
            <router-link to="/home">HOME</router-link>
          </v-tab>
          <v-tab>
            <router-link to="/movie">MOVIE</router-link>
          </v-tab>
          <v-tab>
            <router-link to="/community">Community</router-link>
          </v-tab>
        </v-tabs>
      </template>

      <v-app-bar-title><v-img src="https://user-images.githubusercontent.com/97648026/170070287-cbed1e07-d24c-4a2b-811e-7c784283b2e5.png" width="250px" style="margin-top:20px;"></v-img></v-app-bar-title>

      <v-spacer></v-spacer>
      <v-autocomplete
        class="hidden-sm-and-down"
        rounded
        v-model="model"
        :items="items"
        :loading="isLoading"
        :search-input.sync="search"
        chips
        clearable
        hide-details
        hide-selected
        item-text="title"
        item-value="overview"
        label="원하는 영화를 검색하세요"
        solo
      >
        <template v-slot:no-data>
          <v-list-item>
            <v-list-item-title>
              무슨 영화를 찾으세요?
              <strong>Movie</strong>
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
            <i class="fa-solid fa-film"></i>
            <span v-text="item.title"></span>
          </v-chip>
        </template>
        <template v-slot:item="{ item }">
          <v-list-item-avatar
            color="indigo"
            class="text-h5 font-weight-light white--text"
          >
            <img :src="`https://image.tmdb.org/t/p/w500/${item.poster_path}`" />
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title v-text="item.title"></v-list-item-title>
            <v-list-item-subtitle
              v-text="item.release_date"
            ></v-list-item-subtitle>
            <!-- <v-dialog v-model="dialog" width="800px">
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  color="red lighten-2"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click="dialog = true"
                >
                  Detail
                </v-btn>
              </template>
              <v-card>
                <detail-dialog
                  :movieModal="movieProps"
                  :profile="profile"
                ></detail-dialog>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="primary" text @click="dialog = false">
                    I accept
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog> -->
          </v-list-item-content>
          <v-list-item-action>
            <i class="fa-solid fa-circle-info"></i>
          </v-list-item-action>
        </template>
      </v-autocomplete>
      <v-spacer></v-spacer>
      <v-menu bottom min-width="200px" rounded offset-y>
        <template v-slot:activator="{ on }">
          <v-btn icon x-large v-on="on">
            <v-avatar color="white" size="48">
              <v-img :src="profile.profile_img"></v-img>
            </v-avatar>
          </v-btn>
        </template>
        <v-card>
          <v-list-item-content class="justify-center">
            <div class="mx-auto text-center">
              <v-avatar>
                <v-img
                  :src="
                    isLoggedIn
                      ? profile.profile_img
                      : 'https://i.pinimg.com/originals/89/64/99/8964998576cfac440b3a14df748fc670.png'
                  "
                ></v-img>
              </v-avatar>
              <h3>{{ profile.username }}</h3>
              <p class="text-caption mt-1" v-if="isLoggedIn">
                {{ profile.email }}
              </p>

              <v-divider class="my-3"></v-divider>

              <router-link :to="{ name: 'profile', params: { username } }">
                <v-btn depressed rounded text>Profile</v-btn>
              </router-link>
              <v-divider class="my-3"></v-divider>
              <router-link to="/login" v-if="!isLoggedIn"
                ><v-btn depressed rounded text>LogIn</v-btn></router-link
              >

              <router-link
                v-if="isLoggedIn"
                :to="{
                  name: 'profileEdit',
                  params: { username: profile.username, userInfo: profile },
                }"
                ><v-btn depressed rounded text>Edit Profile</v-btn></router-link
              >

              <v-divider class="my-3"></v-divider>
              <router-link to="/signup" v-if="!isLoggedIn">
                <v-btn depressed rounded text> Signup </v-btn>
              </router-link>
              <router-link
                to="/logout"
                class="btn__router_link"
                v-if="isLoggedIn"
                ><v-btn depressed rounded text>Logout</v-btn></router-link
              >
            </div>
          </v-list-item-content>
        </v-card>
      </v-menu>
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
    isLoading: false,
    items: [],
    model: null,
    search: null,
    tab: null,
    username: null,
  }),
  computed: {
    ...mapGetters(["isLoggedIn", "currentUser", "profile", "isLoggedIn"]),
  },
  methods: {
    ...mapActions(["fetchCurrentUser", "fetchProfile"]),
  },
  watch: {
    model(val) {
      if (val != null) this.tab = 0;
      else this.tab = null;
    },
    search() {
      // Items have already been loaded
      if (this.items.length > 0) return;

      this.isLoading = true;

      // Lazily load input items
      fetch("http://localhost:8000/movies/")
        .then((res) => res.clone().json())
        .then((res) => {
          this.items = res;
        })
        .catch((err) => {
          console.log(err);
        })
        .finally(() => (this.isLoading = false));
    },
  },
  created() {
    this.fetchCurrentUser();
    this.username = JSON.parse(localStorage.getItem("currentUser")).username;
    const payload = { username: this.username };
    this.fetchProfile(payload);
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
.btn__router_link {
  color: grey !important;
  font-family: "Poppins", sans-serif !important;
}
</style>
