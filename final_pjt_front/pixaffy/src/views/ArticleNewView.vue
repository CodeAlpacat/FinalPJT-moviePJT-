<template>
  <div>
    <div class="new-article-title">
      <div>
        <div style="font-family:'Jeju Gothic', sans-serif !important;">새 게시글 작성</div>
      </div>
    </div>
    <div class="new-article">
      <article-form :article="article" action="create"></article-form>
    </div>
  </div>
</template>

<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'AritcleNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style>

  .new-article-title{
    margin: 40px auto 0;
    text-align: center;
    font-size: 40px;
    font-weight: bolder;
    color: rgb(27,45,71);
    font-family:'Jeju Gothic', sans-serif !important; 
  }
  .new-article{
    width: 80%;
    background-color: rgb(237,242,250);
    border: 2px solid rgb(19, 150, 229);
    margin: 40px auto 30px;
    border-radius: 5px;
    padding: 10px 20px;
  }
</style>
