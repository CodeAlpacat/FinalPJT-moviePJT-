<template>
  <div>
    <v-card-actions class="justify-end">
      <v-btn
        text
        @click="toggleDialogDetail"
      >Close</v-btn>
    </v-card-actions>
    <movie-trailer></movie-trailer>
    <div class="d-block mb-6 mt-6 py-6">
      <v-row
        justify="space-between"
      >
        <div>
          <span @click="toggleOverview">OVERVIEW</span> |
          <span @click="toggleReview">REVIEW</span> |
          <span @click="toggleDescription">DESCRIPTION</span>
        </div>
        <div>
          <v-btn
            elevation="8"
            rounded
          > Add To My List</v-btn>
        </div>
      </v-row>
    </div>
    <div>
      <div v-show="overviewShow">
        <overview-detail></overview-detail>
      </div>
      <div v-show="reviewShow">
        <review-detail></review-detail>
      </div>
      <div v-show="descriptionShow">
        <description-detail :movie="movie"></description-detail>
      </div>
    </div>
  </div>
</template>

<script>
import MovieTrailer from './MovieTrailer.vue'
import OverviewDetail from './OverviewDetail.vue'
import ReviewDetail from './ReviewDetail.vue'
import DescriptionDetail from './DescriptionDetail.vue'
import { mapActions } from 'vuex'

export default {
  name: 'detailDialog',
  components: {
    MovieTrailer,
    OverviewDetail,
    ReviewDetail,
    DescriptionDetail,
  },
  props: {
    movies: {
      type: Array,
      required: true,
    }
  },
  data() {
    return {
      overviewShow: true,
      reviewShow: false,
      descriptionShow: false,
    }

  },
  methods: {
    ...mapActions(['toggleDialogDetail']),
    toggleOverview() {
      this.overviewShow = true
      this.reviewShow = false
      this.descriptionShow = false
    },
    toggleReview() {
      this.overviewShow = false
      this.reviewShow = true
      this.descriptionShow = false
    },
    toggleDescription() {
      this.overviewShow = false
      this.reviewShow = false
      this.descriptionShow = true
    },
  }
}
</script>

<style>

</style>