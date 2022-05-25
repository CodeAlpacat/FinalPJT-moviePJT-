<template>
  <div>
    <div class="community-title">
      영화 이야기 판
    </div>
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
      <div v-for="article in articles.slice((page - 1)*10,(page*10))" :key="article.pk">
        <article-view :article="article"></article-view>
      </div>
    </div>
    <div 
      style="text-align:right; width:900px; margin:10px auto 0; text-align: right;"
    >
      <v-btn
        rounded
        large
        color="blue darken-3"
        dark
        @click="$router.push({ name:'articleNew'})"
      >
        <v-icon>mdi-pencil</v-icon>
        <span style="font-family:'Jeju Gothic', sans-serif !important; margin-left:20px;">글 작성하기</span>
      </v-btn>
    </div>
    <div class="text-center">
      <v-pagination
        v-model="page"
        :length="parseInt(Math.ceil(articles.length/10))"
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
    ...mapGetters(['articles','currentUser','likedArticleList'])
  },
  methods: {
    ...mapActions(['fetchArticles','fetchProfile','fetchCurrentUser'])
  },
  async created() {
    await this.fetchArticles();
    const localuser = JSON.parse(window.localStorage.getItem('currentUser'))
    this.fetchProfile({'username':localuser.username});
  }
}
</script>

<style scoped>
  @import url(//fonts.googleapis.com/earlyaccess/jejogothic.css);
  .community-title{
    margin: 60px auto 0;
    text-align: center;
    font-family:'Jeju Gothic', sans-serif !important;
    font-size: 48px;
    color: rgb(28, 165, 220);
    font-weight: bolder;
  }
  .body {
    display: flex;
    flex-direction: column;
    background-color: rgb(59, 119, 172);
    width: 900px;
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
    font-family:'Jeju Gothic', sans-serif !important;
  }
  .articleTable > div {
    color: rgb(223, 214, 210);
    font-family: 'Jeju Gothic', sans-serif;
    font-size: medium;
  }
  
</style>