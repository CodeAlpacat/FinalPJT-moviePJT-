<template>
  <div>
    <div style="display: flex; flex-direction: column; width:90%; margin: 50px auto 0;">
      <review-view :best="true"></review-view>
      <review-view :best="true"></review-view>
      <review-view :best="false"></review-view>
      <review-view :best="false"></review-view>
      <review-view :best="false"></review-view>
      <div style="margin:10px 5px 0 auto">
        <div class="create-review">
          <v-btn
            class="mx-2"
            fab
            dark
            small
            color="indigo darken-3"
          >
            <v-icon dark>
              mdi-plus
            </v-icon>
          </v-btn>
        </div>
      </div>
    </div>
    <v-pagination
      v-model="page"
      :length="6"
    ></v-pagination>
  </div>
</template>

<script>
import ReviewView from './ReviewView.vue'

export default {
  name: 'reviewDetail',
  components: {
    ReviewView,
  },
  data () {
      return {
        page: 1,
      }
    },
}
</script>

<style>
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