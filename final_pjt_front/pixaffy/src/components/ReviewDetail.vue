<template>
  <div>
    <div style="display: flex; flex-direction: column; width:90%; margin: 50px auto 0;">
      <div v-if="movie.reviews">
        <div v-for="review in (page===1 ? sortedReviews.slice(0,3) : [])" :key="review.pk">
          <review-view :review="review" :movie="movie" :best="true"></review-view>
        </div>
        <div v-for="review in (page!==1 ? sortedReviews.slice((page - 1)*10,(page*10)) : sortedReviews.slice(3,10))" :key="review.pk">
          <review-view :review="review" :movie="movie" :best="false"></review-view>
        </div>
        <!-- <div v-for="review in getReverse.slice((page - 1)*10,(page*10))" :key="review.pk">
          <review-view :review="review" :movie="movie"></review-view>
        </div> -->
      </div>
      <div style="margin:20px 5px 0 auto">
        <div class="create-review">
          <!-- 리뷰 작성 버튼 -->
          <v-row justify="center">
            <v-dialog
              v-model="dialog"
              persistent
              max-width="600px"
            >
              <template v-slot:activator="{ on, attrs }">
                <div class="subtitle-item">
                  <v-btn
                    class="mx-2"
                    dark
                    small
                    fab
                    color="indigo darken-3"
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon>mdi-plus</v-icon>
                  </v-btn>
                </div>
              </template>

              <v-card>
                <v-card-title>
                  <span class="review-title">리뷰 작성하기</span>
                </v-card-title>
                <div class="textarea">
                <v-textarea
                  v-model="content"
                  color="amber darken-4"
                >
                  <template v-slot:label>
                    <div>
                      리뷰 내용을 작성해주세요 <small></small>
                    </div>
                  </template>
                </v-textarea>
                </div>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="dialog=false"
                  >
                    닫기
                  </v-btn>
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="dialog=false; createReview({'moviePk': movie.id ? movie.id : movie.pk, 'content':content}); content=''"
                  >
                    완료
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-row>
          <!-- <v-btn
            class="mx-2"
            fab
            dark
            small
            color="indigo darken-3"
          >
            <v-icon dark>
              mdi-plus
            </v-icon>
          </v-btn> -->
        </div>
      </div>
    </div>
    <v-pagination
      v-model="page"
      :length="parseInt(Math.ceil(movie.reviews.length/10))"
    ></v-pagination>
  </div>
</template>

<script>
import ReviewView from './ReviewView.vue'
import { mapActions } from 'vuex'

export default {
  name: 'reviewDetail',
  components: {
    ReviewView,
  },
  data () {
      return {
        page: 1,
        dialog: false,
        content: '',
      }
    },
  props: {
    movie: Object,
  },
  methods: {
    ...mapActions(['createReview','movieSelect']),
  },
  computed: {
    getReverse() {
      let result = this.movie.reviews
      return result.reverse()
    },
    sortedReviews() {
      // function transform(value) {
        let movieReviews = this.movie.reviews
        movieReviews.reverse()
        let first = 0 // 1st
        let firstIndex = null
        let second = 0 // 2nd
        let secondIndex = null
        let third = 0 // 3rd
        let thirdIndex = null
        let index = 0
        let likes = 0
        let test = [] // Top3 저장 리스트
  
        for (let review of movieReviews) { // 1st, 2nd, 3rd 순위 결정
          likes = review.like_count
          if (likes > first){
            third = second
            thirdIndex = secondIndex
            second = first
            secondIndex = firstIndex
            first = likes
            firstIndex = index
          }
          else if (likes > second){
            third = second
            thirdIndex = secondIndex
            second = likes
            secondIndex = index
          }
          else if (likes > third){
            third = likes
            thirdIndex = index
          }
          index = index + 1
        }
        // 순위결정 후 Top3 리스트 push [1st, 2nd, 3rd]
        if (firstIndex){
          test.push(movieReviews[firstIndex])
        }
        if (secondIndex){
          test.push(movieReviews[secondIndex])
        }
        if (thirdIndex){
          test.push(movieReviews[thirdIndex])
        }
        // splice 통한 제거 후, 인덱스 변화를 배제하기 위해 가장 높은 인덱스 값 부터 처리
        let t
        if(thirdIndex){
          if(thirdIndex < secondIndex){
            t = thirdIndex
            thirdIndex = secondIndex
            secondIndex = t
          }
          if(thirdIndex < firstIndex){
            t = thirdIndex
            thirdIndex = firstIndex
            firstIndex = t
          }
        }
        if(secondIndex){
          if(secondIndex < firstIndex){
            t = secondIndex
            secondIndex = firstIndex
            firstIndex = t
          }
        }

        if (thirdIndex){
          movieReviews.splice(thirdIndex, 1)
        }
        if (secondIndex){
          movieReviews.splice(secondIndex, 1)
        }
        if (firstIndex){
          movieReviews.splice(firstIndex, 1)
        }
        movieReviews.splice(0,0,...test)

        return movieReviews
    }
  },
  created() {
    
    this.movieSelect(this.movie)
  }
}
</script>

<style>
  .username {
    padding-left: 20px;
    font-size: 24px;
    font-weight: bold;
    font-family:'Jeju Gothic', sans-serif !important;
    color: rgb(27, 28, 49);
  }
  .review-content {
    font-size: 20px;
    font-family:'Jeju Gothic', sans-serif !important;
    color: rgb(27, 28, 49);
  }
  .likes-count {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .textarea {
    margin: 0 30px;
  }
  .review-title {
    margin: 0 10px;
    font-family: 'Jeju Gothic', sans-serif !important;
    font-weight: bold !important;
    color: rgb(2, 7, 21);
    font-size: 24px !important;
  }
</style>