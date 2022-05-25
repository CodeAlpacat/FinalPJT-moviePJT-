<template>
  <div class="animate__fadeOut">

    <v-sheet
      class="mx-auto"
      elevation="8"
      width="1642px"
      style="background-color: rgb(51, 56, 66)"
    >
      <v-slide-group v-model="model" class="pa-4" show-arrows>
        <v-slide-item
          v-for="movie in movies"
          :key="movie.id"
          style="margin-left: 15px; margin-right: 15px;"
        >
          <card-movie-view-item
            :movie="movie"
            :profile="profile"
            style="background-color: #1f293c !important"
          ></card-movie-view-item>
        </v-slide-item>
      </v-slide-group>
    </v-sheet>
  </div>
</template>

<script>
// import CardMovieViewItem from "./CardMovieViewItem.vue";
import { mapGetters } from "vuex";
export default {
  name: "overviewDetail",
  data: () => ({
    model: null,
    dialog: false,
  }),
  components: {
    CardMovieViewItem: () => import('./CardMovieViewItem.vue')
  },
  computed: {
    ...mapGetters(["profile"]),
  },
  props: {
    movies: Array,
  },
};
</script>

<style></style>
