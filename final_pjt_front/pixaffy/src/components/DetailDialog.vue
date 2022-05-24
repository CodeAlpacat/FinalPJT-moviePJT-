<template>
  <div>
    <movie-trailer :movie="movieModal" :trailer="trailer"></movie-trailer>
    <div class="d-block mb-6 mt-6 py-6">
      <v-row justify="space-between">
        <div>
          <span @click="toggleOverview">OVERVIEW</span> |
          <span @click="toggleReview">REVIEW</span> |
          <span @click="toggleDescription">DESCRIPTION</span>
        </div>
        <div>
          <button
            class="profile__div1__follow_btn"
            @click="
              followMovies(movieModal.id);
              followOrUnfollow();
            "
          >
            <span v-if="unFollowButton">Add To My List</span>
            <span v-if="!unFollowButton">DELETE MOVIE</span>
          </button>
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
import axios from 'axios';

export default {
  name: "DetailDialog",
  props: {
    movieModal: {
      required: true,
    },
    profile: {
      required: true,
    },
  },
  components: {
    MovieTrailer,
    OverviewDetail,
    ReviewDetail,
    DescriptionDetail,
  },
  data() {
    return {
      overviewShow: true,
      reviewShow: false,
      descriptionShow: false,
      toggleDetail: false,
      unFollowButton: true,
      userInfo: null,
      trailer: null,
    };
  },
  created() {
    axios({
        url: `https://api.themoviedb.org/3/movie/${this.movieModal.id}/videos?api_key=c0ea5b6535679915d16aada2f7427157`
      })
        .then(res => {
          this.trailer = res.data.results[0].key
        })
        .catch(error => {
          console.log(error)
        })
    this.userInfo = JSON.parse(localStorage.getItem("currentUser")).pk;
    for (let i = 0; i < this.profile.keep_movies; i++) {
      for (
        let j = 0;
        j < this.profile.keep_movies[i].kept_by_user.length;
        j++
      ) {
        if (this.userInfo == this.profile.keep_movies[i].kept_by_user[j]) {
          this.unFollowButton = false;
          break;
        }
      }
    }
  },
  computed: {
    ...mapGetters(['isVideo'])
  },

  methods: {
    ...mapActions(["followMovies"]),
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
      if (this.profile.kept_by_user) {
        if (this.profile.kept_by_user.some((item) => item == this.userInfo)) {
          this.unFollowButton = true;

        } else {
          this.unFollowButton = false;
        }
      } else {
        if (this.profile.keep_movies.some((item) => item.id == this.userInfo)) {
          this.unFollowButton = true;
        
        } else {
          this.unFollowButton = false;
        
        }
      }
    },
  },
};
</script>

<style>
.profile__div1__follow_btn {
  width: 180px;
  height: 40px;
  border-radius: 30px;
  border: none;
  color: white;
  background-color: rgb(23, 146, 195);
  text-align: center;
  opacity: 1.3;
  cursor: pointer;
  transition: 0.5s;
  margin-top: 35px;
  box-shadow: 2px 2px 2px grey;
}

.profile__div1__follow_btn:hover {
  opacity: 0.9;
}

.profile__div1__follow_btn span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
  font-size: 20px;
  font-weight: bold;
}

.profile__div1__follow_btn span:after {
  content: "\f234";
  font-family: "Font Awesome 5 Free";
  font-weight: 900;
  font-size: 20px;
  position: absolute;
  opacity: 0;
  bottom: -2px;
  right: -10px;
  transition: 0.5s;
}

.profile__div1__follow_btn:hover span {
  padding-right: 25px;
}

.profile__div1__follow_btn:hover span:after {
  opacity: 1;
  right: -1;
}
</style>
