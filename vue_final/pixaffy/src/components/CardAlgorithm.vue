<template>
  <div>
    <card-algorithm-item></card-algorithm-item>
  </div>
</template>

<script>
import CardAlgorithmItem from './CardAlgorithmItem.vue'
export default {
  name: 'CardAlgorithm',
  components: {
    CardAlgorithmItem,
  },
  data() {
    return {
      movies: [],
      genres: []
    }
  },
  async mounted() {
    this.fetchGenres();
    try {
      const response = await this.$http.get("/movie/popular")
      this.movies = response.data.results
    } catch(error) {
      console.log(error)
    }
  },
  methods: {
    async fetchGenres() {
      try {
        const response = await this.$http.get("/genre/movie/list")
        this.genres = response.data.genres;
      } catch(error) {
        console.log(error)
      }
    }
  }
}
</script>

<style>

</style>