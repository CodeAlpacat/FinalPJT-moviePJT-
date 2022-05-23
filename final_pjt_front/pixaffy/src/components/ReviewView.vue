<template>
  <div :class="best ? 'best-review' : 'none-best'">
  <!-- 위에서 best 값이 true 일 경우, best-review style 적용, false 일 경우, none-best style 적용 -->
    <div class="col-2 username">
      {{review.user.username}}
    </div>
    <div class="col-8 review-content">
      {{review.content}}
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
      const currentUser = JSON.parse(localStorage.getItem('currentUser'))
      return {
        page: 1,
        reviewLiked: (this.review.liked_users).includes(currentUser.pk)
        // best: false,
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
    ...mapActions(['likeReview']),
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
  }
  .none-best {
    display: flex;
    height: 75px;
    margin-top: 5px;
    background-color: rgb(212,207,220);
    border-bottom: 4px solid rgb(141, 138, 146);
    border-right: 3px solid rgb(141, 138, 146);
    align-items: center;
    border-radius: 3px;
  }
  .username {
    padding-left: 20px;
    font-size: 24px;
    font-weight: bold;
    color: rgb(27, 28, 49);
  }
  .review-content {
    font-size: 20px;
    color: rgb(27, 28, 49);
  }
  .likes-count {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>