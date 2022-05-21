<template>
  <div>
    <div class="body">
      <div class="articleTable">
        <div class="col-6">
          제목
        </div>
        <div class="col-2">
          글쓴이
        </div>
        <div class="col-2">
          좋아요 수
        </div>
        <div class="col-2">
          날짜
        </div>
      </div>

      <article-view v-for="article in articleList" :key="article.pk" :article="article"></article-view>
    </div>
    <div style="text-align:right; margin-right:10%">
      <v-btn
        icon
        color="blue darken-4"
      >
        <v-icon>mdi-pencil</v-icon>
      </v-btn>
    </div>
    <div class="text-center">
      <v-pagination
        v-model="page"
        :length="6"
      ></v-pagination>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import ArticleView from '@/components/ArticleView.vue'
export default {
  name: 'CommunityView',
  components: {
    ArticleView,
  },
  data () {
      return {
        page: 1,
      }
    },
  computed: {
    ...mapGetters(['articleList'])
  },
  methods: {
    ...mapActions(['fetchArticleList'])
  },
  created() {
    this.fetchArticleList()
  }
}
</script>

<style scoped>
  @import url(//fonts.googleapis.com/earlyaccess/jejogothic.css);
  .body {
    display: flex;
    flex-direction: column;
    background-color: rgb(59, 119, 172);
    width: 80%;
    margin: 50px auto 0;
    border-radius: 3px;
    padding: 5px;
  }
  .articleTable {
    display: flex;
    background-color: rgb(27, 45, 71);
    width: 100%;
    border-radius: 2px;
    text-align: center;
  }
  .articleTable > div {
    color: rgb(223, 214, 210);
    font-family: 'Jeju Gothic', sans-serif;
    font-size: medium;
  }
  
</style>