<template>
  <div>
    <div >
      <card-algorithm></card-algorithm>
    </div>
    <upcoming-movies></upcoming-movies>
  </div>
</template>

<script>
import UpcomingMovies from '@/components/UpcomingMovies.vue';
import CardAlgorithm from '@/components/CardAlgorithm.vue';
export default {
  name: "HomeView",

  components: {
    UpcomingMovies,
    CardAlgorithm
  },

  data() {
    return {
      movies: [],
    };
  },

  async created() {
    const response = await fetch("http://127.0.0.1:8000/movies/");
    this.movies = await response.json();
  },
};
</script>

<style>

</style>