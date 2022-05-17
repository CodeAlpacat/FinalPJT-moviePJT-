<template>
  <div>
    <div >
      hello world
    </div>
    <upcoming-movies></upcoming-movies>
  </div>
</template>

<script>
import UpcomingMovies from '@/components/UpcomingMovies.vue';
export default {
  name: "HomeView",

  components: {
    UpcomingMovies,
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