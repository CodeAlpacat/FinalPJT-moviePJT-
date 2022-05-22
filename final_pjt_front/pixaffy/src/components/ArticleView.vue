<template>
  <div class="article">
    <div 
      class="col-6" 
      @click="$router.push({ name:'article', params: {article: article, articlePk: article.pk, isLiked: isInList, articleComments: article.comments, user: article.user}})"
      style="cursor: pointer;"
    >
      {{ article.title }} <span class="subcontent">{{ article.comment_count }}</span>
    </div>
    <div class="col-2">
      {{ article.user.username }}
    </div>
    <div class="col-2">
      <span class="likes">{{article.like_count}}</span>
    </div>
    <div class="col-2">
      <span class="subcontent">{{ dateForArticle }}</span>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name:"ArticleView",
  data() {
    return {
      presentDate: null,
      createdDate: null,
    }
  },
  props: {
    article: Object,
  },
  computed:{
    ...mapGetters(['isCommentLiked','likedArticleList']),
    isInList() {
      return this.likedArticleList.includes(this.article.pk)
    },
    dateForArticle() {
      if ((this.presentDate.getTime() - this.createdDate.getTime()) / (1000*60*60*24) >= 1){
        return `${this.createdDate.getFullYear()}.${this.createdDate.getMonth()+1}.${this.createdDate.getDate()}`
      }
      else if ((this.presentDate.getTime() - this.createdDate.getTime()) / (1000*60*60) >= 1){
        return `${parseInt((this.presentDate.getTime() - this.createdDate.getTime()) / (1000*60*60))}시간 전`
      }
      else if ((this.presentDate.getTime() - this.createdDate.getTime()) / (1000*60) >= 1){
        return `${parseInt((this.presentDate.getTime() - this.createdDate.getTime()) / (1000*60))}분 전`
      }
      else {
        return '방금 전'
      }
    }
  },
  methods: {
    fetchPresentDate() {
      this.presentDate = new Date()
    },
    fetchCreatedDate() {
      this.createdDate = new Date(this.article.created_at)
    }
  },
  created() {
    this.fetchPresentDate()
    this.fetchCreatedDate()
  }

}
</script>

<style>
  .article {
    display: flex;
    background-color: rgb(179, 196, 229);
    border-radius: 2px;
    text-align: center;
    margin-top: 3px;
  }
  .article > div {
    color: rgb(2, 7, 21);
    font-family: 'Jeju Gothic', sans-serif;
    font-size: small;
  }
  .subcontent {
    color: rgb(117, 126, 139);
    font-family:'Jeju Gothic', sans-serif !important;
  }
  .likes {
    color: rgb(221, 147, 48);
    font-weight: bold;
    font-family:'Jeju Gothic', sans-serif !important;
  }

</style>