<template>
  <vueper-slides
    :breakpoints="breakpoints"
    :touchable="true"
    :gap="2"
    :dragging-distance="50"
    prevent-y-scroll
    style="
      margin-left: 100px;
      margin-right: 100px;
      margin-top: 120px;
      font-family: 'Jeju Gothic', sans-serif !important;
      background-color: rgba(31, 41, 60, 0) !important;
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
          style="background-color: rgba(31, 41, 60, 0.75) !important"
        ></card-movie-view-item-vueper> </template
    ></vueper-slide>
  </vueper-slides>
</template>

<script>
import axios from "axios";
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
  props: {
    keyword: String, // 주소 전체
    is_api: Boolean, // true 일 경우, api요청, false 일 경우, django요청
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
          visibleSlides: 6,
        },
        2200: {
          slideRatio: 1 / 4,
          visibleSlides: 5,
        },
        1900: {
          slideRatio: 1 / 3,
          visibleSlides: 4,
        },
        1600: {
          slideRatio: 1 / 2,
          visibleSlides: 3,
        },
        1300: {
          slideRatio: 1 / 2,
          visibleSlides: 2,
        },
        1000: {
          visibleSlides: 1,
        },
        // The order you list breakpoints does not matter, Vueper Slides will sort them for you.
      },
    };
  },
  methods: {},
  async created() {
    if (this.is_api) {
      // api 요청일 경우
      axios({
        url: this.keyword,
      })
        .then((res) => {
          this.movieDatas = res.data.results;
        })
        .catch((error) => {
          console.log(error);
        });
    } else {
      // django 요청일 경우
      // const response = await fetch(this.keyword);
      // this.movieDatas = await response.json();
      axios({
        url: this.keyword,
      })
        .then((res) => {
          console.log(res.data);
          this.movieDatas = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
  computed: {
    ...mapGetters(["profile"]),
  },
};
</script>

<style>
.vueperslides.vueperslides--ready.vueperslides--touchable
  .vueperslides--bullets-outside {
  background-color: rgba(31, 41, 60, 0.75) !important;
}
</style>
