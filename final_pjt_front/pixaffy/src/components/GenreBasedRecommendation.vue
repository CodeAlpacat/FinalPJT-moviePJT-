<template>
  <div id="carouselMovie">
    <h2 class="mx-3">좋아하는 장르가 있어? 옜다~</h2>
    <carousel-3d
      :controls-visible="true"
      :clickable="false"
      :key="algoBasedMovies.length"
      :listData="algoBasedMovies"
      :height="500"
    >
      <Slide :index="i" v-for="(movie, i) in this.algoBasedMovies" :key="i">
        <figure>
          <img
            :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path"
            alt=""
          />
          <figcaption class="d-flex justify-space-between">
            <!-- 상세페이지로 이동 or 다이얼로그 띄움 -->
            <v-btn text color="white">{{
              movie.title
            }}</v-btn>
            <v-rating
              class="mt-2"
              :value="movie.vote_average / 2"
              color="amber"
              dense
              half-increments
              readonly
              size="14"
            >
            </v-rating>
          </figcaption>
        </figure>
      </Slide>
    </carousel-3d>
  </div>
</template>

<script>
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
  },
  computed: {
    ...mapGetters(["currentUser"]),
  },
  async created() {
    //추천 알고리즘의 User PK가 필요함
    if (typeof this.currentUser.pk == "number") {
      this.userInfo = this.currentUser.pk;
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
</style>
