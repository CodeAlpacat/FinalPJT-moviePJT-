<template>
  <div>
    <div class="edit-article-title">
      <div>
        <div style="font-family:'Jeju Gothic', sans-serif !important;">게시글 수정</div>
      </div>
    </div>
    <div class="edit-article">
      <article-form v-if="isArticle" :article="article" action="update"></article-form>
    </div>
  </div>

</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'AritcleEditView',
    components: { ArticleForm },
    computed: {
      ...mapGetters(['article', 'isArticle',])
    },
    methods: {
      ...mapActions(['fetchArticle'])
    },
    created() {
      this.fetchArticle(this.$route.params.articlePk)
    },
  }
</script>

<style>
  .edit-article-title{
    margin: 40px auto 0;
    text-align: center;
    font-size: 40px;
    font-weight: bolder;
    color: rgb(27,45,71);
    font-family:'Jeju Gothic', sans-serif !important; 
  }
  .edit-article{
    width: 80%;
    background-color: rgb(237,242,250);
    border: 2px solid rgb(19, 150, 229);
    margin: 40px auto 30px;
    border-radius: 5px;
    padding: 10px 20px;
  }
</style>
