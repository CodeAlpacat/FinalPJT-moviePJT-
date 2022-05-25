<template>
  <div
    style="
      background-color: rgb(75,82,97);
    "
  >
    <movie-trailer :movie="movieModal"></movie-trailer>
    <div class="d-block mb-6 mt-6 py-6">
      <v-row justify="space-between">
        <div
          style="
            display: flex;
            align-items: center;
          "
          >
            <div
              style="
                color: rgb(223,220,221);
                padding: 10px;
                margin: 5px 10px;
                border-radius: 40%;
                font-family: 'Jeju Gothic', sans-serif !important;
                font-weight: bold;
                transition: all 2s;
                cursor: pointer;
                "
              @click="toggleOverview"
            >
              RELATED MOVIE
            </div>
            <div
              style="
                color: rgb(223,220,221);
                padding: 10px;
                margin: 5px 10px;
                border-radius: 40%;
                font-family: 'Jeju Gothic', sans-serif !important;
                font-weight: bold;
                transition: all 2s;
                cursor: pointer;
                "
              @click="toggleReview"
            >
              REVIEW
            </div>
            <div
              style="
                color: rgb(223,220,221);
                padding: 10px;
                margin: 5px 10px;
                border-radius: 40%;
                font-family: 'Jeju Gothic', sans-serif !important;
                font-weight: bold;
                transition: all 2s;
                cursor: pointer;
                "
              @click="toggleDescription"
            >
              DESCRIPTION
            </div>
        </div>
        <div style="margin-right: 30px; align-items: center; display: flex;">
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
    <transition
      mode="out-in"
      enter-active-class="animate__animated animate__fadeIn animate__faster animate__delay-1s"
      leave-active-class="animate__animated animate__fadeOut animate__faster"
    >
      <div v-if="overviewShow">
        <overview-detail :movies="recommendMovie"></overview-detail>
      </div>
    </transition>
    <transition
      mode="out-in"
      enter-active-class="animate__animated animate__fadeIn animate__faster animate__delay-1s"
      leave-active-class="animate__animated animate__fadeOut animate__faster"
    >
      <div v-if="reviewShow">
        <review-detail :movie="movieModal"></review-detail>
      </div>
    </transition>
    <transition
      mode="out-in"
      enter-active-class="animate__animated animate__fadeIn animate__faster animate__delay-1s"
      leave-active-class="animate__animated animate__fadeOut animate__faster"
    >
      <div v-if="descriptionShow">
        <description-detail :movie="movieModal"></description-detail>
      </div>
    </transition>
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
      recommendMovie: null,
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
    axios({
      url: `https://api.themoviedb.org/3/movie/${this.movieModal.id}/recommendations?api_key=c0ea5b6535679915d16aada2f7427157&language=ko-KR&page=1`
    })
      .then(res => {
        this.recommendMovie = res.data.results
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
@import "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css";
.profile__div1__follow_btn {
  width: 180px;
  height: 40px;
  border-radius: 30px;
  border: none;
  color: white;
  background-color: rgb(30, 136, 229);
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

.hover {
  color: white;
  background-color: rgb(27,45,71);
}

</style>
