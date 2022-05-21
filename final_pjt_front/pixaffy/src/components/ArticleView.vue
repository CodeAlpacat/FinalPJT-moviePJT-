<template>
  <div class="article">
    <div class="col-6">
      {{ article.title }} <span class="subcontent">{{ article.comment_count }}</span>
    </div>
    <div class="col-2">
      {{ article.user.username }}
    </div>
    <div class="col-2">
      <span class="likes">{{article.like_count}}</span>
    </div>
    <div class="col-2">
      <span class="subcontent">날짜</span>
    </div>
  </div>
</template>

<script>
export default {
  name:"ArticleView",
  props: {
    article: Object,
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
  }
  .likes {
    color: rgb(221, 147, 48);
    font-weight: bold;
  }

</style>