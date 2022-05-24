<template>
  <div>
      <genre-based-recommendation></genre-based-recommendation>
      <card-view></card-view>
  </div>
</template>

<script>
import GenreBasedRecommendation from '@/components/GenreBasedRecommendation.vue';
import CardView from '@/components/CardView.vue';
export default {
  name: "HomeView",

  components: {
    CardView,
    GenreBasedRecommendation
  },

};
</script>

<style>

</style>