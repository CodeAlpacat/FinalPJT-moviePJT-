<template>
  <div id="carouselMovie">
    <!-- <h2 class="mx-3" style="color:#E5EAEE; font-family: 'Jeju Gothic', sans-serif !important;">좋아하는 장르가 있어? 옜다~</h2> -->
    <carousel-3d
      :controls-visible="true"
      :clickable="false"
      :key="algoBasedMovies.length"
      :listData="algoBasedMovies"
      :height="800"
      :width="550"
    >
      <Slide :index="i" v-for="(movie, i) in this.algoBasedMovies" :key="i">
        <genre-based-recommendations-card :movie="movie" :profile="profile"></genre-based-recommendations-card>
      </Slide>
    </carousel-3d>
  </div>
</template>

<script>
import GenreBasedRecommendationsCard from "./GenreBasedRecommendationsCard.vue";
import { Carousel3d, Slide } from "vue-carousel-3d";
import { mapGetters } from "vuex";
export default {
  name: "GenreBasedRecommendation",
  data() {
    return {
      algoBasedMovies: [],
      userInfo: 71,
    };
  },
  components: {
    Carousel3d,
    Slide,
    GenreBasedRecommendationsCard,
  },
  computed: {
    ...mapGetters(["currentUser", "profile", "isLoggedIn"]),
  },
  async mounted() {
    //추천 알고리즘의 User PK가 필요함
    if (this.isLoggedIn) {
      if (this.currentUser.pk) {
        this.userInfo = this.currentUser.pk;
      } else {
        this.userInfo = JSON.parse(localStorage.getItem("currentUser")).pk;
      }
      const response = await fetch(
        `http://127.0.0.1:8000/movies/recommend/${this.userInfo}/`
      );
      this.algoBasedMovies = await response.json();
    } else {
      const response = await fetch(`http://127.0.0.1:8000/movies/nowplaying/`);
      this.algoBasedMovies = await response.json();
    }
  },
};
</script>

<style>
.carousel-3d-container figure {
  margin: 0;
}

.carousel-3d-container figcaption {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  bottom: 0;
  padding: 15px;
  font-size: 12px;
  min-width: 100%;
  box-sizing: border-box;
}

.next span,
.prev span {
  color: red;
}

.slide-btn {
  color: white;
}

#carouselMovie {
  z-index: 1;
}

</style>
