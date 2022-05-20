<template>
  <div class="article">
    <div class="col-6">
      제목1 <span class="subcontent">(댓글 수)</span>
    </div>
    <div class="col-2">
      글쓴이
    </div>
    <div class="col-2">
      <span class="likes">좋아요 수</span>
    </div>
    <div class="col-2">
      <span class="subcontent">날짜</span>
    </div>
  </div>
</template>

<script>
export default {
  name:"ArticleView"
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