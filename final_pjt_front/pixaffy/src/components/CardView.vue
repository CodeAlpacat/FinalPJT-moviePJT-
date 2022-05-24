<template>
  <!-- <div>
    <h2 class="mt-2" style="color: #e5eaee">Now Playing</h2>
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
    :visible-slides="5"
    :touchable="true"
    :gap="2"
    :dragging-distance="50"
    prevent-y-scroll
    style="margin-left: 100px; margin-right: 100px; margin-top: 150px;"
  >
    <vueper-slide v-for="movie in movieDatas" :key="movie.id"
      ><template v-slot:content
        ><vueper-card :movieProps="movie"></vueper-card> </template
    ></vueper-slide>
  </vueper-slides>
</template>

<script>
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";
import VueperCard from "./VueperCard.vue";
// import CardViewItem from "./CardViewItem.vue";
export default {
  name: "CardAlgorithm",
  components: {
    VueperSlides,
    VueperSlide,
    // CardViewItem,
    VueperCard,
  },
  data() {
    return {
      movieDatas: [],
      breakpoints: {
        1200: {
          slideRatio: 1 / 5,
        },
        900: {
          slideRatio: 1 / 3,
        },
        600: {
          slideRatio: 1 / 2,
          arrows: false,
          bulletsOutside: true,
        },
        // The order you list breakpoints does not matter, Vueper Slides will sort them for you.
        1100: {
          slideRatio: 1 / 4,
        },
      },
    };
  },
  methods: {},
  async created() {
    const response = await fetch("http://127.0.0.1:8000/movies/nowplaying/");
    this.movieDatas = await response.json();
  },
};
</script>

<style></style>
