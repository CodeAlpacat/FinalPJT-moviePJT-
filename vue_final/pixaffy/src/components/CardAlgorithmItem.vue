<template>
  <div class="mx-3">
    <h2 class="mt-2 grey--text"></h2>
    <v-container fluid>
      <v-row>
        <!-- <v-col cols="12" sm="3" v-for="movie in movies"></v-col> -->
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'CardAlgorithmItem',
  props: {
    movie: {
      required: true
    },
    genres: {
      required: true
    }
  },

  computed: {
    posterPath() {
      return "https://image.tmdb.org/t/p/w500/" + this.movie.poster_path
    }
  },
  methods: {
    genretypeName(id, index) {
      for(const item of this.genres) {
        if (item.id == id) {
          if(this.movie.genre_ids.length - 1 == index) {
            return item.name
          } else {
            return item.name + ","
          }
        }
      }
    }
  }
}
</script>

<style></style>
