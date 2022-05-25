<template>
  <!-- <div>
    <h2 class="mt-2" style="color:#E5EAEE; font-family: 'Jeju Gothic', sans-serif !important;">Now Playing</h2>
    <v-container fluid>
      <v-row>
        <v-col
          cols="12"
          sm="3"
          lg="2"
          v-for="movie in movieDatas"
          :key="movie.id"
        >
          <card-view-item :movieProps="movie"></card-view-item>
        </v-col>
      </v-row>
    </v-container>
  </div> -->
  <vueper-slides
    :breakpoints="breakpoints"
    :touchable="true"
    :gap="2"
    :dragging-distance="50"
    prevent-y-scroll
    style="
      margin-left: 100px;
      margin-right: 100px;
      margin-top: 150px;
      font-family: 'Jeju Gothic', sans-serif !important;
      background-color: #1f293c !important;
    "
  >
    <vueper-slide
      v-for="movie in movieDatas"
      :key="movie.id"
      class="d-flex justify-center align-center"
      ><template v-slot:content
        ><card-movie-view-item-vueper
          :movie="movie"
          :profile="profile"
          style="background-color: #1f293c !important"
        ></card-movie-view-item-vueper> </template
    ></vueper-slide>
  </vueper-slides>
</template>

<script>
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";
import { mapGetters } from "vuex";
import CardMovieViewItemVueper from "./CardMovieViewItemVueper.vue";

// import CardViewItem from "./CardViewItem.vue";
export default {
  name: "CardAlgorithm",
  components: {
    VueperSlides,
    VueperSlide,
    // CardViewItem,
    CardMovieViewItemVueper,
  },
  data() {
    return {
      movieDatas: [],
      breakpoints: {
        3000: {
          slideRatio: 1 / 5,
          visibleSlides: 6,
        },
        2400: {
          slideRatio: 1 / 5,
          visibleSlides: 4,
        },
        2000: {
          slideRatio: 1 / 4,
          visibleSlides: 3,
        },
        1600: {
          slideRatio: 1 / 3,
          visibleSlides: 2,
        },
        1000: {
          slideRatio: 1 / 2,
          arrows: false,
          bulletsOutside: true,
          visibleSlides: 1,
        },
        // The order you list breakpoints does not matter, Vueper Slides will sort them for you.
      },
    };
  },
  methods: {},
  async created() {
    const response = await fetch("http://127.0.0.1:8000/movies/nowplaying/");
    this.movieDatas = await response.json();
  },
  computed: {
    ...mapGetters(["profile"]),
  },
};
</script>

<style></style>
