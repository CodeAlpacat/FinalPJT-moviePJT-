<template>
  <div>
    <div class="article-frame">
        <div class="title">
          <div>
            <h3>닥터 스트레인지 왜 공포 영화같지~</h3>
          </div>
          <div>
            <v-menu
              bottom
              left
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon
                  v-bind="attrs"
                  v-on="on"
                >
                  <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item>
                  <v-list-item-title>
                    게시글 수정
                  </v-list-item-title>
                </v-list-item>
                <v-list-item>
                  <v-list-item-title>
                    게시글 삭제
                  </v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </div>
        </div>
      <!-- 부제목, username과 좋아요, 댓글버튼 들어감 -->
      <div class="subtitle">
        <div style="display: flex; align-items: center;">
          <div class="subtitle-item">
            <v-avatar
              color="primary"
              size="56"
            >도라</v-avatar>
          </div>
          <div style="margin-left:10px">
            <h4>도라이썬</h4>
          </div>
        </div>
        <div style="display: flex; align-items: center;">
          <div class="subtitle-item">
            <v-btn
              icon
              :color="true ? 'red darken-2' : 'grey'"
            >
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </div>
          <div class="subtitle-item">
            <v-btn
              icon
              color="blue darken-4"
            >
              <v-icon>mdi-message-text</v-icon>
            </v-btn>
          </div>
        </div>
      </div>
      <!-- 내용,  -->
      <div class="content">
        내용
      </div>
      <div class="comments">
        <div>
          <div>
            댓글 작성자
          </div>
          댓글 내용
        </div>
        <div>
          <div>
            댓글 작성자
          </div>
          댓글 내용
        </div>
        <div>
          <div>
            댓글 작성자
          </div>
          댓글 내용
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'ArticleDetailView',
  data: () => ({
    }),
}
</script>

<style>
  @import url(//fonts.googleapis.com/earlyaccess/jejogothic.css);
  .article-frame {
    font-family: 'Jeju Gothic', sans-serif;
    margin: 50px auto;
    width: 900px;
    border: 2px solid rgb(27, 45, 71)
  }
  .title {
    font-family: 'Jeju Gothic', sans-serif;
    display: flex;
    margin-bottom: 30px;
    padding-top: 10px;
    padding-left: 20px;
    padding-right: 10px;
    justify-content: space-between;
  }
  .subtitle {
    font-family: 'Jeju Gothic', sans-serif;
    width: 90%;
    margin: 0 auto 20px;
    font-size: small;
    display: flex;
    justify-content: space-between;
    padding: 5px 5px 15px;
    border-bottom: 3px solid rgb(165, 165, 187);
  }
  .subtitle-item {
    font-family: 'Jeju Gothic', sans-serif;
    margin: 0 5px;
  }
  .article-frame .subtitle .subtitle-item{
    font-family: 'Jeju Gothic', sans-serif;
    color: rgb(242, 237, 243);
  }
  .content {
    width: 90%;
    margin: 20px 5% 30px;
    padding-bottom: 20px;
    border-bottom: 2px solid rgb(165, 165, 187);
  }
  .comments {
    width: 90%;
    margin: 0 5% 20px;
  }
  .comments > div {
    border-bottom: 1px solid rgb(203,206,213);
    margin-top: 15px;
    padding: 5px;
  }
  .comments > div > div {
    background-color: rgb(173,192,221);
    font-weight: bold;
    border-radius: 2px;
  }
</style>