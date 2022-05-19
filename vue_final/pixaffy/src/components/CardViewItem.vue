<template>
  <v-hover v-slot="{ hover }" open-delay="100">
    <v-card :elevation="hover ? 16 : 2" :class="{ 'on-hover': hover }">
      <!-- 나중에 url을 디테일 페이지로 or 모달 -->
      <router-link :to="{ name: 'home' }">
        <v-img :src="posterPath" alt="포스터가 없습니다" class=""></v-img>
      </router-link>
      <v-card-title class="sutitle-2">{{ movie.title }}</v-card-title>
      <v-card-text>
        <v-row align="center" class="mx-0">
          <v-rating
            :value="movie.vote_average / 2"
            color="amber"
            dense
            half-increments
            readonly
            size="14"
          >
          </v-rating>
          <div class="ml-4">
            {{ movie.vote_average * 10 }} % | {{ movie.release_date }}
          </div>
        </v-row>
        <div class="my-4 subtitle-2">
          <span v-for="(genre, index) in movie.genres" :key="genre">
            {{ genretypeName(genre, index) }}
          </span>
        </div>
      </v-card-text>
    </v-card>
  </v-hover>
</template>

<script>
export default {
  name: "CardViewItem",
  props: {
    movie: {
      required: true,
    },
  },
  data() {
    return {
      genres_list: []
    }
  },

  computed: {
    posterPath() {
      return "https://image.tmdb.org/t/p/w500/" + this.movie.poster_path;
    },
  },
  async created() {
    const response = await fetch("http://127.0.0.1:8000/movies/genres/");
    this.genres_list = await response.json()
  },
  methods: {
    genretypeName(id, index) {
      for (const item of this.genres_list) {
        if (item.id == id) {
          if (this.movie.genres.length - 1 == index) {
            return item.name;
          } else {
            return item.name + ",";
          }
        }
      }
    },
  },
};
</script>

<style></style>
