<template>
  <div :class="best ? 'best-review' : 'none-best'">
  <!-- 위에서 best 값이 true 일 경우, best-review style 적용, false 일 경우, none-best style 적용 -->
    <div class="col-2 username">
      {{review.user.username}}
    </div>
    <div class="col-8 review-content">
      {{review.content}}
      <span v-if="(review.user.username === currentUser.username)">
        <v-btn
          icon
          small
          :color="colorActivate ? 'red darken-2' : 'grey'"
          @mouseover="colorActivate = true"
          @mouseleave="colorActivate = false"
          @click="deleteReview({'moviePk': movie.id, 'reviewPk': review.pk})"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </span>  
    </div>
    <div class="col-2 likes-count">
      <div style="margin-top: 14px">
        <v-btn
          icon
          :color="reviewLiked ? 'amber lighten-1' : 'grey'"
          @click="likeReview({'moviePk': movie.id, 'reviewPk': review.pk}); reviewLiked = !reviewLiked;"
        >
        <!-- 위에서 reviwLiked 여부로 색상 반전, 클릭시 toggleReviewLiked 값이 true/false로 토글 -->
          <v-icon>mdi-star</v-icon>
        </v-btn>
      </div>
      <div style="font-size:14px; font-weight: bold;">
        {{review.like_count}}
      </div>
      <!-- 좋아요 수 -->
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'ReviewView',
  props: {
    review: Object,
    movie: Object,
    best: Boolean,
  },
  data () {
    const user = JSON.parse(localStorage.getItem("currentUser"))
    return {
        page: 1,
        currentUser: JSON.parse(localStorage.getItem("currentUser")),
        reviewLiked: (this.review.liked_users).includes(user.pk),
        // best: false,
        colorActivate: false,
      }
    },
  watch: {
    reviewLiked: function () {
      return this.review.liked_users.includes(JSON.parse(localStorage.getItem('currentUser')).pk)
    },

  },
  computed: {
    ...mapGetters(['currentReview'])
  },
  methods: {
    ...mapActions(['likeReview','deleteReview']),
    // toggleReviewLiked (){
    //   this.reviewLiked = !this.reviewLiked
    // }

  },
  // this.review.liked_users.includes(JSON.parse(localStorage.getItem('currentUser').pk))
}
</script>

<style>
  .best-review {
    display: flex;
    height: 75px;
    margin-top: 5px;
    background-color: rgb(91, 146, 230);
    border-bottom: 4px solid rgb(61, 98, 152);
    border-right: 3px solid rgb(61, 98, 152);
    align-items: center;
    border-radius: 3px;
    color: rgb(27, 28, 49);
  }
  .none-best {
    display: flex;
    height: 75px;
    margin-top: 5px;
    background-color: rgb(51,56,66);
    color: rgb(218,221,228);
    border-bottom: 4px solid rgb(26, 28, 32);
    border-right: 3px solid rgb(26, 28, 32);
    align-items: center;
    border-radius: 3px;
  }
  .username {
    padding-left: 20px;
    font-size: 24px;
    font-weight: bold;
  }
  .review-content {
    font-size: 20px;
  }
  .likes-count {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>