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
      <div v-for="article in articles.slice((page - 1)*15,(page*15))" :key="article.pk">
        <article-view :article="article"></article-view>
      </div>
    </div>
    <div 
      class="createArticle"
    >
      <v-btn
        rounded
        large
        color="blue darken-1"
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
        :length="parseInt(Math.ceil(articles.length/15))"
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
    color: rgb(221, 147, 48);
    font-weight: bolder;
  }
  .body {
    display: flex;
    flex-direction: column;
    background-color: rgb(75, 82, 97);
    width: 1350px;
    margin: 50px auto 0;
    border-radius: 3px;
    padding: 5px;
  }
  .articleTable {
    display: flex;
    background-color: rgb(23, 146, 195);
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
  .createArticle {
    text-align:right;
    width:1350px;
    margin:10px auto 0;
    text-align: right;
  }
  @media screen and (max-width: 1349px) {
    .body {
      width: 850px;
    }
    .createArticle {
      width: 850px;
    }
  }

  @media screen and (max-width: 899px) {
    .body {
      width: 590px;
    }
    .createArticle {
      width: 590px;
    }
    .articleTable > div {
      font-size: small;
    }
  }
  
</style>