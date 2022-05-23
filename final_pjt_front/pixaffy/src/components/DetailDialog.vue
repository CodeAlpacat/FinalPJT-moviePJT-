<template>
  <div>
    <movie-trailer></movie-trailer>
    <h1>{{ movieModal.id }}</h1>
    <div class="d-block mb-6 mt-6 py-6">
      <v-row justify="space-between">
        <div>
          <span @click="toggleOverview">OVERVIEW</span> |
          <span @click="toggleReview">REVIEW</span> |
          <span @click="toggleDescription">DESCRIPTION</span>
        </div>
        <div>
          <v-btn elevation="8" rounded @click="followMovies(movieModal.id); followOrUnfollow();"
            ><span v-if="unFollowButton">Add To My List</span>
            <span v-if="!unFollowButton">DELETE MOVIE</span></v-btn
          >
        </div>
      </v-row>
    </div>
    <div>
      <div v-show="overviewShow">
        <overview-detail></overview-detail>
      </div>
      <div v-show="reviewShow">
        <review-detail :movie="movieModal"></review-detail>
      </div>
      <div v-show="descriptionShow">
        <description-detail :movie="movieModal"></description-detail>
      </div>
    </div>
  </div>
</template>

<script>
import MovieTrailer from "./MovieTrailer.vue";
import OverviewDetail from "./OverviewDetail.vue";
import ReviewDetail from "./ReviewDetail.vue";
import DescriptionDetail from "./DescriptionDetail.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "DetailDialog",
  props: {
    movieModal: {
      required: true,
    },
  },
  components: {
    MovieTrailer,
    OverviewDetail,
    ReviewDetail,
    DescriptionDetail,
  },
  computed: {
    ...mapGetters(["profile", "currentUser"]),
  },
  data() {
    return {
      overviewShow: true,
      reviewShow: false,
      descriptionShow: false,
      toggleDetail: false,
      unFollowButton: true,
    };
  },
  created() {
    //현재 유저의 프로필 정보(좋아하는 영화 정보 포함)
    const payload = { username: this.currentUser.username };
    this.fetchProfile(payload);
    setTimeout(() => {
      for (let i = 0; i < this.profile.kept_by_user.length; i++) {
      if (this.currentUser.pk === this.profile.kept_by_user[i]) {
        this.unFollowButton = false;
      }
    }
    }, 200);
    
  },
    
  methods: {
    ...mapActions(["fetchProfile", "followMovies"]),
    toggleOverview() {
      this.overviewShow = true;
      this.reviewShow = false;
      this.descriptionShow = false;
    },
    toggleReview() {
      this.overviewShow = false;
      this.reviewShow = true;
      this.descriptionShow = false;
    },
    toggleDescription() {
      this.overviewShow = false;
      this.reviewShow = false;
      this.descriptionShow = true;
    },
    followOrUnfollow() {
      if (this.profile.kept_by_user.includes(this.currentUser.pk)) {
        this.unFollowButton = true;
      } else {
        this.unFollowButton = false;
      }
    },
  },
};
</script>

<style></style>
